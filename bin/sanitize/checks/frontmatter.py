from __future__ import annotations

import re
from datetime import date, datetime, timedelta
from typing import Any, List, Optional

from ..model import Check, Finding, Page

# Mirrors DEFAULT_VAL_FREQ in bin/check-review-dates.py
DEFAULT_VALIDATION_FREQUENCY_MONTHS = 6
# Review-date policy is not enforced yet; flip to True (or pass stale=True) to flag overdue pages
ENABLE_STALE_CHECK = False
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
# Page types where dates/tags are not expected (landing pages)
METADATA_EXEMPT = {"index"}


def _parse_date(value: Any) -> Optional[date]:
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if isinstance(value, str) and DATE_RE.match(value):
        try:
            return datetime.strptime(value, "%Y-%m-%d").date()
        except ValueError:
            return None
    return None


def _check_title(page: Page, title: str) -> List[Finding]:
    out: List[Finding] = []

    def f(message: str) -> Finding:
        return Finding(page.file, page.url, "frontmatter/title", "warn", message, line=1, evidence=title)

    if page.page_type == "how-to" and not title.startswith("How to "):
        out.append(f('How-to titles must start with "How to"'))
    return out


def check_frontmatter(page: Page, now: Optional[date] = None, stale: bool = ENABLE_STALE_CHECK) -> List[Finding]:
    now = now or date.today()
    fm = page.frontmatter
    out: List[Finding] = []

    def add(check: str, severity: str, message: str, evidence: Optional[str] = None) -> None:
        out.append(Finding(page.file, page.url, check, severity, message, line=1, evidence=evidence))

    title = fm.get("title")
    if not title:
        add("frontmatter/required", "error", "Missing title")
    else:
        out.extend(_check_title(page, str(title)))

    if not fm.get("description"):
        add("frontmatter/required", "error", "Missing description")

    if page.page_type in METADATA_EXEMPT:
        return out

    if not fm.get("tags"):
        add("frontmatter/required", "warn", "Missing tags")

    dates = fm.get("dates") or {}
    if not isinstance(dates, dict):
        dates = {}
    validation_raw = dates.get("validation")
    posted_raw = dates.get("posted")
    validation = _parse_date(validation_raw)
    posted = _parse_date(posted_raw)

    if validation_raw is None:
        add("frontmatter/required", "error", "Missing dates.validation")
    elif validation is None:
        add("frontmatter/date-format", "error", "dates.validation is not yyyy-mm-dd", str(validation_raw))
    if posted_raw is not None and posted is None:
        add("frontmatter/date-format", "error", "dates.posted is not yyyy-mm-dd", str(posted_raw))
    if validation and posted and validation < posted:
        add("frontmatter/date-order", "error", "dates.validation is earlier than dates.posted")
    if validation:
        if validation > now:
            add("frontmatter/date-future", "error", "dates.validation is in the future", str(validation))
        elif stale:
            freq = float(dates.get("validation_frequency") or DEFAULT_VALIDATION_FREQUENCY_MONTHS)
            age = (now - validation).days
            limit = timedelta(days=freq * 30.4).days
            if age > limit:
                add("frontmatter/stale", "error" if age > limit * 2 else "warn",
                    "Last validated %d days ago (review frequency: %g months)" % (age, freq), str(validation))
    return out


CHECK = Check("frontmatter", lambda pages: [f for p in pages for f in check_frontmatter(p)])
