import glob
import os

c_files = sorted(glob.glob("/mnt/second_drive/DOCS/SEC/tests/m5_empirical_verification/snippets/*.c"))

for cf in c_files:
    fname = os.path.basename(cf)
    with open(cf, 'r', encoding='utf-8') as f:
        content = f.read()
    has_main = "int main" in content or "void main" in content
    lines = content.strip().split('\n')
    print(f"=== {fname} ({len(lines)} lines) | has_main={has_main} ===")
    print(f"  First 3 lines: {lines[:3]}")
    print(f"  Last 2 lines: {lines[-2:]}")
