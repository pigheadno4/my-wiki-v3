# docs-marketplaces-currency-conversion-payments retrieval probes

## Q1 — What are processing and settlement currencies, and what choices does this Marketplace page route to?

Answer: The customer pays in the **processing currency**, while the user wants to receive the **settlement currency** (raw lines 24–26). The platform can fix the goods price in either currency, calculate the other amount using the day's prevailing exchange rate, and submit a POST `/payments` with both currency amounts (lines 28–39). The fixed-settlement route holds the user's amount constant; the fixed-processing route holds the customer's amount constant, with detailed guides linked at lines 41–51.

Route: [[index]] → [[adyen-index]] → [[adyen-currencies-and-fx]] → [[source-adyen-docs-marketplaces-currency-conversion-payments]] → [[raw/adyen/docs/marketplaces/currency-conversion/payments/2026-09-15]].

## Q2 — Does this overview establish current eligibility, an FX rate, or a completed payment?

Answer: No. It labels currency conversion **limited availability** and a **pilot** whose process may change (raw lines 19–20). It gives the sequence and two detailed-guide routes but no actual quoted rate, account entitlement, authorized/captured payment, booked user credit or payout evidence (lines 28–51). Consult the dated fixed-settlement or fixed-processing implementation guide for request and remainder detail, then verify current provider/account terms before operational use.

Route: [[index]] → [[adyen-index]] → [[adyen-currencies-and-fx]] → [[source-adyen-docs-marketplaces-currency-conversion-payments]] → [[raw/adyen/docs/marketplaces/currency-conversion/payments/2026-09-15]].
