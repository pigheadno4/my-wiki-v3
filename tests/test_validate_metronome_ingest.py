import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import validate_metronome_ingest  # noqa: E402


class ValidateMetronomeIngestCliTests(unittest.TestCase):
    def test_cli_validates_luna_output_worker_and_final_receipts(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            raw_path = root / "raw/metronome/guides/home.md"
            raw_path.parent.mkdir(parents=True)
            raw_path.write_text("alpha\nbeta\ngamma\n", encoding="utf-8")
            run_dir = "tracking/ingest/metronome/pilot/runs/pilot-home-luna"
            job = {
                "schema_version": 2,
                "job_id": "pilot-home-luna",
                "provider": "metronome",
                "mode": "shadow",
                "canonical_url": "https://docs.metronome.com/guides/home",
                "raw_path": "raw/metronome/guides/home.md",
                "source_page": "wiki/sources/metronome/source-home.md",
                "artifact_dir": run_dir,
                "role": "cheap_ingester",
                "model_provider": "openai",
                "model": "gpt-5.6-luna",
                "reasoning_effort": "high",
                "allowed_write_paths": [run_dir],
                "forbidden_write_paths": ["wiki/metronome-index.md"],
                "forbidden_write_prefixes": ["raw/", "wiki/"],
            }
            quotes = [
                {"line_start": 1, "line_end": 1, "text": "alpha", "supports": "a"},
                {"line_start": 2, "line_end": 2, "text": "beta", "supports": "b"},
                {"line_start": 3, "line_end": 3, "text": "gamma", "supports": "c"},
            ]
            output = {
                "job_id": job["job_id"],
                "raw_path": job["raw_path"],
                "canonical_url": job["canonical_url"],
                "title": "Home",
                "grounding_quotes": quotes,
                "overview": "Overview.",
                "key_takeaways": ["Takeaway."],
                "details": [{"heading": "Scope", "facts": ["Fact."]}],
                "suggested_tags": ["metronome"],
                "suggested_metronome_concepts": [],
                "proposed_raw_link": "[[raw/metronome/guides/home|snapshot]]",
                "unsupported_claim_self_check": [],
            }
            worker = {
                "schema_version": 2,
                "job_id": job["job_id"],
                "provider": job["provider"],
                "canonical_url": job["canonical_url"],
                "raw_path": job["raw_path"],
                "source_page": job["source_page"],
                "status": "success",
                "model_provider": "openai",
                "model": "gpt-5.6-luna",
                "reasoning_effort": "high",
                "attempt_count": 1,
                "started_at": "2026-07-14T00:00:00Z",
                "finished_at": "2026-07-14T00:00:01Z",
                "elapsed_seconds": 1,
                "process_exit_code": 0,
                "output_path": f"{run_dir}/luna-output.json",
                "draft_path": f"{run_dir}/luna-source-draft.md",
                "events_path": f"{run_dir}/attempt-1/events.jsonl",
                "stderr_path": f"{run_dir}/attempt-1/stderr.log",
                "grounding_quotes": quotes,
                "validation": [{"command": "validate_luna_output", "passed": True}],
                "token_usage": None,
                "token_usage_unavailable_reason": "unavailable",
            }
            final = {
                "schema_version": 2,
                "job_id": job["job_id"],
                "provider": job["provider"],
                "canonical_url": job["canonical_url"],
                "raw_path": job["raw_path"],
                "source_page": job["source_page"],
                "mode": "shadow",
                "worker_receipt": f"{run_dir}/luna-worker-receipt.json",
                "luna_draft": f"{run_dir}/luna-source-draft.md",
                "final_status": "approved",
                "repairs": [],
                "coordinator_repair_minutes": 0,
                "concepts_updated": [],
                "contradictions": [],
                "shared_files_updated": [],
                "validation": [{"command": "validate", "passed": True}],
                "review": {
                    "reviewer": "sol-coordinator",
                    "model": "gpt-5.6-sol",
                    "status": "approved",
                    "notes": "checked",
                },
            }
            for name, payload in (
                ("job.json", job),
                ("output.json", output),
                ("worker.json", worker),
                ("final.json", final),
            ):
                (root / name).write_text(json.dumps(payload), encoding="utf-8")

            argv = [
                "validate_metronome_ingest.py",
                "--job",
                "job.json",
                "--luna-output",
                "output.json",
                "--worker-receipt",
                "worker.json",
                "--final-receipt",
                "final.json",
            ]
            stdout = io.StringIO()
            with patch.object(validate_metronome_ingest, "ROOT", root), patch.object(
                sys, "argv", argv
            ), redirect_stdout(stdout):
                result = validate_metronome_ingest.main()

            self.assertEqual(0, result)
            self.assertIn("luna output: valid", stdout.getvalue())
            self.assertIn("worker receipt: valid", stdout.getvalue())
            self.assertIn("final receipt: valid", stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
