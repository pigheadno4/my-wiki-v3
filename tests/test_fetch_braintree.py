import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import fetch_braintree as b


class BraintreeTests(unittest.TestCase):
    def test_inventory_keeps_in_person_docs_without_sdk_fallbacks(self):
        url = b.HOST + '/braintree/in-person/about/technical-overview'
        self.assertEqual(b.canonical(url + '/'), url)
        self.assertEqual(b.fallbacks(url, 2), [])

    def test_inventory_unions_sources_and_deduplicates_fragments(self):
        rows = b.inventory('- [A](/braintree/docs/start/overview#one)\n- [B](/braintree/docs/start/overview#two)',
                           '<urlset><url><loc>https://developer.paypal.com/braintree/docs/start/overview</loc></url><url><loc>https://developer.paypal.com/braintree/articles/control-panel/overview</loc></url></urlset>')
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[1]['sources'], ['llms', 'sitemap'])

    def test_route_candidates_do_not_mutate_explicit_sdk_or_articles(self):
        base = b.HOST + '/braintree/docs/guides/credit-cards/client-side'
        self.assertEqual(b.fallbacks(base, 2), [base + '/node'])
        self.assertEqual(b.fallbacks(base, 3), [base + '/ios/v7', base + '/javascript/v3', base + '/android/v5'])
        self.assertEqual(b.fallbacks(base + '/ios/v7', 2), [])
        self.assertEqual(b.fallbacks(b.HOST + '/braintree/articles/control-panel/overview', 2), [])
        self.assertEqual(b.md_url(base), b.HOST + '/braintree/md/docs/guides/credit-cards/client-side')

    def test_scope_rejects_external_query_traversal_and_placeholders(self):
        for url in ['https://example.com/braintree/docs/a', '/braintree/docs/../a',
                    '/braintree/docs/%2e%2e/a', '/braintree/docs/$', '/braintree/docs/a?version=2']:
            with self.subTest(url=url), self.assertRaises(ValueError):
                b.canonical(url)

    def test_validation_rejects_html_title_only_and_wrong_slug(self):
        url = b.HOST + '/braintree/docs/start/overview'
        for body in ['<!doctype html><html>error</html>', '# Overview',
                     '---\nslug: /docs/wrong/\n---\n# Title\n' + 'Useful details. ' * 20]:
            with self.subTest(body=body), self.assertRaises(ValueError):
                b.validate({'status': 200, 'url': b.md_url(url), 'content_type': 'text/markdown', 'body': body}, url)

    def test_versions_keep_bytes_and_unchanged_creates_no_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            u = b.HOST + '/braintree/docs/reference/request/transaction/sale/node'
            first = b.save_raw(root, u, '# Sale\n\nOriginal\r\n', '2026-09-16')
            data = (root / first['raw_path']).read_bytes()
            same = b.save_raw(root, u, '# Sale\n\nOriginal\r\n', '2026-09-16')
            self.assertEqual(same['state'], 'unchanged')
            changed = b.save_raw(root, u, '# Sale\n\nUpdated\n', '2026-09-16')
            self.assertTrue(changed['raw_path'].endswith('node-2026-09-16-r2.md'))
            self.assertEqual((root / first['raw_path']).read_bytes(), data)

    def test_recovery_keeps_three_variants_and_failure_receipts(self):
        parent = b.HOST + '/braintree/docs/guides/credit-cards/client-side'
        def fetch(url):
            good = any(url.endswith(s) for s in ('/ios/v7', '/javascript/v3', '/android/v5'))
            return {'status': 200 if good else 404, 'url': url, 'content_type': 'text/markdown',
                    'body': '# Guide\n\n' + 'Implementation guidance. ' * 15 if good else 'No document found.'}
        with tempfile.TemporaryDirectory() as tmp:
            events = []
            result = b.collect_target(Path(tmp), parent, '2026-09-16', fetch, events.append, {})
            self.assertEqual(result['state'], 'recovered')
            self.assertEqual(len(result['variants']), 3)
            self.assertEqual([x['stage'] for x in events], [1, 2, 3, 3, 3])
            self.assertEqual(sum(x['state'] == 'failed' for x in events), 2)
            self.assertEqual(len(list((Path(tmp) / 'raw/braintree').rglob('*.md'))), 3)


if __name__ == '__main__':
    unittest.main()
