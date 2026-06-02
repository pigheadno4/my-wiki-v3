---
title: "Save a Payment Method Without Making a Payment"
type: source
date_ingested: 2026-04-21
original_format: webpage
raw_files:
  - "stripe-save-and-reuse-elements-2025.md"
tags: [stripe, setup-intents, checkout-sessions, save-payment-method, setup-mode, off-session, apple-pay, link, radar]
---

## Summary

Integration guide for saving a payment method WITHOUT an initial charge. Two API paths: Checkout Sessions `mode: 'setup'` (simpler) and Setup Intents API (more control). Both result in a saved PaymentMethod that can be charged off-session later. See also [[source-stripe-checkout-save-and-reuse]] for earlier CS coverage.

## Checkout Sessions Path (`mode: 'setup'`)

```js
stripe.checkout.sessions.create({
  mode: 'setup',
  ui_mode: 'elements',
  currency: 'usd',  // required for dynamic PM selection
});
```

**Full flow:**
1. Session create → customer completes
2. `checkout.session.completed` webhook → get `setup_intent` ID from session
3. Retrieve SetupIntent → get `payment_method` ID
4. Attach PM to customer: `stripe.paymentMethods.attach(pmId, { customer: id })`
5. Charge later: `off_session: true, confirm: true`

If off-session charge fails (402) → send customer to new CS with existing customer to pick a new PM.

## Setup Intents Path

```js
// Server
const si = await stripe.setupIntents.create({
  customer: 'cus_...',
  automatic_payment_methods: { enabled: true },
});
// Send si.client_secret to client
```

```js
// Client — confirm
const { error } = await stripe.confirmSetup({
  elements,
  confirmParams: { return_url: 'https://example.com/setup-complete' },
  redirect: 'if_required', // optional: avoids redirect for cards
});
```

**Return URL params**: `setup_intent`, `setup_intent_client_secret`

```js
// Return page
const { setupIntent } = await stripe.retrieveSetupIntent(clientSecret);
// setupIntent.payment_method → saved PM ID
```

## Key Differences: CS Setup vs Setup Intents

| | CS `mode: 'setup'` | Setup Intents |
| --- | --- | --- |
| PM retrieval | Via webhook + SetupIntent lookup | Via return URL + retrieveSetupIntent |
| Apple Pay merchant tokens | No | Yes — `applePay.deferredPaymentRequest` |
| Radar | No | Optional — enable in Dashboard settings |
| Custom PM display | No | Yes — CustomerSession |
| Link prefill | Auto | `defaultValues.billingDetails.email` |

## Apple Pay Merchant Tokens (Setup Intents)

```js
elements.create('payment', {
  applePay: {
    deferredPaymentRequest: {
      paymentDescription: 'My deferred payment',
      managementURL: 'https://example.com/billing',
      deferredBilling: { amount: 2500, label: 'Deferred Fee', deferredPaymentDate: new Date('2030-01-05') },
    }
  },
});
```

## Radar (Setup Intents)

Radar does NOT run on SetupIntents by default. Enable at Dashboard → Radar settings → "Use Radar on payment methods saved for future use".

## Link Prefill (Setup Intents)

```js
elements.create('payment', {
  defaultValues: { billingDetails: { email: 'foo@bar.com' } },
});
```

## Related Pages

- [[stripe-saved-payment-methods]] — concept page
- [[source-stripe-checkout-save-and-reuse]] — earlier CS setup mode source (hosted + embedded)
- [[source-stripe-save-during-payment-elements]] — save WITH initial payment

## Raw Sources

- [[stripe-save-and-reuse-elements-2025]] — verbatim guide (1312 lines, both API paths)
