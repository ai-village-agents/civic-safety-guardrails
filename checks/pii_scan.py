#!/usr/bin/env python3
"""Advisory PII scanner — flags email-like and phone-like patterns in text files.

Usage:
    python pii_scan.py [directory_or_file]

Scans .md, .txt, .py, .json, .yaml, .yml files for:
  - Email-like patterns (user@domain.tld)
  - North American phone-like patterns (xxx-xxx-xxxx, (xxx) xxx-xxxx, etc.)

This is a conservative, advisory tool. It prints warnings but does NOT block.
Exit code 0 on success (even if patterns found), 1 only on unexpected errors.
"""

import os
import re
import sys

EMAIL_RE = re.compile(
    r'\b[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}\b'
)
PHONE_RE = re.compile(
    r'(?<!\d)(?:\+?1[\s\-.]?)?\(?\d{3}\)?[\s\-.]?\d{3}[\s\-.]?\d{4}(?!\d)'
)

EXTENSIONS = {'.md', '.txt', '.py', '.json', '.yaml', '.yml'}

# Allowlisted patterns (example/placeholder addresses, not real PII)
ALLOW_LIST = {
    'user@example.com',
    'volunteer@example.org',
    'name@example.com',
    'help@agentvillage.org',
}


def scan_file(filepath):
    """Scan a single file; return list of (line_no, line, pattern_type) tuples."""
    findings = []
    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            for i, line in enumerate(f, start=1):
                for match in EMAIL_RE.finditer(line):
                    if match.group().lower() not in ALLOW_LIST:
                        findings.append((i, line.rstrip(), 'email'))
                for match in PHONE_RE.finditer(line):
                    findings.append((i, line.rstrip(), 'phone'))
    except (OSError, UnicodeDecodeError):
        pass
    return findings


def scan_tree(root):
    """Walk a directory tree and scan eligible files."""
    total = 0
    for dirpath, _dirs, filenames in os.walk(root):
        # Skip hidden directories
        if any(part.startswith('.') for part in dirpath.split(os.sep)):
            continue
        for fname in filenames:
            _, ext = os.path.splitext(fname)
            if ext.lower() not in EXTENSIONS:
                continue
            full = os.path.join(dirpath, fname)
            hits = scan_file(full)
            for lineno, line, ptype in hits:
                rel = os.path.relpath(full, root)
                print(f"  ⚠  {ptype:6s}  {rel}:{lineno}  →  {line[:120]}")
                total += 1
    return total


def main():
    target = sys.argv[1] if len(sys.argv) > 1 else '.'
    print(f"🔍 PII scan: scanning {target!r} ...")

    if os.path.isfile(target):
        hits = scan_file(target)
        for lineno, line, ptype in hits:
            print(f"  ⚠  {ptype:6s}  {target}:{lineno}  →  {line[:120]}")
        total = len(hits)
    elif os.path.isdir(target):
        total = scan_tree(target)
    else:
        print(f"  ❌  Path not found: {target}")
        sys.exit(1)

    if total:
        print(f"\n📋 Found {total} potential PII pattern(s). Please review before publishing.")
    else:
        print("✅ No PII-like patterns found.")
    sys.exit(0)


if __name__ == '__main__':
    main()
