# Adyen C60 API Explorer webhook selection

Status: **COMPLETE — all 50 exact approved sources ingested and validated**. Prepared 2026-10-31.

C59 committed and pushed as `f23dace2e21080c4afefea0219e124609e2587f0`; origin/main exact SHA verified. C60 proposes **50 complete-body pages across five API Explorer families**: Webhooks 35, ManagementNotification 9, Forward-API-webhooks 2, relayed-authorisation-webhooks 2, onboarding-on-invite-webhooks 2. All 27 title-only stubs are excluded. This continues webhook coverage with Standard payment-event, management, Forward API, relayed-authorisation and onboarding reference families. Family names identify scope; semantics require full reads during approved ingestion.

Size: **23,832 whitespace words, 3,209 raw lines, 172,877 bytes**. Mechanical metadata/body-presence checks only, not semantic reads or ingestion. All exact hashes, latest local pins, distinct canonical URLs/targets, absent targets and unreferenced raw checked. Selection covers available local pins, not complete upstream coverage.

Verified baseline **2763 = 2547 General Docs + 200 API Explorer + 16 GitHub**. Successful ingestion of all fifty gives **2813 = 2547 General Docs + 250 API Explorer + 16 GitHub**. Unreferenced API raw pages would decline **163 → 113**, including the same 27 excluded stubs (86 other complete-body pages). Reconcile concurrent work at activation and close. Other families/General Docs remain out of scope.

Proposed ten shared rolling child slots, medium gpt-6-sol workers and different high initial reviewers. Full numbered model-visible reads of every payload/response schema/example, reread truncation, 3–5 located exact quotes, concept audit first, max three attempts, serial coordinator-only approved concept-before-source promotion, aggregate close once. No size or initial-review waiver. Relayed request/response decisions retain their own contract instead of inheriting generic acknowledgement behavior. [Exact proposed authorization](dispatch-contract.md).

Three fixed root audits: `api-explorer-webhooks-latest-overview`, `api-explorer-relayed-authorisation-webhooks-latest-post-balanceplatform-authorisation-relayed`, `api-explorer-webhooks-latest-post-authorisation`. Material partial/fail expands audits to all fifty. [100 fixed query prompts](proposed-queries.md); exhaustive structural and existing touched typed validation at close. No current availability, delivery or payment proof from snapshots.

| # | Pinned raw | Words | Lines |
| --- | --- | ---: | ---: |
| 1 | `raw/adyen/api-explorer/Webhooks/latest/overview/2026-09-15.md` | 596 | 63 |
| 2 | `raw/adyen/api-explorer/Webhooks/latest/post/AUTHORISATION/2026-09-15.md` | 474 | 68 |
| 3 | `raw/adyen/api-explorer/Webhooks/latest/post/AUTHORISATION_ADJUSTMENT/2026-09-15.md` | 426 | 59 |
| 4 | `raw/adyen/api-explorer/Webhooks/latest/post/AUTORESCUE/2026-09-15.md` | 421 | 63 |
| 5 | `raw/adyen/api-explorer/Webhooks/latest/post/CANCELLATION/2026-09-15.md` | 418 | 59 |
| 6 | `raw/adyen/api-explorer/Webhooks/latest/post/CANCEL_AUTORESCUE/2026-09-15.md` | 423 | 61 |
| 7 | `raw/adyen/api-explorer/Webhooks/latest/post/CAPTURE/2026-09-15.md` | 418 | 59 |
| 8 | `raw/adyen/api-explorer/Webhooks/latest/post/CAPTURE_FAILED/2026-09-15.md` | 433 | 64 |
| 9 | `raw/adyen/api-explorer/Webhooks/latest/post/CHARGEBACK/2026-09-15.md` | 452 | 74 |
| 10 | `raw/adyen/api-explorer/Webhooks/latest/post/CHARGEBACK_REVERSED/2026-09-15.md` | 443 | 61 |
| 11 | `raw/adyen/api-explorer/Webhooks/latest/post/EXPIRE/2026-09-15.md` | 374 | 57 |
| 12 | `raw/adyen/api-explorer/Webhooks/latest/post/INFORMATION_SUPPLIED/2026-09-15.md` | 439 | 64 |
| 13 | `raw/adyen/api-explorer/Webhooks/latest/post/ISSUER_COMMENTS/2026-09-15.md` | 472 | 72 |
| 14 | `raw/adyen/api-explorer/Webhooks/latest/post/OFFER_CLOSED/2026-09-15.md` | 427 | 62 |
| 15 | `raw/adyen/api-explorer/Webhooks/latest/post/ORDER_CLOSED/2026-09-15.md` | 425 | 63 |
| 16 | `raw/adyen/api-explorer/Webhooks/latest/post/ORDER_OPENED/2026-09-15.md` | 413 | 57 |
| 17 | `raw/adyen/api-explorer/Webhooks/latest/post/PAIDOUT_REVERSED/2026-09-15.md` | 511 | 75 |
| 18 | `raw/adyen/api-explorer/Webhooks/latest/post/PAYOUT_DECLINE/2026-09-15.md` | 525 | 79 |
| 19 | `raw/adyen/api-explorer/Webhooks/latest/post/PAYOUT_EXPIRE/2026-09-15.md` | 517 | 75 |
| 20 | `raw/adyen/api-explorer/Webhooks/latest/post/PAYOUT_THIRDPARTY/2026-09-15.md` | 531 | 80 |
| 21 | `raw/adyen/api-explorer/Webhooks/latest/post/POSTPONED_REFUND/2026-09-15.md` | 427 | 62 |
| 22 | `raw/adyen/api-explorer/Webhooks/latest/post/PREARBITRATION_ACCEPTED/2026-09-15.md` | 371 | 32 |
| 23 | `raw/adyen/api-explorer/Webhooks/latest/post/PREARBITRATION_DECLINED/2026-09-15.md` | 371 | 32 |
| 24 | `raw/adyen/api-explorer/Webhooks/latest/post/PREARBITRATION_LOST/2026-09-15.md` | 429 | 64 |
| 25 | `raw/adyen/api-explorer/Webhooks/latest/post/PREARBITRATION_OPEN/2026-09-15.md` | 374 | 32 |
| 26 | `raw/adyen/api-explorer/Webhooks/latest/post/PREARBITRATION_WON/2026-09-15.md` | 415 | 58 |
| 27 | `raw/adyen/api-explorer/Webhooks/latest/post/RECURRING_CONTRACT/2026-09-15.md` | 444 | 68 |
| 28 | `raw/adyen/api-explorer/Webhooks/latest/post/REFUND/2026-09-15.md` | 424 | 59 |
| 29 | `raw/adyen/api-explorer/Webhooks/latest/post/REFUNDED_REVERSED/2026-09-15.md` | 419 | 59 |
| 30 | `raw/adyen/api-explorer/Webhooks/latest/post/REFUND_FAILED/2026-09-15.md` | 429 | 63 |
| 31 | `raw/adyen/api-explorer/Webhooks/latest/post/REPORT_AVAILABLE/2026-09-15.md` | 372 | 60 |
| 32 | `raw/adyen/api-explorer/Webhooks/latest/post/SCHEME_ARBITRATION/2026-09-15.md` | 380 | 32 |
| 33 | `raw/adyen/api-explorer/Webhooks/latest/post/SECOND_CHARGEBACK/2026-09-15.md` | 439 | 63 |
| 34 | `raw/adyen/api-explorer/Webhooks/latest/post/SETTLED_REVERSED/2026-09-15.md` | 464 | 63 |
| 35 | `raw/adyen/api-explorer/Webhooks/latest/post/TECHNICAL_CANCEL/2026-09-15.md` | 422 | 62 |
| 36 | `raw/adyen/api-explorer/ManagementNotification/latest/overview/2026-09-15.md` | 167 | 25 |
| 37 | `raw/adyen/api-explorer/ManagementNotification/latest/post/merchant.created/2026-09-15.md` | 668 | 61 |
| 38 | `raw/adyen/api-explorer/ManagementNotification/latest/post/merchant.updated/2026-09-15.md` | 825 | 133 |
| 39 | `raw/adyen/api-explorer/ManagementNotification/latest/post/paymentMethod.created/2026-09-15.md` | 354 | 53 |
| 40 | `raw/adyen/api-explorer/ManagementNotification/latest/post/paymentMethodRequest.removed/2026-09-15.md` | 337 | 36 |
| 41 | `raw/adyen/api-explorer/ManagementNotification/latest/post/paymentMethodRequest.scheduledForRemoval/2026-09-15.md` | 346 | 36 |
| 42 | `raw/adyen/api-explorer/ManagementNotification/latest/post/terminalAssignment.completed/2026-09-15.md` | 201 | 29 |
| 43 | `raw/adyen/api-explorer/ManagementNotification/latest/post/terminalBoarding.triggered/2026-09-15.md` | 201 | 31 |
| 44 | `raw/adyen/api-explorer/ManagementNotification/latest/post/terminalSettings.modified/2026-09-15.md` | 249 | 33 |
| 45 | `raw/adyen/api-explorer/Forward-API-webhooks/latest/overview/2026-09-15.md` | 65 | 16 |
| 46 | `raw/adyen/api-explorer/Forward-API-webhooks/latest/post/forwardApi.notification/2026-09-15.md` | 533 | 71 |
| 47 | `raw/adyen/api-explorer/relayed-authorisation-webhooks/latest/overview/2026-09-15.md` | 51 | 14 |
| 48 | `raw/adyen/api-explorer/relayed-authorisation-webhooks/latest/post/balancePlatform.authorisation.relayed/2026-09-15.md` | 3,534 | 399 |
| 49 | `raw/adyen/api-explorer/onboarding-on-invite-webhooks/latest/overview/2026-09-15.md` | 64 | 14 |
| 50 | `raw/adyen/api-explorer/onboarding-on-invite-webhooks/latest/post/balancePlatform.accountHolder.onboarded/2026-09-15.md` | 919 | 134 |

Five uncommitted preparation artifacts only; no runtime, workers, candidates or canonical pages created. Awaiting separate exact C60 ingestion approval. No collection/provider operations.

User approved exact C60 ingestion on 2026-10-31. Runtime activated after hash/count reconciliation; historical preparation statements above describe pre-approval state. No commit/push.

C60 close verified: 2813 = 2547 General Docs + 250 API Explorer + 16 GitHub. Historical preparation/activation figures above retain their original meaning. All 50 sources promoted, query/audit/structural/typed checks pass. No commit/push.
