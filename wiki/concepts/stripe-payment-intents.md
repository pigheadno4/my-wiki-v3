---
title: "Stripe Payment Intents"
type: concept
category: technology
tags: [stripe, payment-intents, elements, confirmPayment, useStripe, useElements, webhooks, off-session]
---

## Stripe Payment Intents

Stripe's core payment API for building fully custom checkout flows. Tracks the customer's payment lifecycle, handles failed attempts, and ensures the customer is only charged once. Best for integrations that require maximum control over checkout UI and flow.

## When to Use

| | Payment Intents API | Checkout Sessions API |
| --- | --- | --- |
| Control | Maximum — build everything yourself | Low coding — Stripe handles checkout concerns |
| Tax/shipping | Manual (Stripe Tax API) | Automatic (`automatic_tax`) |
| UI | Full custom via Elements + Appearance API | Full custom via Elements + Appearance API |
| Best for | Highly custom flows | Most integrations |

> **Recommendation**: Use Checkout Sessions API for most integrations. Use Payment Intents only if you need features not available in Checkout Sessions.

## Limitations vs Checkout Sessions

- **No native shipping rates** — must add shipping cost to product total manually, or switch to Checkout Sessions
- **No built-in tax** — must call Tax API separately and link calculations
- **No built-in discounts/coupons** — must calculate manually
- **No session expiration** — sessions don't auto-expire (Checkout Sessions expire after 24h)

## Integration Design: 2×2 Decision Framework

Before building a Payment Intents integration, make two architectural choices:

### Decision 1 — When to Create the Intent

| Approach | Use when |
| --- | --- |
| **Deferred** (create Payment Element first) | Multi-page flows; dynamic amounts (items, quantities, discounts can change before Pay) |
| **Eager** (create Intent + Payment Element together) | Static checkout pages; quickest setup |

**Why deferred matters**: Amount changes affect payment method eligibility. Deferring avoids syncing the Intent with every client-side change.

### Decision 2 — Where to Confirm the Intent

| Approach | Use when |
| --- | --- |
| **Client-side** | No server business logic needed; quickest; Stripe SDK handles 3DS + next actions automatically + localizes errors |
| **Server-side** | Must run business logic before confirmation (PM restrictions, application fees); confirm immediately after to prevent client invalidation |

## Core Flow

1. **Server**: `stripe.paymentIntents.create({ amount, currency, automatic_payment_methods: { enabled: true } })` → returns `client_secret`
2. **Client**: initialize `Elements` provider with `clientSecret`
3. **Client**: `stripe.confirmPayment({ elements, confirmParams: { return_url } })` — redirects for bank auth; immediate error for card declines
4. **Return page**: read `payment_intent_client_secret` URL param → `stripe.retrievePaymentIntent(cs)` → handle status

## Client Setup (React)

```js
import { loadStripe } from "@stripe/stripe-js";
import { Elements } from "@stripe/react-stripe-js";
import { PaymentElement, useStripe, useElements } from "@stripe/react-stripe-js";

// Provider
<Elements options={{ clientSecret, appearance, loader: 'auto' }} stripe={stripePromise}>
  <CheckoutForm />
</Elements>

// In form component
const stripe = useStripe();
const elements = useElements();
await stripe.confirmPayment({ elements, confirmParams: { return_url, receipt_email } });
```

## PaymentIntent Statuses

| Status | Meaning |
| --- | --- |
| `requires_payment_method` | No PM attached or payment failed |
| `requires_confirmation` | Awaiting confirmation |
| `requires_action` | 3DS or redirect needed |
| `processing` | Processing (e.g., bank debit) |
| `succeeded` | Payment complete |
| `canceled` | Canceled |

## Webhook Events

Listen server-side for reliability (clients can close browser):

- `payment_intent.succeeded` — fulfill order
- `payment_intent.processing` — show processing state (e.g. bank debit initiated)
- `payment_intent.payment_failed` — notify customer

**Delayed notification payment methods** (9 methods — funds not immediate): Bacs Direct Debit, Bank transfers, Boleto, Canadian pre-authorized debits, Konbini, OXXO, Pay by Bank, SEPA Direct Debit, ACH Direct Debit. For these, delay fulfillment until `payment_intent.succeeded` fires (may be days after `processing`).

## Stripe Tax Integration

```js
const taxCalculation = await stripe.tax.calculations.create({...});
stripe.paymentIntents.create({
  amount: taxCalculation.amount_total,
  hooks: { inputs: { tax: { calculation: taxCalculation.id } } },
});
```

## Save Payment Method

```js
// On create: setup_future_usage: 'off_session'
// To charge later: off_session: true, confirm: true
```

## ConfirmationToken Metadata

`@stripe/stripe-js@9.15.0` adds `metadata?: MetadataParam` to `ConfirmationTokenCreateParams`, so typed web integrations can attach metadata while calling `stripe.createConfirmationToken({elements, params})`. The declaration documents a maximum of 50 keys and rejects unsupported value types at compile time. This is package-level TypeScript evidence; server persistence and Stripe-hosted runtime availability still require current API and product confirmation.

## Related Concepts

- [[stripe-elements]] — Stripe Elements (UI component library used with Payment Intents)
- [[stripe-checkout]] — Stripe Checkout (Checkout Sessions API — recommended alternative)

## Sources

- [[source-stripe-payment-intents-quickstart]] — Full quickstart: server setup, Elements wiring, confirmPayment, return page, Stripe Tax, email receipts, off-session charging
- [[source-stripe-elements-advanced-payments]] — Checkout Sessions vs Payment Intents comparison matrix
- [[source-stripe-payment-element-design-integration]] — 2×2 integration design framework: when to create Intent × where to confirm (deferred vs eager, client vs server)
- [[source-stripe-migrate-payment-methods-dashboard]] — Migrate to Dashboard payment methods: remove payment_method_types, Google Pay disabled by default, delayed notification PM list + webhook pattern
- [[source-stripe-checkout-dynamic-amounts]] — Dynamic amounts (PI path): paymentIntents.update({ amount }), server-side calculation, cannot increase after confirmation, developer owns client-server sync
- [[source-stripe-email-receipts]] — Receipts (PI path): receipt_email is additional address, no invoice generation (use Stripe Billing), localization doesn't use browser locale, update Charge not PI for receipt changes
- [[source-stripe-receipts]] — Receipts overview: 30-day link expiry, auto/manual send, refund receipts, invoice itemized receipts, Connect branding rules
- [[source-stripe-auth-and-capture]] — Auth+capture: validity windows per card brand, per-PM capture rules, capture_method=manual vs automatic_delayed (private preview), partial capture
- [[source-stripe-payment-element-migration]] — Migration guide: CardElement → PaymentElement, elements.submit() pattern, 11 Elements options, ConfirmationToken migration
- [[source-stripe-two-step-confirmation]] — Two-step checkout: ConfirmationToken flow, Elements options table, saved PMs, tax calc, layouts, limitations
- [[source-stripe-accept-payment-deferred]] — Deferred intent: render Element before PI, elements.submit() required, dynamic updates, payment+setup modes
- [[source-stripe-finalize-payments-server]] — Server-side confirmation: paymentMethodCreation='manual', ConfirmationToken (12hr expiry), handleNextAction, SDK min versions
- [[source-github-stripe-js]] — package-qualified Stripe.js loader and declaration history through `@stripe/stripe-js@9.15.0`, including ConfirmationToken metadata typing
- [[source-stripe-payments-without-auth]] — Legacy US/CA-only: CardElement + createPaymentMethod, error_on_requires_action, synchronous, no webhooks
- [[source-stripe-migrate-basic-card-integration]] — Migrate legacy to auth-handling: remove error_on_requires_action, add confirmation_method='manual', handleCardAction, 1-hour re-confirm window
