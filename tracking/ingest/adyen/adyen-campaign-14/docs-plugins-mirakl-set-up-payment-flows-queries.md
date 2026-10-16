# Fixed queries — docs-plugins-mirakl-set-up-payment-flows

## Q1 — purpose, scope, and non-inference

**Query:** Does Adyen's Mirakl connector implement marketplace pay-in and establish who is merchant of record or whether sellers received funds?

**Answer:** No. The guide says the connector does not manage payment flows; the marketplace operator separately implements authorisations, captures and refunds for seller transactions (raw lines 15–23). It describes balance-account splits and connector synchronization, but does not assign universal merchant-of-record status or prove a live payment, capture, final refund, seller payout, or bank receipt. The payout/commission guide is a separate route (raw lines 154–166). Canonical path: [[adyen-index]] → [[adyen-mirakl]] → [[source-adyen-docs-plugins-mirakl-set-up-payment-flows]] → pinned raw.

## Q2 — central capability, prerequisites, and warnings

**Query:** How does this Mirakl payment-flow guide coordinate payment, captures, refunds and chargebacks, and what limits matter?

**Answer:** A shopper order yields a pending Mirakl debit; the operator retrieves it with PA11, obtains seller-linked Adyen IDs with S20 (rate-limited), and sends Checkout payment or eligible capture data including `applicationInfo` and `splits` (raw lines 31–66). Methods must be marketplace-supported and requested for the merchant account; capture-time splits need separate-capture support; all sellers in a multi-seller order need split representation. The `PaymentFee` type needs Adyen contact and has balance/payout retry risks (lines 25–29, 33, 59–66). Captures and refunds must originate through Mirakl for sync, or Mirakl balances need manual adjustment. `CAPTURE`/`REFUND` webhooks can be followed by failures; Adyen recommends a 15-minute delay before irreversible Mirakl order-status changes, which does not establish finality (lines 119–143). Refunds can be split after Mirakl initiation; chargebacks can debit the liable balance account or follow the original split ratio (lines 131–152). Canonical path: [[adyen-index]] → [[adyen-mirakl]] → [[source-adyen-docs-plugins-mirakl-set-up-payment-flows]] → pinned raw.
