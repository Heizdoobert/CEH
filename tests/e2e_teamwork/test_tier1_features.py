#!/usr/bin/env python3
"""
Tier 1: Feature & Conceptual Coverage Test Suite
Validates that all 21 features from the Feature Inventory are thoroughly
covered in both English and Vietnamese across the documentation corpus.
"""

import os
import unittest
from typing import List, Dict

try:
    from test_utils import (
        get_target_dir,
        get_markdown_files,
        load_file_content,
        FEATURE_INVENTORY_21
    )
except ImportError:
    from tests.e2e_teamwork.test_utils import (
        get_target_dir,
        get_markdown_files,
        load_file_content,
        FEATURE_INVENTORY_21
    )


class TestTier1Features(unittest.TestCase):
    """
    Tier 1 tests asserting coverage of all 21 core teamwork features in EN and VI.
    """

    @classmethod
    def setUpClass(cls):
        cls.target_dir = get_target_dir()
        cls.md_files = get_markdown_files(cls.target_dir)
        cls.corpus = ""
        cls.corpus_lower = ""
        if cls.md_files:
            cls.corpus = "\n\n".join(load_file_content(p) for p in cls.md_files)
            cls.corpus_lower = cls.corpus.lower()

    def _require_corpus(self):
        """Enforces that the target directory contains non-empty markdown files."""
        self.assertTrue(
            os.path.exists(self.target_dir),
            f"Target directory does not exist: {self.target_dir}"
        )
        self.assertGreater(
            len(self.md_files), 0,
            f"No markdown files found in target directory: {self.target_dir}. Target directory is currently empty."
        )
        self.assertGreater(
            len(self.corpus.strip()), 100,
            f"Documentation corpus in {self.target_dir} is empty or under 100 characters."
        )

    def _assert_keywords_bilingual(self, feature_id: int, en_req: List[str], vi_req: List[str], min_en: int = 2, min_vi: int = 2):
        """Helper to assert required keywords are present in both languages."""
        self._require_corpus()
        en_found = [k for k in en_req if k.lower() in self.corpus_lower]
        vi_found = [k for k in vi_req if k.lower() in self.corpus_lower]

        self.assertGreaterEqual(
            len(en_found), min_en,
            f"Feature {feature_id} missing required English concepts. Found {en_found}, expected at least {min_en} of {en_req}."
        )
        self.assertGreaterEqual(
            len(vi_found), min_vi,
            f"Feature {feature_id} missing required Vietnamese concepts. Found {vi_found}, expected at least {min_vi} of {vi_req}."
        )

    def test_feature_01_foundations_and_definitions(self):
        """Feature 1: Katzenbach & Smith definition, Working Group vs True Team, synergy, mutual accountability."""
        en_keys = ["Katzenbach", "Smith", "Working Group", "True Team", "Synergy", "Mutual Accountability"]
        vi_keys = ["Katzenbach", "Smith", "nhóm làm việc", "đội nhóm thực thụ", "cộng hưởng", "trách nhiệm chung"]
        self._assert_keywords_bilingual(1, en_keys, vi_keys, min_en=3, min_vi=3)

    def test_feature_02_tuckman_model(self):
        """Feature 2: Tuckman 5-Stage Model (Forming, Storming, Norming, Performing, Adjourning)."""
        en_keys = ["Tuckman", "Forming", "Storming", "Norming", "Performing", "Adjourning"]
        vi_keys = ["Tuckman", "Hình thành", "Xung đột", "Chuẩn hóa", "Thực thi", "Giải tán"]
        self._assert_keywords_bilingual(2, en_keys, vi_keys, min_en=4, min_vi=4)

    def test_feature_03_psychological_safety(self):
        """Feature 3: Psychological Safety (Google Project Aristotle, Amy Edmondson, interpersonal risk)."""
        en_keys = ["Aristotle", "Amy Edmondson", "Psychological Safety", "Interpersonal Risk"]
        vi_keys = ["Aristotle", "Amy Edmondson", "An toàn tâm lý", "Rủi ro giao tiếp liên cá nhân"]
        self._assert_keywords_bilingual(3, en_keys, vi_keys, min_en=3, min_vi=3)

    def test_feature_04_lencioni_5_dysfunctions(self):
        """Feature 4: Lencioni 5 Dysfunctions (Trust, Conflict, Commitment, Accountability, Results)."""
        en_keys = ["Lencioni", "Absence of Trust", "Fear of Conflict", "Lack of Commitment", "Avoidance of Accountability", "Inattention to Results"]
        vi_keys = ["Lencioni", "Thiếu vắng sự tin tưởng", "Nỗi sợ xung đột", "Thiếu cam kết", "Né tránh trách nhiệm giải trình", "Không chú trọng đến kết quả"]
        self._assert_keywords_bilingual(4, en_keys, vi_keys, min_en=4, min_vi=4)

    def test_feature_05_core_team_roles(self):
        """Feature 5: Core Team Roles (Team Leader, Facilitator, Contributor / IC)."""
        en_keys = ["Team Leader", "Facilitator", "Contributor", "Individual Contributor"]
        vi_keys = ["Trưởng nhóm", "Người điều phối", "đóng góp chuyên môn", "IC"]
        self._assert_keywords_bilingual(5, en_keys, vi_keys, min_en=2, min_vi=2)

    def test_feature_06_belbin_9_team_roles(self):
        """Feature 6: Belbin 9 Team Roles across Action, People, and Thought categories."""
        en_keys = ["Belbin", "Shaper", "Implementer", "Completer Finisher", "Coordinator", "Teamworker", "Resource Investigator", "Plant", "Monitor Evaluator", "Specialist"]
        vi_keys = ["Belbin", "Định hình", "Triển khai", "Hoàn thiện chu toàn", "Điều phối viên", "Gắn kết", "Khai thác nguồn lực", "Kiến tạo ý tưởng", "đánh giá phản biện", "Chuyên gia"]
        self._assert_keywords_bilingual(6, en_keys, vi_keys, min_en=5, min_vi=5)

    def test_feature_07_raci_matrix(self):
        """Feature 7: RACI Responsibility Matrix (Responsible, Accountable, Consulted, Informed)."""
        en_keys = ["RACI", "Responsible", "Accountable", "Consulted", "Informed"]
        vi_keys = ["RACI", "Thực hiện", "Chịu trách nhiệm", "Tham vấn", "Nhận thông tin"]
        self._assert_keywords_bilingual(7, en_keys, vi_keys, min_en=3, min_vi=3)

    def test_feature_08_process_lifecycle(self):
        """Feature 8: Process Lifecycle (Planning, Execution, Review/Retrospective 3-stage loop)."""
        en_keys = ["Planning", "Execution", "Review", "Retrospective", "inspect-and-adapt"]
        vi_keys = ["Hoạch định", "Thực thi", "Đánh giá", "Cải tiến nội bộ", "kiểm tra và thích ứng"]
        self._assert_keywords_bilingual(8, en_keys, vi_keys, min_en=3, min_vi=3)

    def test_feature_09_agile_scrum_ceremonies(self):
        """Feature 9: Agile Frameworks (Scrum 5 ceremonies)."""
        en_keys = ["Scrum", "Sprint Planning", "Daily Standup", "Refinement", "Sprint Review", "Sprint Retrospective"]
        vi_keys = ["Scrum", "Hoạch định", "Họp đứng", "Tinh chỉnh", "Đánh giá", "Cải tiến nội bộ"]
        self._assert_keywords_bilingual(9, en_keys, vi_keys, min_en=4, min_vi=4)

    def test_feature_10_agile_kanban_wip_littles_law(self):
        """Feature 10: Agile Frameworks (Kanban WIP limits, Little's Law, CFD)."""
        en_keys = ["Kanban", "WIP", "Little's Law", "Throughput", "Lead Time"]
        vi_keys = ["Kanban", "WIP", "khối lượng đang thực hiện", "Định luật Little", "thông lượng"]
        self._assert_keywords_bilingual(10, en_keys, vi_keys, min_en=3, min_vi=3)

    def test_feature_11_communication_tools_and_matrix(self):
        """Feature 11: Communication Tools (Sync vs Async matrix, Meeting hygiene, WWW schema)."""
        en_keys = ["Synchronous", "Asynchronous", "Meeting Hygiene", "WWW", "Chat"]
        vi_keys = ["đồng bộ", "bất đồng bộ", "kỷ luật cuộc họp", "WWW"]
        self._assert_keywords_bilingual(11, en_keys, vi_keys, min_en=3, min_vi=2)

    def test_feature_12_documentation_cultures_rfc_adr(self):
        """Feature 12: Documentation Cultures (Single Source of Truth SSOT, RFC, ADR)."""
        en_keys = ["Single Source of Truth", "SSOT", "RFC", "Request for Comments", "ADR", "Architecture Decision Record"]
        vi_keys = ["chân lý duy nhất", "SSOT", "RFC", "đề xuất kỹ thuật", "ADR", "quyết định kiến trúc"]
        self._assert_keywords_bilingual(12, en_keys, vi_keys, min_en=3, min_vi=3)

    def test_feature_13_conflict_resolution_tki_5_modes(self):
        """Feature 13: Conflict Resolution (Thomas-Kilmann Instrument 5 modes)."""
        en_keys = ["Thomas-Kilmann", "TKI", "Competing", "Collaborating", "Compromising", "Avoiding", "Accommodating"]
        vi_keys = ["Thomas-Kilmann", "TKI", "Cạnh tranh", "Hợp tác", "Thỏa hiệp", "Né tránh", "Nhượng bộ"]
        self._assert_keywords_bilingual(13, en_keys, vi_keys, min_en=4, min_vi=4)

    def test_feature_14_conflict_resolution_ibr_and_nvc(self):
        """Feature 14: Conflict Resolution (Interest-Based Relational IBR and Nonviolent Communication NVC OFNR)."""
        en_keys = ["Interest-Based Relational", "IBR", "BATNA", "Nonviolent Communication", "NVC", "OFNR"]
        vi_keys = ["lợi ích và quan hệ", "IBR", "BATNA", "Giao tiếp trắc ẩn", "NVC", "QCNY"]
        self._assert_keywords_bilingual(14, en_keys, vi_keys, min_en=3, min_vi=3)

    def test_feature_15_crucial_conversations_state(self):
        """Feature 15: Crucial Conversations (STATE model)."""
        en_keys = ["Crucial Conversations", "STATE", "Share facts", "Tell your story", "Ask", "Talk tentatively", "Encourage testing"]
        vi_keys = ["đối thoại then chốt", "STATE", "sự thật", "câu chuyện", "hỏi", "thận trọng", "phản biện"]
        self._assert_keywords_bilingual(15, en_keys, vi_keys, min_en=2, min_vi=2)

    def test_feature_16_case_study_apollo_13(self):
        """Feature 16: Case Study 1: Apollo 13 crisis operations and LiOH canister prototyping."""
        en_keys = ["Apollo 13", "Gene Kranz", "White Team", "Tiger Team", "LiOH", "canister"]
        vi_keys = ["Apollo 13", "Gene Kranz", "White Team", "Tiger Team", "LiOH"]
        self._assert_keywords_bilingual(16, en_keys, vi_keys, min_en=3, min_vi=2)

    def test_feature_17_case_study_pixar_braintrust(self):
        """Feature 17: Case Study 2: Pixar Braintrust (Candor, Plus-ing, decoupling critique from authority)."""
        en_keys = ["Pixar", "Braintrust", "Candor", "Plus-ing", "critique"]
        vi_keys = ["Pixar", "Braintrust", "thẳng thắn", "Candor", "Plus-ing", "phản biện"]
        self._assert_keywords_bilingual(17, en_keys, vi_keys, min_en=3, min_vi=3)

    def test_feature_18_case_study_aviation_healthcare_crm(self):
        """Feature 18: Case Study 3: Aviation CRM & Healthcare Surgical Checklists (Two-Challenge Rule, PACE, WHO)."""
        en_keys = ["Crew Resource Management", "CRM", "Two-Challenge Rule", "PACE", "WHO", "Surgical Checklist"]
        vi_keys = ["CRM", "nguồn lực phi hành đoàn", "thách thức", "PACE", "WHO", "phẫu thuật", "bảng kiểm"]
        self._assert_keywords_bilingual(18, en_keys, vi_keys, min_en=3, min_vi=3)

    def test_feature_19_mnemonic_aids_and_active_recall(self):
        """Feature 19: Dual-Language Mnemonics and Active-Recall Challenge QA blocks."""
        en_keys = ["Mnemonic", "Active-Recall", "TUCK", "CLEAR", "SMART"]
        vi_keys = ["Thuật ghi nhớ", "gợi nhớ tích cực", "TUCK", "CLEAR", "ĐO ĐƯỢC"]
        self._assert_keywords_bilingual(19, en_keys, vi_keys, min_en=3, min_vi=2)

    def test_feature_20_canonical_bilingual_glossary(self):
        """Feature 20: Canonical Bilingual Glossary (65 terms across 6 domains in GLOSSARY.md)."""
        self._require_corpus()
        glossary_files = [p for p in self.md_files if "glossary" in os.path.basename(p).lower()]
        self.assertGreater(
            len(glossary_files), 0,
            "No GLOSSARY.md file found in target documentation directory."
        )
        glossary_text = load_file_content(glossary_files[0])
        # Assert glossary contains substantial length and English-Vietnamese table mapping
        self.assertGreater(len(glossary_text), 3000, "GLOSSARY.md is smaller than 3KB.")
        self.assertIn("|", glossary_text, "GLOSSARY.md must contain markdown terminology tables.")

    def test_feature_21_final_packaging_and_critic(self):
        """Feature 21: Final packaging requirements, master guide deliverable, and README."""
        self._require_corpus()
        file_basenames = [os.path.basename(p) for p in self.md_files]
        self.assertTrue(
            any("guide" in f.lower() or "teamwork" in f.lower() or f.startswith("0") for f in file_basenames),
            f"Comprehensive teamwork guide markdown files not found in {file_basenames}"
        )
        self.assertTrue(
            any("readme" in f.lower() for f in file_basenames),
            f"README.md navigation file not found in {file_basenames}"
        )

    def test_all_21_features_presence_summary(self):
        """Comprehensive verification that all 21 features from Feature Inventory are accounted for."""
        self._require_corpus()
        missing_features = []
        for feat in FEATURE_INVENTORY_21:
            fid = feat["id"]
            fname = feat["name"]
            en_found = [k for k in feat["en_keywords"] if k.lower() in self.corpus_lower]
            vi_found = [k for k in feat["vi_keywords"] if k.lower() in self.corpus_lower]
            if len(en_found) < 1 or len(vi_found) < 1:
                missing_features.append(f"Feature {fid} ({fname}): EN={len(en_found)} found, VI={len(vi_found)} found")

        self.assertEqual(
            len(missing_features), 0,
            f"Deficiencies discovered in feature inventory coverage:\n" + "\n".join(missing_features)
        )


if __name__ == "__main__":
    unittest.main()
