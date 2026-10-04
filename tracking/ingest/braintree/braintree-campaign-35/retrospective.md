# Braintree C35 timing and retrospective

Status: complete. Runtime initialized 2026-10-04T05:32:25Z; operational close 2026-10-04T06:20:09Z. Total: 47m44s, versus C34 33m04s. This campaign did not achieve an overall speedup.

## Observed milestone windows

| Window | Elapsed | End UTC |
| --- | --- | --- |
| Start to last initial worker handoff | 17m06s | 05:49:31 |
| Remaining ordinary review tail | 4m19s | 05:53:50 |
| Canonical/catalog preparation tail | 59s | 05:54:49 |
| Initial query-analysis tail | 6m44s | 06:01:33 |
| Initial report-handoff tail | 50s | 06:02:23 |
| Audit conflict correction, targeted review and close | 17m46s | 06:20:09 |

These are non-overlapping milestone windows, not per-role CPU durations: worker, reviewer and coordinator activity overlaps. Final report persistence after operational close is not counted as model ingestion time.

- Raw volume: 2,216 lines / 16,606 words, versus C34 1,682 lines / 12,458 words (+33.3% words). Final sources: 11,699 words. Content sets differ; do not attribute latency changes solely to concurrency or prose guidance.
- Initial sources/catalogs ready in 22m24s, versus C34 24m21s. Despite more raw text, this ordinary pipeline was 1m57s shorter, but that is not a controlled speed benchmark.
- Initial first-review pass 17/20. Twenty full initial reviews, three ordinary targeted reviews, then two audit-driven targeted reviews. Zero repeated full reviews. Twenty-six worker attempts include one runtime-rejected missing-quote-index handoff; the final count of attempt-1 jobs is not the initial first-pass metric.
- Main delay was a real cross-page rounding conflict discovered in fixed queries after initial promotion. Two source corrections, one concept warning, one invalid handoff and targeted rechecks were required. Original failures preserved; no conflict suppressed to improve apparent pass rate.
- Final close checker initially used an overly strong assertion that pricing must link directly to Marketplace concept. Pricing correctly uses payment-platform as its main concept and links the Marketplace source through its warning. Corrected route assertion verifies each source's own main concept and the shared warning routes; no wiki edit was needed for this checker issue.
- Existing structural close passed all twenty sources and 372=355+17 catalogs; 28 initial typed pages and three amended-page checks passed. Final fixed queries 40/40, with original B failure and targeted addendum retained.

## Small next-round improvement

Use existing worker guidance to prevent the specific cross-page overclaim: a link proves navigation, not that the target supports a retained behavior. When the source explicitly attributes a durable rule to a linked page, either verify that page or keep the claim local and clearly bounded. Do not add another review layer or registry.

Validate required quote indexes before external handoff using the existing validator. Shorten audit reporting by stating repeated snapshot/route caveats once; initial reports still repeated detail and showed roughly 68–98 seconds between analysis and handoff in several groups. No hard word caps, new monitoring system or permanent validator changes.

No collection, GitHub ingestion, commit or push. Shared unrelated changes remain untouched.
