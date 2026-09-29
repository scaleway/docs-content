"""Turns a flat list of findings into something a person can work through.

Findings arrive unordered and one-per-problem; a reviewer wants them grouped by file with the worst
files first. Severity weights (error 3, warn 2, info 1) are summed per file to get that order.
Renders to the console and to `findings.md`, which are intentionally the same content.
"""
from __future__ import annotations

import os
from collections import Counter, OrderedDict
from typing import Any, Dict, List

from .model import SEVERITY_WEIGHT, Finding

SEVERITY_ICON = {"error": "✖", "warn": "▲", "info": "·"}


def score(f: Finding) -> int:
    return SEVERITY_WEIGHT[f.severity]


def summarize(findings: List[Finding]) -> Dict[str, Any]:
    by_severity = Counter(f.severity for f in findings)
    by_check = Counter(f.check for f in findings)
    return {
        "total": len(findings),
        "files": len({f.file for f in findings}),
        "by_severity": {s: by_severity.get(s, 0) for s in ("error", "warn", "info")},
        "by_check": OrderedDict(by_check.most_common()),
    }


def group_by_file(findings: List[Finding]) -> List[Dict[str, Any]]:
    """Groups findings per file; files ordered by total score, findings by line."""
    groups: Dict[str, Dict[str, Any]] = {}
    for f in findings:
        g = groups.setdefault(f.file, {
            "file": f.file, "url": f.url, "score": 0,
            "counts": {"error": 0, "warn": 0, "info": 0}, "findings": [],
        })
        g["score"] += score(f)
        g["counts"][f.severity] += 1
        d = f.to_dict()
        d.pop("file")
        d.pop("url")
        g["findings"].append(d)
    for g in groups.values():
        g["findings"].sort(key=lambda d: d["line"] or 0)
    return sorted(groups.values(), key=lambda g: (-g["score"], g["file"]))


def _summary_lines(findings: List[Finding], page_count: int) -> List[str]:
    s = summarize(findings)
    sev = s["by_severity"]
    lines = ["%d pages scanned, %d with findings: %d errors, %d warnings, %d info"
             % (page_count, s["files"], sev["error"], sev["warn"], sev["info"])]
    lines += ["  %6d  %s" % (n, check) for check, n in s["by_check"].items()]
    return lines


def format_console(findings: List[Finding], page_count: int) -> str:
    lines: List[str] = []
    for g in group_by_file(findings):
        lines += ["", "%s  (%s)" % (g["file"], g["url"])]
        for d in g["findings"]:
            ev = "  — %s" % d["evidence"][:80] if d["evidence"] else ""
            loc = ":%s" % d["line"] if d["line"] else ""
            lines.append("  %s %-5s %-32s %s%s%s"
                         % (SEVERITY_ICON[d["severity"]], d["severity"], d["check"], d["message"], ev, loc))
    return "\n".join(lines + [""] + _summary_lines(findings, page_count))


def format_markdown(findings: List[Finding], page_count: int) -> str:
    s = summarize(findings)
    sev = s["by_severity"]
    lines = ["# Sanitize report", "",
             "%d pages scanned, %d with findings: **%d errors**, %d warnings, %d info"
             % (page_count, s["files"], sev["error"], sev["warn"], sev["info"]), "",
             "| Check | Count |", "| --- | ---: |"]
    lines += ["| %s | %d |" % (check, n) for check, n in s["by_check"].items()]
    for g in group_by_file(findings):
        lines += ["", "## %s" % g["file"], "", g["url"], ""]
        for d in g["findings"]:
            ev = " — `%s`" % d["evidence"].replace("`", "'")[:80] if d["evidence"] else ""
            lines.append("- %s L%s `%s` %s%s"
                         % (SEVERITY_ICON[d["severity"]], d["line"] or "?", d["check"], d["message"], ev))
    return "\n".join(lines) + "\n"


def write_report(findings: List[Finding], page_count: int, out_dir: str) -> None:
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "findings.md"), "w", encoding="utf-8") as f:
        f.write(format_markdown(findings, page_count))
