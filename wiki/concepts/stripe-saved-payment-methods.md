---
title: "Stripe Saved Payment Methods"
type: concept
category: technology
tags: [stripe, saved-payment-methods, allow-redisplay, customer-session, setup-future-usage, off-session, recurring, link]
---

## Definition

Stripe lets businesses save a customer's payment method for future use during or after a payment, or set it up without an initial charge. The separate setup paths use Checkout Sessions in setup mode or the Setup Intents API. See [[source-stripe-save-and-reuse-elements]].

## When to Save a Payment Method

- E-commerce: save during purchase for one-click future orders
- Subscriptions: save at first payment for recurring billing
- Deposits: save to charge the full amount later
- Off-session charges: save for charges without the customer present

## `allow_redisplay` Values

Controls whether a saved PM appears in the Payment Element for future sessions:

| Value | Meaning |
| --- | --- |
| `always` | An eligible saved PM can be redisplayed; the Checkout save-consent path sets this value when the customer selects the checkbox |
| `limited` | Excluded from default redisplay. In the dated existing-customer Checkout guide, a Session's `saved_payment_method_options.allow_redisplay_filters` can include `limited`; rendering a saved method still requires consent for that specific future use. |
| `unspecified` | Legacy PMs (saved outside checkout) — won't render by default |

## Checkout Sessions Path

```js
stripe.checkout.sessions.create({
  saved_payment_method_options: { payment_method_save: 'enabled' },
  customer_creation: 'always', // create a new Customer
  ui_mode: 'elements',
});
```

For an existing identity, use `customer` for a Customers v1 Customer or `customer_account` for a customer-configured Accounts v2 Account. The 2026-04-20 [[source-stripe-accept-a-payment|Accept a payment guide]] describes Accounts v2 as generally available for Connect users and in public preview for other Stripe users; preview participants need a preview API version. These are alternative identity routes, subject to that availability.

- **Supported methods**. The April 21, 2026 guide limits saved methods to cards and ACH Direct Debit for Elements with Checkout Sessions.
- Payment Element auto-shows consent checkbox when enabled
- `elementsOptions.savedPaymentMethod.enableSave: 'auto'` (default) or `'never'` for custom UI
- `enableRedisplay: 'auto'` or `'never'` to control redisplay

## Payment Intents Path

For the April 21, 2026 Payment Element saved-method UI, create a **CustomerSession** alongside the PaymentIntent. If CustomerSession creation fails, the guide says to omit its client secret after handling the error. See [[source-stripe-save-during-payment-elements]] for supported saving and redisplay options.

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

When saved for future use, these redirect-based methods generate a `sepa_debit` PaymentMethod. Query saved PMs as `type: 'sepa_debit'`. The dated iDEAL | Wero payment flow in [[source-stripe-ideal-save-during-payment]] retrieves `generated_sepa_debit` from the initial PaymentIntent's expanded `latest_charge`; its 2026-11-07 capture is a variant navigation index only.

## Displaying Saved PMs

- **Checkout Sessions**: A `customer` or eligible `customer_account` identifies whose saved methods Checkout can consider, but identity alone does not make them prefill. In the 2026-04-20 [[source-stripe-accept-a-payment|Accept a payment guide]], selecting the optional save-consent checkbox sets `allow_redisplay: always`; eligible saved **cards** can then prefill returning Checkout purchases. Cards saved through `setup_future_usage` or subscription mode without that checkbox can have `limited` and do not automatically prefill. The retained 2026-05-11 existing-customer guide permits Checkout `saved_payment_method_options.allow_redisplay_filters` to include `limited`; a saved card can prefill after this display setting is adjusted if the other Checkout conditions hold, including `payment` or `subscription` mode and the required billing details. The guide states a 30-minute prefill window after Session creation. Displaying a saved method still requires consent for the specific future use. `unspecified` methods are excluded by default unless redisplay behavior is appropriately changed or overridden; Checkout prefills saved cards only.
- **Payment Intents**: requires CustomerSession with `payment_method_redisplay: 'enabled'`
- **Legacy `unspecified` PMs**: either update `allow_redisplay` to `'always'` via API, or configure CustomerSession filters
- **Payment Element subscription or recurring checkout**: the April 21, 2026 [[source-stripe-payment-element-saved-pms|saved-methods reference]] describes redisplay starting with the most recently added payment method, with the customer's default method shown first when set.
- **Link PaymentIntent checkout**: the May and November 2026 integration guide describes the three most recently used saved cards alongside Link-saved methods when the customer has more than one saved method. See [[source-stripe-add-link-elements-integration#Saved-Data Redisplay and Future Link Payments|the dated Link redisplay examples]].
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

`off_session: true` describes the current confirmation attempt when the customer is absent and cannot authenticate. `setup_future_usage` describes planned reuse. The 2026-04-23 [[source-stripe-inapp-save-card-without-auth|mobile save-card guide]] uses `setup_future_usage: 'on_session'` in its combined example for future payments with the customer present.

```js
stripe.paymentIntents.create({
  customer: 'cus_...',
  payment_method: 'pm_...',
  off_session: true,
  confirm: true,
  return_url: '...',
});
```

### Metronome Indian-card e-mandate flow

In the documented Metronome Indian-card invoice integration, the merchant confirms a Stripe SetupIntent on-session and Stripe creates the mandate. The integration must wait for Stripe status `active`; `pending` may last up to 30 minutes, while `inactive` requires new customer authorization. Stripe may emit `invoice.payment_action_required` and owns mandate creation and lifecycle. The guide requires SetupIntent setup because it characterizes all charges in this specific flow, including the first, as off-session; that requirement must not be generalized to all Stripe saved-payment-method behavior.

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
- [[source-stripe-save-during-payment-elements]] — April 2026 web save-during-payment guide for Checkout Sessions with Elements and Payment Intents, with consent, redisplay and later charging. November links the two variants.
- [[source-stripe-save-and-reuse-elements]] — save without payment: CS mode=setup + Setup Intents, confirmSetup, retrieveSetupIntent, Apple Pay MPANs, Radar note
- [[source-stripe-inapp-save-during-payment]] — 2026-04-22 mobile save-during-payment guide, scoped to the `mobile_payment_element` CustomerSession component and initial PaymentIntent `setup_future_usage` for cards and US bank accounts. The web `payment_element` example above is a separate integration. The 2026-11-07 capture is a Payment Sheet variant index.
- [[source-stripe-inapp-set-up-future-payments]] — April 2026 mobile setup without charge using a precreated SetupIntent. The seven-method list applies to iOS. The Android and React Native variants list cards, Link, and US bank accounts. The separately documented React Native deferred server-confirmation route names cards and PayPal. See [[source-stripe-inapp-finalize-payments-server]].
- [[source-stripe-inapp-customer-sheet]] — CustomerSheet (Payment Method Settings Sheet): app settings PM management UI for iOS/Android/RN; CustomerSession + SetupIntent dual endpoints; retrievePaymentOptionSelection without presenting
- [[source-stripe-inapp-save-card-without-auth]] — 2026-04-23 guide to mobile card saving and later charging for merchants doing business primarily in the US and Canada, with authentication limits and optional CVC re-collection. The November capture is platform navigation.
- [[source-stripe-payments-existing-customers]] — The retained 2026-05-11 guide covers five on-session routes: hosted, full embedded, and Elements Checkout Sessions; a PaymentIntent with CustomerSession; and Direct API PaymentMethod listing plus PaymentIntent confirmation. Redisplay filters, card prefill and events vary by route. The 2026-11-07 canonical capture is variant navigation only, not refreshed behavior.
- [[source-stripe-save-card-without-auth]] — May and November 2026 basic web card-saving guides for businesses operating primarily in the US and Canada. Includes Customers v1 attachment, action-required decline and recovery, future customer-present reuse, and optional CVC re-collection.
- [[source-metronome-guides-customers-billing-optimize-customer-experience-india-e-mandates]] — source-scoped Indian-card SetupIntent mandate creation, activation states, invoice attachment, action-required handling, and Stripe lifecycle ownership
