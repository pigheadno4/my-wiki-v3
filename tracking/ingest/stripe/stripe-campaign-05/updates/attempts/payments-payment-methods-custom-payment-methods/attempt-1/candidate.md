---
title: "Stripe Docs — Custom payment methods"
type: source
date_ingested: 2026-05-08
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/payment-methods/custom-payment-methods"
raw_files:
  - "stripe-payments-payment-methods-custom-payment-methods-2026-11-07.md"
  - "stripe-custom-payment-methods-2025.md"
tags: [stripe, custom-payment-methods, cpmt, third-party, payment-element, connect, compliance]
---

## Overview

Custom payment methods surface payment options handled by a third-party payment service provider (PSP). The merchant or PSP processes the payment, completes the purchase and reconciles orders. Stripe can receive optional Payment Records for unified reporting. Stripe Billing separately manages subscription states and tracks external payment success while the payment method and charges remain with the external processing flow. Stripe's role in recording or tracking leaves charges, refunds, disputes, settlement and funds flows with the external processor and merchant. See November lines 7–11, 73–75 and 116–129 and May lines 6–10, 78–80 and 131–144.

## Custom types and PaymentMethod instances

Create the custom payment method type in the Dashboard and store its `cpmt_` ID for later use. The type itself is unavailable through the API. The November guide directs Payment Element users to a preset and custom front ends or Payment Methods API users to a custom display name and logo. The May 8, 2026 guide described more than 50 presets. The November 7, 2026 guide retains presets without specifying the catalog count.

Create and retrieve custom PaymentMethod instances through the Payment Methods API. At creation pass `type: 'custom'` and the Dashboard type ID in `custom[type]`. The new guide illustrates an HTTP request and the earlier guide shows a Node SDK call with the same type distinction. See November lines 13–55 and May lines 12–66.

## Product support by capture

| Integration | May 8, 2026 | November 7, 2026 |
| --- | --- | --- |
| Checkout | Unsupported | Supported at product level |
| Express Checkout Element | Unsupported | Private preview |
| Payment Links | Unsupported | Unsupported |
| Connect, Payment Element, Mobile Payment Element, Subscriptions, Invoicing and Customer Portal | Supported | Supported |

The November overview says Express Checkout Element can show custom payment method buttons alongside wallets including Apple Pay and Google Pay. It links to the separate implementation section. The product row does not specify which Checkout UIs surface custom methods, and the Express Checkout footnote applies to that Element. See November lines 57–75, May lines 68–80, and [[stripe-express-checkout-element#Custom Payment Methods in v9.14|Express Checkout preview and typed integration]].

## Connect

A platform can create a custom PaymentMethod in a connected account using either the platform's custom type or the connected account's type. The May Node example supplies the connected account ID in the SDK request option `stripeAccount`. November's cURL example sets the HTTP `Stripe-Account` header. Both scope the request to the connected account. See May lines 82–102 and November lines 77–87.

## Merchant and provider responsibilities

The PSP operates and supports the service. The merchant maintains their own direct PSP integration and active agreement, configures the custom method and redirect if applicable, obtains branding and data rights, and presents the correct PSP to the customer. The guides prohibit the specified crypto methods and other crypto-related methods in Indonesia and Thailand and require adherence to provider Marks guidance, including permission before changing Marks and accurate identification of the underlying method.

If the PSP agreement ends or Stripe notifies the merchant of a prohibition or documents the prohibition, immediately remove the custom payment method and disable the PSP integration. The guides separately describe Stripe's ability to remove or block a method. If Stripe gives notice of removal, the merchant must immediately remove the method from their code. If they leave it in place, it no longer renders to customers. See May lines 104–149 and November lines 89–134.

## Related Pages

- [[stripe-custom-payment-methods]] — Custom payment methods concept and implementation routes
- [[source-stripe-payment-element-custom-payment-methods]] — Payment Element implementation
- [[stripe-express-checkout-element]] — Express Checkout capabilities and dated preview
- [[source-stripe-subscriptions-third-party]] — Billing with third-party payment processors
- [[stripe]] — Stripe company page

## Raw Sources

- [[raw/stripe-payments-payment-methods-custom-payment-methods-2026-11-07|November 7, 2026 custom payment methods overview]] — Full guide with dated Checkout and Express Checkout coverage
- [[raw/stripe-custom-payment-methods-2025|May 8, 2026 custom payment methods overview]] — Earlier full guide
