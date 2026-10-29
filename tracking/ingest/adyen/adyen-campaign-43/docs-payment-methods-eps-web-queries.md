# docs-payment-methods-eps-web — Q1/Q2

Retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-eps-web]].

## Q1 — What is this page for, and what cannot be inferred?

[[source-adyen-docs-payment-methods-eps-web]] is an EPS **Web integration chooser** linking EPS Web Drop-in and Web Components, then the corresponding Sessions/Advanced main integration guides (raw/adyen/docs/payment-methods/eps/web/2026-09-15.md:15–36). It contains no request schema, redirect outcome, recurring-token flow or live-eligibility test; its links alone do not prove implementation or payment success (raw lines 19–36).

## Q2 — What central capability, prerequisites, and warnings are stated?

The page presents Web Drop-in as the all-in-one UI choice and Web Components as the other EPS-specific route (raw/adyen/docs/payment-methods/eps/web/2026-09-15.md:19–27). It says to create the main integration before adding EPS and links four base paths: Drop-in Sessions, Components Sessions, Drop-in Advanced and Components Advanced (raw lines 29–36). Consult the selected child and base guides for prerequisites, API fields, redirect handling and payment-result boundaries; this chooser does not state them.
