---
title: "Stripe Payment Intents"
type: concept
category: technology
tags: [stripe, payment-intents, elements, confirmPayment, useStripe, useElements, webhooks, off-session]
---

## Stripe Payment Intents

Stripe's Payment Intents API tracks attempts in custom payment flows. A single PaymentIntent can have several associated Charge records and at most one successful Charge. Reuse the Intent for a resumed cart or session and send a creation idempotency key to prevent duplicate Intent creation for a purchase. See [[source-stripe-payment-intents]].

## When to Use

| | Payment Intents API | Checkout Sessions API |
| --- | --- | --- |
| Control | Maximum — build everything yourself | Low coding — Stripe handles checkout concerns |
| Tax/shipping | Manual (Stripe Tax API) | Automatic (`automatic_tax`) |
| UI | Full custom via Elements + Appearance API | Full custom via Elements + Appearance API |
| Best for | Highly custom flows | Most integrations |

> **Recommendation**: Use Checkout Sessions API for most integrations. Use Payment Intents only if you need features not available in Checkout Sessions.

## Limitations vs Checkout Sessions

- **No built-in shipping-rate calculation or definition** — the 2026-04-21 Payment Intents guide describes calculating the shipping-inclusive total yourself or using Checkout Sessions; neither route is presented as the sole recommendation. See [[source-stripe-charge-shipping]].
- **No built-in tax** — must call Tax API separately and link calculations
- **No built-in discounts/coupons** — must calculate manually
- **Expiration and events**. The November comparison contrasts PaymentIntent payment-status events and merchant-owned checkout lifecycle with Checkout Session lifecycle events and automatic Session expiration. Checkout Sessions default to 24 hours, with `expires_at` configurable from 30 minutes to 24 hours after creation. Payment Intents has no automatic Checkout Session expiry. See [[source-stripe-accept-a-payment]] for the dated API comparison.

## Integration Design: 2×2 Decision Framework

Before building a Payment Intents integration, make two architectural choices:

### Decision 1 — When to Create the Intent

| Approach | Use when |
| --- | --- |
| **Deferred** | Render Payment Element first, then create and confirm the PaymentIntent or SetupIntent on customer submission. Useful for multi-page checkout or changing amounts. |
| **Eager** | Create the PaymentIntent or SetupIntent before loading checkout, then initialize Elements with that Intent’s client secret. The April 2026 guide recommends this for static checkout. |

**Why deferred matters**: Amount changes affect payment method eligibility. Deferring avoids syncing the Intent with every client-side change.

### Decision 2 — Where to Confirm the Intent

| Approach | Use when |
| --- | --- |
| **Client-side** | When server control at confirmation is unnecessary, use the client SDK. It handles supported next actions such as 3D Secure and localizes errors. The rest of the integration can still use a backend. |
| **Server-side** | Run pre-confirmation business logic, such as applying payment method restrictions or adjusting application fees, then confirm immediately. Handle any returned next actions manually or through an SDK. In the linked web PaymentIntent example, use `stripe.handleNextAction` for required customer action. |

Check the resulting Intent state. Confirmation can leave customer action pending, and setup success differs from a completed payment.

## Core Flow

1. **Server**: `stripe.paymentIntents.create({ amount, currency, automatic_payment_methods: { enabled: true } })` → returns `client_secret`
2. **Client**: initialize `Elements` provider with `clientSecret`
3. **Client**: `stripe.confirmPayment({ elements, confirmParams: { return_url } })` — redirects for bank auth; immediate error for card declines
4. **Return page**: In the dated Stripe.js quickstart, Stripe.js appends `payment_intent_client_secret` for `stripe.retrievePaymentIntent` and status messaging. Use verified server events for fulfillment. Keep the secret out of logs and merchant-built URLs.

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

The April and November 2026 Setup Intents guides separately describe no-charge setup. `SetupIntent.usage` uses `on_session` for customer-present-only reuse and `off_session` for off-session or mixed use. It defaults to `off_session`. Get an agreement for off-session charging and bring the customer back online if the issuer requires authentication on a later off-session card payment. See [[source-stripe-payment-intents#Saving a payment method|the Setup Intents guide summary]].

## ConfirmationToken Metadata

`@stripe/stripe-js@9.15.0` adds `metadata?: MetadataParam` to `ConfirmationTokenCreateParams`, so typed web integrations can attach metadata while calling `stripe.createConfirmationToken({elements, params})`. The declaration documents a maximum of 50 keys and rejects unsupported value types at compile time. This is package-level TypeScript evidence; server persistence and Stripe-hosted runtime availability still require current API and product confirmation.

## Server SDK 22.6.0 Type Boundary

`stripe@22.6.0` changes PaymentIntent and SetupIntent **response** `allowed_payment_method_types` to required-but-nullable; create/update/confirm request parameters remain optional. The allowlist enums add `touch_n_go`. ConfirmationToken gains required-but-nullable `metadata` in the server response type. These are versioned SDK contracts, not evidence of universal method availability or a newly mandatory request field. See [[source-github-stripe-node]].

## Stripe.js 10.0.0 Pay by Bank declaration

`@stripe/stripe-js@10.0.0` adds `confirmPayByBankPayment(clientSecret, data?, options?)`, returning `Promise<PaymentIntentResult>`. Data permits an existing PaymentMethod ID or new Pay by Bank data, with optional `return_url`; `handleActions: false` opts into merchant-managed authorization redirection. The method is declared on Stripe, but the new `CreatePaymentMethodPayByBankData` is not added to the standalone `CreatePaymentMethodData` union. Do not infer that every `createPaymentMethod({type: 'pay_by_bank'})` overload is now supported. These are declaration findings, not a newly launched payment method, eligibility or executed redirect/payment proof. Source: [[source-github-stripe-js]].

## Server SDK 23.0.0 Endive Boundary

`stripe@23.0.0` removes request `payment_method_types` from PaymentIntent create/update/confirm and SetupIntent create/update. The response field remains, and SetupIntent confirm is not included in that removal. Existing request `allowed_payment_method_types` adds `card_present` and `interac_present` enum values; do not mechanically rename every occurrence across APIs. PaymentIntent gains expandable `payment_record`, and BLIK gains off-session setup and mandate-expiration options. These are exact-version server contracts, not client confirmation support or payment-method eligibility. Source: [[source-github-stripe-node]].

The separate Endive REST changelog cited in [[source-stripe-payment-intents#Descriptor and metadata boundaries|the implementation guide]] says the linked `2026-09-30.endive` PaymentIntent Create endpoint rejects writable `payment_method_types` with HTTP 400 and `payment_method_types_no_longer_supported`. The stored property is read-only. Its Impact section also names `2026-08-26.preview`, leaving the first affected version unresolved.

## Related Concepts

- [[stripe-elements]] — Stripe Elements (UI component library used with Payment Intents)
- [[stripe-checkout]] — Stripe Checkout (Checkout Sessions API — recommended alternative)

## Sources

- [[source-stripe-api-tour]] — conceptual same-URL tour of PaymentIntent, PaymentMethod, Charge, and Event roles; its state sketch is simplified and its Charge/retry language is conditional.
- [[source-stripe-payment-intents]] — April and November 2026 combined reference for server creation and reuse, scoped client secrets, lifecycle and setup, and asynchronous capture. Async creation can leave Charge balance data unavailable even after confirmation and expansion. The sample response shape and creation default have separate version scopes.
- [[source-stripe-payment-methods]] — April and November Payment Methods API guides on pending orders, verified success for fulfillment, and possible later financial outcomes after PaymentIntent success
- [[source-stripe-payment-intents-quickstart]] — Full quickstart: server setup, Elements wiring, confirmPayment, return page, Stripe Tax, email receipts, off-session charging
- [[source-stripe-elements-advanced-payments]] — Checkout Sessions vs Payment Intents comparison matrix
- [[source-stripe-payment-element-design-integration]] — April 2026 Checkout Sessions and Payment Intents paths, including separate initialization and Intent creation/confirmation choices. The November capture is variant navigation.
- [[source-stripe-migrate-payment-methods-dashboard]] — Migrate to Dashboard payment methods: remove payment_method_types, Google Pay disabled by default, delayed notification PM list + webhook pattern
- [[source-stripe-payment-element-customize-payment-methods]] — April 21 versus November 7, 2026 PaymentIntent-create guide wording for manual method selection (`payment_method_types` versus `allowed_payment_method_types`), plus browser versus server card-filtering policy scope; read alongside the exact-version `stripe@23.0.0` request boundary above
- [[source-stripe-checkout-dynamic-amounts]] — April 21, 2026 full guide: PaymentIntents amount updates require trusted server calculation and client refresh; its wording says post-confirmation increases **generally** are not possible, without specifying exceptions. It separately documents Checkout Sessions `runServerUpdate`/server line-item changes and Session completion/expiry checks, which must not be applied as PaymentIntent fields. The November 7 capture is only a Checkout Sessions/Payment Intents variant index and does not verify current implementation or lifecycle behavior.
- [[source-stripe-email-receipts]] — April 22, 2026 advanced Payment Intents guide. It describes `receipt_email` as additional in that integration, and covers localization, updating receipt data through the Charge, and routing invoicing to Stripe Billing.
- [[source-stripe-receipts]] — May and November 2026 receipts overview with `Charge.receipt_url`, receipt link expiry, live successful-payment `receipt_email`, and dated PDF and test-email guidance.
- [[source-stripe-auth-and-capture]] — April and November 2026 guide to manual capture, Charge card expiry, eligible multicapture and method-specific windows. November adds private-preview timing controls and changes the mixed card/SEPA Direct Debit create example. See the separate versioned API and SDK evidence above.
- [[source-stripe-payment-element-migration]] — Migration guide: CardElement → PaymentElement, elements.submit() pattern, 11 Elements options, ConfirmationToken migration
- [[source-stripe-two-step-confirmation]] — Two-step web checkout: submit deferred Payment Element details, create a ConfirmationToken for review or validation, optionally calculate tax, create a server PaymentIntent, then confirm from the client. The 2026-11-07 guide adds scoped zero-amount US-bank microdeposit suppression and lists `allowedPaymentMethodTypes` where the 2026-05-11 table listed `paymentMethodTypes`; the source preserves the dated save-warning conflict and Account/Customer conditions.
- [[source-stripe-accept-payment-deferred]] — Deferred intent: retained 2026-05-11 guide covers payment, setup, and subscription modes; render Element before server-side Intent or Subscription creation, submit before branch-specific confirmation, and update displayed amounts when needed. The 2026-11-07 canonical capture is a variant index, not current implementation evidence.
- [[source-stripe-finalize-payments-server]] — Server-side confirmation: the retained 2026-05-11 web guide covers payment, setup, and subscription variants with ConfirmationToken and branch-specific Intent handling; its SDK minimums and limitations remain dated. The 2026-11-07 canonical capture supplies variant navigation only, not refreshed implementation behavior.
- [[source-github-stripe-js]] — package-qualified Stripe.js loader and declaration history through `@stripe/stripe-js@9.15.0`, including ConfirmationToken metadata typing
- [[source-stripe-payments-without-auth]] — Stripe's May and November 2026 guides describe a synchronous Card Element path for businesses accepting only US- or Canadian-issued cards. Use `error_on_requires_action` and handle immediate post-payment tasks after `succeeded` without a webhook in this path. Stripe recommends webhooks for the global integration.
- [[source-stripe-legacy-apis]] — April and November 2026 existing Charges migration, Charge read compatibility and the scoped November creation notice. Includes saved-method attachment, the create API fallback and historical Payment Request Button version limits. The separate same-URL Sources transition evidence distinguishes server-verified Intent outcomes, Checkout Session completion and retained Charge events.
- [[source-stripe-migrate-basic-card-integration]] — May and November 2026 guides to handling issuer-requested authentication in the basic card flow. With `confirmation_method=manual`, successful `handleCardAction` leaves `requires_confirmation`; re-confirm the same PaymentIntent on the server within one hour and verify payment success. See the source for dated request examples and sandbox qualifications.
