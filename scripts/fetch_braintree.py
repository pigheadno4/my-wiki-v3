#!/usr/bin/env python3
"""Braintree documentation only: discover, then explicit smoke/full collection.

Serial, single-writer collector. Never ingests or overwrites accepted raw.
"""
import argparse
import datetime as dt
import hashlib
import json
import re
import subprocess
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urljoin, urlsplit, unquote

from collection_versions import classify_candidate, latest_prior, next_target

ROOT = Path(__file__).resolve().parents[1]
HOST = 'https://developer.paypal.com'
BASE = HOST + '/braintree/'
SMOKE = [BASE + p for p in (
    'articles/control-panel/overview', 'docs/start/overview',
    'docs/reference/request/transaction/sale',
    'docs/guides/credit-cards/client-side', 'graphql/guides')]


def canonical(url):
    if any(x in ('.', '..') for x in unquote(urlsplit(url).path).split('/')):
        raise ValueError('unsafe path: ' + url)
    p = urlsplit(urljoin(HOST, url))
    path = unquote(p.path).rstrip('/')
    if (p.scheme != 'https' or p.netloc != 'developer.paypal.com' or p.query
            or not path.startswith('/braintree/')
            or any(x in ('.', '..', '$') for x in path.split('/'))
            or not re.fullmatch(r'/[A-Za-z0-9_./-]+', path)):
        raise ValueError('out-of-scope or ambiguous URL: ' + url)
    path = path.replace('/braintree/md/', '/braintree/', 1)
    return HOST + path


def md_url(url):
    return canonical(url).replace('/braintree/', '/braintree/md/', 1)


def inventory(llms, sitemap):
    links = re.findall(r'^\s*-\s+\[[^\]]+\]\(([^)\s]+)\)', llms, re.M)
    tree = ET.fromstring(sitemap)
    if tree.tag.split('}')[-1] != 'urlset':
        raise ValueError('expected Braintree urlset; inspect changed discovery shape')
    locations = [e.text.strip() for e in tree.iter() if e.tag.split('}')[-1] == 'loc' and e.text]
    if not links or not locations:
        raise ValueError('empty discovery input')
    rows = {}
    for source, values in [('llms', links), ('sitemap', locations)]:
        for original in values:
            try:
                key = canonical(original)
                selected, reason = True, None
            except ValueError as exc:
                key, selected, reason = urljoin(HOST, original), False, str(exc)
            row = rows.setdefault(key, {'url': key, 'selected': selected, 'reason': reason, 'sources': [], 'original_urls': []})
            if source not in row['sources']:
                row['sources'].append(source)
            if original not in row['original_urls']:
                row['original_urls'].append(original)
    return [rows[k] for k in sorted(rows)]


def fetch(url):
    with tempfile.TemporaryDirectory() as tmp:
        dest = Path(tmp) / 'body'
        proc = subprocess.run(['curl', '-sS', '-L', '--max-redirs', '3', '--proto', '=https',
                               '--proto-redir', '=https', '--max-time', '35', '-o', str(dest),
                               '-w', '%{http_code}\n%{content_type}\n%{url_effective}', url],
                              capture_output=True, text=True, timeout=40)
        if proc.returncode:
            raise RuntimeError('curl error ' + str(proc.returncode) + ': ' + proc.stderr.strip()[:300])
        status, content_type, final = proc.stdout.split('\n', 2)
        return {'status': int(status), 'content_type': content_type.split(';')[0],
                'url': final, 'body': dest.read_bytes().decode('utf-8')}


def validate(response, url):
    body = response['body']
    if response['status'] != 200:
        raise ValueError('HTTP ' + str(response['status']))
    if response['url'].rstrip('/') != md_url(url):
        raise ValueError('unexpected redirect identity')
    if response['content_type'] not in ('text/plain', 'text/markdown', 'text/x-markdown'):
        raise ValueError('not Markdown/plain-text')
    content = re.sub(r'\A---\r?\n.*?\r?\n---\r?\n', '', body, count=1, flags=re.S).strip()
    lines = [line for line in content.splitlines() if line.strip()]
    if (len(content) < 100 or len(lines) < 2 or content.lower().startswith(('<html', '<!doctype'))
            or re.search(r'\A(?:#+\s*)?(?:no document found|404\b|page not found|access denied)', content, re.I)):
        raise ValueError('empty, title-only, or error body')
    slug = re.search(r'^slug:\s*[\x27\x22]?([^\s\x27\x22]+)', body, re.M)
    if slug and canonical('/braintree/' + slug.group(1).lstrip('/')) != canonical(url):
        raise ValueError('body slug does not match candidate identity')
    return body


def fallbacks(url, stage):
    path = urlsplit(url).path
    # Only SDK guide/reference families; never articles, GraphQL, or already qualified routes.
    if (not any(path.startswith('/braintree/docs/' + p) for p in ('guides/', 'reference/'))
            or re.search(r'/(node|ios|javascript|android|java|php|python|ruby|dotnet)(/|$)', path)
            or path.endswith('/overview')):
        return []
    suffixes = ['/node'] if stage == 2 else ['/ios/v7', '/javascript/v3', '/android/v5']
    return [url + suffix for suffix in suffixes]


def save_raw(root, url, body, date):
    raw = root / 'raw/braintree'
    relative = Path(canonical(url).split('/braintree/', 1)[1] + '.md')
    prior = latest_prior(raw, relative)
    candidate = '<!-- Source URL: ' + url + ' -->\n<!-- Fetched: ' + date + ' -->\n<!-- Discovery: llms.txt,sitemap.xml -->\n\n' + body
    previous = prior.read_bytes().decode('utf-8') if prior else None
    state = classify_candidate(previous, candidate)
    if state == 'unchanged':
        target = prior
    else:
        target = next_target(raw, relative, date)
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open('xb') as output:
            output.write(candidate.encode('utf-8'))
    return {'state': state, 'raw_path': target.relative_to(root).as_posix(),
            'sha256': hashlib.sha256(target.read_bytes()).hexdigest()}


def collect_target(root, parent, date, getter, emit, cache):
    successes = []
    for stage in (1, 2, 3):
        candidates = [parent] if stage == 1 else fallbacks(parent, stage)
        for candidate in candidates:
            event = {'target': parent, 'candidate': candidate, 'fetch_url': md_url(candidate), 'stage': stage}
            if candidate in cache:
                event.update(cache[candidate], cached=True)
            else:
                event['attempt'] = 1
                try:
                    response = getter(md_url(candidate))
                    event.update(status=response['status'], content_type=response['content_type'], final_url=response['url'])
                    body = validate(response, candidate)
                    event.update(save_raw(root, candidate, body, date))
                except Exception as exc:
                    event.update(state='failed', error=str(exc)[:500])
                cache[candidate] = {k: v for k, v in event.items() if k not in ('target', 'candidate', 'stage', 'fetch_url')}
            emit(event)
            if event['state'] != 'failed':
                successes.append({'url': candidate, 'raw_path': event['raw_path'], 'state': event['state']})
        if successes:
            break  # Stage 3 collects every applicable candidate, not only the first success.
    return {'target': parent, 'state': ('collected' if successes[0]['url'] == parent else 'recovered') if successes else 'failed',
            'variants': successes}


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('discover')
    collect = sub.add_parser('collect')
    collect.add_argument('--inventory', type=Path, required=True)
    mode = collect.add_mutually_exclusive_group(required=True)
    mode.add_argument('--smoke', action='store_true')
    mode.add_argument('--all', action='store_true', help='requires separate full-collection approval')
    args = parser.parse_args()
    stamp = dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H%M%S%fZ')
    tracking = ROOT / 'tracking/collections/braintree'
    if args.command == 'discover':
        responses = {name: fetch(BASE + filename) for name, filename in [('llms', 'llms.txt'), ('sitemap', 'sitemap.xml')]}
        for name, response in responses.items():
            expected = BASE + ('llms.txt' if name == 'llms' else 'sitemap.xml')
            if response['status'] != 200 or response['url'] != expected or response['body'].lstrip().lower().startswith(('<html', '<!doctype')):
                raise ValueError('invalid discovery response: ' + name)
        rows = inventory(responses['llms']['body'], responses['sitemap']['body'])
        snap = ROOT / 'raw/braintree/_discovery' / stamp
        out = tracking / 'inventories' / stamp
        snap.mkdir(parents=True, exist_ok=False)
        out.mkdir(parents=True, exist_ok=False)
        facts = {}
        for name, response in responses.items():
            filename = 'llms.txt' if name == 'llms' else 'sitemap.xml'
            data = response['body'].encode('utf-8')
            (snap / filename).write_bytes(data)
            facts[name] = {'path': (snap / filename).relative_to(ROOT).as_posix(), 'sha256': hashlib.sha256(data).hexdigest()}
        write_json(out / 'inventory.json', rows)
        facts['inventory_sha256'] = hashlib.sha256((out / 'inventory.json').read_bytes()).hexdigest()
        facts['selected'] = sum(r['selected'] for r in rows)
        facts['excluded'] = len(rows) - facts['selected']
        facts['coverage'] = {key: sum(r['sources'] == sources for r in rows) for key, sources in [('both', ['llms', 'sitemap']), ('llms_only', ['llms']), ('sitemap_only', ['sitemap'])]}
        write_json(out / 'manifest.json', facts)
        print(json.dumps(facts), flush=True)
        print('INVENTORY=' + str(out / 'inventory.json'), flush=True)
        return
    path = args.inventory.resolve()
    facts = json.loads(path.with_name('manifest.json').read_text())
    if hashlib.sha256(path.read_bytes()).hexdigest() != facts['inventory_sha256']:
        raise ValueError('inventory hash mismatch')
    for name in ('llms', 'sitemap'):
        if hashlib.sha256((ROOT / facts[name]['path']).read_bytes()).hexdigest() != facts[name]['sha256']:
            raise ValueError('discovery snapshot hash mismatch')
    selected = {r['url'] for r in json.loads(path.read_text()) if r['selected']}
    if args.smoke and not set(SMOKE) <= selected:
        raise ValueError('smoke targets absent from this inventory; review changed catalog')
    targets = SMOKE if args.smoke else sorted(selected)
    run = tracking / 'runs' / stamp
    run.mkdir(parents=True, exist_ok=False)
    write_json(run / 'manifest.json', {'inventory': str(path.relative_to(ROOT)), 'sha256': facts['inventory_sha256'], 'targets': targets, 'mode': 'smoke' if args.smoke else 'all'})
    def emit(event):
        with (run / 'attempts.jsonl').open('a') as output:
            output.write(json.dumps(event) + '\n')
    cache, results = {}, []
    for url in targets:
        result = collect_target(ROOT, url, dt.date.today().isoformat(), fetch, emit, cache)
        results.append(result)
        with (run / 'results.jsonl').open('a') as output:
            output.write(json.dumps(result) + '\n')
        print(json.dumps(result), flush=True)
    summary = {'targets': len(targets), 'direct': sum(r['state'] == 'collected' for r in results),
               'recovered': sum(r['state'] == 'recovered' for r in results),
               'failed': [r['target'] for r in results if r['state'] == 'failed'],
               'distinct_raw_paths': len({v['raw_path'] for r in results for v in r['variants']})}
    write_json(run / 'summary.json', summary)
    print('RUN=' + str(run), flush=True)
    print(json.dumps(summary), flush=True)
    print('STOP: collection only; no ingestion. Review failures and coverage before approval.')


if __name__ == '__main__':
    main()
