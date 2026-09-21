import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts.ingest_pilot import campaign_paths, init_campaign, load_campaign, load_jobs, run_once
from scripts.ingest_pilot.state import PilotError, recover_interrupted
from scripts.ingest_pilot.coordinator import complete_campaign, retry_job


class ProviderRoutingTests(unittest.TestCase):
    def test_same_campaign_name_is_isolated_across_providers(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for provider in ('metronome', 'braintree', 'stripe', 'adyen', 'paypal'):
                with self.subTest(provider=provider):
                    raw = root / 'raw' / provider / 'example.md'
                    raw.parent.mkdir(parents=True)
                    raw.write_text('# Example\n\nProvider evidence.\n')
                    manifest = {
                        'campaign_id': 'campaign-01', 'provider': provider,
                        'jobs': [{
                            'job_id': 'example', 'raw_path': str(raw.relative_to(root)),
                            'raw_sha256': hashlib.sha256(raw.read_bytes()).hexdigest(),
                            'source_target': f'wiki/sources/{provider}/source-example.md',
                            'canonical_url': f'https://example.com/{provider}',
                        }],
                    }
                    init_campaign(root, manifest)
                    selector = f'{provider}/campaign-01'
                    self.assertEqual(load_campaign(root, selector)['provider'], provider)
                    self.assertEqual(load_campaign(root, selector)['campaign_id'], 'campaign-01')
                    output = run_once(root, selector)
                    self.assertEqual(len(output['worker_orders']), 1)
                    attempt = root / f'tracking/ingest/{provider}/campaign-01/attempts/example/attempt-1'
                    self.assertTrue((attempt / 'input.json').is_file())
                    recover_interrupted(root, selector)
                    self.assertEqual(load_jobs(root, selector)[0]['state'], 'failed')
                    retry_job(root, selector, 'example')
                    run_once(root, selector)
                    job = load_jobs(root, selector)[0]
                    result = {
                        'job_id': 'example', 'attempt': 2,
                        'raw_path': job['raw_path'], 'raw_sha256': job['raw_sha256'],
                        'status': 'candidate_ready',
                        'source_page': (
                            '---\ntitle: Example\ntype: source\ndate_ingested: 2026-09-19\n'
                            'original_format: webpage\n'
                            f'canonical_url: "https://example.com/{provider}"\n'
                            f'raw_files:\n  - "{provider}/example.md"\ntags: [example]\n---\n'
                            f'## Raw Sources\n- [[raw/{provider}/example]]\n'
                        ),
                        'quotes': [{'text': text, 'location': 'body'} for text in
                                   ('Example', 'Provider evidence.', 'Provider')],
                        'suggestions': {'company': [], 'concepts': [], 'index': [], 'log': []},
                    }
                    handoff = root / 'worker.json'
                    handoff.write_text(json.dumps(result))
                    run_once(root, selector, worker_result_path=handoff,
                             reviewer_assignments=[{'identity': 'reviewer', 'model': 'Sol'}])
                    self.assertEqual(load_jobs(root, selector)[0]['state'], 'reviewing')
                    review = root / 'review.json'
                    review.write_text(json.dumps({
                        'job_id': 'example', 'attempt': 2, 'verdict': 'approved',
                        'reason': 'Grounded', 'required_changes': [], 'review_scope': 'full',
                        'retry_review_scope': None, 'shared_update_decisions': [],
                    }))
                    run_once(root, selector, review_result_path=review)
                    self.assertEqual(load_jobs(root, selector)[0]['state'], 'approved')
                    complete_campaign(root, selector, coordinator_repairs=0)
                    self.assertEqual(load_campaign(root, selector)['state'], 'complete')
                    self.assertTrue((attempt.parent / 'attempt-2' / 'review.json').is_file())
            self.assertEqual(
                campaign_paths(root, 'campaign-01')['campaign_dir'],
                root / 'tracking/ingest/metronome/campaign-01',
            )
            self.assertEqual(load_campaign(root, 'campaign-01')['provider'], 'metronome')

    def test_invalid_selector_and_manifest_provider_do_not_create_state(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for selector in ('../escape', '/absolute', 'a/b/c', 'braintree/..', ''):
                with self.subTest(selector=selector), self.assertRaises(PilotError):
                    campaign_paths(root, selector)
            for provider in ('../escape', '', None):
                with self.subTest(provider=provider), self.assertRaises(PilotError):
                    init_campaign(root, {'campaign_id': 'campaign-01', 'provider': provider, 'jobs': []})
            self.assertFalse((root / 'tracking').exists())
