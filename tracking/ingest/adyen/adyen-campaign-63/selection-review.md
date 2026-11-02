# Adyen C63 recovered Checkout API selection

Status: **COMPLETE — all 10 sources approved and validated**. Prepared 2026-11-02.

Approved recovery collection completed for all37 gap items: **10 Checkout complete-body pages recovered**, **27 stub retries still title-only and excluded**, zero HTTP/network failures. A successful HTTP response is not evidence of substantive documentation: the27 HTTP200 stub responses remain ineligible. [Collection manifest](../../../collections/adyen/c63-recovery-2026-11-02/manifest.md), [collection summary](../../../collections/adyen/c63-recovery-2026-11-02/summary.json). Original preparation/collection scope is retained in [recovery-selection-review.md](recovery-selection-review.md).

Exact proposed ingestion: **10 new Checkout source units**, **20 fixed query answers**, **three distinct fixed full-read audits**. Raw captured2026-11-02; response bodies preserved byte-for-byte after collection metadata. Distinct raw hashes/URLs/targets, absent targets and unreferenced raw checked. Structural complete-body screens are not semantic full reads. Size: **34,352 whitespace words, 2,662 raw lines, 227,938 bytes**.

Current baseline **2,899 = 2,547 General Docs + 336 API Explorer + 16 GitHub**. Successful ingestion gives **2,909 = 2,547 General Docs + 346 API Explorer + 16 GitHub**. API Explorer now has373 raw snapshots:336 previously ingested complete-body pages,10 newly recovered complete-body pages,27 excluded stubs. Remaining unreferenced raw would fall37→27 after these ten pass. No complete upstream coverage claim. No semantic outcomes inferred from collection.

[Exact proposed provider authorization](dispatch-contract.md) retains ten shared rolling child slots, medium gpt-6-sol workers and different high initial reviewers, full numbered raw reads including all schemas/examples, 3–5 located quotes, concept audit first, max3attempts, coordinator-only serial approved concept-before-source promotion and aggregate close once. [20 original fixed prompts](proposed-queries.md) require actual independently checked answers.

Fixed coordinator audit jobs: `api-explorer-checkout-latest-get-paymentlinks-linkid`, `api-explorer-checkout-latest-post-payments-paymentpspreference-captures`, `api-explorer-checkout-latest-delete-storedpaymentmethods-storedpaymentmethodid`. Material partial/fail expands to allten. No runtime initialized, workers dispatched, wiki changes, commit or push. Await separate exact C63 ingestion approval.

| # | Operation | Words | Raw lines |
| --- | --- | ---: | ---: |
| 1 | GET `/paymentLinks/{linkId}` | 6,323 | 385 |
| 2 | PATCH `/paymentLinks/{linkId}` | 6,375 | 399 |
| 3 | POST `/payments/{paymentPspReference}/amountUpdates` | 4,055 | 331 |
| 4 | POST `/payments/{paymentPspReference}/cancels` | 1,519 | 229 |
| 5 | POST `/payments/{paymentPspReference}/captures` | 7,461 | 573 |
| 6 | POST `/payments/{paymentPspReference}/refunds` | 6,030 | 387 |
| 7 | POST `/payments/{paymentPspReference}/reversals` | 1,510 | 229 |
| 8 | GET `/sessions/{sessionId}` | 633 | 57 |
| 9 | PATCH `/sessions/{sessionId}` | 273 | 39 |
| 10 | DELETE `/storedPaymentMethods/{storedPaymentMethodId}` | 173 | 33 |

User approved exact C63 ingestion on 2026-11-02. Runtime activated after hash/count reconciliation; historical preparation statements above describe pre-approval state. No commit/push.

C63 closed: 2909 total sources; 346 API Explorer sources. Remaining 27 API raw pages are excluded title-only stubs. No commit/push.
