# Cash App Afterpay overview retrieval check

- Canonical source stem: `source-adyen-docs-payment-methods-cash-app-afterpay`.
- Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-cash-app-afterpay.md` → `raw/adyen/docs/payment-methods/cash-app-afterpay/2026-09-15.md`.

## Q1 — Purpose, scope, and inference limit

**Query:** What regional product does this overview describe, and can its feature table or regional names prove current eligibility?

**Expected:** It describes US/USD Cash App Afterpay, also called $Afterpay, as a buy now, pay later redirect method for US merchants with four installments. Afterpay in AU/NZ and Clearpay in the UK are regional naming pointers, not a license to transfer the US table to them. The feature matrix is a captured directory, not account approval; refunds says “See note” without note text on this page, and recurring is marked unavailable. No completed payment or shopper approval is shown. Evidence: raw `# Cash App Afterpay` lines 15–31.

## Q2 — Central capability, risk condition, chargeback and route warnings

**Query:** What conditional risk/payout statement and chargeback windows are given, and where should implementation details be found?

**Expected:** Cash App Afterpay checks shopper risk before approval; only **if successful** does the page say it takes full fraud risk and pays the merchant up front. The chargeback section states 120 days for initiation, 13 days to defend or accept after an opened dispute, loss/account debit on no response or acceptance, and 30 days for a decision after defense. The page routes to Web, iOS, Android, API-only and Pay by Link guides; those routes own request, redirect/return and lifecycle implementation detail. These source statements do not prove live merchant terms or successful execution. Evidence: raw `# Cash App Afterpay` lines 23–29, `## Chargebacks` lines 33–37 and `## How do you want to integrate?` lines 39–69.
