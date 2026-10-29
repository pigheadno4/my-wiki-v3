# Clearpay overview retrieval checks

## Q1 — What Clearpay scope does this page describe, and what cannot be inferred?

Route `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-clearpay]]` → `[[raw/adyen/docs/payment-methods/clearpay/2026-09-15]]`. Canonical source stem: `source-adyen-docs-payment-methods-clearpay`. Full pinned raw path: `raw/adyen/docs/payment-methods/clearpay/2026-09-15.md`. Raw lines 23–29 describe UK Clearpay, four installments and a GB/GBP redirect matrix. Raw line 31 names separate regional brands. The captured page does not establish current merchant/account eligibility, approval of a shopper, a completed transaction or behavior of the US/ANZ products.

## Q2 — Which capabilities, conditions and dispute warnings matter?

Use the same root/provider/concept/source/raw route. Raw line 25 makes Clearpay's full fraud-risk assumption and merchant payment up front conditional on successful preapproval risk checks. The line 29 matrix marks recurring unavailable and refunds, separate/partial/multiple partial captures and chargebacks available for its GB/GBP row. Raw lines 33–37 give a 120-day shopper dispute initiation window, 13-day merchant defend/accept response period (silence or acceptance loses dispute and debits account), and 30-day Clearpay decision period after a defense. Raw lines 39–81 route to platform, API-only and Pay by Link guides; the overview does not implement those paths.
