# Adyen C59 API Explorer webhook selection

Status: **COMPLETE — all 50 exact approved sources ingested and validated**. Prepared 2026-10-31.

C58 committed and pushed as `0622795e0d67d1dca9be8d380b8e4d509e167535`; origin/main exact SHA verified. C59 proposes **50 complete-body webhook reference pages**: Configuration 30, Transfer 3, Balance 3, Transaction 2, Report 2, Dispute 3, Capital 5, Negative Balance Compensation Warning 2. All 27 title-only stubs are excluded. This follows the modern balance-resource and transfer references with their event contracts; POST event references are incoming notification contracts, not provider operations to execute.

Size: **32,015 whitespace words, 4,707 raw lines, 246,359 bytes**. These are mechanical metadata/body-presence checks, not semantic reads or ingestion. All exact hashes, latest local pins, distinct canonical URLs/targets, absent targets and unreferenced raw checked. The selection covers available local pages, not complete upstream families or event semantics.

Verified baseline **2713 = 2547 General Docs + 150 API Explorer + 16 GitHub**. Successful ingestion of all fifty gives **2763 = 2547 General Docs + 200 API Explorer + 16 GitHub**. Unreferenced API raw pages would decline **213 → 163**, including the same 27 excluded stubs (136 other complete-body pages). Reconcile concurrent work at activation and close. Other families/General Docs remain out of scope.

Proposed ten shared rolling child slots, medium gpt-6-sol workers and different high initial reviewers. Full numbered model-visible reads of every payload/schema/example, reread truncation, 3–5 located exact quotes, concept audit first, max three attempts, serial coordinator-only approved concept-before-source promotion, aggregate close once. No size waiver. [Exact proposed authorization](dispatch-contract.md).

Three fixed root audits: `api-explorer-balanceplatform-webhooks-latest-overview`, `api-explorer-transfer-webhooks-latest-post-balanceplatform-transfer-updated`, `api-explorer-transfer-webhooks-latest-post-balanceplatform-transfer-created`. A material partial/fail expands audits to all fifty. [100 fixed query prompts](proposed-queries.md), exhaustive structural and existing touched typed validation at close. No current availability/delivery/payment proof from snapshots.

| # | Pinned raw | Words | Lines |
| --- | --- | ---: | ---: |
| 1 | `raw/adyen/api-explorer/balanceplatform-webhooks/latest/overview/2026-09-15.md` | 413 | 45 |
| 2 | `raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.accountHolder.created/2026-09-15.md` | 1,056 | 261 |
| 3 | `raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.accountHolder.updated/2026-09-15.md` | 1,022 | 244 |
| 4 | `raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccount.created/2026-09-15.md` | 528 | 59 |
| 5 | `raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccount.recurringTopUp.created/2026-09-15.md` | 550 | 92 |
| 6 | `raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccount.recurringTopUp.deleted/2026-09-15.md` | 550 | 92 |
| 7 | `raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccount.recurringTopUp.updated/2026-09-15.md` | 649 | 96 |
| 8 | `raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccount.updated/2026-09-15.md` | 530 | 60 |
| 9 | `raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountPayoutSchedule.created/2026-09-15.md` | 643 | 42 |
| 10 | `raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountPayoutSchedule.deleted/2026-09-15.md` | 642 | 42 |
| 11 | `raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountPayoutSchedule.updated/2026-09-15.md` | 643 | 42 |
| 12 | `raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountPayoutScheduleAutoApplication.failed/2026-09-15.md` | 273 | 32 |
| 13 | `raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountPayoutScheduleExecution.failed/2026-09-15.md` | 294 | 36 |
| 14 | `raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountPayoutScheduleExecution.skipped/2026-09-15.md` | 295 | 36 |
| 15 | `raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountPayoutScheduleExecution.succeeded/2026-09-15.md` | 294 | 36 |
| 16 | `raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountSweep.created/2026-09-15.md` | 993 | 80 |
| 17 | `raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountSweep.deleted/2026-09-15.md` | 993 | 80 |
| 18 | `raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountSweep.updated/2026-09-15.md` | 993 | 80 |
| 19 | `raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balancePlatformPayoutSchedule.created/2026-09-15.md` | 529 | 39 |
| 20 | `raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balancePlatformPayoutSchedule.deleted/2026-09-15.md` | 528 | 39 |
| 21 | `raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balancePlatformPayoutSchedule.updated/2026-09-15.md` | 529 | 39 |
| 22 | `raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.cardorder.created/2026-09-15.md` | 473 | 82 |
| 23 | `raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.cardorder.updated/2026-09-15.md` | 470 | 95 |
| 24 | `raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.mandate.created/2026-09-15.md` | 311 | 37 |
| 25 | `raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.mandate.updated/2026-09-15.md` | 311 | 37 |
| 26 | `raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.networkToken.created/2026-09-15.md` | 884 | 58 |
| 27 | `raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.networkToken.updated/2026-09-15.md` | 889 | 58 |
| 28 | `raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.paymentInstrument.created/2026-09-15.md` | 744 | 103 |
| 29 | `raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.paymentInstrument.updated/2026-09-15.md` | 680 | 78 |
| 30 | `raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.score.triggered/2026-09-15.md` | 424 | 75 |
| 31 | `raw/adyen/api-explorer/transfer-webhooks/latest/overview/2026-09-15.md` | 90 | 17 |
| 32 | `raw/adyen/api-explorer/transfer-webhooks/latest/post/balancePlatform.transfer.created/2026-09-15.md` | 2,986 | 371 |
| 33 | `raw/adyen/api-explorer/transfer-webhooks/latest/post/balancePlatform.transfer.updated/2026-09-15.md` | 4,766 | 1,290 |
| 34 | `raw/adyen/api-explorer/balance-webhooks/latest/overview/2026-09-15.md` | 103 | 23 |
| 35 | `raw/adyen/api-explorer/balance-webhooks/latest/post/balancePlatform.balanceAccount.balance.block.released/2026-09-15.md` | 633 | 101 |
| 36 | `raw/adyen/api-explorer/balance-webhooks/latest/post/balancePlatform.balanceAccount.balance.updated/2026-09-15.md` | 371 | 73 |
| 37 | `raw/adyen/api-explorer/transaction-webhooks/latest/overview/2026-09-15.md` | 79 | 20 |
| 38 | `raw/adyen/api-explorer/transaction-webhooks/latest/post/balancePlatform.transaction.created/2026-09-15.md` | 999 | 179 |
| 39 | `raw/adyen/api-explorer/report-webhooks/latest/overview/2026-09-15.md` | 73 | 16 |
| 40 | `raw/adyen/api-explorer/report-webhooks/latest/post/balancePlatform.report.created/2026-09-15.md` | 466 | 72 |
| 41 | `raw/adyen/api-explorer/dispute-webhooks/latest/overview/2026-09-15.md` | 75 | 17 |
| 42 | `raw/adyen/api-explorer/dispute-webhooks/latest/post/balancePlatform.dispute.created/2026-09-15.md` | 365 | 37 |
| 43 | `raw/adyen/api-explorer/dispute-webhooks/latest/post/balancePlatform.dispute.updated/2026-09-15.md` | 365 | 37 |
| 44 | `raw/adyen/api-explorer/capital-webhooks/latest/overview/2026-09-15.md` | 108 | 19 |
| 45 | `raw/adyen/api-explorer/capital-webhooks/latest/post/balancePlatform.balanceAccountHolder.capitalOffer.created/2026-09-15.md` | 496 | 43 |
| 46 | `raw/adyen/api-explorer/capital-webhooks/latest/post/balancePlatform.capital.dynamicOffer.created/2026-09-15.md` | 402 | 39 |
| 47 | `raw/adyen/api-explorer/capital-webhooks/latest/post/balancePlatform.grants.created/2026-09-15.md` | 468 | 40 |
| 48 | `raw/adyen/api-explorer/capital-webhooks/latest/post/balancePlatform.grants.updated/2026-09-15.md` | 491 | 42 |
| 49 | `raw/adyen/api-explorer/negative-balance-compensation-warning-webhooks/latest/overview/2026-09-15.md` | 92 | 14 |
| 50 | `raw/adyen/api-explorer/negative-balance-compensation-warning-webhooks/latest/post/balancePlatform.negativeBalanceCompensationWarning.scheduled/2026-09-15.md` | 454 | 62 |

Five uncommitted preparation artifacts only; no runtime, workers, candidates or canonical pages created. Awaiting separate exact C59 ingestion approval. No collection/provider operations.

User approved exact C59 ingestion on 2026-10-31. Runtime activated after hash/count reconciliation; historical preparation statements above describe pre-approval state. No commit/push.

C59 close verified: 2763 = 2547 General Docs + 200 API Explorer + 16 GitHub. Historical preparation/activation figures above retain their original meaning. All 50 sources promoted, query/audit/structural/typed checks pass. No commit/push.
