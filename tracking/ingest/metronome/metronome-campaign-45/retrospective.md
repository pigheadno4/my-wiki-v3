# Campaign 45 retrospective

Status: COMPLETE. Exact five-page selection approved. Runtime 2026-09-13T08:09:06Z–2026-09-13T08:30:59Z: 1,313 seconds (21m53s). No commit/push.

## Execution notes

- Initial native live-agent listing contained only coordinator. Preserve unrelated work and prior C43/C44 plus scheduler/rule edits, all uncommitted.
- Scope is documentation-only; prior C44 full suite passed 773 tests. No new full-suite loop.
- Long schema size is not a source-size target. No default cross-version analysis. Independent initial reviews and query audit remain required.
- Three actual native worker dispatches succeeded. Preflight confirmed all five hashes, latest local snapshots, absent source targets, and a passing capsule baseline (222 total sources, 70 unreferenced snapshots).

## Role timing

Pending UTC observations; windows overlap and cannot be added.

| Role | UTC observed interval | Qualification |
| --- | --- | --- |
| v1 worker | 08:10:43–08:12:39 | 1m56s excludes raw read, which finished before first captured clock; not full worker time |
| v2 worker | 08:10:05–08:13:49 | 3m44s reported full task interval |
| Commits worker | 08:10:32–08:13:28 | 2m56s reported full task interval |
| v1 full reviewer | 08:13:39–08:16:53 | 3m14s; full raw read finished 08:16:28 |
| Plan end worker | 08:14:44–08:17:41 | 2m57s |
| Commits full reviewer | 08:14:21–08:18:02 | 3m41s |
| Ordering worker | 08:18:23–08:20:52 | 2m29s |
| v2 full reviewer | 08:17:53–08:21:28 | 3m35s |
| Plan end full reviewer | 08:18:49–08:21:29 | 2m40s |
| Commits bounded worker 2 | 08:21:33–08:22:24 | 51s; no full raw reread |
| Commits targeted reviewer | 08:23:07–08:23:58 | 51s; no full raw reread |
| Ordering full reviewer | 08:22:05–08:24:23 | 2m18s |
| Audit A analysis | 08:22:36–08:25:55 | 3m19s for 6,691 selected raw lines and four questions |
| Audit B analysis | 08:25:16–08:28:28 | 3m12s; report/handoff tracked separately |

Audit B selected one additional 190-line raw: update-the-rate-card-products-order, because its related operation might resolve the omitted-product question. Full read confirmed it is a separate relative-move operation and cannot establish set-order omission behavior. This was justified query-driven depth, not a required historical sweep or new ingestion. All six answers passed; final completeness/handoff at 08:30:02, 1m34s after analysis end (4m46s group total). No repairs requested.

Audit A reported handoff 08:26:00; coordinator received/read it shortly after. Q1–Q4 pass, requested object/actions match, complete selected v1/v2 reads confirmed, no extra raw reads or repairs. Reports preserve observed route line numbers at read time, before later catalog insertions.

Last ordering source promoted by 08:24:50; audit B dispatched for commits, Plan end and ordering. All five approved reciprocal updates are navigation-only, across three existing concepts. Company/index/log aggregation completed by 08:25:41.

One aggregate mechanical/capsule validation passed by 08:26:13: 10 typed pages, exact candidate/receipt/source content, approved suggestion IDs and text/anchors, hashes, raw paths/canonical URLs, reciprocal links, unique catalog entries, provider routing and counts. Validator 0.462s. Capsule: 310 raw snapshots, 227 total source pages, 221 official-document source records, 65 unreferenced snapshots. Source words: v1 317, v2 363, commits 324, Plan end 312, ordering 253; total 1,569. Diff whitespace check passed. No repeated unit suite.

Commits promoted by 08:24:20. Its review-end to targeted-approval loop was 5m56s (08:18:02–08:23:58); worker and reviewer observed work summed to 1m42s, leaving 4m14s of queue/dispatch/handoff intervals. No simultaneous same-role competitor was ready when its targeted worker/reviewer was selected, so this does not isolate the new priority's causal effect. No full rereview or coordinator semantic repair.

v2 and Plan end promoted by 08:22:11 with separate approved reciprocal links; audit A for v1/v2 dispatched next, its slot subtracted from runtime capacity. The commits correction removed only access-type from a summary category list (plus attempt increment), leaving quotes, suggestions and raw locators unchanged. After worker completion it was dispatched immediately to the original reviewer for targeted review; no full reread. Initial correction wait was 3m31s from review end to worker start, reflecting existing role allocation/capacity rather than within-worker ordering among multiple jobs.

v1 first-pass approved and promoted by 08:17:54 with one reciprocal navigation link. Commits needs one bounded removal/qualification of access_type because the raw marks it with feature annotations and x-stainless-skip. The raw locator alone does not qualify that retained selector claim. Review requests targeted retry; shared suggestion is approved. At intake an ordering worker was active, so review-first allocation dispatched the ready Plan-end reviewer before this queued correction. No cross-role priority behavior was changed.

All three long-page workers confirmed full pinned-raw reads and passed receipt checks. With two initial reviewers active, the normal worker reserve assigned the fourth (Plan end) job before the queued v2 review; this is unchanged cross-role policy.

## Outcome

All five sources approved and promoted. First-pass 4/5; five full initial reviews, one targeted review, no full rereviews, rejected/failed jobs, coordinator semantic repairs or query repairs. Ten final query answers pass; one justified extra 190-line adjacent raw read. All five concept changes are reciprocal navigation entries across three concepts. Aggregate mechanical/capsule and whitespace checks passed once; close transition succeeded.

| Stage | UTC window | Elapsed / qualification |
| --- | --- | --- |
| Initialization through all initial workers finished | 08:09:06–08:20:52 | 11m46s including setup/queue; no precise all-worker start window because v1 captured clock after raw reading |
| Five initial reviews | 08:13:39–08:24:23 | 10m44s overlapping window |
| Bounded correction plus targeted review | 08:21:33–08:23:58 | 51s worker + 51s reviewer; intervening 43s handoff/dispatch |
| Initial rejection through targeted approval | 08:18:02–08:23:58 | 5m56s; 1m42s observed role work, 4m14s queue/dispatch/handoff |
| Promotions | first by 08:17:54, final by 08:24:50 | serial writes overlapping other jobs |
| Final promotion through aggregate validation | 08:24:50–08:26:13 | 1m23s including shared catalogs; validator 0.462s |
| Query audits | 08:22:36–08:30:02 | 7m26s overlapping window; A 3m24s reported, B 4m46s |
| Final audit handoff through closure | 08:30:02–08:30:59 | 57s |
| Operational total | 08:09:06–08:30:59 | 21m53s |

Do not sum overlapping windows. C44 closed in 18m01s: this run is 3m52s longer (~21.5%) despite 5.4x raw lines (8,149 vs 1,519). Sources total 1,569 words vs C44 1,489 (+5.4%); the long v1/v2 pages produced 317/363-word sources. This supports continuing retrieval-sized sources on long schemas, not a causal benchmark or a promise for future pages. First-pass >=4/5 and <=35m observations both met.

The one failure came from retaining an unnecessary feature-annotated selector category without qualification. Removing it preserved raw discoverability and avoided full rereview. No new invariant/checklist is warranted. The targeted path worked but had no simultaneous same-role competitor, so priority-specific savings remain unproven. Audit B's report/check handoff still cost 1m34s after analysis; keep the existing compact-report instruction rather than adding a new reporting mechanism or reopening this completed audit.

Five frozen-inventory canonical identities remain: create-a-package, get-a-contract-v1, list-all-packages, get-a-package, and update-the-rate-card-products-order. No next campaign is authorized by this closure. All modifications remain local/uncommitted, preserving prior campaigns/rule changes and unrelated PayPal work/CLAUDE copy.md. No collection, historical source rewrite, commit or push. Final retrospective prose after operational closure is excluded from 21m53s.
