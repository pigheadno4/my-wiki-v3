# Adyen C56 API Explorer selection and execution plan

Status: **COMPLETE — all 50 exact approved sources ingested and validated**.
Prepared 2026-10-30 after C55 commit `d1ae0ca000eb85eb43fbdcc88eade1cf68f39e4a` was pushed and remote origin/main exactly verified.

Scope expanded by the user on 2026-10-30 to **50 collected API Explorer pages**, preserving the original twenty Checkout pins unchanged and adding complete local families: **Payment 14, Recurring 7, Disputes 6 and BinLookup 3**. Total: **151,153 whitespace-delimited words**, **14,251 raw lines**, 1,014,363 bytes. These are mechanical size/body-presence checks, not semantic full reads or ingest completion. All fifty have body beyond a heading, distinct URLs and targets, latest available local pins and SHA-256. All **27 title-only stubs are explicitly excluded**, re-screened across all 363 API Explorer raw files.

The expanded scope groups Checkout with related Classic payment, recurring/token, dispute and card/BIN reference families. Approved source_required applies only to these fifty exact pins; no disposition change for the other API families. Keep API/version/object and historical/current boundaries explicit. In particular, Classic Payment contracts cannot fill missing Checkout schemas by analogy. Ten Checkout methods/paths lack page-level raw, as listed below; no collection is authorized.

Published C55 baseline: **2561 = 2547 General Docs + 0 API Explorer + 14 GitHub**. Relative to that baseline, successful promotion of all fifty gives **2611 = 2547 General Docs + 50 API Explorer + 14 GitHub**. API Explorer unreferenced raw pages would decrease from 363 to **313**, comprising 286 other complete-body pages plus the same 27 incomplete stubs. Independent shared-checkout work may advance source totals before execution: reconcile current approved catalogs/counts at activation and close and add fifty to that verified baseline. The Japanese General Docs page and older unreferenced Customer Area snapshot remain outside scope.

Use the prior coordinator-controlled model: ten shared rolling child slots, approved gpt-6-sol medium workers and different high reviewers; one full source per worker, full independent first reviews, 3–5 verbatim located quotes, concept audit first, serial approved promotion, aggregate close once, max three attempts. Preserve version/environment/object identity, required/conditional fields, failure/lifecycle/propagation behavior and asynchronous outcome boundaries. All large schema tables and examples require complete model-visible reads; no programmatic substitute or size waiver. [Exact approved authorization](dispatch-contract.md).

Predetermined root full-read audits: Checkout overview (standard); Checkout POST /payments (largest/schema-heavy); Payment POST /capture (ordinary sample). Any material partial/fail expands the audit to all fifty pages. One hundred [fixed query prompts](proposed-queries.md), raw/provenance/count/catalog/link checks and touched typed validation at close. General Docs and API Explorer source counts remain separately visible; no current-version or live-payment proof is implied.

| # | Path below api-explorer | Whitespace words | Raw lines |
| --- | --- | ---: | ---: |
| 1 | `Checkout/latest/overview` | 648 | 108 |
| 2 | `Checkout/latest/post/paymentMethods` | 5,976 | 2,053 |
| 3 | `Checkout/latest/post/sessions` | 15,955 | 880 |
| 4 | `Checkout/latest/post/payments` | 18,019 | 1,457 |
| 5 | `Checkout/latest/post/payments/details` | 3,077 | 293 |
| 6 | `Checkout/latest/get/storedPaymentMethods` | 1,547 | 112 |
| 7 | `Checkout/latest/post/storedPaymentMethods` | 1,914 | 168 |
| 8 | `Checkout/latest/post/orders` | 1,415 | 225 |
| 9 | `Checkout/latest/post/orders/cancel` | 1,015 | 194 |
| 10 | `Checkout/latest/post/paymentMethods/balance` | 8,645 | 477 |
| 11 | `Checkout/latest/post/cancels` | 1,506 | 225 |
| 12 | `Checkout/latest/post/paymentLinks` | 11,754 | 640 |
| 13 | `Checkout/latest/post/cardDetails` | 638 | 139 |
| 14 | `Checkout/latest/post/applePay/sessions` | 275 | 58 |
| 15 | `Checkout/latest/post/paypal/updateOrder` | 1,727 | 328 |
| 16 | `Checkout/latest/post/forward` | 1,190 | 111 |
| 17 | `Checkout/latest/post/donationCampaigns` | 1,463 | 247 |
| 18 | `Checkout/latest/post/donations` | 9,651 | 620 |
| 19 | `Checkout/latest/post/originKeys` | 994 | 195 |
| 20 | `Checkout/latest/post/validateShopperId` | 459 | 98 |
| 21 | `Payment/latest/overview` | 418 | 74 |
| 22 | `Payment/latest/post/adjustAuthorisation` | 2,132 | 204 |
| 23 | `Payment/latest/post/authorise` | 12,186 | 705 |
| 24 | `Payment/latest/post/authorise3d` | 8,933 | 406 |
| 25 | `Payment/latest/post/authorise3ds2` | 9,286 | 427 |
| 26 | `Payment/latest/post/cancel` | 2,032 | 189 |
| 27 | `Payment/latest/post/cancelOrRefund` | 1,579 | 199 |
| 28 | `Payment/latest/post/capture` | 2,171 | 208 |
| 29 | `Payment/latest/post/donate` | 1,201 | 171 |
| 30 | `Payment/latest/post/getAuthenticationResult` | 1,308 | 167 |
| 31 | `Payment/latest/post/refund` | 2,174 | 209 |
| 32 | `Payment/latest/post/retrieve3ds2Result` | 1,191 | 160 |
| 33 | `Payment/latest/post/technicalCancel` | 2,111 | 203 |
| 34 | `Payment/latest/post/voidPendingRefund` | 2,097 | 212 |
| 35 | `Recurring/latest/overview` | 367 | 90 |
| 36 | `Recurring/latest/post/createPermit` | 1,029 | 111 |
| 37 | `Recurring/latest/post/disable` | 878 | 112 |
| 38 | `Recurring/latest/post/disablePermit` | 772 | 99 |
| 39 | `Recurring/latest/post/listRecurringDetails` | 1,520 | 140 |
| 40 | `Recurring/latest/post/notifyShopper` | 1,127 | 147 |
| 41 | `Recurring/latest/post/scheduleAccountUpdater` | 1,252 | 172 |
| 42 | `Disputes/latest/overview` | 228 | 40 |
| 43 | `Disputes/latest/post/acceptDispute` | 621 | 117 |
| 44 | `Disputes/latest/post/defendDispute` | 642 | 119 |
| 45 | `Disputes/latest/post/deleteDisputeDefenseDocument` | 646 | 119 |
| 46 | `Disputes/latest/post/retrieveApplicableDefenseReasons` | 957 | 190 |
| 47 | `Disputes/latest/post/supplyDefenseDocument` | 702 | 128 |
| 48 | `BinLookup/latest/overview` | 224 | 54 |
| 49 | `BinLookup/latest/post/get3dsAvailability` | 1,205 | 154 |
| 50 | `BinLookup/latest/post/getCostEstimate` | 2,296 | 297 |

## Collected overview paths without page-level raw

These are navigation/collection gaps only; no schema or operation claims are inferred.

- `GET /paymentLinks/{linkId}`
- `PATCH /paymentLinks/{linkId}`
- `POST /payments/{paymentPspReference}/amountUpdates`
- `POST /payments/{paymentPspReference}/cancels`
- `POST /payments/{paymentPspReference}/captures`
- `POST /payments/{paymentPspReference}/refunds`
- `POST /payments/{paymentPspReference}/reversals`
- `GET /sessions/{sessionId}`
- `PATCH /sessions/{sessionId}`
- `DELETE /storedPaymentMethods/{storedPaymentMethodId}`

User approved the exact expanded manifest and provider contract on 2026-10-30. All fifty sources are promoted and validated; no commit or push. Current activation baseline is recorded in activation-baseline.json.

Verified close baseline: 2612 = 2547 General Docs + 50 API Explorer + 15 GitHub. Historical preparation totals above remain preparation evidence; current close counts include independent GitHub work. See results.md.
