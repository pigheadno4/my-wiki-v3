---
title: "Accept a Payment with the Express Checkout Element"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/elements/express-checkout-element/accept-a-payment"
raw_files:
  - "stripe-express-checkout-element-accept-payment-2025.md"
tags: [stripe, elements, express-checkout, apple-pay, google-pay, paypal, link, klarna, amazon-pay, checkout-sessions, payment-intents, integration-guide, connect]
---

## Summary

The 2026-04-21 capture is a combined Express Checkout Element integration guide for Checkout Sessions API and Payment Intents API. The 2026-11-07 capture of this base URL is an index pointing to those two variants, without their detailed contents. The apparent deletion of detailed instructions in the diff is a navigation split, not evidence that wallet methods, options, test values, or API behavior were deprecated or remain currently available. All technical instructions below are historical claims from the April guide; current variant behavior needs separately captured variant bodies.

## Method configuration and availability in the 2026-04-21 guide

Both paths default to the Stripe Dashboard payment-method settings. Explicit method lists are **optional overrides**, not universally required. For Checkout Sessions, set `payment_method_types` on the Session if overriding. For Payment Intents, use `paymentMethodTypes` on deferred Elements options or `payment_method_types` on an Intent created before Elements. The historical guide's method tables differ:

| Method | Checkout Sessions API | Payment Intents API | Types when explicitly configured |
| --- | --- | --- | --- |
| Apple Pay | Listed | Listed | `card` |
| Google Pay | Listed | Listed | `card` |
| Link | Listed | Listed | `link` and `card` |
| PayPal | Listed | Listed | `paypal` |
| Amazon Pay | Listed | Listed | `amazon_pay` |
| Klarna | Not listed in that variant's table | Listed | `klarna` |

A method's appearance still depends on account and payment-method settings, country, domain registration, device, browser, and a suitable customer wallet. The guide says the `ready` event's `availablePaymentMethods` indicates which buttons actually display. This table is not a claim of current eligibility or that both paths support the same six methods.

## Checkout Sessions API path (historical)

The server creates a Checkout Session with line items, `mode: 'payment'`, `ui_mode: 'elements'`, and a return URL. Its **Session client secret** goes to the client for `stripe.initCheckoutElementsSdk({ clientSecret })`; the client creates and mounts the Express Checkout Element. In the HTML/JS flow, `checkout.loadActions()` must return success before its `actions.confirm({ expressCheckoutConfirmEvent: event })` is called from the Element's `confirm` event. The React variant uses `CheckoutElementsProvider`, `useCheckout()`, and `ExpressCheckoutElement` from `@stripe/react-stripe-js/checkout`. Optional Session settings in the older guide include phone collection, shipping collection and options, and automatic tax; these are options, not universal prerequisites.

## Payment Intents API path (historical)

The older guide recommends **collecting payment details before creating an Intent within this path**. That is an ordering preference, not a ranking of Checkout Sessions over Payment Intents. Initialize deferred Elements with `mode`, `amount`, and `currency`, then mount the Express Checkout Element. The server must decide the actual charge amount, create the PaymentIntent with matching amount and currency, and return **that PaymentIntent's** client secret. A concise order for the guide's deferred flow is:

1. In the Element's `confirm` handler, call `elements.submit()` and stop on its error.
2. Call the server's Intent-creation endpoint; the server determines the amount and returns `client_secret` for its PaymentIntent.
3. Call `stripe.confirmPayment({ elements, clientSecret, confirmParams: { return_url } })` with that returned secret, then handle immediate errors and later payment status appropriately.

The historical guide also shows a distinct ConfirmationToken route for server validation: submit Elements, create the token, create an Intent server-side, then use its client secret and the token to confirm. It is a separate option, not a missing step in the ordinary deferred-Intent route. The guide says the PaymentIntent amount must match the amount presented through Elements; for Amazon Pay, Klarna, and PayPal, confirmation must match the buyer's pre-authorized amount. A `confirmPayment` call or browser animation alone does not prove final settlement.

### Elements options

In the older Payment Intents variant, `mode` and `currency` are required Elements options; `amount` is required for payment and subscription modes. Optional settings include `setupFutureUsage` (not supported for Klarna here), `captureMethod`, `onBehalfOf` for Connect, `paymentMethodTypes`, `paymentMethodCreation`, and `paymentMethodOptions`. Equivalent Elements options and Intent parameters must match or errors can result. The guide's options table and schema details are at historical raw lines 604–629.

## Customer details, wallet events, and tests

The historical Payment Intents variant can request payer email and phone, shipping address and rates, and line items. `billingAddressRequired` defaults to true unless one of the guide's specified shipping, payer, Apple Pay, line-item, or business options is supplied. PayPal normally omits billing address beyond country and phone; if required details are unavailable, the PayPal button is hidden. A browser may anonymize the shipping address before confirmation. If handling `shippingaddresschange` or `shippingratechange`, the handler must resolve or reject; a rate change can update the Elements amount. The `cancel` example resets the amount. The `ready` event can support a fallback UI when no wallet button is available. Apple Pay merchant-token options are documented for recurring, deferred, or auto-reload use cases, not automatically enabled by mounting the Element.

The April guide's sandbox tables include Link OTPs (any other six digits succeed; `000001`, `000002`, and `000003` are error cases), wallet testing and domain/browser prerequisites, Amazon Pay test-card outcomes, and Payment Intents-path Klarna country test data. These are **sandbox fixtures**, not live approvals or current country support. It says Google Pay and Apple Pay cannot be tested from an Indian IP address, even for a non-Indian Stripe account. The detailed fixtures remain in the historical raw, not in the November index.

## Connect, environment, and disclosure

The Checkout Sessions Connect example creates the Session on the connected account with a `Stripe-Account` request header. The Payment Intents variant scopes the client Stripe instance with `stripeAccount` before creating the Element; its example specifies `apiVersion: '2026-03-25.dahlia'`. These are distinct path examples, not interchangeable secrets or a general version requirement. The guide also instructs registration of each domain where the Element appears. It describes HTTPS for development and production, wallet/browser conditions, and merchant responsibility to disclose Stripe's collection of interaction data and obtain needed rights and consents. Account-specific eligibility, final payment outcome, and current Connect behavior were not tested by this capture.

## Detail locators

- [[raw/stripe-express-checkout-element-accept-payment-2025|2026-04-21 combined guide]], Checkout Sessions path lines 28–472; Dashboard default and optional override 51–65; server Session/client secret 67–87; client confirmation 221–237; tests 378–439; Connect 441–466.
- Same guide, Payment Intents path lines 474–1892; path-specific ordering preference 478; Dashboard default and method table 499–519; Elements options 604–629; customer details and wallet events 673–995; ConfirmationToken option 1073–1219; server Intent and authoritative amount 1221–1323; deferred confirm order 1325–1439; sandbox/Klarna fixtures 1443–1864; Connect 1865–1886.

## Related Pages

- [[stripe-express-checkout-element]] — concept and integration context.
- [[source-stripe-express-checkout-element]] — Element overview and button behavior.
- [[source-stripe-express-checkout-element-migration]] — Payment Request Button migration.
- [[stripe]] — provider.

## Related raw API references

- [[raw/stripe-elements-express-checkout-element-accept-a-payment-2026-11-07|2026-11-07 base-URL variant index]] — links the Checkout Sessions API and Payment Intents API pages (lines 9–14); their bodies were not captured in this unit.

## Raw Sources

- [[raw/stripe-express-checkout-element-accept-payment-2025|Express Checkout Element combined guide, captured 2026-04-21]] — historical detailed evidence.
