---
title: "Adyen Pay by Bank (Europe) Web Component integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/pay-by-bank-europe/web-component"
raw_files:
  - "adyen/docs/payment-methods/pay-by-bank-europe/web-component/2026-09-15.md"
tags: [adyen, pay-by-bank-europe, web, components, open-banking, sepa-direct-debit]
---

## Overview

This 2026-09-15-captured Adyen guide adds **Pay by Bank (Europe)** to an existing **Web Components** integration using Sessions or Advanced server-side flow. Its metadata says last modified 2019-09-06, while the captured body includes v6 Component and later Checkout examples; use the pinned content and stated version gates rather than inferring a 2019 API baseline. The method overview separately says **onboarding requires Adyen approval** (related raw overview line 23). This page does not establish current country or merchant eligibility, live activation, a completed bank transfer, or successful settlement. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Prerequisites and fields:** Both Sessions and Advanced tabs require an existing Web Components integration at **v5.70.0 or later** and contact with Adyen Support to add the method in Customer Area. Both `/sessions` and `/payments` tables mark shopper `countryCode` required for available-method filtering; the stated two-letter format has a **QZ (Kosovo)** exception. The general API-reference line calls `/sessions` the default from v5.0.0, but does not supersede this method's v5.70.0 integration minimum. The v6 import link on this Components page points to a **Drop-in** route, so check the Components base guide when implementing imports (pinned raw lines 21–65).
- **Component and issuer choice:** The v6 examples import `PayByBank` and use `new PayByBank(checkout, configuration)`; v5.x examples use `checkout.create('paybybank', configuration)`, within the v5.70.0 minimum. Bank-list display is optional only **where issuer selection is supported**. The guide says Germany has too many banks to show a list, so Tink handles bank selection; in the UK a shopper can preselect from a merchant-shown list or select after redirect to Tink. `showImage`, `issuer`, `highlightedIssuers` and `placeholder` are optional configuration, with `highlightedIssuers` labeled added in v5.1.0; the UK issuer IDs are presented as captured test/live examples, not current availability. Issuer choice does not remove the redirect to Tink (raw lines 67–182).
- **Recurring is through SEPA Direct Debit:** The guide says Pay by Bank (Europe) recurring transactions use **SEPA Direct Debit**, not a recurring `paybybank` payment-method type. It strongly **recommends** explicit shopper permission for future charges because clarity on schedule and amount reduces chargeback risk; it does not phrase that recommendation as a technical required field. The described path creates a SEPA token, receives `recurring.token.created` with `storedPaymentMethodId`, then uses that ID for future `Subscription` or `UnscheduledCardOnFile` payments when the shopper is **not present**. The later examples use `paymentMethod.type: sepadirectdebit`, `shopperInteraction: ContAuth` and a recurring processing model (raw lines 184–200, 549–580, 898–924).
- **Example tension:** The section titled “Create a token” shows a `storedPaymentMethodId` already in its first request; an extra legacy request block under “unscheduled card-on-file” uses `recurringProcessingModel: Subscription` (raw lines 201–225 and 1241–1261). These do not provide a verified start-to-finish token creation recipe or prove that either recurring mode is already enabled for a merchant. Follow the linked tokenization guidance and actual API contract.
- **Results, testing and live setup:** The page says a successfully **received** payment response carries `resultCode: Received` and a `pspReference`, and instructs tracking success through webhooks; `Received` is not final settlement. It recommends testing approved, authentication-error and cancelled scenarios with Tink and lists historical UK, Germany, France and Finland test credentials and UK issuer IDs. Before live acceptance, add Pay by Bank (Europe) in the live Customer Area (raw lines 1522–1582). The related method overview warns that even a successful AUTHORISATION webhook can precede failed funding and chargeback; it says chargebacks cannot be defended (related raw overview lines 45–60). The overview prose names Germany, France and UK, while its matrix also lists Finland and this guide has Finland **test** credentials; those snapshots do not resolve current Finnish live eligibility (related raw overview lines 27, 41–43; this raw lines 1574–1582).

## Detail locators

- Requirements, v5.70.0 minimum, Support setup, v6 import route and required `countryCode`: pinned raw lines 21–65.
- v6/v5 Component creation, conditional bank-list display and optional issuer settings: lines 67–145; UK test/live issuer IDs: lines 146–182.
- SEPA recurring positioning, shopper-permission recommendation and token creation examples: lines 184–549.
- Token webhook, shopper-absent future payments and Subscription/UnscheduledCardOnFile examples: lines 549–1240; extra legacy Subscription block under the unscheduled heading: lines 1241–1520.
- `Received` result boundary, test scenarios/credentials and live Customer Area setup: lines 1522–1582.

## Related

- [[adyen-online-payments]]
- [[raw/adyen/docs/payment-methods/pay-by-bank-europe/2026-09-15|Pay by Bank (Europe) method overview raw, captured 2026-09-15]] — related approval, regional and settlement qualifications

## Raw Sources

- [[raw/adyen/docs/payment-methods/pay-by-bank-europe/web-component/2026-09-15|Pay by Bank (Europe) Web Component guide, captured 2026-09-15]]
