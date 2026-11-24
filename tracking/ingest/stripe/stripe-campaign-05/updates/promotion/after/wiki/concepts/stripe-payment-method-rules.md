---
title: "Stripe Payment Method Rules"
type: concept
category: technology
tags: [stripe, payment-method-rules, dynamic-payment-methods, checkout, payment-element, klarna, bnpl, conversion]
---

## Definition

Payment method rules let merchants control when specific payment methods appear — based on order amount or buyer country/currency — directly from the Dashboard with no code. Part of the [[stripe-dynamic-payment-methods]] customization suite.

**Requires**: dynamic payment methods + Payment Element, Express Checkout Element, Checkout, or Payment Links.

## What Rules Can Do

- **Amount-based**: hide/show a PM if order total is above or below a threshold (e.g., require ≥ $100 for Klarna)
- **Location-based**: hide/show a PM for buyers in specific countries or using specific currencies

The November 7, 2026 guide limits rules to supported non-card methods and excludes wallets such as Apple Pay and Google Pay. Rules do not apply on the Hosted Invoice Page or when the listed integrations create a subscription. The May guide also documented the subscription exception.

## Setup

In Dashboard payment method settings, choose **Customize availability** for a supported method and select **Apply Overrides**. The May 8, 2026 guide displayed a **Customized** tag. The November capture leaves the tag unverified.

For direct charges, the November rules guide gives connected accounts the platform template conditions without account override. Destination-charge conditions come from the platform's direct settings. The separate Connect guide uses connected-account enablement/configuration for all direct charges and for indirect charges with `on_behalf_of`, and platform enablement/configuration for indirect charges without it. The interaction on destination charges with `on_behalf_of` remains unresolved.

Limits are configured in one currency; Stripe auto-converts at current exchange rate for other-currency transactions.

## Compatibility

- Works with [[stripe-ab-testing-payment-methods]] — rules can serve as A/B experiment targeting criteria
- Works with payment method configurations (different PM sets per scenario)

## Testing Location-Based Rules

**Checkout**: pass `customer_email: 'test+location_FR@example.com'` (ISO country code suffix) when creating a Checkout Session.

**Payment Links**: pass `prefilled_email` or `locked_prefilled_email` URL parameter with the location-formatted email.

## Sources

- [[source-stripe-payment-method-rules]] — May and November rules for method visibility, supported surfaces, direct and destination charges, and test location simulation
