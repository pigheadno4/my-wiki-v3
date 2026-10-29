---
title: "Scalapay iOS Drop-in integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/scalapay/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/scalapay/ios-drop-in/2026-09-15.md"
tags: [adyen, scalapay, ios, drop-in, sessions, redirect]
---

## Overview

This [[adyen|Adyen]] guide, fetched and last-modified on 2026-09-15, adds Scalapay to an existing iOS Drop-in integration using Sessions or Advanced server flow. It gives request-field additions, pricing and live setup notes, and says no Scalapay-specific Drop-in configuration is required. See [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-scalapay|Scalapay overview]] for the captured EUR redirect and feature matrix. This guide does not itself describe capture, refund, redirect-return outcome or recurring mechanics, and does not prove current merchant eligibility or successful payment execution.

## Key takeaways

- Both flow tabs assume an existing iOS Drop-in integration and Scalapay added in Customer Area. The page says activation defaults to standard pricing and instructs merchants to ask their account manager before activation about Enterprise-pricing eligibility if volume may qualify. This is a pricing check, not a guarantee of method enablement.
- `/sessions` is called the default with Drop-in v5.0.0 or later. Its table marks `countryCode` and shopper first/last name required; it lists IT, FR, PT and ES as country codes. Billing address, delivery address and `lineItems` have no required mark. The `/payments` table for an additional use case has the same core field markings and adds optional airline outbound-flight date or lodging check-in date; its prose says to provide either field in the same transaction. See the raw table for the two formats.
- The Advanced `/payments` example is a TEST Checkout API v72 request for `paymentMethod.type: scalapay_3x` with IT/EUR, shopper name and the iOS app-scheme `returnUrl` placeholder `my-app://` (raw line 94). The guide does not show a completed redirect-return outcome or establish that this placeholder is a working merchant app URL. Language snippets name their own library versions. This is one product and country example, not a promise of all Scalapay offers or authorization.
- The Drop-in section says no Scalapay-specific integration is required. Test instructions point to Scalapay test scenarios and Customer Area test status; the live section says to request Scalapay in live Customer Area. These are setup instructions, not proof of live eligibility. The See also tokenization link is general navigation; the [[source-adyen-docs-payment-methods-scalapay|overview]] marks recurring unsupported, so this guide does not establish recurring Scalapay payments.

## Detail locators

- Existing Sessions/Advanced iOS Drop-in prerequisites and pricing qualification: pinned raw lines 15–39.
- `/sessions` fields and Drop-in v5 default: lines 41–55. `/payments` fields, optional airline/lodging data and IT `scalapay_3x` example with the app-scheme `returnUrl` placeholder: lines 57–96 (return URL at line 94); language examples: 98–428.
- No required method-specific Drop-in configuration: lines 430–432. Test/live instructions and general See also routes: lines 434–447.

## Related

- [[adyen-online-payments]] — main provider integration concept
- [[source-adyen-docs-payment-methods-scalapay]] — captured method/country/currency and feature matrix

## Raw Sources

- [[raw/adyen/docs/payment-methods/scalapay/ios-drop-in/2026-09-15|Scalapay iOS Drop-in guide, fetched 2026-09-15]]
