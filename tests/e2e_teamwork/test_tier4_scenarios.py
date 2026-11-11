#!/usr/bin/env python3
"""
Tier 4: Real-World Scenarios, Tooling & Delivery Packaging Test Suite
Validates external acceptance criteria, agent_critic static compliance,
and deployment zip packaging integrity:
1. agent_critic Check: Every markdown file scores 100/100 without diagnostics or rule violations.
2. Zip Archive Integrity: teamwork_bilingual.zip exists, is valid, uncorrupted, and contains all deliverables.
3. End-to-End Extraction Scenario: Clean extraction and structure reproduction in a staging environment.
"""

import os
import zipfile
import tempfile
import unittest
from typing import List

try:
    from test_utils import (
        get_target_dir,
        get_archive_path,
        get_markdown_files,
        load_file_content,
        run_agent_critic
    )
except ImportError:
    from tests.e2e_teamwork.test_utils import (
        get_target_dir,
        get_archive_path,
        get_markdown_files,
        load_file_content,
        run_agent_critic
    )


class TestTier4Scenarios(unittest.TestCase):
    """
    Tier 4 tests validating static critic audit compliance and final delivery packaging.
    """

    @classmethod
    def setUpClass(cls):
        cls.target_dir = get_target_dir()
        cls.archive_path = get_archive_path()
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

    def test_agent_critic_score_100(self):
        """
        Verify that all markdown files in target directory pass agent_critic with 100.0/100 score.
        """
        self._require_files()
        critic_results = {}
        for fpath in self.md_files:
            fname = os.path.basename(fpath)
            res = run_agent_critic(fpath)
            critic_results[fname] = res

            status = res.get("status", "FAIL")
            score = float(res.get("score", 0.0))
            diagnostics = res.get("diagnostics", [])

            self.assertEqual(
                status, "PASS",
                f"File {fname} failed agent_critic: status={status}, diagnostics={diagnostics}"
            )
            self.assertEqual(
                score, 100.0,
                f"File {fname} did not achieve 100/100 on agent_critic. Score: {score}/100, Diagnostics: {diagnostics}"
            )

    def test_zip_archive_existence_and_integrity(self):
        """
        Verify that teamwork_bilingual.zip exists, is a valid zipfile, and passes testzip() integrity test.
        """
        self.assertTrue(
            os.path.isfile(self.archive_path),
            f"Zip archive does not exist at expected path: {self.archive_path}"
        )
        self.assertTrue(
            zipfile.is_zipfile(self.archive_path),
            f"File is not a valid zip archive: {self.archive_path}"
        )

        with zipfile.ZipFile(self.archive_path, 'r') as zf:
            bad_file = zf.testzip()
            self.assertIsNone(
                bad_file,
                f"Zip archive contains corrupted file entry: {bad_file}"
            )

            file_list = zf.namelist()
            self.assertGreater(
                len(file_list), 0,
                f"Zip archive {self.archive_path} is empty."
            )

            md_entries = [f for f in file_list if f.endswith(".md")]
            self.assertGreater(
                len(md_entries), 0,
                f"Zip archive contains no markdown documentation files. Contents: {file_list}"
            )

        archive_size = os.path.getsize(self.archive_path)
        self.assertGreater(
            archive_size, 5000,
            f"Zip archive is suspiciously small: {archive_size} bytes (minimum 5,000 bytes expected)."
        )

    def test_deliverable_artifacts_presence(self):
        """
        Verify that all expected deliverable markdown files are present in target directory:
        1. Master teamwork comprehensive guide
        2. Canonical GLOSSARY.md
        3. README.md navigation index
        """
        self._require_files()
        basenames = [os.path.basename(p).lower() for p in self.md_files]

        has_guide = any("guide" in b or "teamwork" in b or b.startswith("0") for b in basenames)
        has_glossary = any("glossary" in b for b in basenames)
        has_readme = any("readme" in b for b in basenames)

        self.assertTrue(
            has_guide,
            f"Comprehensive teamwork guide markdown files missing. Available files: {basenames}"
        )
        self.assertTrue(
            has_glossary,
            f"Canonical GLOSSARY.md missing. Available files: {basenames}"
        )
        self.assertTrue(
            has_readme,
            f"README.md missing. Available files: {basenames}"
        )

    def test_end_to_end_extraction_scenario(self):
        """
        Simulate an end-to-end user scenario:
        Extract the archive into an isolated temporary directory,
        verify file presence, readability, and content non-emptiness.
        """
        self.assertTrue(
            os.path.isfile(self.archive_path),
            f"Archive file not found for extraction test: {self.archive_path}"
        )

        with tempfile.TemporaryDirectory() as tmp_dir:
            with zipfile.ZipFile(self.archive_path, 'r') as zf:
                zf.extractall(tmp_dir)

            extracted_files = []
            for root, _, files in os.walk(tmp_dir):
                for f in files:
                    extracted_files.append(os.path.join(root, f))

            self.assertGreater(
                len(extracted_files), 0,
                "Extracted directory is completely empty."
            )

            md_extracted = [f for f in extracted_files if f.endswith(".md")]
            self.assertGreater(
                len(md_extracted), 0,
                "No markdown files found after extraction."
            )

            for f in md_extracted:
                size = os.path.getsize(f)
                self.assertGreater(size, 500, f"Extracted file {os.path.basename(f)} is empty or under 500 bytes.")


if __name__ == "__main__":
    unittest.main()
