---
title: "Clearpay API-only integration | Adyen Docs"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/clearpay/api-only"
raw_files:
  - "adyen/docs/payment-methods/clearpay/api-only/2026-09-15.md"
tags: [adyen, clearpay, api-only, redirect, checkout]
---

## Overview

This 2026-09-15 Adyen Docs page adds **Clearpay** to an existing API-only integration: the merchant builds the payment form, discovers the method, makes a server-side payment request and handles a redirect through the linked base guide. The related Clearpay overview identifies the UK brand and GB/GBP matrix. See [[adyen-online-payments]], [[source-adyen-docs-payment-methods-clearpay]] and [[adyen]].

## Key takeaways

- The prerequisite is an existing API-only Advanced-flow integration with redirect handling and Clearpay added in Customer Area (raw lines 23–29). The merchant-built form must collect full name, email, billing address and delivery address for Clearpay risk checks (lines 31–50). This is separate from the page's server request table.
- For `/paymentMethods` discovery, the guide says to use `countryCode: GB` and `amount.currency: GBP` to include Clearpay in the response (lines 52–60). Its v72 TEST response example shows `type: clearpay` (lines 61–91); that response is an example, not proof the method will be enabled for a given merchant. The example curl has `-X POST` on one line and `-d` on the next without a continuation (lines 64–69).
- The `/payments` table marks shopper name/email/reference (reference minimum three characters), country code, billing/delivery addresses and line items required; phone is optional (lines 93–106). The v72 TEST example sets `paymentMethod.type: clearpay` (lines 108–170) and has the same `-X POST`/missing-continuation issue (lines 111–116). Its initial response is `RedirectShopper` with a redirect action (lines 172–186), not final authorisation or capture proof. Use the linked base integration for return handling and outcome.
- Capture may be automatic after authorisation or manual, depending on merchant-account configuration. Delay requires delay setup or manual capture; partial capture requires manual capture. Clearpay requires capture within **13 days** after authorisation; otherwise it cancels and refunds the first instalment charged during authorisation. Test authorisations expire in **one day** (lines 188–196). A partial manual capture cancels the unclaimed remainder unless **multiple partial captures** are enabled by Support, which creates a new invoice per capture (lines 198–207).
- An uncaptured payment can be cancelled; captured funds are returned through refund. Full or partial refund requests specify `amount.value`, with `lineItems` optional (lines 209–218). The discount prose says a negative amount is required and calls the example **£1** off Item #2, but the example uses quantity **2** at **-100** minor units and lowers the order total by 200; it also omits a comma between the second item and discount object (lines 220–254). Treat that example as inconsistent, not copy-ready.
- Testing needs a Clearpay sandbox and shopper account, with regional sandbox details and linked test-card references. In sandbox the merchant display name is Adyen; live acceptance requires submitting a Clearpay request in live Customer Area (lines 256–271). Test status does not establish live enablement, capture, refund or settlement.

## Detail locators

- Scope, prerequisites, form and shopper details: raw lines 15–50.
- GB/GBP method discovery and v72 TEST example: lines 52–91.
- Payment request table, v72 TEST example and redirect response: lines 93–186.
- Capture expiry, partial capture, refunds/cancellations: lines 188–218.
- Discount prose/example conflict and malformed example: lines 220–254.
- Sandbox/live setup and base API-only route: lines 256–275.
- Linked overview UK/GB/GBP branding: `raw/adyen/docs/payment-methods/clearpay/2026-09-15.md` lines 23–31.

## Related

- [[adyen-online-payments]] — provider online-payment architecture.
- [[source-adyen-docs-payment-methods-clearpay]] — UK product and GB/GBP matrix.

## Raw Sources

- [[raw/adyen/docs/payment-methods/clearpay/api-only/2026-09-15|2026-09-15 Clearpay API-only redirect and lifecycle guide]]
