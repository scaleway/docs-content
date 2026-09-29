from __future__ import annotations

import hashlib
import os
from typing import Any, Dict, Iterable, List, Optional, Tuple

import yaml

from .model import PAGE_TYPES, Page

PAGES_DIR = "pages"
TUTORIALS_DIR = "tutorials"


def file_to_url(file: str) -> str:
    """pages/kubernetes/how-to/create-cluster.mdx -> /kubernetes/how-to/create-cluster/"""
    rel = file.replace(os.sep, "/")
    if rel.startswith(PAGES_DIR + "/"):
        rel = rel[len(PAGES_DIR) + 1 :]
    elif rel.startswith(TUTORIALS_DIR + "/"):
        rel = "tutorials/" + rel[len(TUTORIALS_DIR) + 1 :]
    if rel.endswith(".mdx"):
        rel = rel[:-4]
    if rel.endswith("/index"):
        rel = rel[: -len("/index")]
    if rel == "index":
        rel = ""
    return "/" + rel + ("/" if rel else "")


def classify(file: str, frontmatter: Dict[str, Any]) -> Tuple[str, str]:
    """Returns (product, page_type)."""
    segments = [s for s in file_to_url(file).split("/") if s]
    if segments and segments[0] == "tutorials":
        products = frontmatter.get("products") or []
        return (products[0] if products else "tutorials"), "tutorial"
    product = segments[0] if segments else ""
    # Product landing page and section landing pages (how-to/index.mdx) are both "index"
    if len(segments) < 2 or os.path.basename(file) == "index.mdx":
        return product, "index"
    return product, (segments[1] if segments[1] in PAGE_TYPES else "other")


def split_frontmatter(raw: str) -> Tuple[Dict[str, Any], str, int]:
    """Returns (frontmatter, body, body_start_line). Tolerates files without frontmatter."""
    if not raw.startswith("---"):
        return {}, raw, 1
    end = raw.find("\n---", 3)
    if end == -1:
        return {}, raw, 1
    yaml_text = raw[3:end]
    body_start = end + len("\n---")
    # skip the newline that follows the closing fence
    if raw[body_start : body_start + 1] == "\n":
        body_start += 1
    data = yaml.safe_load(yaml_text) or {}
    if not isinstance(data, dict):
        data = {}
    return data, raw[body_start:], raw[:body_start].count("\n") + 1


def load_page(file: str) -> Page:
    with open(file, encoding="utf-8") as f:
        raw = f.read()
    frontmatter, body, body_start_line = split_frontmatter(raw)
    product, page_type = classify(file, frontmatter)
    return Page(
        file=file,
        url=file_to_url(file),
        product=product,
        page_type=page_type,
        frontmatter=frontmatter,
        body=body,
        body_start_line=body_start_line,
        hash=hashlib.sha1(raw.encode("utf-8")).hexdigest(),
    )


def walk_mdx(*dirs: str) -> Iterable[str]:
    for d in dirs:
        for root, _, files in os.walk(d):
            for name in sorted(files):
                if name.endswith(".mdx"):
                    yield os.path.join(root, name)


def load_corpus(product: Optional[str] = None, files: Optional[List[str]] = None) -> List[Page]:
    paths = files if files is not None else list(walk_mdx(PAGES_DIR, TUTORIALS_DIR))
    pages = [load_page(p) for p in paths if p.endswith(".mdx") and os.path.isfile(p)]
    if product:
        pages = [p for p in pages if p.product == product]
    return pages
