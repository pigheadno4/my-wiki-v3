import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import fetch_psp as fetch


class AdyenLayoutTests(unittest.TestCase):
    def test_collection_preserves_paths_versions_and_manifest_links(self):
        cases = [
            ('https://docs.adyen.com/.md', 'adyen/docs/index'),
            ('https://docs.adyen.com/account.md', 'adyen/docs/account'),
            ('https://docs.adyen.com/api-explorer/Checkout/latest/post/sessions.md',
             'adyen/api-explorer/Checkout/latest/post/sessions'),
        ]
        with tempfile.TemporaryDirectory() as tmp, patch.object(fetch, 'RAW', Path(tmp)), patch.object(fetch.time, 'sleep'):
            for url, folder in cases:
                source = {'name': 'docs', 'url': 'https://docs.adyen.com/llms.txt'}
                cfg = {'raw_prefix': 'adyen', 'host': 'docs.adyen.com', 'raw_root': 'raw/adyen'}
                def collect(body, date):
                    result = {'new': [], 'changed': [], 'unchanged': 0, 'errors': []}
                    with patch.object(fetch, 'TODAY', date), patch.object(fetch, 'http_get', side_effect=[f'[Page]({url})', body]):
                        fetch.collect_source('adyen', cfg, source, None, False, result)
                    return result
                result = collect('# Original', '2026-09-14')
                old = Path(tmp) / folder / '2026-09-14.md'
                self.assertTrue(old.exists(), str(old))
                original = old.read_bytes()
                self.assertEqual(result['new'], [folder + '/2026-09-14.md'])
                self.assertEqual(collect('# Original', '2026-09-15')['unchanged'], 1)
                result = collect('# Changed', '2026-09-15')
                self.assertEqual(result['changed'][0][:2], (folder + '/2026-09-15.md', folder + '/2026-09-14.md'))
                self.assertEqual(old.read_bytes(), original)
                current = Path(tmp) / folder / '2026-09-15.md'
                before = current.read_bytes()
                collect('# Do not overwrite', '2026-09-15')
                self.assertEqual(current.read_bytes(), before)


if __name__ == '__main__':
    unittest.main()
