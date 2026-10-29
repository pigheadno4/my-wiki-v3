---
title: "Klarna Web Drop-in integration | Adyen Docs"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/klarna/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/klarna/web-drop-in/2026-09-15.md"
tags: [adyen, klarna, web-drop-in, online-payments]
---

## Overview

This 2026-09-15 Adyen Docs guide adds Klarna to an **existing Web Drop-in** integration using the Klarna widget in merchant checkout or a redirect to Klarna. It covers Sessions and Advanced server flows, Klarna request data, optional widget configuration, capture, recurring tokens and test/live preparation. It does not establish current merchant eligibility or a completed payment. See [[adyen-online-payments]], [[source-adyen-docs-payment-methods-klarna]] and [[adyen]].

## Key takeaways

- The prerequisite is a built Web Drop-in Sessions or Advanced flow and Klarna added in Customer Area. The page calls `/sessions` the default with Web Drop-in v5.0.0 or later; its `/payments` tab is for an additional use case. Web Drop-in v6 has a separate Klarna import. The guide's curl and API-library snippets use different pinned API/library versions and TEST endpoints; use their matching tab and version rather than mixing examples.
- Both endpoint tabs mark `lineItems`, `shopperEmail` and `countryCode` required for this Klarna guide. Klarna approval requires the line-item total to match `amount.value` and every line item to have `description`. The note says shopper email is needed to defend potential shopper disputes. `countryCode` must match the billing-address country; `shopperLocale`, if sent, must match country and currency. Name and billing address are recommended for conversion, while delivery address defaults to billing address if omitted. Some products/business models can require Base64-encoded `additionalData.openinvoicedata.merchantData`; the guide says not to include it in TEST because test values cause an error.
- No Klarna-specific Drop-in configuration is required. To choose the optional widget rather than redirect, the example sets `useKlarnaWidget: true` in `paymentMethodsConfiguration` for `klarna`, `klarna_account` and `klarna_paynow`; the `type` examples distinguish Pay later, Pay over time and Pay now. This is a Web Drop-in setting, not a claim about other clients.
- Automatic capture can be configured when capture delay is **immediate** and the merchant complies with Klarna's shipping-within-24-hours rule. Otherwise the guide requires manual capture within **90 days** of authorization, even when automatic capture is enabled on the merchant account; after that, authorization expires. The manual `/payments/{paymentPspReference}/captures` request uses original-payment PSP reference, amount and invoice `lineItems`. Its `status: received` response has a new capture PSP reference; final success/failure comes from the later `CAPTURE` webhook. A failure reason must be reviewed and corrected before resubmission. The partial-capture section separately describes a `/capture` call with `modificationAmount` below the authorized amount and correct `openinvoicedata`; do not silently treat the two endpoint presentations as identical.
- Recurring requires an initial token request (`storePaymentMethod: true` and `shopperReference`), a `recurring.token.created` webhook **after settlement**, and a future `/payments` request using the token, `shopperInteraction: ContAuth`, `recurringProcessingModel` and Klarna payment-request data. The Pay now/CardOnFile example is one case, not universal recurring eligibility; the related Klarna overview tells merchants to contact Adyen Support before offering recurring payments, and limits Pay over time to long-term subscriptions, excluding monthly subscriptions and one-off/on-demand tokenized purchases; its product/country conditions also apply.
- Before live use the page calls for TEST validation, live-account method addition, legal/brand presentation and correct invoice/VAT display. Its live-testing conditions use real shopper data, a reasonable qualifying amount and limited test frequency; failures can return `Refused` with an "Option Not Available" widget page. These velocity and shopper checks are described as LIVE-only, so a TEST result does not establish live acceptance.

## Detail locators

- Flow prerequisites, Web v6 import, Sessions-vs-Advanced API tabs: raw lines 19–59 and 771–789.
- Endpoint-specific field tables, notes and versioned request examples: `### Tab: /sessions`, lines 57–770; `### Tab: /payments`, lines 771–1511. Note that sample `shopperLocale: en_US` appears with `countryCode: SE` and SEK although the prose requires locale to match country/currency (lines 69, 89–90 and parallel `/payments` tab); do not copy that combination as validated.
- Optional widget setting and method codes: `## Drop-in configuration`, lines 1512–1548.
- Conditional automatic capture, 90-day manual capture, invoice lines, distinct response/webhook states, optional shipping and partial capture: `## Capture the payment`, lines 1550–2125. The guide presents Checkout `/payments/{paymentPspReference}/captures` for manual capture, then legacy `/capture` in the optional shipping and partial-capture examples (lines 2076–2125); select the intended API/version and verify fields in its own reference.
- Token creation after settlement, future token payment and example models: `## Recurring payments`, lines 2133–2245.
- Test, live checklist, live-only refusal conditions: `## Test and go live`, lines 2247–2274.

## Related

- [[adyen-online-payments]] — provider online-payment context.
- [[source-adyen-docs-payment-methods-klarna]] — product/country matrix and recurring qualifications.
- [[source-adyen-docs-online-payments-capture]] — general capture lifecycle.

## Raw Sources

- [[raw/adyen/docs/payment-methods/klarna/web-drop-in/2026-09-15|2026-09-15 Klarna Web Drop-in guide, full API examples and lifecycle]]
