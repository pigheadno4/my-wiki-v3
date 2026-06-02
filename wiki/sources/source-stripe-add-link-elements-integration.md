---
title: "Stripe Docs — Build a custom checkout page that includes Link"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-add-link-elements-integration-2025.md"
tags: [stripe, link, payment-element, link-authentication-element, address-element, react, custom-checkout, manual-capture]
---

## Summary

Comprehensive integration guide for Link with custom checkout pages using the Payment Intents API + Payment Element or Link Authentication Element. Covers React and HTML+JS for all three email strategies, shipping, prefill, manual capture, and submit.

## Three Email Collection Strategies

| Strategy | Use when | Element |
| --- | --- | --- |
| **Pass email** (recommended) | Email collected before payment page | Payment Element only |
| **Collect in Payment Element** | No prior email collection; no shipping | Payment Element only |
| **Link Authentication Element** | Need shipping collection | LAE + Address Element + Payment Element |

## Key Integration Details

### Pass-in email (Payment Element)

```js
elements.create('payment', { defaultValues: { billingDetails: { email, name, phone, address } } })
```

Email (required), name/phone/address (optional). Same-page update: `paymentElement.update({ defaultValues: ... })` on `onblur` of form fields.

### LAE path

- Page order: LAE → Address Element → Payment Element
- Multi-page checkout supported — LAE only needs to appear once
- `onChange` to extract email: `event.value.email`
- Prefill email triggers Link auth immediately: `elements.create('linkAuthentication', { defaultValues: { email } })`

### Shipping (Address Element)

- Must appear AFTER LAE for Link autofill to work
- Payment Element auto-detects and hides redundant billing address fields
- `onChange` retrieves address; `defaultValues` prefills address

### Manual Capture

`capture_method: 'manual'` on PaymentIntent → **must capture within 7 days** or authorization auto-cancels. `amount_to_capture` can be less than authorized but not more.

### Submit

```js
stripe.confirmPayment({ elements, confirmParams: { return_url } })
```

`return_url` receives `payment_intent` + `payment_intent_client_secret`.

## CDN Assets (9 images/diagrams)

- `stripe-link-in-payment-element.png` — Link in PE (reused)
- `stripe-link-payment-flow-diagram.svg` — Payment flow overview
- `stripe-link-lape-unregistered.png` — Unregistered user in PE
- `stripe-link-collect-email-returning.png` — Returning user email collection
- `stripe-link-with-elements.png` — Multi-element layout
- `stripe-link-prefill-pe-new-user.png` — Prefill new user (PE path)
- `stripe-link-prefill-lae-new-user.png` — Prefill new user (LAE path)
- `stripe-link-appearance-example.png` — Appearance API customization
- `stripe-link-customer-saved-data.png` — Saved customer data view

## Related Pages

- [[stripe-link]] — Link concept page (Custom Checkout section)
- [[source-stripe-payment-element-link]] — Link in Payment Element (conceptual overview)
- [[source-stripe-elements-link]] — Link Authentication Element guide
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-add-link-elements-integration-2025]] — verbatim webpage content (1,424 lines)
