# docs-marketplaces-currency-conversion-refunds-your-platform retrieval probes

## Q1 — How does a Marketplace route a currency-conversion refund remainder to its platform?

Answer: The captured guide marks this as a limited-availability pilot (raw lines 19–20). For a **captured** online payment, the platform needs Checkout integration/API credentials, webhook handling, account-holder capabilities and configured merchant currencies (lines 32–44). POST `/payments/{paymentPspReference}/refunds` using the original customer processing-currency `amount` and original user settlement-currency `splits.amount`; add a `Remainder` split whose `account` is the **platform's liable balance account**, without specifying its amount (lines 53–99). In the example, the customer paid PLN 201.74 and the user received CZK 1000.00 (lines 24, 59–62).

Route: [[index]] → [[adyen-index]] → [[adyen-currencies-and-fx]] → [[source-adyen-docs-marketplaces-currency-conversion-refunds-your-platform]] → [[raw/adyen/docs/marketplaces/currency-conversion/refunds/your-platform/2026-09-15]].

## Q2 — Who bears the remainder, and what does the response prove?

Answer: The title, line 24, line 30, flow at lines 46–51 and explicit `Remainder.account` at lines 59–99 route the remainder to the platform liable account. Raw line 26 instead says “to the customer”; that is an internal wording conflict, not a separate allocation rule. The example response says `status: received` (lines 502–536), so it does not prove completed refund, customer credit, final booking, settlement or payout. Current pilot availability remains unverified.

Route: [[index]] → [[adyen-index]] → [[adyen-currencies-and-fx]] → [[source-adyen-docs-marketplaces-currency-conversion-refunds-your-platform]] → [[raw/adyen/docs/marketplaces/currency-conversion/refunds/your-platform/2026-09-15]].
