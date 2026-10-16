# Fixed queries — Adyen reserve

## Q1 — purpose, scope, and what must not be inferred

**Query:** What does the merchant-account reserve cover, and what happens when a refund lacks funds?

**Answer:** Reserve helps cover refunds, chargebacks and other operational expenses. A refund draws from pending and next payout balances before reserve; if all are insufficient, it fails. Adyen does not automatically retry an insufficient-funds failure, so the failed refund request must be resubmitted once funding is available. A configured threshold or top-up request does not prove a successful refund or completed funding. Raw: `raw/adyen/docs/account/balances/reserve/2026-09-15.md:17-25,39-41`. Canonical route: `[[source-adyen-docs-account-balances-reserve]]` → `[[adyen-account-structure]]`.

## Q2 — central capability, prerequisites, and warnings

**Query:** How are reserve funds added or released, and what roles, currency and transfer timing conditions matter?

**Answer:** Threshold increases draw from payable and decreases release excess to payable when the payout batch closes. Auto-funding initiates a payout-bank-account direct debit after the selected percentage of reserve is used and is limited to EUR/GBP/USD payout bank accounts; setup requires both Merchant financial and Merchant admin. A top-up is credited upon receipt, subject to the stated business-day timing; a different currency credits payable instead of reserve. Transfers require both merchant accounts to share company and legal entity and have a common processing currency. Customer Area transfer requires Merchant financial; API transfer requires Balance control API - Balances management and uses minor-unit amount. Source pending is debited on initiation, while destination pending may take up to an hour to show funds. The page has conflicting singular/plural API path text, so use its linked API reference to resolve implementation. Raw: `raw/adyen/docs/account/balances/reserve/2026-09-15.md:33-37,39-53,76-106,118-149,153-186,207-223`. Canonical route: `[[source-adyen-docs-account-balances-reserve]]` → `[[adyen-account-structure]]`.
