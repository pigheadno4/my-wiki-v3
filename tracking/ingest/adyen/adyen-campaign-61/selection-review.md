# Adyen C61 API Explorer selection

Status: **COMPLETE — all 50 exact approved sources ingested and validated**. Prepared 2026-10-31.

C60 committed and pushed as `ddbf8ec15e3f978c9dbf81e59d62b4c5d3e0f224`; origin/main exact SHA verified. C61 proposes **50 complete-body pages across nine API Explorer families**: Notification 9, Tokenization-webhooks 5, managed-risk-webhooks 9, payment-webhooks 7, acs-webhook 3, capital 5, a2aissuer-api 7, transfers-api 3, open-banking 2. All 27 title-only stubs are excluded. This continues API Explorer coverage with Classic Notification, token lifecycle, managed risk, payment-event and ACS webhook references plus Capital, A2A issuer, transfers-api and open-banking references. Family names identify scope; semantics require full reads during approved ingestion.

Size: **36,936 whitespace words, 5,417 raw lines, 261,608 bytes**. Mechanical metadata/body-presence checks only, not semantic reads or ingestion. All exact hashes, latest local pins, distinct canonical URLs/targets, absent targets and unreferenced raw checked. Selection covers available local pins, not complete upstream coverage.

Verified baseline **2813 = 2547 General Docs + 250 API Explorer + 16 GitHub**. Successful ingestion of all fifty gives **2863 = 2547 General Docs + 300 API Explorer + 16 GitHub**. Unreferenced API raw pages would decline **113 → 63**, including the same 27 excluded stubs (36 other complete-body pages). Reconcile concurrent work at activation and close. Other families/General Docs remain out of scope.

Proposed ten shared rolling child slots, medium gpt-6-sol workers and different high initial reviewers. Full numbered model-visible reads of every payload/response schema/example, reread truncation, 3–5 located exact quotes, concept audit first, max three attempts, serial coordinator-only approved concept-before-source promotion, aggregate close once. No size or initial-review waiver. Provider APIs, asynchronous notifications and ACS challenge/decision contracts retain their own request, response and lifecycle semantics. [Exact proposed authorization](dispatch-contract.md).

Three fixed root audits: `api-explorer-notification-latest-overview`, `api-explorer-transfers-api-latest-post-disputes`, `api-explorer-tokenization-webhooks-latest-post-recurring-token-created`. Material partial/fail expands audits to all fifty. [100 fixed query prompts](proposed-queries.md); exhaustive structural and existing touched typed validation at close. No current availability, delivery or payment proof from snapshots.

| # | Pinned raw | Words | Lines |
| --- | --- | ---: | ---: |
| 1 | `raw/adyen/api-explorer/Notification/latest/overview/2026-09-15.md` | 280 | 37 |
| 2 | `raw/adyen/api-explorer/Notification/latest/post/ACCOUNT_CLOSED/2026-09-15.md` | 458 | 72 |
| 3 | `raw/adyen/api-explorer/Notification/latest/post/ACCOUNT_CREATED/2026-09-15.md` | 707 | 91 |
| 4 | `raw/adyen/api-explorer/Notification/latest/post/ACCOUNT_UPDATED/2026-09-15.md` | 672 | 87 |
| 5 | `raw/adyen/api-explorer/Notification/latest/post/BENEFICIARY_SETUP/2026-09-15.md` | 507 | 77 |
| 6 | `raw/adyen/api-explorer/Notification/latest/post/PAYMENT_FAILURE/2026-09-15.md` | 547 | 87 |
| 7 | `raw/adyen/api-explorer/Notification/latest/post/REPORT_AVAILABLE/2026-09-15.md` | 439 | 81 |
| 8 | `raw/adyen/api-explorer/Notification/latest/post/SCHEDULED_REFUNDS/2026-09-15.md` | 986 | 174 |
| 9 | `raw/adyen/api-explorer/Notification/latest/post/TRANSFER_FUNDS/2026-09-15.md` | 551 | 90 |
| 10 | `raw/adyen/api-explorer/Tokenization-webhooks/latest/overview/2026-09-15.md` | 102 | 19 |
| 11 | `raw/adyen/api-explorer/Tokenization-webhooks/latest/post/recurring.token.alreadyExisting/2026-09-15.md` | 313 | 52 |
| 12 | `raw/adyen/api-explorer/Tokenization-webhooks/latest/post/recurring.token.created/2026-09-15.md` | 300 | 52 |
| 13 | `raw/adyen/api-explorer/Tokenization-webhooks/latest/post/recurring.token.disabled/2026-09-15.md` | 293 | 50 |
| 14 | `raw/adyen/api-explorer/Tokenization-webhooks/latest/post/recurring.token.updated/2026-09-15.md` | 315 | 52 |
| 15 | `raw/adyen/api-explorer/managed-risk-webhooks/latest/overview/2026-09-15.md` | 147 | 25 |
| 16 | `raw/adyen/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.balance.block.released/2026-09-15.md` | 573 | 86 |
| 17 | `raw/adyen/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.reserveWaiver.applied/2026-09-15.md` | 262 | 46 |
| 18 | `raw/adyen/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.reserveWaiver.removed/2026-09-15.md` | 263 | 46 |
| 19 | `raw/adyen/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.rollingReserve.applied/2026-09-15.md` | 294 | 49 |
| 20 | `raw/adyen/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.rollingReserve.lifted/2026-09-15.md` | 231 | 45 |
| 21 | `raw/adyen/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.rollingReserve.updated/2026-09-15.md` | 295 | 49 |
| 22 | `raw/adyen/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.settlementDelay.lifted/2026-09-15.md` | 264 | 47 |
| 23 | `raw/adyen/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.settlementDelay.updated/2026-09-15.md` | 344 | 56 |
| 24 | `raw/adyen/api-explorer/payment-webhooks/latest/overview/2026-09-15.md` | 149 | 23 |
| 25 | `raw/adyen/api-explorer/payment-webhooks/latest/post/balancePlatform.incomingTransfer.created/2026-09-15.md` | 1,292 | 123 |
| 26 | `raw/adyen/api-explorer/payment-webhooks/latest/post/balancePlatform.incomingTransfer.updated/2026-09-15.md` | 1,282 | 125 |
| 27 | `raw/adyen/api-explorer/payment-webhooks/latest/post/balancePlatform.outgoingTransfer.created/2026-09-15.md` | 1,669 | 143 |
| 28 | `raw/adyen/api-explorer/payment-webhooks/latest/post/balancePlatform.outgoingTransfer.updated/2026-09-15.md` | 1,648 | 139 |
| 29 | `raw/adyen/api-explorer/payment-webhooks/latest/post/balancePlatform.payment.created/2026-09-15.md` | 2,100 | 389 |
| 30 | `raw/adyen/api-explorer/payment-webhooks/latest/post/balancePlatform.payment.updated/2026-09-15.md` | 2,008 | 396 |
| 31 | `raw/adyen/api-explorer/acs-webhook/latest/overview/2026-09-15.md` | 59 | 15 |
| 32 | `raw/adyen/api-explorer/acs-webhook/latest/post/balancePlatform.authentication.created/2026-09-15.md` | 1,009 | 177 |
| 33 | `raw/adyen/api-explorer/acs-webhook/latest/post/balancePlatform.authentication.relayed/2026-09-15.md` | 834 | 135 |
| 34 | `raw/adyen/api-explorer/capital/latest/overview/2026-09-15.md` | 451 | 66 |
| 35 | `raw/adyen/api-explorer/capital/latest/get/dynamicOffers/2026-09-15.md` | 628 | 66 |
| 36 | `raw/adyen/api-explorer/capital/latest/get/grantOffers/2026-09-15.md` | 851 | 85 |
| 37 | `raw/adyen/api-explorer/capital/latest/get/grants/2026-09-15.md` | 868 | 85 |
| 38 | `raw/adyen/api-explorer/capital/latest/post/grants/2026-09-15.md` | 787 | 71 |
| 39 | `raw/adyen/api-explorer/a2aissuer-api/latest/overview/2026-09-15.md` | 265 | 58 |
| 40 | `raw/adyen/api-explorer/a2aissuer-api/latest/post/ideal/profile/auth-link/2026-09-15.md` | 931 | 191 |
| 41 | `raw/adyen/api-explorer/a2aissuer-api/latest/post/ideal/profile/authenticate/2026-09-15.md` | 942 | 186 |
| 42 | `raw/adyen/api-explorer/a2aissuer-api/latest/post/ideal/profile/register/2026-09-15.md` | 988 | 207 |
| 43 | `raw/adyen/api-explorer/a2aissuer-api/latest/post/payments/cancel/2026-09-15.md` | 1,046 | 218 |
| 44 | `raw/adyen/api-explorer/a2aissuer-api/latest/post/payments/confirm/2026-09-15.md` | 1,454 | 301 |
| 45 | `raw/adyen/api-explorer/a2aissuer-api/latest/post/payments/details/2026-09-15.md` | 1,226 | 229 |
| 46 | `raw/adyen/api-explorer/transfers-api/latest/overview/2026-09-15.md` | 335 | 61 |
| 47 | `raw/adyen/api-explorer/transfers-api/latest/get/disputes/2026-09-15.md` | 850 | 91 |
| 48 | `raw/adyen/api-explorer/transfers-api/latest/post/disputes/2026-09-15.md` | 2,400 | 155 |
| 49 | `raw/adyen/api-explorer/open-banking/latest/overview/2026-09-15.md` | 242 | 48 |
| 50 | `raw/adyen/api-explorer/open-banking/latest/post/accountVerification/routes/2026-09-15.md` | 1,479 | 164 |

Five uncommitted preparation artifacts only; no runtime, workers, candidates or canonical pages created. Awaiting separate exact C61 ingestion approval. No collection/provider operations.

User approved exact C61 ingestion on 2026-10-31. Runtime activated after hash/count reconciliation; historical preparation statements above describe pre-approval state. No commit/push.

C61 close verified: 2863 = 2547 General Docs + 300 API Explorer + 16 GitHub. Historical preparation/activation figures above retain their original meaning. All 50 sources promoted, query/audit/structural/typed checks pass. No commit/push.
