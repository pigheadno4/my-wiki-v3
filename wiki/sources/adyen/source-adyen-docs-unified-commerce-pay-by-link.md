---
title: "Adyen Pay by Link overview"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/unified-commerce/pay-by-link"
raw_files:
  - "adyen/docs/unified-commerce/pay-by-link/2026-09-15.md"
tags: [adyen, pay-by-link, payment-links, hosted-payments, unified-commerce]
---

## Overview

Adyen's Pay by Link overview describes accepting payments by sending shoppers a payment link to an Adyen-hosted payment page. It gives invoice, showroom-follow-up, and chat/email/social interaction examples. This is a merchant payment-acceptance route, not an order-management or in-person Terminal API flow. See [[adyen]] and [[adyen-unified-commerce]].

## Key takeaways

- For an online shop, Adyen says Pay by Link should supplement an online-payments integration, not be the shop's sole way to accept payments.
- The link takes the shopper to a secure Adyen payment page with a preferred payment method; the page works across devices and can show the merchant's brand name and logo. The overview does not establish which methods are enabled for a particular merchant or prove a completed payment.
- Adyen says payment links are removed automatically three months after creation. This is removal of links; the page does not specify payment authorization, capture, refund, or settlement behavior.
- Before creating the first **live** payment link, the merchant must add a terms-and-conditions URL to the Adyen-hosted page. Adding it in the live Customer Area requires either the Merchant admin or Pay by Link Settings user role. The general terms cover product/service and payment details, third parties, the processing legal entity, and governing law. The privacy policy describes stored and third-party-shared data and cookies. Delivery information states how long the shopper waits for the product or service; delivery countries/regions apply if relevant. The refund/cancellation policy covers eligibility and return/cancellation process. The merchant's website or app contact information must show its legal entity name, email address, and phone number.
- The page points platform users to a prebuilt Pay by Link UI component as an alternative to an API-only integration and mentions an iOS app for managing links. Those are navigation paths, not evidence of API request shape or platform eligibility.

## Detail locators

- Lines 23–35: purpose, use cases, supplemental online-shop warning, hosted page and three-month link removal.
- Lines 42–58: live terms-and-conditions prerequisite, user roles and Customer Area settings path.
- Lines 60–103: required terms, privacy, delivery, refund/cancellation and contact information.
- Lines 105–117: settings, creation and release-note navigation.

## Related

- [[adyen-unified-commerce]] — provider concept and reciprocal source route.
- [[adyen-online-payments]] — primary online-payments integration context for an online shop.

## Raw Sources

- [[raw/adyen/docs/unified-commerce/pay-by-link/2026-09-15|Pay by Link, captured 2026-09-15]]
