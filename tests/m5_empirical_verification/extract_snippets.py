import re
import os

files = [
    ("/mnt/second_drive/DOCS/Backend/os_study_guide_full.md", "sg"),
    ("/mnt/second_drive/DOCS/Backend/os_deep_knowledge_full.md", "dk"),
    ("/mnt/second_drive/DOCS/Backend/os_cheat_sheet_full.md", "cs"),
    ("/mnt/second_drive/DOCS/Backend/os_exam_questions_full.md", "eq")
]

out_dir = "/mnt/second_drive/DOCS/SEC/tests/m5_empirical_verification/snippets"
os.makedirs(out_dir, exist_ok=True)

manifest = []

for filepath, prefix in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    in_block = False
    lang = ""
    start_line = 0
    block_lines = []
    block_idx = 0
    indent_len = 0
    
    for idx, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith("```"):
            if not in_block:
                in_block = True
                lang = stripped[3:].strip()
                start_line = idx
                block_lines = []
                indent_len = len(line) - len(line.lstrip())
            else:
                in_block = False
                end_line = idx
                block_idx += 1
                if lang in ['c', 'python', 'py']:
                    ext = "c" if lang == "c" else "py"
                    filename = f"{prefix}_b{block_idx}_L{start_line}_{lang}.{ext}"
                    filepath_out = os.path.join(out_dir, filename)
                    # strip common indent if indented block
                    processed_lines = []
                    for bl in block_lines:
                        if len(bl) >= indent_len and bl[:indent_len].isspace():
                            processed_lines.append(bl[indent_len:])
                        else:
                            processed_lines.append(bl)
                    content = "".join(processed_lines)
                    with open(filepath_out, 'w', encoding='utf-8') as out_f:
                        out_f.write(content)
                    manifest.append({
                        "file": filepath,
                        "prefix": prefix,
                        "block_idx": block_idx,
                        "start_line": start_line,
                        "end_line": end_line,
                        "lang": lang,
                        "out_path": filepath_out,
                        "line_count": len(block_lines),
                        "bytes": len(content.encode('utf-8'))
                    })
        else:
            if in_block:
                block_lines.append(line)

print(f"Extracted {len(manifest)} code snippets:")
for m in manifest:
    print(f"  [{m['prefix'].upper()}] L{m['start_line']}-L{m['end_line']} ({m['lang']}, {m['line_count']} lines, {m['bytes']} bytes) -> {os.path.basename(m['out_path'])}")
