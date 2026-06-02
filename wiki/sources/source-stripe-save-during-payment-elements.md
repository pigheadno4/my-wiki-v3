---
title: "Save a Customer's Payment Method During Payment"
type: source
date_ingested: 2026-04-21
original_format: webpage
raw_files:
  - "stripe-save-during-payment-elements-2025.md"
tags: [stripe, checkout-sessions, payment-intents, save-payment-method, customer-session, allow-redisplay, off-session, sepa-debit]
---

## Summary

Comprehensive guide for saving payment methods during payment. Covers both Checkout Sessions and Payment Intents paths with full code samples, off-session charging, and test credentials. See also [[source-stripe-checkout-save-during-payment]] for earlier CS-specific coverage.

## Checkout Sessions Path

### Key Difference from Existing Source

CS API **only supports card and ACH Direct Debit** for saved PMs. Other methods can't be saved.

### Session Setup

```js
stripe.checkout.sessions.create({
  saved_payment_method_options: { payment_method_save: 'enabled' },
  customer_creation: 'always',  // or pass customer/customer_account
  ui_mode: 'elements',
});
```

### `elementsOptions.savedPaymentMethod`

| Option | Values | Default |
| --- | --- | --- |
| `enableSave` | `'auto'`, `'never'` | `'auto'` |
| `enableRedisplay` | `'auto'`, `'never'` | `'auto'` |

Set both to `'never'` to build a fully custom saved PM UI.

### Custom Saved PM UI

```js
// List saved PMs
actions.getSession().savedPaymentMethods.forEach((pm) => { /* render */ });

// Confirm with consent
actions.confirm({ savePaymentMethod: checkbox.checked });

// Confirm with saved PM
actions.confirm({ paymentMethod: selectedPmId });
```

React: same methods from `checkoutState.checkout`.

## Payment Intents Path

### CustomerSession — Required for Saved PMs

PI path requires creating both a PaymentIntent AND a CustomerSession with explicit feature flags:

```js
const customerSession = await stripe.customerSessions.create({
  customer: 'cus_...',  // or customer_account: 'acct_...'
  components: {
    payment_element: {
      enabled: true,
      features: {
        payment_method_redisplay: 'enabled',
        payment_method_save: 'enabled',
        payment_method_save_usage: 'off_session',
        payment_method_remove: 'enabled',
      },
    },
  },
});
```

Pass both client secrets to Elements:

```js
stripe.elements({
  clientSecret: paymentIntentClientSecret,
  customerSessionClientSecret: customerSession.client_secret,
});
```

### `setup_future_usage` vs `payment_method_save_usage`

**Mutually exclusive** — do not set both on the same transaction. An integration error results.

| | When to use |
| --- | --- |
| `setup_future_usage` on PI | Auto-save without customer checkbox |
| `payment_method_save_usage` on CustomerSession | Save only when customer checks checkbox |

### Per-PM `setup_future_usage`

To save only reusable methods (not all):

```js
paymentIntents.create({
  payment_method_options: {
    card: { setup_future_usage: 'off_session' },
    // Giropay: not saveable — no setup_future_usage
  },
});
```

### Off-Session Charge

```js
paymentIntents.create({
  customer: 'cus_...',
  payment_method: 'pm_...',
  off_session: true,
  confirm: true,
  return_url: '...',
});
```

### Bancontact/iDEAL/Sofort → SEPA Debit

When saving Bancontact, iDEAL, or Sofort for future use, Stripe generates a `sepa_debit` PaymentMethod. Query saved PMs as `type: 'sepa_debit'` to find these.

## Test Credentials (PI Path)

### SEPA Debit Email Test Patterns

| Email | PI status transition |
| --- | --- |
| `generatedSepaDebitIntentsSucceed@example.com` | `processing` → `succeeded` |
| `generatedSepaDebitIntentsFail@example.com` | `processing` → `requires_payment_method` |
| `generatedSepaDebitIntentsSucceedDelayed@example.com` | Delayed `succeeded` (≥3 min) |
| `generatedSepaDebitIntentsFailsDueToInsufficientFunds@example.com` | `insufficient_funds` failure |

Full test table in raw file.

## Related Pages

- [[stripe-saved-payment-methods]] — concept page
- [[source-stripe-checkout-save-during-payment]] — earlier CS-specific save-during-payment source
- [[source-stripe-payment-element-saved-pms]] — saved PM display/management reference
- [[stripe-payment-intents]] — Payment Intents concept page

## Raw Sources

- [[stripe-save-during-payment-elements-2025]] — verbatim guide (963 lines, both API paths)
