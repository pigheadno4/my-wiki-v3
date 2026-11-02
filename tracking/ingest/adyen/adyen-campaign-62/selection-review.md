# Adyen C62 API Explorer final complete-body selection

Status: **COMPLETE — all 36 sources approved and validated**. Prepared 2026-11-01.

C61 committed and pushed as `7cb8a3b3794ea0ed6bd15d06feb8a0acd5104468`; origin/main exact SHA verified. C62 proposes **36 complete-body pages across ten API Explorer families**: terminal-api 19, Hop 3, BalanceControl 2, BalanceControlv1 2, Document-Collector 2, cloud-device-api 1, payments-app 1, possdk 2, sessionauthentication 2, softpos-configuration-api 2. These are all remaining unreferenced complete-body pages in the local API Explorer collection. The 27 title-only stubs remain excluded; the final round is 36 rather than padded to 50. Family/path metadata identifies scope only; behavioral claims require full reads during approved ingestion.

Size: **36,952 whitespace words, 3,224 raw lines, 239,318 bytes**. Mechanical metadata/body-presence checks only, not semantic reads or ingestion. All hashes, latest local pins, distinct canonical URLs/targets, absent targets and unreferenced raw checked. This is local collection coverage, not a claim of complete upstream API documentation.

Verified baseline **2863 = 2547 General Docs + 300 API Explorer + 16 GitHub**. Successful ingestion of all 36 gives **2899 = 2547 General Docs + 336 API Explorer + 16 GitHub**. Unreferenced API raw pages decline **63 → 27**, all 27 remaining pages being excluded title-only stubs. No complete-body local API Explorer pages would remain unreferenced. Reconcile concurrent work at activation and close.

Proposed ten shared rolling child slots, medium gpt-6-sol workers and different high initial reviewers. Full numbered model-visible reads of every schema/example, reread truncation, 3–5 located exact quotes, concept audit first, max three attempts, serial coordinator-only approved concept-before-source promotion, aggregate close once. No size or initial-review waiver. [Exact proposed authorization](dispatch-contract.md).

Three fixed root audits: `api-explorer-terminal-api-latest-overview`, `api-explorer-terminal-api-latest-post-payment`, `api-explorer-sessionauthentication-latest-post-sessions`. Material partial/fail expands audits to all 36. [72 fixed query prompts](proposed-queries.md) require actual located answers and independent answer checks. Exhaustive structural and existing touched typed validation at close. Snapshot evidence does not establish current availability or successful provider/device/payment operations.

| # | Pinned raw | Words | Lines |
| --- | --- | ---: | ---: |
| 1 | `raw/adyen/api-explorer/terminal-api/latest/overview/2026-09-15.md` | 797 | 152 |
| 2 | `raw/adyen/api-explorer/terminal-api/latest/post/abort/2026-09-15.md` | 883 | 56 |
| 3 | `raw/adyen/api-explorer/terminal-api/latest/post/admin/2026-09-15.md` | 265 | 40 |
| 4 | `raw/adyen/api-explorer/terminal-api/latest/post/balanceinquiry/2026-09-15.md` | 1,700 | 87 |
| 5 | `raw/adyen/api-explorer/terminal-api/latest/post/cardacquisition/2026-09-15.md` | 3,270 | 131 |
| 6 | `raw/adyen/api-explorer/terminal-api/latest/post/cardreaderapdu/2026-09-15.md` | 454 | 47 |
| 7 | `raw/adyen/api-explorer/terminal-api/latest/post/diagnosis/2026-09-15.md` | 602 | 53 |
| 8 | `raw/adyen/api-explorer/terminal-api/latest/post/display/2026-09-15.md` | 939 | 61 |
| 9 | `raw/adyen/api-explorer/terminal-api/latest/post/enableservice/2026-09-15.md` | 953 | 60 |
| 10 | `raw/adyen/api-explorer/terminal-api/latest/post/gettotals/2026-09-15.md` | 851 | 62 |
| 11 | `raw/adyen/api-explorer/terminal-api/latest/post/input/2026-09-15.md` | 2,113 | 97 |
| 12 | `raw/adyen/api-explorer/terminal-api/latest/post/login/2026-09-15.md` | 1,226 | 70 |
| 13 | `raw/adyen/api-explorer/terminal-api/latest/post/logout/2026-09-15.md` | 287 | 40 |
| 14 | `raw/adyen/api-explorer/terminal-api/latest/post/payment/2026-09-15.md` | 5,301 | 212 |
| 15 | `raw/adyen/api-explorer/terminal-api/latest/post/print/2026-09-15.md` | 592 | 51 |
| 16 | `raw/adyen/api-explorer/terminal-api/latest/post/reconciliation/2026-09-15.md` | 732 | 59 |
| 17 | `raw/adyen/api-explorer/terminal-api/latest/post/reversal/2026-09-15.md` | 1,887 | 100 |
| 18 | `raw/adyen/api-explorer/terminal-api/latest/post/storedvalue/2026-09-15.md` | 2,538 | 124 |
| 19 | `raw/adyen/api-explorer/terminal-api/latest/post/transactionstatus/2026-09-15.md` | 1,186 | 70 |
| 20 | `raw/adyen/api-explorer/Hop/latest/overview/2026-09-15.md` | 242 | 46 |
| 21 | `raw/adyen/api-explorer/Hop/latest/post/getOnboardingUrl/2026-09-15.md` | 1,364 | 146 |
| 22 | `raw/adyen/api-explorer/Hop/latest/post/getPciQuestionnaireUrl/2026-09-15.md` | 815 | 127 |
| 23 | `raw/adyen/api-explorer/BalanceControl/latest/overview/2026-09-15.md` | 211 | 47 |
| 24 | `raw/adyen/api-explorer/BalanceControl/latest/post/balanceTransfers/2026-09-15.md` | 765 | 111 |
| 25 | `raw/adyen/api-explorer/BalanceControlv1/latest/overview/2026-09-15.md` | 170 | 36 |
| 26 | `raw/adyen/api-explorer/BalanceControlv1/latest/post/balanceTransfer/2026-09-15.md` | 639 | 89 |
| 27 | `raw/adyen/api-explorer/Document-Collector/latest/overview/2026-09-15.md` | 219 | 50 |
| 28 | `raw/adyen/api-explorer/Document-Collector/latest/post/crossBorderInvoices/2026-09-15.md` | 1,327 | 224 |
| 29 | `raw/adyen/api-explorer/cloud-device-api/latest/overview/2026-09-15.md` | 475 | 90 |
| 30 | `raw/adyen/api-explorer/payments-app/latest/overview/2026-09-15.md` | 205 | 42 |
| 31 | `raw/adyen/api-explorer/possdk/latest/overview/2026-09-15.md` | 274 | 42 |
| 32 | `raw/adyen/api-explorer/possdk/latest/post/sessions/2026-09-15.md` | 380 | 61 |
| 33 | `raw/adyen/api-explorer/sessionauthentication/latest/overview/2026-09-15.md` | 235 | 41 |
| 34 | `raw/adyen/api-explorer/sessionauthentication/latest/post/sessions/2026-09-15.md` | 1,129 | 206 |
| 35 | `raw/adyen/api-explorer/softpos-configuration-api/latest/overview/2026-09-15.md` | 325 | 76 |
| 36 | `raw/adyen/api-explorer/softpos-configuration-api/latest/post/auth/certificate/2026-09-15.md` | 1,601 | 218 |

Five uncommitted preparation artifacts only; no runtime, workers, candidates or canonical pages created. Awaiting separate exact C62 ingestion approval. No collection/provider operations.

User approved exact C62 ingestion on 2026-11-02. Runtime activated after hash/count reconciliation; historical preparation statements above describe pre-approval state. No commit/push.

C62 closed: 2899 total sources; 336 API Explorer sources. Remaining 27 API raw pages are excluded title-only stubs. No commit/push.
