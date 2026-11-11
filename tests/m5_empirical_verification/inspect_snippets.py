import re

filepath = '/mnt/second_drive/DOCS/Backend/os_deep_knowledge_full.md'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

pattern = re.compile(r'```([a-zA-Z0-9_-]*)\n(.*?)```', re.DOTALL)
matches = pattern.findall(text)

print(f"Total fenced blocks in {filepath}: {len(matches)}")
for i, (lang, code) in enumerate(matches, 1):
    lines = code.strip().split('\n')
    first_line = lines[0] if lines else ""
    print(f"[{i}] lang='{lang}' lines={len(lines)} first_line='{first_line[:70]}'")
