import os
import sys

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace non-breaking hyphen (U+2011) with regular hyphen (U+002D)
    new_content = content.replace('\u2011', '-')
    
    if new_content != content:
        print(f"Fixed Unicode hyphens in {filepath}")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

# Files to check
files_to_check = [
    'README.md',
    'index.html', 
    'templates/ui-guardrails-snippet.md'
]

fixed_any = False
for filepath in files_to_check:
    if os.path.exists(filepath):
        if fix_file(filepath):
            fixed_any = True

if fixed_any:
    print("Unicode hyphen fixes applied.")
else:
    print("No Unicode hyphens found.")
