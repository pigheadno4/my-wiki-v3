# docs-payment-methods-eps-ios-component — Q1/Q2

Retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-eps-ios-component]].

## Q1 — What is this page for, and what cannot be inferred?

[[source-adyen-docs-payment-methods-eps-ios-component]] is an EPS-specific iOS Component add-on to existing Sessions or Advanced integrations. It initializes `EPSComponent` from an issuer-list method and assumes the parent integration handles a redirect action (raw/adyen/docs/payment-methods/eps/ios-component/2026-09-15.md:15–36, 50–73, 122–168). It is not a standalone redirect-result or final-status guide. Test status lookup and live EPS request instructions do not prove merchant approval, actual payment success or settlement (raw lines 116–120, 211–215).

## Q2 — What central capability, prerequisites, and warnings are stated?

Sessions requires existing iOS Components, Checkout API v68+, redirect handling and Customer Area EPS setup; Advanced requires existing iOS Components, redirect handling and EPS setup but states no API minimum there (raw/adyen/docs/payment-methods/eps/ios-component/2026-09-15.md:25–36, 122–132). The page says no EPS-specific `/sessions` or `/payments` fields and no extra Component configuration; Sessions delegates `EPSComponent` to the session, Advanced delegates to self (raw lines 38–73, 134–168). Both snippets nevertheless pass `epsConfiguration`, and the Advanced requirement link points to Drop-in while labeling Components, so verify those snippets/links before implementation (raw lines 46–69, 128–155). Recurring is through SEPA Direct Debit: `/payments` token creation after permission guidance, token webhook only after settlement, then later `ContAuth` requests; live EPS requires a separate live Customer Area request (raw lines 75–120, 170–215).
