# Fixed retrieval checks — Mirakl seller payouts

Q1. What is this source's purpose and scope, and what must not be inferred?
- Expected: A 2026-09-15 Adyen guide to the Mirakl connector's seller-payout and commission flow. A Mirakl seller invoice initiates payout of its net remaining amount; commissions and subscription fees are moved to the operator's liable balance account during that flow. The source does not define transaction merchant of record or legal seller, prove bank receipt, establish universal payout timing/currency/reversal treatment or show a live account completed a payout.
- Raw locators: `raw/adyen/docs/plugins/mirakl/payouts/2026-09-15.md:15-25`, `:27-40`.
- Canonical route: `wiki/sources/adyen/source-adyen-docs-plugins-mirakl-payouts.md` → `[[adyen-mirakl]]`.

Q2. What conditions, sequence and warnings control seller and operator payouts?
- Expected: For each Mirakl payment cycle, an invoice is created per seller and the connector attempts payout of the invoice net after commission/subscription fees; Mirakl billing cycles default to 10 days. On success, the connector initiates a separate `/transfers` request to move commission/fees to the operator's liable balance account. On failure, configured operators get email and the guide describes daily 03:00 CET retries, up to 10 before seller-account deactivation and another email. The connector does not pay operator commission to its bank; moving seller funds outside the connector can cause insufficient-balance missed payouts needing manual reconciliation. The older Mirakl overview generally says operator-implemented pay-in splits allocate seller funds and collect commission, whereas this payout guide says a `type`: **Commission** pay-in split is unnecessary for its later commission/fee transfer; keep these phases and both source routes distinct, without making either a universal rule. These are process descriptions, not guaranteed bank arrival or finality.
- Raw locators: `raw/adyen/docs/plugins/mirakl/payouts/2026-09-15.md:21-40`.
- Canonical route: `wiki/sources/adyen/source-adyen-docs-plugins-mirakl-payouts.md` → `[[adyen-mirakl]]`.
