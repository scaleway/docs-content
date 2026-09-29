from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from typing import Dict, List

from ..model import Check, Finding, Page

SEVERITY = {"error": "error", "warning": "warn", "suggestion": "info"}
VALE_CONFIG = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "vale", ".vale.ini")


def run_vale(pages: List[Page]) -> List[Finding]:
    """Runs Vale with the package's config and maps its JSON alerts."""
    if not pages:
        return []
    if shutil.which("vale") is None:
        print("warning: vale not found; skipping prose checks (brew install vale)", file=sys.stderr)
        return []
    by_file: Dict[str, Page] = {p.file: p for p in pages}
    # "./" prefix so a file name starting with "-" can never be parsed as a vale flag
    proc = subprocess.run(
        ["vale", "--config=" + VALE_CONFIG, "--output=JSON", "--no-exit"] + ["./" + f for f in by_file],
        capture_output=True, text=True, check=False,
    )
    if not proc.stdout.strip():
        if proc.returncode != 0:
            raise RuntimeError("vale failed: %s" % proc.stderr)
        return []
    out: List[Finding] = []
    for rel, alerts in json.loads(proc.stdout).items():
        page = by_file.get(rel[2:] if rel.startswith("./") else rel)
        if page is None:
            continue
        for a in alerts:
            out.append(Finding(page.file, page.url, "vale/" + a["Check"],
                               SEVERITY.get(a["Severity"], "info"), a["Message"],
                               line=a["Line"], evidence=a["Match"]))
    return out


CHECK = Check("vale", run_vale)
