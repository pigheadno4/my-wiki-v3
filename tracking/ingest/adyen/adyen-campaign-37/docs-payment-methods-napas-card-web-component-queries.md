# docs-payment-methods-napas-card-web-component — attempt 1

Q1. What purpose and scope does this source serve, and what cannot be inferred?

It is a Napas card add-on for existing **Web Components** Sessions or Advanced integrations (source-adyen-docs-payment-methods-napas-card-web-component; raw lines 15–37). It does not itself establish current merchant enablement, an exact Checkout API minimum, the full Napas gateway/OTP return lifecycle or a successful authorization/settlement (raw lines 39–97). It names Napas card while showing `momo_atm` in both Component snippets; do not infer interchangeability with other method identifiers (raw lines 46–76).

Q2. What are its central capability, prerequisites and warnings?

The page requires the appropriate Web Components base integration and Customer Area addition, says no extra Napas fields are needed, and calls `/sessions` the default for **Components v5.0.0+** with `/payments` for an additional use case (raw lines 21–44). The v6+ snippet uses `new Redirect(..., { type: 'momo_atm' })`, whereas v5.x.x-or-earlier uses `checkout.create('momo_atm')`, both mounting to the named DOM element (raw lines 46–76). The page lists test-only card/OTP scenario fixtures and test status checks, while live acceptance needs a separate live Customer Area request; fixtures are not real-payment evidence or instructions for handling live card/PIN/OTP data (raw lines 78–91).

Retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-napas-card-web-component]] → [[raw/adyen/docs/payment-methods/napas-card/web-component/2026-09-15]].
