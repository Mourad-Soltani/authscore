# AuthScore Health Tests
# Signature: Mourad.Soltani
# These tests must pass for the minimal complete codebase.

import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from authscore import score_domain, check_spf, check_dmarc

class TestAuthScore(unittest.TestCase):
    def test_perfect_score(self):
        records = ["v=spf1 include:_spf.google.com ~all", "v=DMARC1; p=reject; rua=mailto:dmarc@example.com"]
        result = score_domain("example.com", mock_records=records)
        self.assertEqual(result["total_score"], 100)
        self.assertEqual(result["grade"], "A")
        self.assertIn("Mourad.Soltani", result["signature"])

    def test_no_records(self):
        result = score_domain("example.com", mock_records=[])
        self.assertEqual(result["total_score"], 0)
        self.assertEqual(result["grade"], "F")
        self.assertTrue(any("No SPF" in i for i in result["issues"]))
        self.assertTrue(any("No DMARC" in i for i in result["issues"]))

    def test_spf_only_good(self):
        records = ["v=spf1 -all"]
        spf_score, issues = check_spf("test.com", records)
        self.assertGreaterEqual(spf_score, 40)
        self.assertEqual(len(issues), 0)

    def test_dmarc_none(self):
        records = ["v=DMARC1; p=none"]
        dmarc_score, issues = check_dmarc("test.com", records)
        self.assertLess(dmarc_score, 50)
        self.assertTrue(any("p=none" in i for i in issues))

    def test_health_signature(self):
        result = score_domain("healthcheck.com", mock_records=["v=spf1 ~all", "v=DMARC1; p=quarantine"])
        self.assertIn("signature", result)
        self.assertEqual(result["signature"], "Mourad.Soltani")

if __name__ == "__main__":
    unittest.main()
