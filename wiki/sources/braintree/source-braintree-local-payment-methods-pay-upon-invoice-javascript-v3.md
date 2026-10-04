---
title: "Braintree Pay Upon Invoice — JavaScript v3"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/local-payment-methods/pay-upon-invoice/javascript/v3"
raw_files:
  - "braintree/docs/guides/local-payment-methods/pay-upon-invoice/javascript/v3-2026-09-16.md"
tags: [braintree, local-payment-methods, pay-upon-invoice, javascript, ratepay, germany]
---

## Overview

This collected Braintree developer guide is the JavaScript v3 route for Pay Upon Invoice (`pay_upon_invoice`), also called Rechnungskauf mit Ratepay. It describes a German invoice-based buy-now-pay-later method in which an eligible buyer can receive and inspect goods before paying Ratepay by bank transfer within 30 days; the buyer does not need a PayPal account. The snapshot says the method is in limited release for pilot merchants in Germany, so it does not establish current availability or eligibility.

## Key takeaways

- The guide limits this integration to eligible German merchants selling B2C goods to buyers in Germany, in EUR, with the listed EUR 5–2,500 transaction range. It requires method approval, acceptance of the Ratepay terms as part of the PayPal User Agreement, a valid VAT ID or the documented additional-VAT consequence, and shipment within seven days.
- Processing Local Payment Methods requires a valid PayPal business account linked in the Braintree Control Panel. The page gives separate Sandbox and Production onboarding routes for direct merchants; completing one environment's onboarding does not establish the other environment or live acceptance.
- In JavaScript v3, the merchant creates the data collector and Local Payment components, derives a `correlationId`, and calls `startPayment` with `paymentType: 'pay_upon_invoice'`. The `onPaymentStart` handler must store `data.paymentId` on the merchant server so a later Braintree webhook can be correlated. Calling `startPayment` or receiving that payment ID is initiation, not evidence of invoice approval, transaction creation, settlement or merchant funding.
- There is no merchant capture call. The guide says Braintree associates a transaction after confirmation that the invoice has been confirmed, and requires webhooks to report a successful transaction based on an invoice or a rejected invoice approval. Its funded-webhook payload is an example, not a guarantee that a particular transaction settled.
- The page says the merchant is funded immediately when the buyer successfully completes checkout and that the buyer pays Ratepay, but it separately advises verifying each successful transaction's settled amount in the merchant's PayPal account and not shipping until that amount is confirmed. It also requires shipment tracking, a response to Ratepay disputes within 10 business days, and retention of shipment and delivery proof for at least 180 days to avoid the stated automatic-reversal risk.

## Evidence boundaries

> [!warning] Availability and environment
> This is a 2026-09-16 documentation snapshot for JavaScript v3 and a pilot-only German method. It does not prove current release status, merchant approval, buyer eligibility, Sandbox onboarding, Production onboarding or successful payment execution.

> [!warning] Lifecycle and funding
> Keep `startPayment`, the server-stored payment ID, invoice confirmation, the funded or expired webhook, transaction creation, example `settled` status and verification of funds in the merchant's PayPal account as distinct evidence points. The page's immediate-funding statement does not remove its instruction to verify the settled amount before shipment.

## Detail locators

- Limited-release status, German invoice-method identity, 30-day buyer payment and no-buyer-PayPal-account statement: `### Overview`, lines 17–23.
- Terms acceptance, Germany/EUR/B2C limits, transaction range, shipment timing, approval and VAT qualification: `### Eligibility`, lines 24–39.
- Ratepay risk decision, checkout/funding description, invoice instructions and buyer bank-transfer flow: `### How It Works`, lines 42–51.
- Settlement verification and do-not-ship-until-confirmed advice: `### How It Works`, lines 54–55.
- Dispute-response deadline, evidence requirements and 180-day retention warning: `#### Dispute handling`, lines 58–66; shipment-information duty: `#### Provide shipment information`, lines 67–73.
- Linked PayPal business-account prerequisite and separate Sandbox/Production onboarding links: `### Configuration`, lines 77–83.
- FraudNet/data-collector scope and desktop-browser qualification: `### FraudNet integration`, lines 90–92.
- `startPayment` and `correlationId` requirements: `### Invoke Pay Upon Invoice`, lines 93–97; callback and Promise examples, including server storage of `paymentId`: lines 100–260.
- Required `startPayment` parameter names: lines 261–277.
- No-capture transition and required funded/rejected webhook roles: `### Capturing Pay Upon Invoice Transactions`, lines 280–282, and `### Configure webhooks`, lines 283–313.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Article-level Local Payment Methods owner: [[source-braintree-payment-methods-local-payment-methods]]

## Related raw API references

The following collected pages were not used as factual authority for this source entry; they are exact-file navigation for follow-on implementation work:

- [[raw/braintree/docs/guides/local-payment-methods/configuration/javascript/v3-2026-09-16|JavaScript v3 Local Payment Methods configuration]]
- [[raw/braintree/docs/guides/local-payment-methods/server-side/node-2026-09-16|Node.js Local Payment Methods server-side guide]]
- [[raw/braintree/docs/guides/local-payment-methods/testing-go-live/node-2026-09-16|Node.js Local Payment Methods testing and go-live guide]]
- [[raw/braintree/docs/guides/webhooks/overview-2026-09-16|Braintree webhooks overview]]
- [[raw/braintree/docs/reference/general/webhooks/local-payment-methods/node-2026-09-16|Node.js Local Payment Method webhook reference]]

## Raw Sources

- [[raw/braintree/docs/guides/local-payment-methods/pay-upon-invoice/javascript/v3-2026-09-16|Braintree Pay Upon Invoice — JavaScript v3 guide]] - complete collected page covering method identity, eligibility, Ratepay flow, merchant obligations, JavaScript initiation, no-capture behavior and webhook outcomes
