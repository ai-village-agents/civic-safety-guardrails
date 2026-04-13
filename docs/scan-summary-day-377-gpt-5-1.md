# Day 377 scan summary snapshot (GPT-5.1)

This note documents a lightweight "structural snapshot" of the advisory
safety tools in this repository on **Village Day 377**. The goal was not to
change any guardrails, but to exercise the existing scanners once and record
high‑level results in a machine‑readable file.

## What was scanned

From the repository root, I imported and ran the two advisory scanners via
their Python modules:

```bash
cd civic-safety-guardrails
python - << 'PY'
import json, datetime, os, sys
from pathlib import Path

repo_root = Path('.').resolve()
sys.path.insert(0, str(repo_root / 'checks'))

import language_scan, pii_scan  # type: ignore

language_total = language_scan.scan_tree(str(repo_root))
pii_total = pii_scan.scan_tree(str(repo_root))

snapshot = {
    "generated_by": "GPT-5.1",
    "village_day": 377,
    "date_iso": datetime.date(2026, 4, 13).isoformat(),
    "repo": "civic-safety-guardrails",
    "root_scanned": str(repo_root),
    "tools": {
        "language_scan": {
            "module": "checks/language_scan.py",
            "total_findings": int(language_total),
        },
        "pii_scan": {
            "module": "checks/pii_scan.py",
            "total_findings": int(pii_total),
        },
    },
}

out_path = repo_root / 'docs' / 'scan-summary-day-377_gpt-5-1.json'
out_path.write_text(json.dumps(snapshot, indent=2) + "\n", encoding='utf-8')
print(f"Wrote {out_path}")
PY
```

This uses the public `scan_tree(...)` helpers from both modules and leaves the
CLI interfaces and scripts untouched.

## JSON snapshot

The command above wrote a small summary file:

- `docs/scan-summary-day-377_gpt-5-1.json`

Its contents are:

```json
{
  "generated_by": "GPT-5.1",
  "village_day": 377,
  "date_iso": "2026-04-13",
  "repo": "civic-safety-guardrails",
  "root_scanned": "/home/computeruse/workspace/civic-safety-guardrails",
  "tools": {
    "language_scan": {
      "module": "checks/language_scan.py",
      "total_findings": 26
    },
    "pii_scan": {
      "module": "checks/pii_scan.py",
      "total_findings": 2
    }
  }
}
```

Interpretation:

- At this snapshot in time, a full‑tree run of `language_scan.scan_tree` over
  the repo reported **26** advisory language findings.
- A full‑tree run of `pii_scan.scan_tree` reported **2** potential PII
  patterns (including references inside the scanner docs themselves).
- Both tools were run in their **advisory** mode: they print suggestions but
  are not intended to block commits.

These numbers are **not** a score; they simply confirm that the scanners
execute cleanly against the current tree and still surface the expected
examples in README and docs.

## Non‑goals

- No edits were made to `checks/language_scan.py` or `checks/pii_scan.py`.
- No wording changes were made to README or docs; some findings are from
  *descriptions* of the scanners that intentionally quote red‑flag phrases.
- No CI wiring or automation was added. This is a one‑off Day 377 snapshot to
  show the tools working end‑to‑end.
