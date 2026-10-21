# Retrieval checks — docs-marketplaces-settle-funds-pass-through-settlement

Q1. How does pass-through settlement work, and how is it reconciled? Answer: Schemes/payment methods determine when proceeds reach batches; after batch close, Adyen says funds settle next business day, so a sales day can span multiple settlement days and batches can mix days. Refunds/chargebacks adjust before settlement, working days exclude bank holidays, and payment-level Accounting Reports are needed because day-total reconciliation is unavailable. Raw lines 19–39.

Q2. What lifecycle and configuration boundary matters? Answer: The snapshot explicitly deprecates the model and says it will not be available for new integrations after July 1, 2025. The same page says pass-through is enabled by default and documents an existing-account revert from sales-day settlement via PATCH `platformPaymentConfiguration` with `salesDayClosingTime: "00:00"` and `settlementDelayDays: null`, while an integer delay enables sales-day settlement. Those configuration examples do not prove present eligibility, settlement of a given payment, payout, or bank receipt. Raw lines 19, 41–62, 278–305.

Forward route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-settle-funds-pass-through-settlement]] → [[raw/adyen/docs/marketplaces/settle-funds/pass-through-settlement/2026-09-15]].
