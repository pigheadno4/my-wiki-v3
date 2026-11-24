---
title: "Stripe: PayPal Button"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-paypal-button-2025.md"
tags: [stripe, wallets, paypal, paypal-button, express-checkout-element, checkout, billing-address, recurring]
---

## Summary

Guide for maximizing PayPal button availability in Express Checkout Element and Stripe Checkout. Stripe decides button vs redirect — merchants configure options to increase button chance. Key: avoid billing/shipping/phone collection; PayPal must not be the only payment method in Checkout.

## Key Details

**Express Checkout Element blockers** (button not shown):
- Billing address collection enabled
- Shipping address collection enabled (recurring only)
- Phone number collection enabled
- For recurring: must explicitly set `billingAddressRequired: false`

**Checkout blockers** (falls back to redirect):
- Billing address collection enabled
- Consent collection enabled
- Custom fields used
- PayPal is the **only** payment method type
- Phone number collection enabled
- Shipping address collection for recurring
- Tax ID collection enabled

**Maximize button in Checkout**: use `billing_address_collection: 'auto'`, `automatic_tax: { enabled: false }`, include multiple payment methods (not PayPal-only).

**Testing**: recommend creating PayPal Sandbox account.

## Raw Sources

- [[stripe-paypal-button-2025]] — verbatim webpage content (90 lines); no italic fixes needed
