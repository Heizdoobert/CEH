import re

files = [
    "/mnt/second_drive/DOCS/Backend/os_study_guide_full.md",
    "/mnt/second_drive/DOCS/Backend/os_deep_knowledge_full.md",
    "/mnt/second_drive/DOCS/Backend/os_cheat_sheet_full.md",
    "/mnt/second_drive/DOCS/Backend/os_exam_questions_full.md"
]

pattern = re.compile(r'```([a-zA-Z0-9_-]*)\n(.*?)```', re.DOTALL)

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()
    matches = pattern.findall(text)
    print(f"=== {fpath.split('/')[-1]} (Total blocks: {len(matches)}) ===")
    for idx, (lang, code) in enumerate(matches, 1):
        lines = code.strip().split('\n')
        first_line = lines[0] if lines else ""
        print(f"  [{idx}] lang='{lang}' lines={len(lines)} :: {first_line[:80]}")
