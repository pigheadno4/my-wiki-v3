# docs-marketplaces-currency-conversion-refunds-your-user retrieval probes

## Q1 — How can a Marketplace refund book the FX remainder to the user, and what are the prerequisites?

Answer: This captured page labels the feature a limited-availability pilot (raw lines 19–20). A captured online payment, Checkout integration/API credentials, required webhook handling, account-holder capabilities and currency setup precede a refund (lines 39–57). Option 1 sends original processing-currency `amount` and settlement-currency `splits.amount` with a `Remainder` split to the user's balance account (lines 69–76). Option 2 requires the Foreign Exchange API role and enablement, calculates `splitRefund` with `exchangeSide: sell`, then sends the adjusted settlement-currency split and user-directed remainder (lines 546–661). The customer receives the fixed processing-currency amount; the user bears the difference in settlement currency (lines 24–37, 61–67).

Route: [[index]] → [[adyen-index]] → [[adyen-currencies-and-fx]] → [[source-adyen-docs-marketplaces-currency-conversion-refunds-your-user]] → [[raw/adyen/docs/marketplaces/currency-conversion/refunds/your-user/2026-09-15]].

## Q2 — What is the booking and outcome boundary, and can the samples be copied directly?

Answer: The raw says mismatches or miscalculations are booked to the `Remainder` split's named balance account, with reconciliation through the Balance Platform Accounting Report (raw line 661). Its PLN 201.74/CZK 1000.00 example calculates CZK 1032.31 for the user's refund, including CZK 32.31 remainder (lines 585–643). The example Checkout response says `received`, which does not prove final refund, booking, or payout (lines 1095–1129). The FX curl at lines 607–611 omits a comma between JSON fields and uses a live endpoint at line 600, while Checkout examples use TEST; it is not a copyable request or authorization for live calls.

Route: [[index]] → [[adyen-index]] → [[adyen-currencies-and-fx]] → [[source-adyen-docs-marketplaces-currency-conversion-refunds-your-user]] → [[raw/adyen/docs/marketplaces/currency-conversion/refunds/your-user/2026-09-15]].
