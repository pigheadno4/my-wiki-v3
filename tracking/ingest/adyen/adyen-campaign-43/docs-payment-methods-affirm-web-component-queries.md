# Fixed retrieval checks — Affirm Web Component

Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-affirm-web-component.md`.

## Q1. What is this source's purpose and scope, and what cannot be inferred?

This 2026-09-15 guide adds **Affirm to existing Web Components** Sessions or Advanced integrations, with request fields, Component mounting, optional form data, capture and test/live gates (primary raw `raw/adyen/docs/payment-methods/affirm/web-component/2026-09-15.md:15-53,1259-1411`; canonical source stem `source-adyen-docs-payment-methods-affirm-web-component`). It does not itself prove shopper financing approval, current country/merchant eligibility, completed authorization, capture or settlement. The `allowedCountries` option controls address dropdown choices, not financing availability (`:1293-1307`). Live processing requires both Affirm-provided live credentials and an Affirm request/credentials in Adyen live Customer Area (`:1405-1411`).

## Q2. What are the central capabilities, prerequisites and warnings?

Use an existing Web Components Sessions or Advanced flow and add Affirm in Customer Area; v6 imports/mounts `Affirm` directly while v5 uses `checkout.create('affirm')` (`:19-45,1259-1289`). `/sessions` and `/payments` require shopper first/last name, phone and email; `countryCode` is described as required for **CA/UK** despite a blank Required cell because omission defaults to US; address `stateOrProvince` is required in CA/US but optional UK, and `lineItems` are recommended rather than required (`:51-64,766-779`). `readOnly` form groups require corresponding pre-filled data (`:1366-1397`). The curl samples contain literal hint-wrapped address keys and should not be copied as request field names (`:87-104,805-822`). Capture within **28 days** after authorization or it expires; capture starts installments, and lesser fulfillment requires capture then refund the difference per this guide (`:1399-1403`). TEST credentials come from Affirm, with a separate live Customer Area request and Affirm live credentials before acceptance (`:1405-1411`).
