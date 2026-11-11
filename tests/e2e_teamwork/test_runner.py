#!/usr/bin/env python3
"""
Comprehensive 4-Tier Automated Test Runner for Bilingual Teamwork Documentation Set.
Author: test_writer_e2e_1
Environment: /usr/bin/python3.11

Runs all 4 test tiers:
- Tier 1: Feature & Conceptual Coverage (assert all 21 features in EN and VI)
- Tier 2: Boundary & Linguistic Quality (Jaccard < 0.5%, zero dummy strings, diacritics > 15%, balanced fences, control chars)
- Tier 3: Cross-Feature Symmetry & Parity (heading symmetry, paragraph parity, 65-term glossary conformance)
- Tier 4: Real-World Scenarios & Delivery (agent_critic check, teamwork_bilingual.zip archive verification)

Usage:
  /usr/bin/python3.11 tests/e2e_teamwork/test_runner.py
  /usr/bin/python3.11 tests/e2e_teamwork/test_runner.py --tier 1
  /usr/bin/python3.11 tests/e2e_teamwork/test_runner.py --target-dir /path/to/docs
  /usr/bin/python3.11 tests/e2e_teamwork/test_runner.py --self-test
"""

import os
import sys
import time
import json
import tempfile
import argparse
import unittest
from typing import Dict, List, Any, Optional

# Add test suite directory to path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

from test_utils import (
    DEFAULT_TARGET_DIR,
    DEFAULT_ARCHIVE_PATH,
    create_synthetic_valid_documentation
)

from test_tier1_features import TestTier1Features
from test_tier2_boundaries import TestTier2Boundaries
from test_tier3_cross_feature import TestTier3CrossFeature
from test_tier4_scenarios import TestTier4Scenarios

# ANSI styling helpers
USE_COLOR = sys.stdout.isatty() and not os.environ.get("NO_COLOR")

def color_text(text: str, color_code: str) -> str:
    if not USE_COLOR:
        return text
    return f"\033[{color_code}m{text}\033[0m"

def green(text: str) -> str:
    return color_text(text, "32;1")

def red(text: str) -> str:
    return color_text(text, "31;1")

def yellow(text: str) -> str:
    return color_text(text, "33;1")

def cyan(text: str) -> str:
    return color_text(text, "36;1")

def bold(text: str) -> str:
    return color_text(text, "1")


class DetailedTestResult(unittest.TestResult):
    """Custom test result collector capturing timing, status, and failure details per test."""

    def __init__(self):
        super().__init__()
        self.test_records: List[Dict[str, Any]] = []
        self._start_time = 0.0

    def startTest(self, test: unittest.TestCase):
        super().startTest(test)
        self._start_time = time.time()

    def addSuccess(self, test: unittest.TestCase):
        super().addSuccess(test)
        duration = time.time() - self._start_time
        self.test_records.append({
            "test": test.id(),
            "name": test._testMethodName,
            "class": test.__class__.__name__,
            "status": "PASS",
            "duration": duration,
            "error": None
        })

    def addFailure(self, test: unittest.TestCase, err):
        super().addFailure(test, err)
        duration = time.time() - self._start_time
        err_msg = self._exc_info_to_string(err, test)
        self.test_records.append({
            "test": test.id(),
            "name": test._testMethodName,
            "class": test.__class__.__name__,
            "status": "FAIL",
            "duration": duration,
            "error": err_msg
        })

    def addError(self, test: unittest.TestCase, err):
        super().addError(test, err)
        duration = time.time() - self._start_time
        err_msg = self._exc_info_to_string(err, test)
        self.test_records.append({
            "test": test.id(),
            "name": test._testMethodName,
            "class": test.__class__.__name__,
            "status": "ERROR",
            "duration": duration,
            "error": err_msg
        })


def build_suite(tier_selection: str = "all") -> unittest.TestSuite:
    """Builds test suite based on requested tier selection."""
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    tier_map = {
        "1": (TestTier1Features, "Tier 1: Feature Coverage (21 Features in EN and VI)"),
        "2": (TestTier2Boundaries, "Tier 2: Linguistic & Boundary Quality (Jaccard, Diacritics, Stubs)"),
        "3": (TestTier3CrossFeature, "Tier 3: Cross-Feature Symmetry & Parity (Headings, Paragraphs, Glossary)"),
        "4": (TestTier4Scenarios, "Tier 4: Delivery Scenarios (agent_critic, Zip Archive Integrity)")
    }

    if tier_selection == "all":
        selected_tiers = ["1", "2", "3", "4"]
    else:
        selected_tiers = [t.strip() for t in tier_selection.split(",") if t.strip() in tier_map]

    for t in selected_tiers:
        test_cls, _ = tier_map[t]
        suite.addTests(loader.loadTestsFromTestCase(test_cls))

    return suite


def run_tests(target_dir: str, archive_path: str, tier_selection: str = "all", verbose: bool = False) -> Dict[str, Any]:
    """Executes the test suite against target_dir and archive_path."""
    os.environ["TEAMWORK_DIR"] = target_dir
    os.environ["TEAMWORK_ARCHIVE"] = archive_path

    # Reload classes so setUpClass reads updated env vars
    TestTier1Features.setUpClass()
    TestTier2Boundaries.setUpClass()
    TestTier3CrossFeature.setUpClass()
    TestTier4Scenarios.setUpClass()

    suite = build_suite(tier_selection)
    result = DetailedTestResult()

    start_wall = time.time()
    suite.run(result)
    total_duration = time.time() - start_wall

    tier_breakdown: Dict[str, Dict[str, int]] = {
        "Tier 1 (Features)": {"total": 0, "pass": 0, "fail": 0},
        "Tier 2 (Boundaries)": {"total": 0, "pass": 0, "fail": 0},
        "Tier 3 (Cross-Feature)": {"total": 0, "pass": 0, "fail": 0},
        "Tier 4 (Scenarios)": {"total": 0, "pass": 0, "fail": 0}
    }

    class_to_tier = {
        "TestTier1Features": "Tier 1 (Features)",
        "TestTier2Boundaries": "Tier 2 (Boundaries)",
        "TestTier3CrossFeature": "Tier 3 (Cross-Feature)",
        "TestTier4Scenarios": "Tier 4 (Scenarios)"
    }

    for record in result.test_records:
        t_tier = class_to_tier.get(record["class"], "Other")
        if t_tier in tier_breakdown:
            tier_breakdown[t_tier]["total"] += 1
            if record["status"] == "PASS":
                tier_breakdown[t_tier]["pass"] += 1
            else:
                tier_breakdown[t_tier]["fail"] += 1

    summary = {
        "target_dir": target_dir,
        "archive_path": archive_path,
        "tier_selection": tier_selection,
        "total_tests": result.testsRun,
        "passed": len(result.test_records) - len(result.failures) - len(result.errors),
        "failed": len(result.failures),
        "errors": len(result.errors),
        "duration_seconds": total_duration,
        "all_passed": (len(result.failures) == 0 and len(result.errors) == 0),
        "tier_breakdown": tier_breakdown,
        "records": result.test_records
    }
    return summary


def print_report(summary: Dict[str, Any], verbose: bool = False):
    """Prints a beautiful, structured terminal report."""
    print("=" * 80)
    print(bold(cyan(" BILINGUAL TEAMWORK DOCUMENTATION E2E TEST SUITE REPORT ")))
    print("=" * 80)
    print(f" Target Directory : {summary['target_dir']}")
    print(f" Archive Target   : {summary['archive_path']}")
    print(f" Tiers Executed   : {summary['tier_selection']}")
    print("-" * 80)

    print(f" {'Tier / Test Group':<30} | {'Total':<6} | {'Pass':<6} | {'Fail/Error':<10} | {'Status':<10}")
    print("-" * 80)

    for tier_name, stats in summary["tier_breakdown"].items():
        if stats["total"] == 0:
            continue
        status_str = green("PASS") if stats["fail"] == 0 and stats["total"] > 0 else red("FAIL")
        print(f" {tier_name:<30} | {stats['total']:<6} | {stats['pass']:<6} | {stats['fail']:<10} | {status_str}")

    print("-" * 80)
    overall_status = green("ALL TESTS PASSED") if summary["all_passed"] else red("TEST FAILURES DETECTED")
    print(f" Total Tests : {summary['total_tests']}")
    print(f" Passed      : {green(str(summary['passed']))}")
    print(f" Failed      : {red(str(summary['failed']))}")
    print(f" Errors      : {red(str(summary['errors']))}")
    print(f" Duration    : {summary['duration_seconds']:.2f}s")
    print(f" Verdict     : {overall_status}")
    print("=" * 80)

    # If failures exist or verbose, print detailed test cases
    failures = [r for r in summary["records"] if r["status"] != "PASS"]
    if failures:
        print(bold(red("\n--- FAILURE DIAGNOSTICS ---")))
        for f in failures:
            print(f"\n[{red(f['status'])}] {bold(f['class'])}.{f['name']} ({f['duration']:.3f}s)")
            if f["error"]:
                # Print concise failure reason
                err_lines = [l for l in f["error"].splitlines() if l.strip()]
                for l in err_lines[-4:]:
                    print(f"    {l}")
        print("=" * 80)
    elif verbose:
        print(bold(green("\n--- ALL TESTS COMPLETED SUCCESSFULLY ---")))
        for r in summary["records"]:
            print(f"  [{green('OK')}] {r['class']}.{r['name']} ({r['duration']:.3f}s)")
        print("=" * 80)


def run_self_test() -> bool:
    """
    Executes a comprehensive self-test using a synthetic compliant documentation fixture
    to mathematically verify the correctness of the test harness itself.
    """
    print(bold(cyan("\n>>> RUNNING TEST HARNESS SELF-VERIFICATION (Synthetic Fixture Mode)...")))
    with tempfile.TemporaryDirectory() as tmp_dir:
        archive_path = create_synthetic_valid_documentation(tmp_dir)
        summary = run_tests(tmp_dir, archive_path, tier_selection="all", verbose=False)
        print_report(summary, verbose=False)

        if not summary["all_passed"]:
            print(red("SELF-TEST FAILED: Synthetic compliant fixture did not pass all assertions!"))
            return False

        print(green("SELF-TEST PASSED: Test harness accurately validates fully compliant bilingual documentation suites!"))
        return True


def main():
    parser = argparse.ArgumentParser(description="4-Tier E2E Test Runner for Bilingual Teamwork Documentation")
    parser.add_argument("--target-dir", default=DEFAULT_TARGET_DIR, help="Path to documentation directory")
    parser.add_argument("--archive", default=DEFAULT_ARCHIVE_PATH, help="Path to teamwork_bilingual.zip")
    parser.add_argument("--tier", default="all", help="Tiers to run (1, 2, 3, 4, or 'all')")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose test execution details")
    parser.add_argument("--json", dest="json_path", default=None, help="Save summary report to JSON file")
    parser.add_argument("--self-test", action="store_true", help="Run self-verification against synthetic valid fixture")

    args = parser.parse_args()

    if args.self_test:
        success = run_self_test()
        sys.exit(0 if success else 1)

    summary = run_tests(
        target_dir=os.path.abspath(args.target_dir),
        archive_path=os.path.abspath(args.archive),
        tier_selection=args.tier,
        verbose=args.verbose
    )

    print_report(summary, verbose=args.verbose)

    if args.json_path:
        with open(args.json_path, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2)
        print(f"Saved JSON report to {args.json_path}")

    sys.exit(0 if summary["all_passed"] else 1)


if __name__ == "__main__":
    main()
