---
title: "Stripe Checkout Sessions API"
type: source
date_ingested: 2026-04-19
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/checkout-sessions"
raw_files:
  - "stripe-payments-checkout-sessions-2026-11-07.md"
  - "stripe-checkout-sessions-api-2025.md"
tags: [stripe, checkout-sessions, checkout, payment-element, adaptive-pricing, subscriptions]
---

## Summary

The April and November 2026 Stripe overviews recommend the Checkout Sessions API for most payments integrations. It supplies built-in tax calculation, discounts, shipping, subscriptions and Adaptive Pricing with less merchant-written checkout logic than the Payment Intents API. Stripe describes managed authentication, Session status/expiration and lifecycle tracking, and duplicate-charge prevention as product advantages. The lifecycle varies by payment UI; these overview statements do not show a completed payment or a universal outcome guarantee. See new raw lines 7-35 and old raw lines 6-34.

## Key Takeaways

- **Three UI routes:** Stripe-hosted redirect page, embedded form, and a custom payment flow built with Stripe Elements including the Payment Element. The Checkout Sessions API is the back end for all three. See new raw lines 11-17.
- **Server/client boundary in the linked Elements quickstart:** The server creates a Checkout Session; the client receives its `client_secret` for Stripe Elements. The overview does not show the client confirmation or paid state. The November quickstart URL is `https://docs.stripe.com/payments/quickstart.md`; the April overview linked `payments/quickstart-checkout-sessions.md`. See new raw lines 15-17, 54-56; old raw lines 14-16, 59-61.
- **Checkout Sessions versus Payment Intents:** Stripe says the former covers similar scenarios with significantly less code and built-in support for the listed features. It recommends Payment Intents when an integration needs control of every aspect of checkout state or builds discount, tax, subscription and currency-conversion logic itself. This overview does not say every Payment Intents integration lacks all ancillary services. See new raw lines 19-31.
- **Metadata:** Attach an internal order identifier to a Session for Dashboard/report reconciliation. Do not put personally identifiable information, card details or other sensitive data in metadata. See new raw lines 37-50.

## Captured UI and Mode Examples

| Route | Overview description |
| --- | --- |
| Stripe-hosted page | Redirect customer to Stripe-hosted payment page. |
| Embedded form | Embed Stripe payment form on merchant site. |
| Custom Elements flow | Build a custom checkout page using Stripe Elements/Payment Element. |

Both captured overviews illustrate server-side Session creation for the custom flow with literal `ui_mode=custom`, `mode=payment`, a return URL and `metadata[order_id]=6735`. The 2026-04-19 illustration is Node.js; the 2026-11-07 illustration is equivalent curl:

```sh
curl https://api.stripe.com/v1/checkout/sessions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d mode=payment \
  -d ui_mode=custom \
  --data-urlencode "return_url=https://example.com/return" \
  -d "metadata[order_id]=6735"
```

The request shows creation and metadata association, not client confirmation, completed Session status, payment success or fulfillment. Preserve the example's `custom` value as printed in these overviews. Separate version-qualified React guidance for a new custom Checkout Elements page uses `ui_mode: 'elements'` with `CheckoutElementsProvider`; these captures do not settle which mode name a particular current SDK/API-version integration should use. See old raw lines 40-55, new raw lines 41-50, and [[stripe-checkout]].

## Dated Comparison

No substantive feature or lifecycle delta is established by the two pinned overviews. November changes the custom-flow and quickstart link to `payments/quickstart.md`, changes the metadata example language from Node to curl, and reflows headings/table formatting. The request fields and central claims remain. An updated link is navigation, not evidence about the linked guide's implementation or product rollout.

## Related Pages

- [[stripe]] — Stripe company route.
- [[stripe-checkout]] — concept, including the separate version-qualified `elements` React path.
- [[source-stripe-how-checkout-works]] — Checkout lifecycle and UI details.
- [[source-stripe-payment-intents]] — distinct Payment Intents and Setup Intents reference.

## Raw Sources

- [[raw/stripe-payments-checkout-sessions-2026-11-07|2026-11-07 Checkout Sessions overview]] — newer full capture and curl metadata example.
- [[raw/stripe-checkout-sessions-api-2025|2026-04-19 Checkout Sessions overview]] — older full capture and Node metadata example.
