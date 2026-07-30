import unittest
from copy import deepcopy

from scripts.ingest_pilot.scheduler import review_order, worker_orders
import scripts.ingest_pilot.scheduler as scheduler


def make_jobs(count):
    return [
        {
            "job_id": f"job-{number}",
            "attempt": 0,
            "queue_position": number,
            "state": "queued",
            "raw_path": f"raw/metronome/job-{number}.md",
            "raw_sha256": str(number) * 64,
            "source_target": f"wiki/sources/metronome/source-job-{number}.md",
            "canonical_url": f"https://docs.metronome.com/job-{number}",
        }
        for number in range(1, count + 1)
    ]


class SchedulerTests(unittest.TestCase):
    def test_worker_orders_fill_five_slots_then_refill_one(self):
        jobs = make_jobs(10)

        first = worker_orders(
            jobs,
            worker_concurrency=5,
            max_attempts=3,
            available_worker_slots=5,
        )

        self.assertEqual([order["job_id"] for order in first], [f"job-{number}" for number in range(1, 6)])
        for job in jobs[:5]:
            job["state"] = "running"
        jobs[0]["state"] = "candidate_ready"
        refill = worker_orders(
            jobs,
            worker_concurrency=5,
            max_attempts=3,
            available_worker_slots=1,
        )

        self.assertEqual([order["job_id"] for order in refill], ["job-6"])

    def test_review_order_is_serial(self):
        jobs = make_jobs(3)
        jobs[0]["state"] = "candidate_ready"
        jobs[1]["state"] = "candidate_ready"

        self.assertEqual(review_order(jobs)["job_id"], "job-1")
        jobs[0]["state"] = "reviewing"

        self.assertIsNone(review_order(jobs))

    def test_failed_and_rejected_jobs_do_not_consume_worker_slots(self):
        jobs = make_jobs(5)
        jobs[0]["state"] = "failed"
        jobs[1]["state"] = "rejected"

        orders = worker_orders(
            jobs,
            worker_concurrency=3,
            max_attempts=3,
            available_worker_slots=3,
        )

        self.assertEqual([order["job_id"] for order in orders], ["job-3", "job-4", "job-5"])

    def test_worker_orders_use_ascending_queue_position_without_mutating_jobs(self):
        jobs = make_jobs(3)
        jobs[0]["queue_position"] = 3
        jobs[1]["queue_position"] = 1
        jobs[2]["queue_position"] = 2
        before = deepcopy(jobs)

        orders = worker_orders(
            jobs,
            worker_concurrency=5,
            max_attempts=3,
            available_worker_slots=8,
        )

        self.assertEqual([order["job_id"] for order in orders], ["job-2", "job-3", "job-1"])
        self.assertEqual([order["attempt"] for order in orders], [1, 1, 1])
        self.assertEqual(jobs, before)

    def test_worker_orders_skip_jobs_at_the_maximum_attempts(self):
        jobs = make_jobs(2)
        jobs[0]["attempt"] = 3

        orders = worker_orders(
            jobs,
            worker_concurrency=2,
            max_attempts=3,
            available_worker_slots=2,
        )

        self.assertEqual([order["job_id"] for order in orders], ["job-2"])

    def test_worker_order_carries_portable_routing_metadata(self):
        jobs = make_jobs(1)
        jobs[0]["recommended_worker_tier"] = "strong"
        jobs[0]["routing_reason"] = "schema-heavy API"

        orders = worker_orders(
            jobs,
            worker_concurrency=1,
            max_attempts=3,
            available_worker_slots=1,
        )

        self.assertEqual(
            orders[0],
            {
                "action": "spawn_worker",
                "job_id": "job-1",
                "attempt": 1,
                "raw_path": "raw/metronome/job-1.md",
                "raw_sha256": "1" * 64,
                "source_target": "wiki/sources/metronome/source-job-1.md",
                "canonical_url": "https://docs.metronome.com/job-1",
                "result_contract": {
                    "top_level_keys": [
                        "job_id",
                        "attempt",
                        "source_page",
                        "quotes",
                        "suggestions",
                        "raw_path",
                        "raw_sha256",
                        "status",
                    ],
                    "quote_required_keys": ["text", "location"],
                },
                "preflight": [
                    "Copy canonical_url exactly into source_page frontmatter.",
                    "Return exactly result_contract.top_level_keys and no other top-level keys.",
                    "Ensure every quote has non-empty text and location.",
                ],
                "recommended_worker_tier": "strong",
                "routing_reason": "schema-heavy API",
            },
        )

    def test_shared_slots_start_three_workers_then_one_review_and_two_workers(self):
        jobs = make_jobs(6)

        first = scheduler.shared_slot_orders(
            jobs, worker_concurrency=5, review_concurrency=2, max_attempts=3, total_subagent_slots=3
        )
        self.assertEqual([order["job_id"] for order in first["worker_orders"]], ["job-1", "job-2", "job-3"])
        self.assertEqual(first["review_orders"], [])

        jobs = make_jobs(6)
        jobs[0]["state"] = "candidate_ready"
        second = scheduler.shared_slot_orders(
            jobs, worker_concurrency=5, review_concurrency=2, max_attempts=3, total_subagent_slots=3
        )
        self.assertEqual([order["job_id"] for order in second["review_orders"]], ["job-1"])
        self.assertEqual([order["job_id"] for order in second["worker_orders"]], ["job-2", "job-3"])

    def test_shared_slots_emit_two_ready_reviews_and_do_not_reserve_when_worker_is_active(self):
        jobs = make_jobs(5)
        jobs[0]["state"] = "candidate_ready"
        jobs[1]["state"] = "candidate_ready"
        jobs[2]["state"] = "running"

        orders = scheduler.shared_slot_orders(
            jobs, worker_concurrency=5, review_concurrency=2, max_attempts=3, total_subagent_slots=3
        )

        self.assertEqual([order["job_id"] for order in orders["review_orders"]], ["job-1", "job-2"])
        self.assertEqual(orders["worker_orders"], [])


if __name__ == "__main__":
    unittest.main()
