---
title: "Braintree Apple Pay"
type: source
date_ingested: 2026-09-29
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/payment-methods/apple-pay"
raw_files:
  - "braintree/articles/guides/payment-methods/apple-pay-2026-09-16.md"
tags: [braintree, apple-pay, digital-wallets, mobile-payments, web-payments, vaulting]
---

## Overview

This collected Braintree guide describes Apple Pay for mobile and web purchases, including its device-specific tokenization model, merchant and customer availability boundaries, processing behavior, vaulting limits, and integration setup. It is a retrieval route to the exact collected requirements rather than proof that a particular merchant, buyer, device, browser, card, or transaction is currently eligible.

## Key takeaways

- Apple Pay uses a card associated with a supported Apple mobile device. The guide says Braintree can accept it on newer iOS and Safari versions and describes Apple replacing the card number with an encrypted, device-specific DPAN that Braintree and processing banks use for transactions.
- Merchant availability depends on business location and processing settings. The page separately says eligible merchants can accept customers from Apple Pay-supported countries and regions, but warns that the merchant must be domiciled where Braintree onboarding and Apple Pay compatibility both apply. Card-brand and American Express-account qualifications remain at the raw locator.
- For desktop web purchases, the page requires an authorizing Apple device, macOS Sierra 10.12 or later, and Safari, while saying the latest Apple Pay SDK also enables non-Safari browsers. In-app, mobile-web, iframe, and exact device requirements remain at the raw locators below.
- The guide says Apple Pay transactions process and settle like credit-card transactions. Its exact pricing, dispute, network- and iOS-qualified liability-shift, Basic versus Premium fraud-tool, and billing-postal-code statements remain discoverable at the processing locators rather than being generalized here.
- Apple Pay cards can be vaulted for recurring billing and split shipments only with customer consent during checkout for future merchant-initiated transactions. The page warns against reusing a vaulted Apple Pay card when the customer is present and able to authorize the future payment, saying that use results in declines.
- Setup requires work with Braintree and Apple on Apple Pay certificates and Merchant IDs, followed by an iOS and/or JavaScript v3 client integration plus a server integration. For Braintree's iOS client SDK, the guide says the Apple Pay certificate expires after 25 months and must remain current to avoid processing disruption.

> [!warning] Collected availability and compatibility are conditional
> The page's current-tense support statements are a 2026-09-16 collection snapshot. Confirm current merchant onboarding, processing settings, Apple platform and browser requirements, card eligibility, liability behavior, fraud-tool compatibility, and certificate state before relying on them.

## Detail locators

- Payment-method purpose, mobile/web scope and DPAN tokenization: `# Apple Pay`, lines 16-18.
- Merchant regions, processor-setting qualification, card brands and own-American-Express-account condition: `## Availability`, lines 23-35.
- In-app and mobile-web device requirements: `## Availability > ### Customer availability > #### Device requirements`, lines 41-55.
- Desktop authorization-device, macOS, Safari and latest-Apple-Pay-SDK browser scope: `## Availability > ### Customer availability > #### Device requirements`, lines 57-62.
- iframe requirements: `## Availability > ### Customer availability > #### iframe support`, lines 65-71.
- Customer-country scope versus merchant domicile and onboarding qualification: `## Availability > ### Customer availability > #### Location requirements`, lines 74-80.
- Credit-card-like processing, pricing and dispute handling: `## Processing`, lines 85-97.
- Network- and iOS-qualified liability-shift statements: `## Processing > ### Liability Shift`, lines 100-106.
- Basic/Premium fraud-tool compatibility and billing-postal-code recommendation: `## Processing > ### Fraud tools`, lines 109-115.
- Vaulting, recurring billing, split shipments and consent/present-customer boundary: `## Processing > ### Recurring billing and vaulting`, lines 118-122.
- Certificate, Merchant ID, client/server integration and 25-month iOS certificate-renewal boundary: `## Setup`, lines 125-132.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-apple-pay]]
- Related concepts: [[braintree-payment-methods]], [[recurring-payments]], [[disputes]]

## Related raw API references

- [[raw/braintree/docs/guides/apple-pay/overview-2026-09-16|Braintree Apple Pay developer overview]] - unread navigation-only implementation route linked by this guide
- [[raw/braintree/docs/guides/apple-pay/configuration/javascript/v3-2026-09-16|Braintree Apple Pay JavaScript v3 configuration]] - unread navigation-only web-configuration route
- [[raw/braintree/docs/guides/apple-pay/configuration/ios/v7-2026-09-16|Braintree Apple Pay iOS v7 configuration]] - unread navigation-only iOS-configuration and certificate-renewal route

## Raw Sources

- [[raw/braintree/articles/guides/payment-methods/apple-pay-2026-09-16|Braintree Apple Pay payment-method guide]] - complete collected article covering identity, availability, platform requirements, processing boundaries, vaulting and setup
