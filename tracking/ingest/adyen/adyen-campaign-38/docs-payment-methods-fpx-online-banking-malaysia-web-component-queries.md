# docs-payment-methods-fpx-online-banking-malaysia-web-component — attempt 1

Q1. What purpose and scope does this source serve, and what cannot be inferred?

It is Adyen's method-specific **FPX Online Banking Malaysia Web Component** add-on to an existing Components integration, divided into Sessions and Advanced server-side flows (source-adyen-docs-payment-methods-fpx-online-banking-malaysia-web-component; raw lines 15–25, 127–135). It does not itself supply a complete main integration, merchant eligibility decision, final bank-payment status or settlement proof (raw lines 19–23, 119–125, 171–177). The page does not state a currency or a Checkout API minimum for the Advanced section (raw lines 127–169).

Q2. What is its central capability, prerequisites and warnings?

Sessions requires an existing Web Components Sessions integration, Checkout API v68+, redirect handling and Customer Area method addition; it adds no extra `/sessions` parameters (source-adyen-docs-payment-methods-fpx-online-banking-malaysia-web-component; raw lines 25–42). The guide imports/initializes `MolPayEBankingMY`; Sessions offers optional bank issuer/display configuration, with `highlightedIssuers` introduced in Web v5.1.0 and a full issuer-ID table (raw lines 44–107). Advanced requires an existing Advanced Web Components integration, redirect handling and Customer Area method addition, with no extra `/payments` parameters stated (raw lines 127–169). The test-payment/status-check directions are distinct from the live Customer Area request and do not establish approval or a final result (raw lines 119–125, 171–177).

Retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-fpx-online-banking-malaysia-web-component]] → [[raw/adyen/docs/payment-methods/fpx-online-banking-malaysia/web-component/2026-09-15]].
