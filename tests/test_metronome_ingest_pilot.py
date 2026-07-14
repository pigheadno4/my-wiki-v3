import sys
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from metronome_ingest_pilot import validate_job, validate_receipt  # noqa: E402


class MetronomeIngestPilotTests(unittest.TestCase):
    def make_root(self) -> Path:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        raw = root / "raw" / "metronome" / "guides" / "home.md"
        raw.parent.mkdir(parents=True)
        raw.write_text("alpha\nbeta\ngamma\ndelta\n", encoding="utf-8")
        return root

    def valid_job(self):
        source = "wiki/sources/metronome/source-home.md"
        concept = "wiki/concepts/metronome/metronome-usage-based-billing.md"
        return {
            "schema_version": 1,
            "job_id": "pilot-home-baseline",
            "provider": "metronome",
            "canonical_url": "https://docs.metronome.com/guides/home",
            "raw_path": "raw/metronome/guides/home.md",
            "source_page": source,
            "concept_leases": [concept],
            "role": "strong_baseline",
            "allowed_write_paths": [source, concept],
            "forbidden_write_paths": [
                "wiki/companies/metronome.md",
                "wiki/metronome-index.md",
                "wiki/metronome-log.md",
                "wiki/index.md",
                "wiki/log.md",
            ],
            "forbidden_write_prefixes": [
                "raw/",
                "wiki/comparisons/",
            ],
        }

    def valid_receipt(self, job):
        return {
            "schema_version": 1,
            "job_id": job["job_id"],
            "provider": job["provider"],
            "canonical_url": job["canonical_url"],
            "raw_path": job["raw_path"],
            "source_page": job["source_page"],
            "status": "success",
            "grounding_quotes": [
                {"line_start": 1, "line_end": 1, "text": "alpha"},
                {"line_start": 2, "line_end": 2, "text": "beta"},
                {"line_start": 3, "line_end": 4, "text": "gamma\ndelta"},
            ],
            "files_changed": list(job["allowed_write_paths"]),
            "worker_commit": "1234567abcdef",
            "validation": [
                {"command": "python3 scripts/validate_wiki.py source.md", "passed": True}
            ],
            "worker": {
                "role": job["role"],
                "model_provider": "openai",
                "model": "gpt-5",
                "token_usage": None,
                "token_usage_unavailable_reason": "runtime does not expose per-job usage",
            },
            "review": {
                "status": "approved",
                "reviewer": "coordinator",
                "notes": "Claims and quotes checked against raw lines.",
            },
        }

    def test_valid_job_has_existing_raw_and_disjoint_write_sets(self):
        root = self.make_root()

        self.assertEqual([], validate_job(root, self.valid_job()))

    def test_job_rejects_missing_raw_and_overlapping_forbidden_path(self):
        root = self.make_root()
        job = self.valid_job()
        job["raw_path"] = "raw/metronome/guides/missing.md"
        job["forbidden_write_paths"].append(job["source_page"])

        errors = validate_job(root, job)

        self.assertTrue(any("raw_path does not exist" in error for error in errors))
        self.assertTrue(any("allowed and forbidden write paths overlap" in error for error in errors))

    def test_receipt_identity_must_match_job(self):
        root = self.make_root()
        job = self.valid_job()
        receipt = self.valid_receipt(job)
        receipt["canonical_url"] = "https://docs.metronome.com/wrong"

        errors = validate_receipt(root, job, receipt)

        self.assertTrue(any("canonical_url does not match job" in error for error in errors))

    def test_receipt_rejects_files_outside_allowed_write_set(self):
        root = self.make_root()
        job = self.valid_job()
        receipt = self.valid_receipt(job)
        receipt["files_changed"].append("wiki/metronome-index.md")

        errors = validate_receipt(root, job, receipt)

        self.assertTrue(any("outside allowed_write_paths" in error for error in errors))

    def test_grounding_quote_must_match_exact_raw_lines(self):
        root = self.make_root()
        job = self.valid_job()
        receipt = self.valid_receipt(job)
        receipt["grounding_quotes"][0]["text"] = "not alpha"

        errors = validate_receipt(root, job, receipt)

        self.assertTrue(any("does not match raw lines 1-1" in error for error in errors))

    def test_success_receipt_requires_commit_validation_model_and_review(self):
        root = self.make_root()
        job = self.valid_job()
        receipt = self.valid_receipt(job)
        receipt["worker_commit"] = ""
        receipt["validation"][0]["passed"] = False
        receipt["worker"]["model"] = ""
        receipt["review"]["status"] = "pending"

        errors = validate_receipt(root, job, receipt)

        self.assertTrue(any("worker_commit" in error for error in errors))
        self.assertTrue(any("validation command did not pass" in error for error in errors))
        self.assertTrue(any("model is required" in error for error in errors))
        self.assertTrue(any("review status must be approved" in error for error in errors))

    def test_null_token_usage_requires_reason(self):
        root = self.make_root()
        job = self.valid_job()
        receipt = deepcopy(self.valid_receipt(job))
        receipt["worker"].pop("token_usage_unavailable_reason")

        errors = validate_receipt(root, job, receipt)

        self.assertTrue(any("token_usage_unavailable_reason" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
