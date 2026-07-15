import json
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from run_metronome_model_worker import (  # noqa: E402
    build_codex_command,
    build_page_profile,
    repair_raw_link,
    repair_quote_bounds,
    run_worker,
)


class ModelWorkerRunnerTests(unittest.TestCase):
    def make_root(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        raw = root / "raw/metronome/guides/home.md"
        raw.parent.mkdir(parents=True)
        raw.write_text("# Alpha\nintro\n## Beta\nrequired when enabled\n", encoding="utf-8")
        schema = root / "tracking/ingest/metronome/pilot/schemas/model-output-v3.schema.json"
        schema.parent.mkdir(parents=True)
        schema.write_text('{"type":"object"}', encoding="utf-8")
        prompt = root / "tracking/ingest/metronome/pilot/prompts/source-summary-v3.md"
        prompt.parent.mkdir(parents=True)
        prompt.write_text("Read raw.md completely and return JSON.", encoding="utf-8")
        job = self.valid_job()
        job_path = root / "tracking/ingest/metronome/pilot/jobs/terra-home.json"
        job_path.parent.mkdir(parents=True)
        job_path.write_text(json.dumps(job), encoding="utf-8")
        return root, job_path, job

    def valid_job(self):
        run_dir = "tracking/ingest/metronome/pilot/runs/terra-home"
        return {
            "schema_version": 3,
            "job_id": "terra-home",
            "provider": "metronome",
            "mode": "real_ingest",
            "canonical_url": "https://docs.metronome.com/guides/home",
            "raw_path": "raw/metronome/guides/home.md",
            "source_page": "wiki/sources/metronome/source-home.md",
            "artifact_dir": run_dir,
            "role": "cheap_ingester",
            "model_provider": "openai",
            "model": "gpt-5.6-terra",
            "reasoning_effort": "medium",
            "allowed_write_paths": [run_dir],
            "forbidden_write_paths": ["wiki/metronome-index.md"],
            "forbidden_write_prefixes": ["raw/", "wiki/"],
        }

    def valid_output(self, job):
        return {
            "job_id": job["job_id"],
            "raw_path": job["raw_path"],
            "canonical_url": job["canonical_url"],
            "title": "Home",
            "grounding_quotes": [
                {"id": "q1", "line_start": 1, "line_end": 1, "text": "# Alpha", "supports": "title"},
                {"id": "q2", "line_start": 2, "line_end": 2, "text": "intro", "supports": "overview"},
                {"id": "q3", "line_start": 3, "line_end": 4, "text": "## Beta\nrequired when enabled", "supports": "condition"},
            ],
            "overview": "Overview.",
            "overview_evidence_quote_ids": ["q2"],
            "key_takeaways": [{"text": "Takeaway.", "evidence_quote_ids": ["q1"]}],
            "details": [{"heading": "Beta", "facts": [{"text": "Fact.", "evidence_quote_ids": ["q3"]}]}],
            "sections_covered": ["Alpha", "Beta"],
            "scope_boundaries": [],
            "conditional_requirements": [{"text": "Conditional.", "evidence_quote_ids": ["q3"]}],
            "feature_gates": [],
            "internal_inconsistencies": [],
            "material_omissions": [],
            "suggested_tags": ["metronome"],
            "suggested_metronome_concepts": [],
            "proposed_raw_link": "[[raw/metronome/guides/home|snapshot]]",
            "unsupported_claim_self_check": [],
        }

    def test_command_uses_job_model_reasoning_read_only_and_minimal_cwd(self):
        command = build_codex_command(
            Path("/tmp/minimal"), Path("/repo/schema.json"), Path("/repo/output.json"),
            "prompt", "gpt-5.6-terra", "medium"
        )

        self.assertIn("gpt-5.6-terra", command)
        self.assertIn('model_reasoning_effort="medium"', command)
        self.assertEqual("read-only", command[command.index("-s") + 1])
        self.assertEqual("/tmp/minimal", command[command.index("-C") + 1])
        self.assertIn("--skip-git-repo-check", command)
        self.assertNotIn("--ignore-user-config", command)
        for feature in ("plugins", "remote_plugin", "apps", "hooks", "memories"):
            positions = [index for index, value in enumerate(command) if value == "--disable"]
            self.assertTrue(any(command[index + 1] == feature for index in positions))

    def test_page_profile_covers_headings_and_conditional_hints(self):
        profile = build_page_profile("# Alpha\n## Beta\nrequired when enabled\n")

        self.assertEqual(["Alpha", "Beta"], profile["headings"])
        self.assertEqual([3], profile["conditional_hint_lines"])

    def test_unique_exact_quote_gets_local_line_repair(self):
        output = {"grounding_quotes": [{"line_start": 9, "line_end": 9, "text": "beta"}]}

        repaired = repair_quote_bounds("alpha\nbeta\ngamma\n", output)

        self.assertEqual(1, repaired)
        self.assertEqual((2, 2), (output["grounding_quotes"][0]["line_start"], output["grounding_quotes"][0]["line_end"]))

    def test_ambiguous_quote_is_not_repaired(self):
        output = {"grounding_quotes": [{"line_start": 9, "line_end": 9, "text": "same"}]}

        self.assertEqual(0, repair_quote_bounds("same\nother\nsame\n", output))

    def test_raw_link_target_is_repaired_without_changing_label(self):
        job = self.valid_job()
        output = {"proposed_raw_link": "[[raw/metronome/wrong|dated snapshot]]"}

        self.assertTrue(repair_raw_link(job, output))
        self.assertEqual(
            "[[raw/metronome/guides/home|dated snapshot]]",
            output["proposed_raw_link"],
        )

    def test_retry_receipt_sums_usage_and_keeps_rejected_reason(self):
        root, job_path, job = self.make_root()
        calls = []
        staged_files = []

        def fake_runner(command, **kwargs):
            calls.append((command, kwargs))
            staged_files.append((Path(kwargs["cwd"]) / "raw.md").is_file())
            output = self.valid_output(job)
            if len(calls) == 1:
                output["key_takeaways"][0]["evidence_quote_ids"] = ["missing"]
            output_path = Path(command[command.index("-o") + 1])
            output_path.write_text(json.dumps(output), encoding="utf-8")
            usage = {"input_tokens": 100 * len(calls), "output_tokens": 10 * len(calls)}
            return SimpleNamespace(returncode=0, stdout=json.dumps({"usage": usage}) + "\n", stderr="")

        result = run_worker(root, job_path, "2026-07-14", runner=fake_runner)

        self.assertEqual(0, result)
        self.assertEqual(2, len(calls))
        self.assertEqual(900, calls[0][1]["timeout"])
        self.assertNotEqual(root, calls[0][1]["cwd"])
        self.assertEqual([True, True], staged_files)
        receipt = json.loads((root / job["artifact_dir"] / "model-worker-receipt.json").read_text())
        self.assertEqual({"input_tokens": 300, "output_tokens": 30}, receipt["cumulative_token_usage"])
        self.assertIn("undefined grounding quote", receipt["attempts"][0]["retry_reason"])
        self.assertEqual("rejected", receipt["attempts"][0]["status"])
        self.assertEqual("accepted", receipt["attempts"][1]["status"])

    def test_quote_only_failure_is_repaired_without_retry(self):
        root, job_path, job = self.make_root()
        calls = []

        def fake_runner(command, **kwargs):
            calls.append(command)
            output = self.valid_output(job)
            output["grounding_quotes"][0]["line_start"] = 99
            output["grounding_quotes"][0]["line_end"] = 99
            output_path = Path(command[command.index("-o") + 1])
            output_path.write_text(json.dumps(output), encoding="utf-8")
            return SimpleNamespace(returncode=0, stdout="", stderr="")

        result = run_worker(root, job_path, "2026-07-14", runner=fake_runner)

        self.assertEqual(0, result)
        self.assertEqual(1, len(calls))
        receipt = json.loads((root / job["artifact_dir"] / "model-worker-receipt.json").read_text())
        self.assertEqual(1, receipt["quote_line_repairs"])


if __name__ == "__main__":
    unittest.main()
