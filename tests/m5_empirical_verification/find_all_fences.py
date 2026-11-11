import re

files = [
    "/mnt/second_drive/DOCS/Backend/os_study_guide_full.md",
    "/mnt/second_drive/DOCS/Backend/os_deep_knowledge_full.md",
    "/mnt/second_drive/DOCS/Backend/os_cheat_sheet_full.md",
    "/mnt/second_drive/DOCS/Backend/os_exam_questions_full.md"
]

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(f"\n==================== {fpath} ====================")
    in_block = False
    start_idx = 0
    lang = ""
    for idx, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith("```"):
            if not in_block:
                in_block = True
                start_idx = idx
                lang = stripped[3:].strip()
            else:
                in_block = False
                end_idx = idx
                print(f"L{start_idx}-L{end_idx}: lang='{lang}' (fence: '{line.rstrip()}')")
                lang = ""
