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
    in_block = False
    start_idx = 0
    lang = ""
    block_lines = []
    for idx, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith("```"):
            if not in_block:
                in_block = True
                start_idx = idx
                lang = stripped[3:].strip()
                block_lines = []
            else:
                in_block = False
                end_idx = idx
                if lang == "":
                    # check if it looks like code
                    content = "".join(block_lines)
                    is_code = any(kw in content for kw in ["def ", "class ", "#include", "int main", "void ", "for (", "while (", "if ("])
                    first_few = [l.strip() for l in block_lines[:3] if l.strip()]
                    first_line = first_few[0] if first_few else ""
                    print(f"{fpath.split('/')[-1]} L{start_idx}-L{end_idx}: is_code={is_code} :: {first_line[:60]}")
