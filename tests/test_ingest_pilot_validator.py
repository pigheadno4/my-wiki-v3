import tempfile
import unittest
from pathlib import Path

from scripts.ingest_pilot.validator import (
    ValidationError,
    sha256_file,
    validate_worker_result,
)


class WorkerResultValidationTests(unittest.TestCase):
    def setUp(self):
        temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(temporary_directory.cleanup)
        self.root = Path(temporary_directory.name)
        self.raw_path = "raw/metronome/guides/platform-configuration/security-principles-2026-07-13.md"
        self.raw = self.root / self.raw_path
        self.raw.parent.mkdir(parents=True)
        self.raw.write_text(
            "# Metronome's security principles\n\n"
            "Least privilege\n"
            "Separation of duties\n"
            "Secure by default\n",
            encoding="utf-8",
        )
        self.job = {
            "job_id": "security-principles",
            "attempt": 1,
            "raw_path": self.raw_path,
            "raw_sha256": sha256_file(self.raw),
            "source_target": "wiki/sources/metronome/source-metronome-security-principles.md",
            "canonical_url": "https://docs.metronome.com/guides/platform-configuration/security-principles.md",
            "contract_version": 2,
        }

    def valid_result(self, **overrides):
        result = {
            "job_id": self.job["job_id"],
            "attempt": self.job["attempt"],
            "source_page": (
                "---\n"
                "title: \"Metronome security principles\"\n"
                "type: source\n"
                "date_ingested: 2026-07-27\n"
                "canonical_url: \"https://docs.metronome.com/guides/platform-configuration/security-principles.md\"\n"
                "original_format: webpage\n"
                "raw_files:\n"
                "  - \"metronome/guides/platform-configuration/security-principles-2026-07-13.md\"\n"
                "tags: [metronome, security]\n"
                "---\n\n"
                "## Raw Sources\n"
                "- [[raw/metronome/guides/platform-configuration/security-principles-2026-07-13|security-principles-2026-07-13]] — verbatim documentation\n"
            ),
            "quotes": [
                {"text": "Least privilege", "location": "Metronome's security principles"},
                {"text": "Separation of duties", "location": "Metronome's security principles"},
                {"text": "Secure by default", "location": "Metronome's security principles"},
            ],
            "suggestions": {"company": [], "concepts": [], "index": [], "log": []},
            "raw_path": self.job["raw_path"],
            "raw_sha256": self.job["raw_sha256"],
            "status": "candidate_ready",
        }
        result.update(overrides)
        return result

    def assert_invalid(self, result):
        with self.assertRaises(ValidationError):
            validate_worker_result(self.root, self.job, result)

    def test_valid_worker_result_requires_quotes_hash_and_raw_link(self):
        result = self.valid_result()

        validated = validate_worker_result(self.root, self.job, result)

        self.assertEqual(validated["status"], "candidate_ready")
        self.assertEqual(len(validated["quotes"]), 3)

    def test_rejects_two_or_six_quotes(self):
        for count in (2, 6):
            with self.subTest(count=count):
                quotes = self.valid_result()["quotes"]
                self.assert_invalid(self.valid_result(quotes=(quotes * 2)[:count]))

    def test_rejects_a_quote_absent_from_the_raw_bytes(self):
        result = self.valid_result()
        result["quotes"][0]["text"] = "Not present in the raw file"

        self.assert_invalid(result)

    def test_rejects_a_wrong_raw_path(self):
        self.assert_invalid(self.valid_result(raw_path="raw/metronome/other.md"))

    def test_rejects_a_wrong_raw_sha256(self):
        self.assert_invalid(self.valid_result(raw_sha256="0" * 64))

    def test_rejects_missing_or_wrong_raw_files_entry(self):
        for raw_entry in (None, "metronome/guides/platform-configuration/other.md"):
            with self.subTest(raw_entry=raw_entry):
                source_page = self.valid_result()["source_page"]
                if raw_entry is None:
                    source_page = source_page.replace(
                        "raw_files:\n"
                        "  - \"metronome/guides/platform-configuration/security-principles-2026-07-13.md\"\n",
                        "",
                    )
                else:
                    source_page = source_page.replace(
                        "metronome/guides/platform-configuration/security-principles-2026-07-13.md",
                        raw_entry,
                    )
                self.assert_invalid(self.valid_result(source_page=source_page))

    def test_rejects_missing_or_wrong_canonical_url(self):
        expected = (
            'canonical_url: "https://docs.metronome.com/guides/'
            'platform-configuration/security-principles.md"\n'
        )
        for replacement in (
            "",
            'canonical_url: "https://docs.metronome.com/guides/other.md"\n',
        ):
            with self.subTest(replacement=replacement):
                source_page = self.valid_result()["source_page"].replace(expected, replacement)
                self.assert_invalid(self.valid_result(source_page=source_page))

    def test_rejects_expected_raw_path_outside_raw_files(self):
        source_page = self.valid_result()["source_page"].replace(
            "raw_files:\n"
            "  - \"metronome/guides/platform-configuration/security-principles-2026-07-13.md\"\n",
            "raw_files:\n"
            "  - \"metronome/guides/platform-configuration/other.md\"\n"
            "other_files:\n"
            "  - \"metronome/guides/platform-configuration/security-principles-2026-07-13.md\"\n",
        )

        self.assert_invalid(self.valid_result(source_page=source_page))

    def test_rejects_missing_raw_sources_heading(self):
        source_page = self.valid_result()["source_page"].replace("## Raw Sources\n", "")

        self.assert_invalid(self.valid_result(source_page=source_page))

    def test_rejects_a_nonexact_raw_sources_heading(self):
        source_page = self.valid_result()["source_page"].replace(
            "## Raw Sources\n", "## Raw Sources Notes\n"
        )

        self.assert_invalid(self.valid_result(source_page=source_page))

    def test_rejects_a_wrong_raw_wikilink(self):
        source_page = self.valid_result()["source_page"].replace(
            "[[raw/metronome/guides/platform-configuration/security-principles-2026-07-13|security-principles-2026-07-13]]",
            "[[other-raw-file]]",
        )

        self.assert_invalid(self.valid_result(source_page=source_page))

    def test_rejects_a_filename_only_raw_wikilink(self):
        source_page = self.valid_result()["source_page"].replace(
            "[[raw/metronome/guides/platform-configuration/security-principles-2026-07-13|security-principles-2026-07-13]]",
            "[[security-principles-2026-07-13]]",
        )

        self.assert_invalid(self.valid_result(source_page=source_page))

    def test_rejects_a_raw_wikilink_outside_the_raw_sources_section(self):
        source_page = self.valid_result()["source_page"].replace(
            "## Raw Sources\n",
            "[[raw/metronome/guides/platform-configuration/security-principles-2026-07-13|security-principles-2026-07-13]] — misplaced raw link\n\n## Raw Sources\n",
        ).replace(
            "- [[raw/metronome/guides/platform-configuration/security-principles-2026-07-13|security-principles-2026-07-13]] — verbatim documentation\n",
            "",
        )

        self.assert_invalid(self.valid_result(source_page=source_page))

    def test_rejects_a_raw_wikilink_in_a_later_section(self):
        source_page = self.valid_result()["source_page"].replace(
            "- [[raw/metronome/guides/platform-configuration/security-principles-2026-07-13|security-principles-2026-07-13]] — verbatim documentation\n",
            "- [[other-raw-file]] — wrong link\n\n"
            "## Related\n"
            "- [[raw/metronome/guides/platform-configuration/security-principles-2026-07-13|security-principles-2026-07-13]] — misplaced raw link\n",
        )

        self.assert_invalid(self.valid_result(source_page=source_page))

    def test_rejects_missing_suggestions_key(self):
        result = self.valid_result()
        result["suggestions"].pop("log")

        self.assert_invalid(result)

    def test_accepts_a_structured_concept_update_grounded_in_a_quote(self):
        result = self.valid_result(suggestions={
            "company": [],
            "concepts": [{
                "update_id": "concept-billing-link",
                "target_path": "wiki/concepts/metronome/metronome-billing.md",
                "update_kind": "durable_fact",
                "anchor": "## Sources",
                "proposed_markdown": "- [[source-job-1]] — documented billing behavior",
                "quote_indexes": [0],
                "warnings": [],
            }],
            "index": [],
            "log": [],
        })

        self.assertEqual(validate_worker_result(self.root, self.job, result)["suggestions"], result["suggestions"])

    def test_rejects_malformed_structured_suggestions(self):
        valid_update = {
            "update_id": "concept-billing-link",
            "target_path": "wiki/concepts/metronome/metronome-billing.md",
            "update_kind": "durable_fact",
            "anchor": "## Sources",
            "proposed_markdown": "- [[source-job-1]] — documented billing behavior",
            "quote_indexes": [0],
            "warnings": [],
        }
        invalid_updates = (
            {"update_id": "../escape"},
            {**valid_update, "target_path": "raw/metronome/source.md"},
            {**valid_update, "update_kind": "rewrite_everything"},
            {**valid_update, "quote_indexes": [3]},
            {**valid_update, "warnings": "none"},
        )
        for update in invalid_updates:
            with self.subTest(update=update):
                self.assert_invalid(self.valid_result(suggestions={
                    "company": [], "concepts": [update], "index": [], "log": [],
                }))

    def test_rejects_an_output_key_outside_the_fixed_schema(self):
        result = self.valid_result()
        result["unexpected"] = True

        self.assert_invalid(result)


if __name__ == "__main__":
    unittest.main()
