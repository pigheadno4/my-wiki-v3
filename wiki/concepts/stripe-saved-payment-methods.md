---
title: "Stripe Saved Payment Methods"
type: concept
category: technology
tags: [stripe, saved-payment-methods, allow-redisplay, customer-session, setup-future-usage, off-session, recurring, link]
---

## Definition

Stripe's pattern for saving a customer's payment method during or after a payment so it can be reused in future sessions. Both the Checkout Sessions API and Payment Intents API support this, but with different mechanics.

## When to Save a Payment Method

- E-commerce: save during purchase for one-click future orders
- Subscriptions: save at first payment for recurring billing
- Deposits: save to charge the full amount later
- Off-session charges: save for charges without the customer present

## `allow_redisplay` Values

Controls whether a saved PM appears in the Payment Element for future sessions:

| Value | Meaning |
| --- | --- |
| `always` | PM renders and can be reused — customer gave explicit consent |
| `limited` | PM won't appear for future purchases (e.g. setup_future_usage without consent checkbox) |
| `unspecified` | Legacy PMs (saved outside checkout) — won't render by default |

## Checkout Sessions Path

```js
stripe.checkout.sessions.create({
  saved_payment_method_options: { payment_method_save: 'enabled' },
  customer_creation: 'always', // or customer/customer_account
  ui_mode: 'elements',
});
```

- **Supported methods**: card, ACH Direct Debit only (not bank redirects, etc.)
- Payment Element auto-shows consent checkbox when enabled
- `elementsOptions.savedPaymentMethod.enableSave: 'auto'` (default) or `'never'` for custom UI
- `enableRedisplay: 'auto'` or `'never'` to control redisplay

## Payment Intents Path

Requires a **CustomerSession** alongside the PaymentIntent:

```js
const cs = await stripe.customerSessions.create({
  customer: 'cus_...',
  components: { payment_element: { enabled: true, features: {
    payment_method_redisplay: 'enabled',
    payment_method_save: 'enabled',
    payment_method_save_usage: 'off_session',
    payment_method_remove: 'enabled',
  }}},
});

stripe.elements({
  clientSecret: piSecret,
  customerSessionClientSecret: cs.client_secret,
});
```

> **Mutually exclusive**: `setup_future_usage` on the PaymentIntent and `payment_method_save_usage` on the CustomerSession cannot both be set — causes an integration error.

## Per-PM `setup_future_usage`

To save only reusable methods (e.g. cards but not Giropay):

```js
payment_method_options: { card: { setup_future_usage: 'off_session' } }
```

## Bancontact / iDEAL / Sofort → SEPA Debit

When saved for future use, these redirect-based methods generate a `sepa_debit` PaymentMethod. Query saved PMs as `type: 'sepa_debit'`.

## Displaying Saved PMs

- **Checkout Sessions**: Payment Element auto-redisplays when customer/customer_account is on session
- **Payment Intents**: requires CustomerSession with `payment_method_redisplay: 'enabled'`
- **Legacy `unspecified` PMs**: either update `allow_redisplay` to `'always'` via API, or configure CustomerSession filters
- **Display order**: most recently added first; default PM always first
- **Subscription warning**: removing a PM from the saved section also removes it from active subscriptions — disable `payment_method_remove` and use account settings instead

## Save Without an Initial Payment (Setup Mode)

### Checkout Sessions `mode: 'setup'`

```js
stripe.checkout.sessions.create({ mode: 'setup', ui_mode: 'elements', currency: 'usd' });
```

After `checkout.session.completed`: retrieve session → get `setup_intent` → retrieve SetupIntent → `payment_method` ID → attach to customer.

### Setup Intents API

```js
// Server: stripe.setupIntents.create({ customer, automatic_payment_methods: { enabled: true } })
// Client: stripe.confirmSetup({ elements, confirmParams: { return_url }, redirect: 'if_required' })
// Return page: stripe.retrieveSetupIntent(clientSecret) → setupIntent.payment_method
```

**Radar**: does NOT run on SetupIntents by default — enable in Dashboard → Radar settings.

**Apple Pay merchant tokens**: configure `applePay.deferredPaymentRequest` on the Payment Element for deferred/recurring setups.

## Off-Session Charging

```js
stripe.paymentIntents.create({
  customer: 'cus_...',
  payment_method: 'pm_...',
  off_session: true,
  confirm: true,
  return_url: '...',
});
```

## Link Integration

Works with saved PMs without extra config. Business-saved PMs displayed before Link PMs.

## CVC Re-Collection

```js
payment_method_options: { card: { require_cvc_recollection: true } }
```

## Custom Saved PM UI

Disable built-in UI with `enableSave: 'never'` + `enableRedisplay: 'never'`, then:

- Render `savedPaymentMethods` from session object
- Call `actions.confirm({ savePaymentMethod: bool })` or `actions.confirm({ paymentMethod: id })`

## Key Players

- [[stripe]] — the sole provider of this feature

## Sources

- [[source-stripe-checkout-save-during-payment]] — CS path: setup_future_usage, saved_payment_method_options, allow_redisplay semantics
- [[source-stripe-payment-element-saved-pms]] — display/management: allow_redisplay values, CVC re-collection, subscription removal warning, unspecified legacy PMs
- [[source-stripe-save-during-payment-elements]] — full integration: both API paths, CustomerSession, enableSave/enableRedisplay, Bancontact→SEPA, off-session charging
- [[source-stripe-save-and-reuse-elements]] — save without payment: CS mode=setup + Setup Intents, confirmSetup, retrieveSetupIntent, Apple Pay MPANs, Radar note
- [[source-stripe-inapp-save-during-payment]] — Mobile save-during-payment: setup_future_usage supports cards + US bank only on mobile, mobile_payment_element CustomerSession, allowsDelayedPaymentMethods
- [[source-stripe-inapp-set-up-future-payments]] — Mobile setup without charge: SetupIntent supports card/Bancontact/iDEAL/Link/SEPA/Sofort/US bank (more than setup_future_usage), setupIntentClientSecret
- [[source-stripe-inapp-customer-sheet]] — CustomerSheet (Payment Method Settings Sheet): app settings PM management UI for iOS/Android/RN; CustomerSession + SetupIntent dual endpoints; retrievePaymentOptionSelection without presenting
- [[source-stripe-inapp-save-card-without-auth]] — Legacy save-card (US/Canada only): attach PM to Customer, charge with error_on_requires_action, setup_future_usage=on_session, CVC re-collection; non-compliant in India
- [[source-stripe-payments-existing-customers]] — Existing customer flows: 4 paths (hosted/embedded/Elements/custom), allow_redisplay rules, prefill conditions, 30-min timeout
- [[source-stripe-save-card-without-auth]] — Web legacy save card (US/CA only): createPaymentMethod→attach Customer, error_on_requires_action, setup_future_usage=on_session, CVC re-collection
