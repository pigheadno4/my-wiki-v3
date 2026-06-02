---
title: "PayPal Expanded Checkout: Customize Buyers' Experience"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-expanded-checkout-customize-overview.md"
tags: [paypal, expanded-checkout, customization, reference, 3d-secure, fraud-protection, card-fields, sca, level2-level3, chargeback]
---

## PayPal Expanded Checkout: Customize Buyers' Experience

Feature catalog for extending an Advanced Credit and Debit Card (Expanded Checkout) integration — 14 customization features.

Source URL: <https://developer.paypal.com/docs/checkout/advanced/customize/>

Last updated: 2025-12-10

## Feature Catalog

| Feature | What you get |
| ------- | ------------ |
| 3D Secure | Customer authentication via card issuer |
| Acquirer reference number | Transaction tracking identifier |
| Card fields style guide | Layout, width, height, outer styling of card fields |
| Card field properties | Capture field properties, customize event callbacks and style |
| Card field events | Subscribe to card events for UI updates |
| Fraud protection | Risk management toolkit for ACDC payments |
| Chargeback protection | Fraud analysis to approve/decline transactions |
| Real-time account updater | Reduce declined payments via real-time card updates |
| SCA payment indicators | Strong Customer Authentication payment processing |
| Level 2/Level 3 processing | Additional payment data for reduced processing costs |
| Third-party network token processing | Process payments with 3rd-party tokens (no raw card data) |
| Update order details | Adjust order/transaction details during checkout |
| Handle errors | Manage payer checkout experience on payment errors |
| Initiate future transactions | Website Payments Pro: future transactions via transaction ID |

## Grouping by theme

**Security & authentication:** 3D Secure, SCA payment indicators, Fraud protection, Chargeback protection

**Card field UX:** Card fields style guide, Card field properties, Card field events

**Payment optimization:** Level 2/Level 3 processing, Real-time account updater, Third-party network token processing, Acquirer reference number

**Order management:** Update order details, Handle errors, Initiate future transactions

## Expanded vs Standard Checkout customizations

Expanded Checkout adds features not available in Standard Checkout:
- Acquirer reference number
- Card fields style guide, properties, events (card-specific)
- Chargeback protection
- Real-time account updater
- SCA payment indicators
- Level 2/Level 3 processing
- Third-party network token processing
- Initiate future transactions

Standard Checkout equivalents are documented in [[source-paypal-checkout-customize-overview]].

## Raw Sources

- [[paypal-expanded-checkout-customize-overview]] — verbatim webpage content

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-expanded-checkout]] — Expanded Checkout concept page
- [[source-paypal-checkout-customize-overview]] — Standard Checkout customization catalog (compare)
- [[source-paypal-expanded-checkout-integrate]] — Base Expanded Checkout integration
