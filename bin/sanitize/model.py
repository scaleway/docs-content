"""Shared vocabulary for the suite: what a page is, what a finding is, what a check is.

Deliberately dependency-free so checks, the corpus loader and the reporter can all import it
without cycles. `Page` is what the corpus loader produces, `Finding` is what every check emits,
and `Check` is the only contract a new analyzer has to satisfy.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional

Severity = str  # "error" | "warn" | "info"
SEVERITY_WEIGHT = {"error": 3, "warn": 2, "info": 1}

PAGE_TYPES = {"concepts", "quickstart", "faq", "how-to", "api-cli", "reference-content", "troubleshooting"}


@dataclass
class Page:
    file: str  # relative to the docs-content root, e.g. pages/kubernetes/how-to/create-cluster.mdx
    url: str  # site-relative, leading + trailing slash, e.g. /kubernetes/how-to/create-cluster/
    product: str
    page_type: str  # one of PAGE_TYPES, or "index" | "tutorial" | "other"
    frontmatter: Dict[str, Any]
    body: str
    body_start_line: int  # 1-indexed line where the body starts, for line offsets
    hash: str  # sha1 of the raw file, for caching expensive checks


@dataclass
class Finding:
    file: str
    url: str
    check: str
    severity: Severity
    message: str
    line: Optional[int] = None
    evidence: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return dict(self.__dict__)


@dataclass
class Check:
    name: str
    run: Callable[[List[Page]], List[Finding]]
