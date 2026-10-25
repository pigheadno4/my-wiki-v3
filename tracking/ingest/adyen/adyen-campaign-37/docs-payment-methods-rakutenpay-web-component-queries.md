# docs-payment-methods-rakutenpay-web-component — attempt 1

Q1. What purpose and scope does this source serve, and what cannot be inferred?

It is a Rakuten Pay-specific **Web Components Redirect** add-on for existing Sessions or Advanced integrations (source-adyen-docs-payment-methods-rakutenpay-web-component; raw lines 15–25, 90–98). It does not establish current merchant approval for a recurring model, LIVE enablement, runnable correctness of the initialization sample or a final transaction outcome (raw lines 70–88, 120–144). This page does not state its own country/currency matrix; the Rakuten Pay overview is separate authority.

Q2. What are its central capability, prerequisites and warnings?

Sessions requires Checkout API v68+, redirect handling, Customer Area addition and the existing Web Components flow, with no extra ordinary `/sessions` parameters/configuration; Advanced similarly needs the base Web Components/redirect flow and no extra ordinary `/payments` fields (raw lines 29–60, 90–128). The page uses the `Redirect` class, but both examples show `type:rakutenpay` without defining that identifier on the page (raw lines 48–71, 104–121). Recurring is tightly qualified: reviewed one-off card-on-file for subscription/unscheduled business models, a prohibition on card-on-file Recurring Processing Model initiation without periodic cadence, primarily Food & Beverage context, and an application for **every** model; explicit shopper permission is strongly recommended (raw lines 74–80, 130–136). TEST uses a named DGFT acquirer account and simulator without the wallet app, while live steps and final webhook semantics are absent (raw lines 82–88, 138–144).

Retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-rakutenpay-web-component]] → [[raw/adyen/docs/payment-methods/rakutenpay/web-component/2026-09-15]].
