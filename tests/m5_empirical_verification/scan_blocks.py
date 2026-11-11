import re
import os
import glob

files = [
    "/mnt/second_drive/DOCS/Backend/os_study_guide_full.md",
    "/mnt/second_drive/DOCS/Backend/os_deep_knowledge_full.md",
    "/mnt/second_drive/DOCS/Backend/os_cheat_sheet_full.md",
    "/mnt/second_drive/DOCS/Backend/os_exam_questions_full.md"
]

for filepath in files:
    print(f"=== File: {filepath} ===")
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    in_block = False
    lang = ""
    start_line = 0
    block_lines = []
    
    for idx, line in enumerate(lines, 1):
        if line.startswith("```"):
            if not in_block:
                in_block = True
                lang = line.strip()[3:].strip()
                start_line = idx
                block_lines = []
            else:
                in_block = False
                end_line = idx
                print(f"  Line {start_line}-{end_line}: lang='{lang}' ({len(block_lines)} lines)")
                if lang in ['c', 'python', 'py']:
                    preview = "".join(block_lines[:3]).strip().replace('\n', ' ')
                    print(f"    Preview: {preview[:80]}...")
        else:
            if in_block:
                block_lines.append(line)
