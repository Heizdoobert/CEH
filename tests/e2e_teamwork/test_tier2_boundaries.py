#!/usr/bin/env python3
"""
Tier 2: Boundary & Linguistic Quality Test Suite
Validates strict boundary conditions and quality invariants across all documentation files:
1. Pairwise Line Jaccard Similarity < 0.5% (asserts zero verbatim copy-paste duplication).
2. Zero forbidden dummy / placeholder strings (TODO, TBD, FIXME, stubs, etc.).
3. Vietnamese Diacritics Density > 15.0%.
4. Balanced markdown code fences with explicit syntax language tags.
5. Zero illegal ASCII control characters (C0 control chars except \\t, \\n, \\r, zero form feeds, zero bells, zero null bytes).
"""

import os
import unittest
from typing import List

try:
    from test_utils import (
        get_target_dir,
        get_markdown_files,
        load_file_content,
        load_file_bytes,
        compute_jaccard_similarity,
        compute_diacritic_density,
        scan_forbidden_patterns,
        validate_code_fences,
        check_illegal_bytes
    )
except ImportError:
    from tests.e2e_teamwork.test_utils import (
        get_target_dir,
        get_markdown_files,
        load_file_content,
        load_file_bytes,
        compute_jaccard_similarity,
        compute_diacritic_density,
        scan_forbidden_patterns,
        validate_code_fences,
        check_illegal_bytes
    )


class TestTier2Boundaries(unittest.TestCase):
    """
    Tier 2 tests enforcing linguistic quality, boundary constraints, and structural cleanliness.
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

    def test_pairwise_line_jaccard_similarity(self):
        """
        Verify Jaccard similarity between English lines and Vietnamese lines is strictly < 0.5%.
        Also verifies intersection set is empty (0 identical lines).
        """
        self._require_files()
        for fpath in self.md_files:
            fname = os.path.basename(fpath)
            content = load_file_content(fpath)
            jaccard_pct, inter = compute_jaccard_similarity(content)

            self.assertLess(
                jaccard_pct, 0.5,
                f"File {fname} has Jaccard similarity {jaccard_pct:.4f}% >= 0.5% threshold. "
                f"Duplicated lines: {list(inter)[:5]}"
            )
            self.assertEqual(
                len(inter), 0,
                f"File {fname} contains verbatim identical lines in both EN and VI sets: {list(inter)[:5]}"
            )

    def test_zero_forbidden_dummy_strings(self):
        """
        Verify complete absence of forbidden placeholder and dummy strings
        (TODO, TBD, FIXME, stubs, lorem ipsum, 'Vietnamese translation of:', etc.).
        """
        self._require_files()
        violations = {}
        for fpath in self.md_files:
            fname = os.path.basename(fpath)
            content = load_file_content(fpath)
            matches = scan_forbidden_patterns(content)
            if matches:
                violations[fname] = matches

        self.assertEqual(
            len(violations), 0,
            f"Forbidden dummy strings found in documentation files: {violations}"
        )

    def test_vietnamese_diacritic_density(self):
        """
        Verify Vietnamese diacritics density ratio exceeds 15.0% across the documentation.
        """
        self._require_files()
        for fpath in self.md_files:
            fname = os.path.basename(fpath)
            content = load_file_content(fpath)
            density, vn_words, total_words = compute_diacritic_density(content)

            # Files like GLOSSARY or master guide must have healthy Vietnamese vocabulary
            self.assertGreater(
                density, 15.0,
                f"File {fname} has insufficient Vietnamese diacritic density: {density:.2f}% "
                f"({vn_words}/{total_words} words). Expected > 15.0%."
            )

    def test_markdown_code_fences_and_syntax_tags(self):
        """
        Verify all markdown code fences are balanced and all opening fences have explicit syntax language tags.
        """
        self._require_files()
        for fpath in self.md_files:
            fname = os.path.basename(fpath)
            content = load_file_content(fpath)
            is_valid, errors = validate_code_fences(content)

            self.assertTrue(
                is_valid,
                f"File {fname} has invalid code fences:\n" + "\n".join(errors)
            )

    def test_zero_illegal_ascii_control_characters(self):
        """
        Verify zero illegal ASCII control characters (< 32, excluding \\t, \\n, \\r),
        zero null bytes, zero form feeds (0x0c), and zero bell characters (0x07).
        """
        self._require_files()
        for fpath in self.md_files:
            fname = os.path.basename(fpath)
            raw_bytes = load_file_bytes(fpath)
            is_clean, errors = check_illegal_bytes(raw_bytes)

            self.assertTrue(
                is_clean,
                f"File {fname} contains illegal binary/control characters:\n" + "\n".join(errors)
            )

    def test_file_size_and_volume_minimums(self):
        """
        Verify files are non-empty and satisfy minimum volume sanity thresholds
        based on deliverable artifact roles.
        """
        self._require_files()
        for fpath in self.md_files:
            fname = os.path.basename(fpath).lower()
            size = os.path.getsize(fpath)
            content = load_file_content(fpath)
            lines = content.splitlines()

            if "guide" in fname or "teamwork" in fname:
                self.assertGreater(
                    size, 5000,
                    f"Master guide {fname} is suspiciously small: {size} bytes (minimum 5,000 bytes)."
                )
                self.assertGreater(
                    len(lines), 100,
                    f"Master guide {fname} has too few lines: {len(lines)} lines (minimum 100 lines)."
                )
            elif "glossary" in fname:
                self.assertGreater(
                    size, 3000,
                    f"Glossary {fname} is suspiciously small: {size} bytes (minimum 3,000 bytes)."
                )
                self.assertGreater(
                    len(lines), 50,
                    f"Glossary {fname} has too few lines: {len(lines)} lines (minimum 50 lines)."
                )
            elif "readme" in fname:
                self.assertGreater(
                    size, 500,
                    f"README {fname} is suspiciously small: {size} bytes (minimum 500 bytes)."
                )
                self.assertGreater(
                    len(lines), 15,
                    f"README {fname} has too few lines: {len(lines)} lines (minimum 15 lines)."
                )
            else:
                self.assertGreater(size, 500, f"File {fname} is under 500 bytes.")
                self.assertGreater(len(lines), 15, f"File {fname} has fewer than 15 lines.")



if __name__ == "__main__":
    unittest.main()
