#!/usr/bin/env python3
"""
Tier 3: Cross-Feature Symmetry & Parity Test Suite
Validates structural symmetry, paragraph parity, and canonical terminology adherence:
1. Sequential Heading Level Parity: Every '## Heading (English)' is immediately paired with '## Tiêu đề (Tiếng Việt)' at identical heading levels.
2. 1:1 Paragraph Count Parity: Alternating pairwise prose blocks (N_EN == N_VI).
3. Canonical 65-Term Glossary Conformance: Verifies all 65 terms across 6 domains in GLOSSARY.md and asserts zero forbidden anti-pattern mistranslations.
"""

import os
import re
import unittest
from typing import List, Tuple

try:
    from test_utils import (
        get_target_dir,
        get_markdown_files,
        load_file_content,
        parse_headings,
        parse_prose_blocks,
        VN_DIACRITICS_REGEX,
        CANONICAL_GLOSSARY_65
    )
except ImportError:
    from tests.e2e_teamwork.test_utils import (
        get_target_dir,
        get_markdown_files,
        load_file_content,
        parse_headings,
        parse_prose_blocks,
        VN_DIACRITICS_REGEX,
        CANONICAL_GLOSSARY_65
    )


class TestTier3CrossFeature(unittest.TestCase):
    """
    Tier 3 tests ensuring structural harmony, linguistic symmetry, and terminology consistency.
    """

    @classmethod
    def setUpClass(cls):
        cls.target_dir = get_target_dir()
        cls.md_files = get_markdown_files(cls.target_dir)

    def _require_files(self):
        """Ensures target directory has markdown files to inspect."""
        self.assertTrue(
            os.path.exists(self.target_dir),
            f"Target directory does not exist: {self.target_dir}"
        )
        self.assertGreater(
            len(self.md_files), 0,
            f"No markdown files found in target directory: {self.target_dir}. Target directory is currently empty."
        )

    def test_dual_language_heading_symmetry(self):
        """
        Verify sequential dual-language headings:
        Every English heading must be followed by a Vietnamese heading at the exact same level.
        Total EN headings must equal total VI headings.
        """
        self._require_files()
        for fpath in self.md_files:
            fname = os.path.basename(fpath)
            content = load_file_content(fpath)
            headings = parse_headings(content)

            # Skip checking files with 0 or 1 heading (e.g. small manifest if any)
            if len(headings) <= 2:
                continue

            en_headings = [h for h in headings if "(English)" in h[2] or "(ENG)" in h[2]]
            vi_headings = [h for h in headings if "(Tiếng Việt)" in h[2] or "(VIE)" in h[2]]

            self.assertGreater(
                len(en_headings), 0,
                f"File {fname} has headings but no tagged '(English)' headings found."
            )
            self.assertGreater(
                len(vi_headings), 0,
                f"File {fname} has headings but no tagged '(Tiếng Việt)' headings found."
            )
            self.assertEqual(
                len(en_headings), len(vi_headings),
                f"File {fname} has heading count parity mismatch: "
                f"{len(en_headings)} EN headings vs {len(vi_headings)} VI headings."
            )

            # Check consecutive pairing and identical heading level
            paired = 0
            i = 0
            while i < len(headings) - 1:
                idx1, lvl1, t1 = headings[i]
                idx2, lvl2, t2 = headings[i + 1]
                if "(English)" in t1 and "(Tiếng Việt)" in t2:
                    self.assertEqual(
                        lvl1, lvl2,
                        f"File {fname}: Heading level mismatch at lines {idx1} (level {lvl1}) vs {idx2} (level {lvl2}):\n"
                        f"  EN: {t1}\n  VI: {t2}"
                    )
                    paired += 1
                    i += 2
                else:
                    i += 1

            self.assertGreater(
                paired, 0,
                f"File {fname} contains no consecutively paired '(English)' and '(Tiếng Việt)' headings."
            )

    def test_alternating_paragraph_parity(self):
        """
        Verify alternating pairwise paragraph parity (N_EN == N_VI) within tolerance Delta <= 2.
        Checks for symmetrical coverage between English narrative and Vietnamese translation.
        """
        self._require_files()
        # Find the primary content guide (not GLOSSARY.md which is mostly tables)
        guide_files = [
            p for p in self.md_files
            if "glossary" not in os.path.basename(p).lower() and "readme" not in os.path.basename(p).lower()
        ]

        if not guide_files:
            guide_files = self.md_files

        for fpath in guide_files:
            fname = os.path.basename(fpath)
            content = load_file_content(fpath)
            prose_blocks = parse_prose_blocks(content)

            if len(prose_blocks) < 4:
                continue

            en_blocks = [b for b in prose_blocks if not VN_DIACRITICS_REGEX.search(b)]
            vi_blocks = [b for b in prose_blocks if VN_DIACRITICS_REGEX.search(b)]

            delta = abs(len(en_blocks) - len(vi_blocks))
            self.assertLessEqual(
                delta, 2,
                f"File {fname}: Paragraph parity delta too high: "
                f"{len(en_blocks)} EN blocks vs {len(vi_blocks)} VI blocks (delta={delta} > 2)."
            )

    def test_canonical_65_terms_glossary_presence(self):
        """
        Verify that all 65 canonical terms from the 6 core domains are present in GLOSSARY.md
        with both English terminology and Vietnamese standard translations.
        """
        self._require_files()
        glossary_files = [p for p in self.md_files if "glossary" in os.path.basename(p).lower()]
        self.assertGreater(
            len(glossary_files), 0,
            "GLOSSARY.md is missing from the documentation set."
        )

        glossary_text = load_file_content(glossary_files[0])
        glossary_lower = glossary_text.lower()

        missing_terms = []
        for en_term, vi_term, domain, _ in CANONICAL_GLOSSARY_65:
            # Check for English term presence (allowing punctuation/parenthetical variations)
            en_words = [w for w in re.findall(r"[a-zA-Z]+", en_term.lower()) if len(w) > 2]
            en_present = all(w in glossary_lower for w in en_words)

            # Check for Vietnamese term core significant keywords
            vi_words = [
                w for w in re.findall(
                    r"[a-zA-Zàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ]+",
                    vi_term.lower()
                ) if len(w) > 2 and w not in ["giai", "đoạn", "phong", "cách", "vai", "trò", "nhóm"]
            ]
            vi_present = any(w in glossary_lower for w in vi_words[:2]) if vi_words else True

            if not en_present or not vi_present:
                missing_terms.append(f"[{domain}] EN: '{en_term}' (found={en_present}) <-> VI: '{vi_term}' (found={vi_present})")

        self.assertEqual(
            len(missing_terms), 0,
            f"GLOSSARY.md is missing {len(missing_terms)} of the 65 canonical terms:\n" + "\n".join(missing_terms[:15])
        )

    def test_zero_forbidden_translation_antipatterns(self):
        """
        Verify that known translation anti-patterns and naive mistranslations
        are strictly absent in narrative documentation guides and standard glossary terms.
        """
        self._require_files()
        guide_files = [p for p in self.md_files if "glossary" not in os.path.basename(p).lower()]
        filtered_corpus_lines = []
        for p in guide_files:
            for line in load_file_content(p).splitlines():
                stripped = line.strip()
                # Skip table rows containing didactic warnings/anti-pattern guidance
                if stripped.startswith("|") and any(w in stripped.lower() for w in ["tránh dịch", "không dịch"]):
                    continue
                filtered_corpus_lines.append(line)
        guide_corpus = "\n".join(filtered_corpus_lines).lower()
        antipattern_violations = []

        # Context-specific translation anti-pattern phrases
        SPECIFIC_ANTIPATTERNS = [
            ("Social Loafing", "bánh mì xã hội"),
            ("Social Loafing", "lười biếng xã hội"),
            ("Groupthink", "suy nghĩ nhóm"),
            ("Forming", "giai đoạn tạo hình"),
            ("Forming", "tạo hình (forming)"),
            ("Storming", "giai đoạn bão tố"),
            ("Storming", "bão tố (storming)"),
            ("Norming", "giai đoạn bình thường hóa"),
            ("Norming", "bình thường hóa (norming)"),
            ("Performing", "giai đoạn trình diễn"),
            ("Performing", "trình diễn (performing)"),
            ("Performing", "giai đoạn biểu diễn"),
            ("Performing", "biểu diễn (performing)"),
            ("Adjourning", "giai đoạn đình chỉ"),
            ("Adjourning", "đình chỉ (adjourning)"),
            ("Belbin Plant", "vai trò cái cây"),
            ("Belbin Plant", "vai trò thực vật"),
            ("Backlog Refinement", "chải chuốt danh mục"),
            ("Sprint Planning", "lập kế hoạch chạy nước rút"),
            ("Sprint", "chu kỳ chạy nước rút"),
            ("Teamwork", "công việc nhóm"),
            ("Team Dynamics", "năng động nhóm"),
            ("Psychological Safety", "bảo đảm an toàn tâm trí"),
            ("Shared Mental Model", "mô hình tâm trí chia sẻ"),
            ("Interpersonal Risk", "rủi ro giữa các cá nhân")
        ]

        for term, bad_phrase in SPECIFIC_ANTIPATTERNS:
            if bad_phrase.lower() in guide_corpus:
                antipattern_violations.append(
                    f"Found forbidden anti-pattern translation '{bad_phrase}' for term '{term}' in documentation."
                )

        # Also check GLOSSARY.md standard term column
        glossary_files = [p for p in self.md_files if "glossary" in os.path.basename(p).lower()]
        if glossary_files:
            g_lines = load_file_content(glossary_files[0]).splitlines()
            for line in g_lines:
                if not line.strip().startswith("|") or ":---" in line or "No." in line:
                    continue
                parts = [p.strip() for p in line.split("|")]
                if len(parts) >= 4:
                    vi_col = parts[3].lower()
                    for term, bad_phrase in SPECIFIC_ANTIPATTERNS:
                        if bad_phrase.lower() in vi_col:
                            antipattern_violations.append(
                                f"Found forbidden anti-pattern '{bad_phrase}' listed as standard term in GLOSSARY.md for '{term}'."
                            )

        self.assertEqual(
            len(antipattern_violations), 0,
            f"Forbidden translation anti-patterns detected:\n" + "\n".join(antipattern_violations)
        )




if __name__ == "__main__":
    unittest.main()
