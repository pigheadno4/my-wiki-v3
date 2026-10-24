# docs-payment-methods-boost-web-component retrieval queries

Canonical source: [[source-adyen-docs-payment-methods-boost-web-component]] (`wiki/sources/adyen/source-adyen-docs-payment-methods-boost-web-component.md`).
Forward route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-boost-web-component]] → [[raw/adyen/docs/payment-methods/boost/web-component/2026-09-15|pinned raw]].

## Q1 — What is this page for, and what cannot be inferred?

It is a 2026-09-15 Boost Wallet add-on for an **existing Web Components** integration, split into Sessions and Advanced server-side flows (raw lines 15–25, 78–86). It is not a standalone integration specification, present-day eligibility record, or observed successful payment. Redirect setup is required, but this page does not show the return/details or webhook outcome path (raw lines 31–36, 82–86, 112–120). The Boost overview is a separate source for MY/MYR and capability claims. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-boost-web-component]] → pinned raw above.

## Q2 — What capability, prerequisites and warnings matter?

For Sessions, an existing Web Components Sessions flow needs Checkout API v68+, `action.type: redirect` handling and Boost added in Customer Area; no extra `/sessions` parameters or Boost configuration are stated (raw lines 31–42, 56–60). Advanced likewise needs an existing Advanced Components flow, redirect handling and Customer Area setup, with no extra `/payments` parameters stated (raw lines 80–86, 112–116). Both import and initialize `Redirect` (raw lines 46–72, 90–110), but the shown `NoneComponent`/`#None-container` and unquoted `type:molpay_boost` are snippet defects, so they should not be copied as verified runnable code (raw lines 70–72, 108–110). The guide states no Boost TEST environment and recommends LIVE penny tests; that is historical guidance, not permission or evidence of execution (raw lines 74–76, 118–120). Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-boost-web-component]] → pinned raw above.
