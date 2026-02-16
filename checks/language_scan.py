#!/usr/bin/env python3
"""Advisory carceral-language scanner — flags red-flag phrases in text files.

Usage:
    python language_scan.py [directory_or_file]

Scans .md, .txt, .py, .json, .yaml, .yml files for phrases that may
conflict with non-carceral, community-centered values. Examples:
  - "sweep encampments", "clean up vagrants", "crackdown"

This is an advisory tool. It prints suggestions but does NOT block.
Exit code 0 on success (even if patterns found), 1 only on unexpected errors.

See docs/non-carceral-language-guide.md for better framing alternatives.
"""

import os
import re
import sys

# Each entry: (compiled regex, short description, suggested alternative)
RED_FLAGS = [
    (re.compile(r'\bsweep\s+(?:the\s+)?encampments?\b', re.I),
     'sweep encampments',
     'Consider: "address encampment conditions" or remove this framing entirely'),
    (re.compile(r'\bcrackdown\b', re.I),
     'crackdown',
     'Consider: "enforcement action" or reframe around community benefit'),
    (re.compile(r'\bclean\s+(?:up|out)\s+(?:the\s+)?(?:vagrants?|homeless|transients?)\b', re.I),
     'clean up vagrants/homeless',
     'We clean trash, not people. Reframe around litter/hazards, not people.'),
    (re.compile(r'\bclear\s+(?:out|away)\s+(?:the\s+)?(?:encampments?|camps?|tents?)\b', re.I),
     'clear out encampments',
     'Focus on trash and hazards. Do not move or discard personal belongings.'),
    (re.compile(r'\billegals?\b', re.I),
     'illegals (dehumanizing)',
     'Use person-first language: "undocumented people" or remove entirely'),
    (re.compile(r'\bvagrants?\b', re.I),
     'vagrants (dehumanizing)',
     'Use: "unhoused people", "people experiencing homelessness"'),
    (re.compile(r'\bbums?\b(?!\.\w)', re.I),
     'bums (dehumanizing)',
     'Use: "unhoused people", "people experiencing homelessness"'),
    (re.compile(r'\beverict\b', re.I),
     'evict',
     'Community cleanups should not involve displacement. Reframe.'),
    (re.compile(r'\broust\b', re.I),
     'roust (aggressive displacement)',
     'Community cleanups should not involve displacement. Reframe.'),
    (re.compile(r'\bcall\s+(?:the\s+)?(?:cops?|police)\b', re.I),
     'call the cops/police',
     'Reserve for genuine emergencies. See non-carceral-language-guide.md'),
]

EXTENSIONS = {'.md', '.txt', '.py', '.json', '.yaml', '.yml'}


def scan_file(filepath):
    """Scan a single file; return list of (line_no, line, description, suggestion) tuples."""
    findings = []
    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            for i, line in enumerate(f, start=1):
                for pattern, desc, suggestion in RED_FLAGS:
                    if pattern.search(line):
                        findings.append((i, line.rstrip(), desc, suggestion))
    except (OSError, UnicodeDecodeError):
        pass
    return findings


def scan_tree(root):
    """Walk a directory tree and scan eligible files."""
    total = 0
    for dirpath, _dirs, filenames in os.walk(root):
        if any(part.startswith('.') for part in dirpath.split(os.sep)):
            continue
        for fname in filenames:
            _, ext = os.path.splitext(fname)
            if ext.lower() not in EXTENSIONS:
                continue
            full = os.path.join(dirpath, fname)
            hits = scan_file(full)
            for lineno, line, desc, suggestion in hits:
                rel = os.path.relpath(full, root)
                print(f"  ⚠  {rel}:{lineno}")
                print(f"     Phrase: {desc}")
                print(f"     Line:  {line[:120]}")
                print(f"     💡 {suggestion}")
                print()
                total += 1
    return total


def main():
    target = sys.argv[1] if len(sys.argv) > 1 else '.'
    print(f"🔍 Language scan: scanning {target!r} for carceral/dehumanizing language ...")
    print()

    if os.path.isfile(target):
        hits = scan_file(target)
        for lineno, line, desc, suggestion in hits:
            print(f"  ⚠  {target}:{lineno}")
            print(f"     Phrase: {desc}")
            print(f"     Line:  {line[:120]}")
            print(f"     💡 {suggestion}")
            print()
        total = len(hits)
    elif os.path.isdir(target):
        total = scan_tree(target)
    else:
        print(f"  ❌  Path not found: {target}")
        sys.exit(1)

    if total:
        print(f"📋 Found {total} phrase(s) to review. See docs/non-carceral-language-guide.md for alternatives.")
    else:
        print("✅ No carceral or dehumanizing language patterns found.")
    sys.exit(0)


if __name__ == '__main__':
    main()
