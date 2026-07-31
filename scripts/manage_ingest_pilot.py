"""Thin JSON CLI for the minimum Metronome ingest dry run."""

import argparse
import json
import sys
from pathlib import Path

from ingest_pilot.coordinator import complete_campaign, init_campaign, reject_job, retry_job, run_once, status
from ingest_pilot.state import PilotError


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest="command", required=True)

    init = commands.add_parser("init")
    init.add_argument("--manifest", required=True)

    run = commands.add_parser("run")
    run.add_argument("--campaign", required=True)
    run.add_argument("--worker-result")
    run.add_argument("--review-result")
    run.add_argument("--available-worker-slots", type=int)
    run.add_argument("--total-subagent-slots", type=int)
    run.add_argument("--worker-assignment", action="append", default=[])
    run.add_argument("--reviewer-assignment", action="append", default=[])

    campaign = commands.add_parser("status")
    campaign.add_argument("--campaign", required=True)

    retry = commands.add_parser("retry")
    retry.add_argument("--campaign", required=True)
    retry.add_argument("--job", required=True)

    reject = commands.add_parser("reject")
    reject.add_argument("--campaign", required=True)
    reject.add_argument("--job", required=True)
    reject.add_argument("--reason", required=True)

    complete = commands.add_parser("complete")
    complete.add_argument("--campaign", required=True)
    complete.add_argument("--coordinator-repairs", required=True, type=int)

    return parser


def main() -> int:
    parser = _parser()
    arguments = parser.parse_args()
    root = Path.cwd()
    try:
        if arguments.command == "init":
            output = init_campaign(root, Path(arguments.manifest))
        elif arguments.command == "run":
            def assignments(values):
                output = []
                for value in values:
                    identity, separator, model = value.partition("=")
                    if not separator or not identity or not model or "=" in model:
                        raise PilotError("assignment must use IDENTITY=MODEL")
                    output.append({"identity": identity, "model": model})
                return output

            output = run_once(
                root,
                arguments.campaign,
                worker_result_path=Path(arguments.worker_result) if arguments.worker_result else None,
                review_result_path=Path(arguments.review_result) if arguments.review_result else None,
                available_worker_slots=arguments.available_worker_slots,
                total_subagent_slots=arguments.total_subagent_slots,
                worker_assignments=assignments(arguments.worker_assignment),
                reviewer_assignments=assignments(arguments.reviewer_assignment),
            )
        elif arguments.command == "status":
            output = status(root, arguments.campaign)
        elif arguments.command == "retry":
            output = retry_job(root, arguments.campaign, arguments.job)
        elif arguments.command == "complete":
            output = complete_campaign(root, arguments.campaign, arguments.coordinator_repairs)
        else:
            output = reject_job(root, arguments.campaign, arguments.job, arguments.reason)
    except PilotError as error:
        print(str(error), file=sys.stderr)
        return 1
    print(json.dumps(output, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
