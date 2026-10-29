---
title: "Adyen Scalapay Web Drop-in integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/scalapay/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/scalapay/web-drop-in/2026-09-15.md"
tags: [adyen, scalapay, web-drop-in, online-payments]
---

## Overview

This [[adyen]] guide describes adding Scalapay to an existing **Web Drop-in** integration, with separate Sessions and Advanced server-side flow prerequisites. The captured method scope is IT, FR, PT or ES, and its Advanced examples use `scalapay_3x` with EUR. It is an add-on to the base Drop-in integration, not a standalone redirect or capture guide. The related [[source-adyen-docs-payment-methods-scalapay]] overview identifies the BNPL redirect method and its snapshot feature matrix. Use [[adyen-online-payments]] for the general checkout architecture.

## Key takeaways

- **Flow and account gates:** The Sessions tab requires an existing Sessions Web Drop-in integration; the Advanced tab requires an existing Advanced Web Drop-in integration. Both say to add Scalapay in Customer Area (raw lines 21–37). The page says activation defaults to standard pricing and asks merchants to contact their account manager before activation to check eligibility for Enterprise pricing (raw line 39). These instructions do not establish current merchant enablement.
- **Request fields by endpoint:** The guide calls `/sessions` the default with Drop-in v5.0.0 or later, while showing `/payments` for an additional use case (raw lines 41–59). Both tables mark `countryCode` (IT, FR, PT or ES) and `shopperName` (`firstName`, `lastName`) as required; billing address, delivery address and `lineItems` have no Required mark in those tables (raw lines 49–69). The `/payments` table additionally lists optional flight or lodging dates and says to provide either `additionalData.airline.flight_date` or `additionalData.lodging.checkInDate` in one transaction (raw lines 68–69). The Advanced example uses `countryCode: IT`, `paymentMethod.type: scalapay_3x` and EUR (raw lines 71–96).
- **Example limits:** The multilingual Advanced `/payments` snippets are TEST-oriented and use different library versions (raw lines 73–428). The C# and Go examples render `countryCode` in lower case as a member name (raw lines 225–234, 306–314), while the prose table marks the request field required. Treat those snippets as examples needing version-specific validation, not proof that they compile or authorize a payment.
- **Drop-in and live boundary:** No Scalapay-specific Drop-in configuration is specified (raw lines 430–432). The guide points to Scalapay test cards, test Customer Area payment status, and a separate live Customer Area request before accepting live payments (raw lines 434–440). It gives no method-specific capture, refund or final-outcome procedure; follow the base flow and applicable Scalapay method guide. Its generic tokenization See also link (raw line 446) does not override the overview table's unsupported recurring mark.

## Detail locators

- Sessions and Advanced prerequisites plus pricing note: pinned raw lines 15–39.
- `/sessions` and `/payments` request field tables: pinned raw lines 41–69.
- Advanced TEST examples, type/currency and versioned snippets: pinned raw lines 71–428.
- Drop-in configuration and test/live instructions: pinned raw lines 430–447.

## Related

- [[adyen-online-payments]] — Web Drop-in and server-side flow context.
- [[source-adyen-docs-payment-methods-scalapay]] — BNPL redirect identity, country/currency scope and feature marks.

## Raw Sources

- [[raw/adyen/docs/payment-methods/scalapay/web-drop-in/2026-09-15|Scalapay Web Drop-in guide, captured 2026-09-15]]
