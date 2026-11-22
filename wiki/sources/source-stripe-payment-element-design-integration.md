---
title: "Design a Custom Payment Element Integration"
type: source
date_ingested: 2026-04-21
date_updated: 2026-11-22
canonical_url: "https://docs.stripe.com/payments/payment-element/design-an-integration"
original_format: webpage
raw_files:
  - "stripe-payment-element-design-integration-2025.md"
tags: [stripe, payment-element, payment-intents, setup-intents, integration-design, deferred-intent, client-confirmation, server-confirmation]
---

## Summary

The April 21, 2026 guide describes two custom Payment Element routes. It recommends Checkout Sessions for most integrations, including one-time payments and checkouts with tax, discounts, shipping, or subscriptions. The lower-level Payment Intents route leaves checkout features such as tax, discounts, shipping, and currency conversion to the integration.

The November 7, 2026 capture gives two documentation links. The Checkout Sessions variant uses `payment-ui=embedded-components` and the Payment Intents variant uses `payment-ui=elements`. These query parameters select documentation. The November index supplies no updated integration steps or API and SDK versions.

## April Checkout Sessions route

The April guide uses `ui_mode: "elements"` in its Checkout Sessions example. The Checkout Session client secret initializes Checkout itself. The HTML path uses `stripe.initCheckoutElementsSdk` and confirms with `actions.confirm()` after loading actions. The React path imports from `@stripe/react-stripe-js/checkout`, supplies the secret to `CheckoutElementsProvider`, and uses `checkout.confirm`. Keep this initialization and confirmation separate from Elements initialized with a PaymentIntent or SetupIntent client secret.

The same capture describes Checkout Sessions for both basic payment collection with `price_data` and full line-item checkout, and assigns Adaptive Pricing to Checkout Sessions in this comparison. See the [[source-stripe-checkout-sessions-vs-payment-intents|separate API comparison]].

## April Payment Intents route

The Payment Element supplies payment details to a PaymentIntent for payment or to a SetupIntent to prepare a method for future use. The April guide gives two decisions for this route.

### When to create the Intent

| Approach | Order and use |
| --- | --- |
| **Deferred** | Render the Payment Element first. Create and confirm the PaymentIntent or SetupIntent after the customer submits the payment form. This suits multi-page checkouts and checkouts with changing items, quantities, or discounts. Changing amounts can affect payment method eligibility. Deferring the Intent avoids synchronizing it after every client-side change. |
| **Eager** | Create the PaymentIntent or SetupIntent before loading checkout. Create Elements with that Intent’s `client_secret` so the Payment Element is associated with the Intent. This is the April guide’s quick-start choice for a static checkout. |

### Where to confirm the Intent

| Approach | Responsibility |
| --- | --- |
| **Client-side** | Client code uses a Stripe SDK to confirm. The SDK handles supported next actions such as 3D Secure and localizes errors. Choose this when the integration does not need server control at confirmation. The integration can still use a backend. |
| **Server-side** | Run the required business logic first, such as applying payment method restrictions or adjusting application fees, then confirm immediately on the server before the client can change the inputs. Handle any returned next actions manually or with a Stripe SDK. The linked PaymentIntent route uses `stripe.handleNextAction` for required customer authentication or redirects. |

Confirmation associates the submitted details with the Intent. Check the resulting state separately for required customer action or a successful payment or setup. The companion [[source-stripe-finalize-payments-server|server-finalization guide]] gives the dated web PaymentIntent `requires_action` example.

## Related Pages

- [[stripe-payment-intents]] — Intent creation, confirmation and lifecycle
- [[source-stripe-checkout-sessions-vs-payment-intents]] — API comparison
- [[source-stripe-finalize-payments-server]] — server confirmation and next actions
- [[stripe]] — company page

## Raw Sources

- [[raw/stripe-payment-element-design-integration-2025|2026-04-21 Payment Element design guide]] — verbatim architectural decision guide, 48 lines

## Related raw API references

- [[raw/stripe-payments-payment-element-design-an-integration-2026-11-07|2026-11-07 Payment Element design index]] — Checkout Sessions and Payment Intents variant navigation
