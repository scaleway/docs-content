from datetime import date

from bin.sanitize.checks.frontmatter import check_frontmatter
from bin.sanitize.checks.structure import check_headings, check_links, check_requirements
from bin.sanitize.checks.versions import check_versions, extract_versions
from bin.sanitize.corpus import classify, file_to_url, split_frontmatter
from bin.sanitize.model import Finding, Page
from bin.sanitize.report import csv_cell, format_csv_rows, group_by_file, score

NOW = date(2026, 9, 16)


def page(file="pages/kubernetes/how-to/create-cluster.mdx", body="", **fm_overrides):
    fm = {
        "title": "How to create a cluster",
        "description": "x" * 130,
        "tags": "kubernetes cluster",
        "dates": {"validation": date(2026, 9, 1), "posted": date(2020, 1, 1)},
    }
    fm.update(fm_overrides)
    product, page_type = classify(file, fm)
    return Page(file, file_to_url(file), product, page_type, fm, body, 8, "abc")


def checks(findings):
    return [f.check for f in findings]


# --- corpus ---------------------------------------------------------------

def test_file_to_url():
    assert file_to_url("pages/kubernetes/how-to/create-cluster.mdx") == "/kubernetes/how-to/create-cluster/"
    assert file_to_url("pages/kubernetes/concepts.mdx") == "/kubernetes/concepts/"
    assert file_to_url("pages/kubernetes/index.mdx") == "/kubernetes/"
    assert file_to_url("pages/kubernetes/how-to/index.mdx") == "/kubernetes/how-to/"
    assert file_to_url("tutorials/strapi/index.mdx") == "/tutorials/strapi/"


def test_classify():
    assert classify("pages/vpc/how-to/x.mdx", {}) == ("vpc", "how-to")
    assert classify("pages/vpc/how-to/index.mdx", {}) == ("vpc", "index")
    assert classify("pages/vpc/index.mdx", {}) == ("vpc", "index")
    assert classify("pages/vpc/faq.mdx", {}) == ("vpc", "faq")
    assert classify("pages/vpc/videos.mdx", {}) == ("vpc", "other")
    assert classify("tutorials/strapi/index.mdx", {"products": ["instances"]}) == ("instances", "tutorial")


def test_split_frontmatter_line_offsets():
    raw = "---\ntitle: T\ndates:\n  validation: 2026-01-01\n---\n\n## Heading\n"
    fm, body, start = split_frontmatter(raw)
    assert fm["title"] == "T"
    assert fm["dates"]["validation"] == date(2026, 1, 1)
    assert body == "\n## Heading\n"
    assert start == 6  # "## Heading" is file line 7 = start + 1


def test_split_frontmatter_without_frontmatter():
    assert split_frontmatter("just text") == ({}, "just text", 1)


# --- frontmatter ----------------------------------------------------------

def test_valid_page_passes():
    assert check_frontmatter(page(), NOW) == []


def test_missing_required_fields():
    f = check_frontmatter(page(title=None, description=None, tags=None, dates=None), NOW)
    assert checks(f).count("frontmatter/required") == 4


def test_stale_disabled_by_default():
    assert "frontmatter/stale" not in checks(check_frontmatter(page(dates={"validation": "2024-01-01"}), NOW))


def test_stale_when_enabled():
    opts = {"stale": True}
    p = page(dates={"validation": "2026-01-01", "validation_frequency": 6})
    assert "frontmatter/stale" in checks(check_frontmatter(p, NOW, **opts))
    fresh = page(dates={"validation": "2026-01-01", "validation_frequency": 12})
    assert "frontmatter/stale" not in checks(check_frontmatter(fresh, NOW, **opts))
    old = check_frontmatter(page(dates={"validation": "2024-01-01"}), NOW, **opts)
    assert next(f for f in old if f.check == "frontmatter/stale").severity == "error"


def test_date_order_format_future():
    assert "frontmatter/date-order" in checks(
        check_frontmatter(page(dates={"validation": "2020-01-01", "posted": "2021-01-01"}), NOW))
    assert "frontmatter/date-format" in checks(check_frontmatter(page(dates={"validation": "01/01/2026"}), NOW))
    assert "frontmatter/date-future" in checks(check_frontmatter(page(dates={"validation": "2030-01-01"}), NOW))


def test_description_length_and_howto_title():
    c = checks(check_frontmatter(page(title="Create a cluster", description="short"), NOW))
    assert "frontmatter/description-length" in c
    assert "frontmatter/title" in c


def test_landing_pages_need_no_dates():
    assert check_frontmatter(page(file="pages/kubernetes/how-to/index.mdx", dates=None, tags=None), NOW) == []


# --- structure ------------------------------------------------------------

def test_headings():
    p = page(body="# Title\n\n## Good heading\n\n#### Skipped\n\n## Deploy The Ingress Controller Now\n")
    assert [(f.check, f.line) for f in check_headings(p)] == [
        ("structure/heading-h1", 8),
        ("structure/heading-skip", 12),
        ("structure/heading-case", 14),
    ]


def test_headings_ignore_code_fences():
    assert check_headings(page(body="```bash\n# not a heading\n```\n")) == []


def test_links_compliant():
    p = page(body="See the [VPC Quickstart](/vpc/quickstart/) and [InstantApps](/instances/concepts/#instantapp) "
                  "or [here](#local).\n[Wikipedia](https://en.wikipedia.org/wiki/Foo)\n")
    assert checks(check_links(p)) == ["links/text"]


def test_links_malformed():
    body = "\n".join([
        "[a](/vpc/quickstart)",
        "[b](/en/docs/vpc/quickstart/)",
        "[c](https://www.scaleway.com/en/docs/vpc/quickstart/)",
        "[d](vpc/quickstart/)",
        "[e](/instances/concepts/#instantapp/)",
    ])
    assert checks(check_links(page(body=body))) == [
        "links/trailing-slash",
        "links/internal-prefix",
        "links/internal-absolute",
        "links/relative",
        "links/anchor-trailing-slash",
    ]


def test_links_ignore_images():
    assert check_links(page(body="![alt](assets/img.webp)")) == []


def test_requirements():
    assert len(check_requirements(page(body="text"))) == 1
    assert check_requirements(page(body="<Requirements />")) == []
    assert check_requirements(page(file="pages/vpc/faq.mdx", body="text")) == []


# --- versions -------------------------------------------------------------

CYCLES = {
    "ubuntu": {"20.04": date(2025, 5, 31), "22.04": date(2027, 6, 1), "24.04": date(2029, 4, 25)},
    "python": {"3.7": date(2023, 6, 27), "3.9": date(2026, 10, 31), "3.12": date(2028, 10, 2)},
    "nodejs": {"14": date(2023, 4, 30)},
    "centos": {"7": date(2024, 6, 30)},
}


def fake_fetcher(product):
    return CYCLES.get(product)


def test_extract_versions_prose_and_code():
    p = page(body="Install on Ubuntu 22.04.\n```\ndocker run ubuntu:20.04\nFROM python:3.12\n```\n"
                  "node:14 and Node.js v14")
    got = [(v[0], v[2]) for v in extract_versions(p)]
    assert got == [("ubuntu", "22.04"), ("ubuntu", "20.04"), ("python", "3.12"), ("nodejs", "14"), ("nodejs", "14")]


def test_versions_eol_warn_and_dedupe():
    p = page(body="Ubuntu 20.04\n\nagain Ubuntu 20.04 and CentOS 7")
    f = check_versions(p, fetcher=fake_fetcher, now=NOW)
    assert [(x.check, x.severity, x.line) for x in f] == [("versions/eol", "warn", 8), ("versions/eol", "warn", 10)]
    assert "2 mentions" in f[0].message


def test_versions_eol_soon_and_supported():
    p = page(body="Python 3.9 or Python 3.12")
    f = check_versions(p, fetcher=fake_fetcher, now=NOW)
    assert [(x.check, x.severity) for x in f] == [("versions/eol-soon", "info")]


def test_versions_unknown_cycle_or_product_is_silent():
    p = page(body="Ubuntu 99.99 and Windows Server 2012")
    assert check_versions(p, fetcher=fake_fetcher, now=NOW) == []


def test_versions_acknowledged_is_info():
    p = page(body="| Python 3.7 | End of Life |")
    assert [x.severity for x in check_versions(p, fetcher=fake_fetcher, now=NOW)] == ["info"]
    mixed = page(body="| Python 3.7 | End of Life |\nUse Python 3.7 now")
    assert [x.severity for x in check_versions(mixed, fetcher=fake_fetcher, now=NOW)] == ["warn"]


# --- report ---------------------------------------------------------------

def test_ranking():
    a = Finding("f", "/", "c", "info", "m")
    b = Finding("g", "/", "c", "error", "m")
    c = Finding("h", "/", "c", "warn", "m")
    assert score(b) > score(c) > score(a)
    assert [g["file"] for g in group_by_file([a, b, c, a])] == ["g", "f", "h"]  # 3, 2, 2 -> tie by name


def test_csv_cell_neutralizes_formulas():
    for hostile in ("=1+1", "+1", "-1", "@SUM(A1)", "\tx", "\rx"):
        assert csv_cell(hostile) == "'" + hostile
    assert csv_cell("plain text") == "plain text"
    assert csv_cell("a=b") == "a=b"  # only a leading character matters
    assert csv_cell(3) == 3  # non-strings pass through


def test_csv_rows_sanitize_untrusted_content():
    f = Finding("f.mdx", "/f/", "structure/heading-case", "info", "msg", line=1, evidence="=HYPERLINK(\"http://x\")")
    row = format_csv_rows([f])[0]
    assert row[-1] == "\'=HYPERLINK(\"http://x\")"
