# Fixed retrieval checks — Getting paid

Q1. Whose funds and account flow does this guide cover, and what must not be inferred?
- Expected: Funds from Adyen-processed merchant transactions are sent to the merchant payout account separately by merchant account. The payout model assigns payable batches; a positive balance when a batch closes leads Adyen to instruct payout. This merchant-settlement route differs from the recipient Payout API. The source does not prove bank arrival, current account eligibility, a specific merchant-of-record allocation or live payout success.
- Raw locators: `raw/adyen/docs/account/getting-paid/2026-09-15.md:17-27`, `:72-74`.
- Canonical route: `wiki/sources/adyen/source-adyen-docs-account-getting-paid.md` → `[[adyen-sales-day-payout]]`; distinguish `[[adyen-payouts]]`.

Q2. How do the payout models, net amount, currency, timing and Customer Area roles differ?
- Expected: Sales day payout groups a whole sales day regardless of scheme transfer; pass-through can spread it over several batches. The captured guide calls sales day the default but pass-through the only model in Africa, Brazil and Turkey. Net payout deducts costs, refunds, chargebacks and adjustments. Like-for-like currency requires payment-method settlement support; payout currency depends on acquiring-connection country. Frequency is per merchant account; currency/bank-dependent bank-arrival guidance and holidays qualify timing. Payout viewing and schedule changes have separate listed roles, and changing destination bank account is a separate route.
- Raw locators: `raw/adyen/docs/account/getting-paid/2026-09-15.md:29-55`, `:63-86`, `:101-123`.
- Canonical route: `wiki/sources/adyen/source-adyen-docs-account-getting-paid.md` → `[[adyen-sales-day-payout]]`.
