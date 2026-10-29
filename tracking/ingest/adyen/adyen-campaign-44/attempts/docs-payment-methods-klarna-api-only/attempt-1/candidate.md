---
title: "Adyen Klarna API-only integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/klarna/api-only"
raw_files:
  - "adyen/docs/payment-methods/klarna/api-only/2026-09-15.md"
tags: [adyen, klarna, api-only, online-payments, capture, tokenization]
---

## Overview

This [[adyen]] guide adds Klarna to an existing Web API-only checkout. The merchant builds the payment form and sends server-side Checkout API requests; the shopper either uses an embedded Klarna widget or redirects to Klarna. The guide covers Pay Now, Pay Later and Pay Over Time, plus capture and recurring-token paths. It is a 2026-09-15 capture of a page marked last modified 2024-01-02. Use [[adyen-online-payments]] for broader architecture and [[adyen-tokenization]] for stored-payment context.

## Key takeaways

- **Two payment paths and prerequisites:** The guide requires an existing API-only integration, Klarna added in test Customer Area and webhooks for payment outcome (raw lines 23–42). In the server-side `/payments` request, `paymentMethod.type` selects `klarna_paynow`, `klarna` or `klarna_account`; `paymentMethod.subtype: sdk` chooses the widget, while omitting the subtype chooses redirect (raw lines 130–155). The widget returns a client token/category and later an authorization token; redirect uses the returned `action.url` and a return `redirectResult` (raw lines 899–1014).
- **Request and approval conditions:** The country/currency/product matrix for `/paymentMethods` is method-specific (raw lines 56–81). For payment, `countryCode`, currency and billing-address country must agree, and alternative locale must match that combination (raw lines 91–128). The guide's request table marks `lineItems`, `shopperEmail` and `countryCode`; line-item total must match `amount.value`, and each item needs a description. Name and billing address are recommended in the request; Klarna asks the shopper for them when absent. `shopperEmail` also has a dispute-defense note, despite the separate form table's blank Required column (raw lines 44–54, 157–170). Refer to the raw table for other fields and market combinations.
- **Outcome and dated change:** The page states that from **2024-01-31**, `/payments/details` is no longer required for Klarna transactions, though it can still check final status; webhooks are needed to update order management for all final outcomes (raw lines 19, 955, 1030). The widget and redirect instructions still describe `/payments/details` as a step (raw lines 938–953, 985–1018), so follow the dated qualification rather than treating those examples as an unconditional requirement. Its presented results include Authorised, Cancelled and Refused; Klarna may refuse on risk checks (raw lines 1016–1028). Neither a shopper return nor `Pending` alone proves final authorization.
- **Capture boundary:** Capture follows shipment. Automatic capture in live Customer Area is described only when capture delay is immediate **and** Klarna's shipping-within-24-hours Scheme Rule is met. Otherwise manual capture is required within **90 days** after authorization, even if merchant-account automatic capture is enabled; absent capture, authorization expires (raw lines 29–33, 1032–1034). The Checkout `/payments/{paymentPspReference}/captures` response has `status: received` and a separate capture PSP reference; wait for the `CAPTURE` webhook to determine success or failure (raw lines 1036–1052, 1494–1525). Partial capture needs a lower amount and correct invoice-line amounts (raw lines 1600–1607). The page also includes a separate legacy `/capture`/`openinvoicedata` shipping example (raw lines 1529–1607); do not merge its fields into the Checkout captures request without checking the endpoint.
- **Recurring qualification:** The guide describes `storePaymentMethod: true` plus `shopperReference`, and a `recurring.token.created` webhook only after the initial payment settles; later requests use `storedPaymentMethodId`, shopper reference, `ContAuth` and a recurring processing model (raw lines 1609–1654). The related Klarna overview's recurring footnote says to contact Support, limits Pay Over Time to long-term subscriptions, and excludes monthly subscriptions and one-off on-demand tokenized purchases (Klarna overview raw lines 31–39). This guide's generic model table does not override those product conditions.
- **Test/live boundary:** The guide asks for test-environment validation, separate addition of Klarna in live Customer Area and review of legal/privacy, presentation, invoice/VAT and rejection fallback (raw lines 1723–1738). It says live shopper-data, minimum-amount and velocity checks can yield Refused and are bypassed in test (raw lines 1740–1748). The captured examples use TEST endpoints and versioned library snippets; they do not establish live merchant enablement or payment success.

## Detail locators

- `/paymentMethods` country/currency/product matrix and type codes: pinned raw lines 56–87.
- Country/currency/locale payment matrix: pinned raw lines 91–128.
- Server `/payments` fields and example clients: pinned raw lines 130–892. Example SDK versions vary by language.
- Widget, redirect, return and result handling: pinned raw lines 899–1030.
- Capture request, response, webhook, optional shipping and partial capture: pinned raw lines 1032–1607.
- Token creation and token payment fields: pinned raw lines 1609–1721.
- Test and live checklist: pinned raw lines 1723–1750.

## Related

- [[adyen-online-payments]] — API-only checkout and webhook context.
- [[adyen-tokenization]] — provider tokenization context.
- [[source-adyen-docs-payment-methods]] — broader catalog; product-specific conditions belong to the Klarna pages.

## Raw Sources

- [[raw/adyen/docs/payment-methods/klarna/api-only/2026-09-15|Klarna API-only guide, captured 2026-09-15]]
