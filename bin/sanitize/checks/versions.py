"""Flags software versions that are past end-of-life according to https://endoflife.date.

Scans prose *and* code blocks: versions in commands and image tags are exactly what goes stale.
Cycle data is fetched once per product and cached for CACHE_TTL_DAYS in .cache/endoflife/.
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import date, datetime
from typing import Callable, Dict, List, Optional, Tuple

from ..model import Check, Finding, Page

API_URL = "https://endoflife.date/api/{product}.json"
CACHE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".cache", "endoflife")
CACHE_TTL_DAYS = 7
# A line that already says the version is dead is documenting it, not recommending it -> info instead of warn
ACKNOWLEDGED_RE = re.compile(r"end of life|\bEOL\b|deprecated|no longer supported|unsupported|not supported", re.I)

# (endoflife.date product slug, display name, regex with one group capturing the cycle)
# Keep patterns strict: a false "EOL" finding costs more trust than a missed one.
PATTERNS: List[Tuple[str, str, "re.Pattern"]] = [
    ("ubuntu", "Ubuntu", re.compile(r"\bubuntu[ :\-](\d\d\.\d\d)\b", re.I)),
    ("debian", "Debian", re.compile(r"\bdebian[ :\-](\d{1,2})\b(?!\.)", re.I)),
    ("kubernetes", "Kubernetes", re.compile(r"\bkubernetes (?:version )?v?(1\.\d\d)\b", re.I)),
    ("python", "Python", re.compile(r"\bpython[ :\-]?(3\.\d{1,2})\b", re.I)),
    ("nodejs", "Node.js", re.compile(r"\bnode(?:\.js)?[ :\-]?v?(\d\d)\b", re.I)),
    ("php", "PHP", re.compile(r"\bphp[ :\-](\d\.\d)\b", re.I)),
    ("go", "Go", re.compile(r"\b(?:go|golang)[ :\-](1\.\d\d)\b", re.I)),
    ("postgresql", "PostgreSQL", re.compile(r"\bpostgres(?:ql)?[ :\-](\d\d)\b", re.I)),
    ("mysql", "MySQL", re.compile(r"\bmysql[ :\-](\d\.\d)\b", re.I)),
    ("terraform", "Terraform", re.compile(r"\bterraform (?:v|version )?(\d\.\d{1,2})\b", re.I)),
    ("windows-server", "Windows Server", re.compile(r"\bwindows server (\d{4})\b", re.I)),
    ("rocky-linux", "Rocky Linux", re.compile(r"\brocky ?linux[ :\-](\d)\b", re.I)),
    ("almalinux", "AlmaLinux", re.compile(r"\balma ?linux[ :\-](\d)\b", re.I)),
    ("centos", "CentOS", re.compile(r"\bcentos[ :\-](\d)\b", re.I)),
]

Cycles = Dict[str, Optional[date]]  # cycle -> eol date (None = no EOL / still supported)
Fetcher = Callable[[str], Optional[Cycles]]


def _parse_eol(value) -> Optional[date]:
    if isinstance(value, str):
        try:
            return datetime.strptime(value, "%Y-%m-%d").date()
        except ValueError:
            return None
    if value is True:  # endoflife.date uses true for "already EOL, date unknown"
        return date(1970, 1, 1)
    return None


def fetch_cycles(product: str) -> Optional[Cycles]:
    """endoflife.date cycles for a product, from the local cache or the network. None if unavailable."""
    os.makedirs(CACHE_DIR, exist_ok=True)
    cache_file = os.path.join(CACHE_DIR, product + ".json")
    data = None
    if os.path.exists(cache_file) and time.time() - os.path.getmtime(cache_file) < CACHE_TTL_DAYS * 86400:
        with open(cache_file, encoding="utf-8") as f:
            data = json.load(f)
    else:
        try:
            with urllib.request.urlopen(API_URL.format(product=product), timeout=10) as resp:
                data = json.load(resp)
            with open(cache_file, "w", encoding="utf-8") as f:
                json.dump(data, f)
        except (urllib.error.URLError, json.JSONDecodeError, OSError) as e:
            print("warning: endoflife.date lookup failed for %s: %s" % (product, e), file=sys.stderr)
            if os.path.exists(cache_file):  # stale cache beats nothing
                with open(cache_file, encoding="utf-8") as f:
                    data = json.load(f)
    if data is None:
        return None
    return {str(c["cycle"]): _parse_eol(c.get("eol")) for c in data}


def extract_versions(page: Page) -> List[Tuple[str, str, str, int, str, bool]]:
    """Returns (product, display, cycle, line, evidence, acknowledged) for every version mention."""
    out = []
    for i, text in enumerate(page.body.split("\n")):
        acknowledged = bool(ACKNOWLEDGED_RE.search(text))
        for product, display, pattern in PATTERNS:
            for m in pattern.finditer(text):
                out.append((product, display, m.group(1), page.body_start_line + i, m.group(0), acknowledged))
    return out


def check_versions(page: Page, fetcher: Fetcher = fetch_cycles, now: Optional[date] = None) -> List[Finding]:
    now = now or date.today()
    # (product, cycle) -> (first line, evidence, count, every mention acknowledged as EOL)
    seen: Dict[Tuple[str, str], Tuple[int, str, int, bool]] = {}
    for product, display, cycle, line, evidence, acknowledged in extract_versions(page):
        key = (product, cycle)
        if key in seen:
            first_line, ev, n, ack = seen[key]
            seen[key] = (first_line, ev, n + 1, ack and acknowledged)
        else:
            seen[key] = (line, evidence, 1, acknowledged)

    display_by_product = {p: d for p, d, _ in PATTERNS}
    out: List[Finding] = []
    for (product, cycle), (line, evidence, n, acknowledged) in seen.items():
        cycles = fetcher(product)
        if cycles is None or cycle not in cycles:
            continue  # unknown cycle: typo, or not tracked; stay silent rather than guess
        eol = cycles[cycle]
        if eol is None:
            continue
        name = "%s %s" % (display_by_product[product], cycle)
        times = " (%d mentions)" % n if n > 1 else ""
        if eol <= now:
            when = "" if eol == date(1970, 1, 1) else " on %s" % eol.isoformat()
            out.append(Finding(page.file, page.url, "versions/eol", "info" if acknowledged else "warn",
                               "%s reached end of life%s%s" % (name, when, times), line=line, evidence=evidence))
    return out


def run(pages: List[Page]) -> List[Finding]:
    cache: Dict[str, Optional[Cycles]] = {}

    def cached(product: str) -> Optional[Cycles]:
        if product not in cache:
            cache[product] = fetch_cycles(product)
        return cache[product]

    return [f for p in pages for f in check_versions(p, fetcher=cached)]


CHECK = Check("versions", run)
