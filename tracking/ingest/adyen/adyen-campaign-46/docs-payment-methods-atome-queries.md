# Atome overview retrieval checks

## Q1 — Purpose, scope and what not to infer

**Canonical source stem:** `source-adyen-docs-payment-methods-atome`
**Full pinned raw:** `raw/adyen/docs/payment-methods/atome/2026-09-15.md`
**Verified locators:** `# Atome`, lines 15–25; payment journey lines 27–43; capability matrix lines 45–47; `## Transaction limits`, lines 49–56.
**Route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-atome.md` → pinned raw.
**Answer boundary:** This is a captured Atome method overview for MY/SG, fetched in 2026 and marked last modified in 2023. It does not prove current account enablement, shopper approval, payment success or additional markets.

## Q2 — Central capability, prerequisites and warnings

**Verified locators:** installments/risk/automatic capture line 25; desktop QR, mobile app and browser OTP paths lines 27–41; portable-electronics restriction line 43; matrix lines 45–47; limits lines 49–56.
**Answer boundary:** Atome is a three-installment redirect BNPL method in the snapshot. Shopper risk checks precede approval; first installment is charged during authorisation and capture is automatic afterward. Disable Atome for portable electronics in checkout. The table marks refunds and partial/multiple partial refunds but not recurring or merchant-initiated capture variants. Transaction limits vary by MY/SG and debit versus credit card; consult the exact raw table before applying amounts. The redirect back is a journey step, not proof of final payment.
