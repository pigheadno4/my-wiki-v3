# C37 fixed-query audit B — jobs 5–8

## Shared checks

- Fully read all four selected source pages and pinned raw files, plus the routed concept sections. Root/provider/concept/source/raw links resolve in both routed directions where required. Recomputed SHA-256 values exactly match the C37 manifest.
- Gap sweep found processor/region sibling pages, but none was needed to support these exact-route answers. The only material comparison needed here is already within the selected evidence: AU preserves its internal settled-transaction/all-authorizations tension, while APAC states a separately scoped operation-specific rule; no universal resolution is inferred.

## Job 5 — APAC statements and reconciliation

Route: `wiki/index.md:11` → `wiki/braintree-index.md:549` → `wiki/concepts/payment-reconciliation-reporting.md:113` ↔ `wiki/sources/braintree/source-braintree-articles-apac-statements-reconciliation.md:46,50` → `raw/braintree/articles/apac/statements-reconciliation-2026-09-16.md` (`sha256 4c96755c02b11215fc510b8ada3f6fe1981f6aed3ec66fde1e55abb222eef32b`).

1. **Scope — PASS.** Exact Braintree-hosted APAC statements/reconciliation snapshot: monthly merchant statements, settlement-currency Daily Disbursement Details, and the daily APAC Transaction Detail Report. It is account/pricing/fee/timing-qualified APAC documentation, not AU transfer policy, independent bank authority, a guarantee of arrival, or proof of an individual settlement/deposit. Raw identity and availability are at lines 1–19; settlement-currency and disbursement scope at 57–70; report scope at 73–86.
2. **Purpose/action — PASS.** Use the Control Panel statements and same-disbursement-date APAC Transaction Detail Report to reconcile settlement totals, transaction fees, chargebacks, and bank deposits. `View Statements` is required for statements (17–28); `Create, Run, and Download Reports` is required for the report (82–93). Fee arithmetic is qualified because the report excludes authorization and chargeback fees (96–100), and the first monthly disbursement also requires the statement-listed authorization-fee deduction (103–104); cutoff and rollover limitations are at 43–54 and 57–70.

## Job 6 — AU pricing and fees

Route: `wiki/index.md:11` → `wiki/braintree-index.md:531` → `wiki/concepts/braintree-payment-platform.md:32` ↔ `wiki/sources/braintree/source-braintree-articles-au-pricing-fees.md:42,46` → `raw/braintree/articles/au/pricing-fees-2026-09-16.md` (`sha256 0fb90cbd9f0f6048e9e102dc7dca9b81faa359eb053630ec278e90cda4e367bf`).

1. **Scope — PASS.** Exact AU documentation route for account-determined transaction and billable-event fees plus IC+ and IC++ pricing models. It provides no numeric rate schedule, merchant agreement, FX/multi-currency rule, or universal/current Australian policy. Account dependence is explicit at raw line 16 and pricing-model assignment at 46–48.
2. **Purpose/action — PASS.** Determine which fee classes/model apply to the merchant account and route account questions to Braintree. Preserve the page's own wording tension: transaction fees are introduced for settled transactions at 24–26, while the per-transaction fee applies to all authorizations—including verifications, failures, voids, and refunds—at 29–38. Billable-event triggers and possible multiplicity are at 41–43; IC+/IC++ composition, variability, and last-business-day monthly deduction at 51–62; agreement-set chargeback/pre-arbitration fee and time-qualified no-retrieval-fee wording at 65–67.

## Job 7 — APAC pricing and fees

Route: `wiki/index.md:11` → `wiki/braintree-index.md:531` → `wiki/concepts/braintree-payment-platform.md:33` ↔ `wiki/sources/braintree/source-braintree-articles-apac-pricing-fees.md:40,49` → `raw/braintree/articles/apac/pricing-fees-2026-09-16.md` (`sha256 9e90febc9a3a73e6305125bce3533f649bdb423edb86dcf2ca70aa30f15c6b06`).

1. **Scope — PASS.** Exact APAC documentation route for account-selected blended/IC++ pricing, fee operation scope, APAC Transaction Detail reporting, refund/void treatment, and settlement-currency dispute fees. It is not AU/AIB evidence, a merchant-specific agreement, or a current universal rate schedule. Raw account/model and regional document scope are at lines 17–33 and 36–63.
2. **Purpose/action — PASS.** Apply the account's model: per-transaction fee to approved/declined authorizations, verifications, voids, and gateway rejections; ad valorem only to settled transactions; deduct fees before disbursement (17–28). Blended/IC++ components and account/currency/card/merchant variability are at 36–49, including the snapshot's additional 1% IC++ multi-currency conversion fee. The report's usual timing—not a guarantee—and contents are at 54–63. Refund wording must remain paired: no refund-processing fee, but a full refund credits everything except the original per-transaction fee (66–70). Outcome-independent 30 SGD/160 HKD/90 MYR chargeback/pre-arbitration fees and time-qualified retrieval exclusion are at 73–82.

## Job 8 — APAC transaction descriptors

Route: `wiki/index.md:11` → `wiki/braintree-index.md:538` → `wiki/concepts/braintree-control-panel.md:20` ↔ `wiki/sources/braintree/source-braintree-articles-apac-transactions-descriptors.md:33,37` → `raw/braintree/articles/apac/transactions/descriptors-2026-09-16.md` (`sha256 b75bd2ca73bb51f92cc4d96ea996ba8bdb8205654aa3efd0225c9981c7c7acba`).

1. **Scope — PASS.** Exact APAC-routed transaction-descriptor snapshot covering application-derived hard/soft descriptors and per-transaction API dynamic descriptors; no named processor or pricing schedule is established. It is not proof of current account/region eligibility, exact bank rendering, payment success, refund completion, or posting timing. Raw identity and descriptor scope are at lines 1–31.
2. **Purpose/action — PASS.** Use descriptors to identify purchases on customer statements: soft while an authorization is pending, hard after settlement/bank finalization, or a dynamic value replacing both (22–31). Hard/soft values come from the application and changes go through Braintree contact; PayPal changes use the PayPal console (17–18, 33–40). Required hard/soft field constraints are at 43–64; dynamic name/country/phone constraints and the per-transaction developer route at 67–100. Refunds default to the original transaction's dynamic descriptor (103–104), which does not prove refund completion or bank timing.

## Handoff

All eight fixed questions PASS; no blocking route, hash, scope, object/action, or material-qualification failure found.
