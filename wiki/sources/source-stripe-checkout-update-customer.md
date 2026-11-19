---
title: "Update the Customer During Checkout"
type: source
date_ingested: 2026-04-21
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/checkout/update-customer"
raw_files:
  - "stripe-payments-checkout-update-customer-2026-11-07.md"
  - "stripe-checkout-update-customer-2025.md"
tags: [stripe, checkout-sessions, customer, guest-checkout, authentication, saved-payment-methods, preview]
---

## Overview

The April 21 and November 7, 2026 captures describe attaching a **Customer** to an **existing Checkout Session after Session creation** for a mid-checkout guest-to-login experience. The Customer's saved payment methods, email and billing information can then populate without losing information the buyer already entered (new raw lines 5-9; old raw lines 4-8). The identity boundary is the Customer being attached to an already-created Checkout Session. The page does not prescribe an initial `customer` value or a universal guest Session configuration.

## Preview access qualification

The November capture adds an **“Interested in updating the customer during checkout?”** section. It explicitly calls this a **preview feature** and asks for an email to request access; a Stripe team member will contact the requester (new raw lines 11-13). Its example `POST https://docs.stripe.com/preview/register` uses a Referer for this page and `{"email":"EMAIL","preview":"custom_checkout_preview"}` (new raw lines 15-20). That request is for preview access, not an example of updating a Checkout Session, proof of approval, or evidence that a merchant account has the feature enabled.

The older full page ended with the behavioral description and did not show this request-access section (old raw lines 4-8). The new wording of the guest-login example is editorial; the access qualification is the consequential addition. Treat the behavior and preview status as capture-dated documentation, not a verified current account entitlement or completed checkout.

## Integration boundary

Neither pinned capture gives a `checkout.sessions.update(...)` call, a `customer` parameter schema, an API version, SDK requirement, client/server division, or supported Checkout UI mode. The older summary named `checkout.sessions.update(sessionId, { customer: ... })` and asserted a guest Session begins without a Customer, but those details are not established by these two pages. A developer needs separately read API or implementation authority before treating that syntax or initial Session setup as supported. Attaching a Customer and populating fields does not itself confirm a payment, save a new method, or establish settlement.

## Related

- [[stripe]] — company context.
- [[stripe-checkout]] — Checkout concept and reciprocal preview route.

## Raw Sources

- [[raw/stripe-payments-checkout-update-customer-2026-11-07|November 7, 2026 Customer update preview page]] — full 21-line capture with access-request example.
- [[raw/stripe-checkout-update-customer-2025|April 21, 2026 Customer update page]] — earlier full eight-line behavior description.
