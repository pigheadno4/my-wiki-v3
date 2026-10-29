# Afterpay overview retrieval check

- Canonical source stem: `source-adyen-docs-payment-methods-afterpaytouch`.
- Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-afterpaytouch.md` → `raw/adyen/docs/payment-methods/afterpaytouch/2026-09-15.md`.

## Q1 — Purpose, scope, and inference limit

**Query:** What product and regional scope does Adyen's Afterpay overview describe, and can its US/UK naming note or checkmarks establish current eligibility?

**Expected:** The pinned overview describes a buy now, pay later redirect method in AU/CA/NZ and lists AUD/CAD/NZD, with shoppers paying in four installments. US Cash App Afterpay and UK Clearpay are naming pointers, not an extension of the AU/CA/NZ table or proof of account availability. The table is a feature directory; its recurring/refund checkmarks say “See note,” without note text in this captured page. Evidence: raw `# Afterpay` lines 23–31.

## Q2 — Central flow, conditions and warnings

**Query:** What is the outlined Afterpay flow, who bears fraud risk, and which dispute deadlines are stated?

**Expected:** The shopper selects Afterpay and enters details; the merchant includes purchase-item information in the request, relies on its integration for redirect handling and captures payment. Afterpay performs shopper risk checks before approval; only **if successful** does the page say it takes full fraud risk and pays the merchant up front. The page states 120 days for shopper chargeback initiation, 13 days to defend or accept an opened dispute, account debit on loss, and 30 days for Afterpay's decision after a defense. These are captured source statements, not live account terms or successful execution proof. Evidence: raw `# Afterpay` line 25, `## How it works` lines 33–39 and `## Chargebacks` lines 41–45.
