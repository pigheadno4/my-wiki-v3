---
title: "Stripe Terminal: Saving Payment Details"
type: concept
category: technology
tags: [stripe, stripe-terminal, saved-payment-methods, generated-card, off-session, card-fingerprint, compliance]
---

## Definition

Stripe Terminal can collect card-present payment methods and save them for future online reuse. Because card-present PaymentMethods can't be saved directly, Stripe creates a `generated_card` PaymentMethod representing the same card — usable for online charges, subscriptions, and off-session payments.

## How generated_card Works

1. Complete a Terminal PaymentIntent or SetupIntent with a card-present payment method
2. Stripe automatically creates a `generated_card` PaymentMethod linked to the same underlying card
3. Attach `generated_card` to a `Customer` (v1) or customer-configured `Account` (v2) — **required for reuse**
4. Charge the saved method via the standard PaymentIntents API (online, not Terminal SDK)

**If you attach `generated_card` only to a PaymentIntent without a Customer/Account, it cannot be reused.**

## Two Save Flows

- **Save directly** (without charging): use a SetupIntent to collect and vault card details without an initial payment
- **Save after payment**: save as part of a Terminal PaymentIntent — card is charged and saved in one flow

### Save Directly: SetupIntent Flow

**Card networks supported**: Visa, Mastercard, Amex, Discover, co-branded Interac/eftpos/girocard (must be inserted — Tap to Pay doesn't support co-branded Interac). Single-branded Interac, eftpos, girocard are NOT supported.

**`generated_card` is CNP**: all charges via `generated_card` are card-not-present — no liability shift, no card-present pricing applies.

**3-step flow**:

1. Create or retrieve a `Customer` (or customer-configured `Account` in Accounts v2)
2. Create a `SetupIntent` with `payment_method_types: ['card_present']`; optionally set `usage=on_session` if only reusing when customer is present
3. Collect payment method + confirm (combined in newer SDK versions)

**`allow_redisplay` required** (replaced legacy `customer_consent_collected`):

- `always` — payment method can be shown in any future checkout flow
- `limited` — restricted display (used automatically for saved mobile wallets)
- Mandatory since March 31, 2025 for non-React Native; Sept 30, 2025 for React Native

**SDK compatibility**:

| SDK | Compatible readers | Notes |
| --- | --- | --- |
| Server-driven | WisePOS E, S700/S710 only | Uses `process_setup_intent` API |
| JavaScript | All | Separate `collectSetupIntentPaymentMethod` + `confirmSetupIntent` calls |
| iOS 5.0.0+ | All | `processSetupIntent` combines collect + confirm |
| Android 5.0.0+ | All | `processSetupIntent` combines collect + confirm |
| React Native 0.0.1-beta.29+ | All | `processSetupIntent` available |

**Retrieving `generated_card`**: expand `latest_attempt` on the SetupIntent, or list Customer's `card` payment methods. `SetupIntent.payment_method` is the `card_present` PaymentMethod (not chargeable online) — the `generated_card` is a separate `card` PaymentMethod that attaches to the Customer automatically if Customer was provided during SetupIntent creation.

**Mobile wallets**: saved wallets get `allow_redisplay=limited`; must use `off_session=true` when charging; if customer is present in checkout flow, use Apple Pay / Google Pay integrations directly instead.

### Save After Payment: PaymentIntent Flow

Card is charged and saved in one in-person transaction. The initial payment is card-present; all subsequent `generated_card` charges are CNP (no liability shift, no card-present pricing).

**How it works**:

1. Create Customer or Accounts v2 customer-configured Account
2. Create PaymentIntent with `setup_future_usage: 'off_session'` (or `'on_session'`) to request a `generated_card`
3. Collect payment with `allow_redisplay: 'always'` or `'limited'` passed at collect time
4. Retrieve `generated_card` by expanding `latest_charge` → `payment_method_details.card_present.generated_card`; auto-attaches to Customer if Customer ID was provided at PaymentIntent creation

**Server-driven options**: `process_payment_intent` (one-step) or `collect_payment_method` + `confirm_payment_intent` (two-step — gives access to card brand/funding before confirming).

**SDK minimums**: iOS SDK v4.3.0+, Android SDK v4.0.0+.

**When `generated_card` is absent**: digital wallets and single-branded Interac/eftpos/girocard don't produce one. Fallback: prompt customer to use the save-directly (SetupIntent) flow, or refund and restart with a different card.

## Charging a Saved PaymentMethod

- Set `off_session: true` when charging outside the checkout flow — causes PaymentIntent to error if customer authentication is required
- **Terminal SDK methods cannot process `generated_card` payments** — these are online payments processed via the Stripe API directly

```javascript
// Accounts v2
const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ['card'],
  amount: 1099,
  currency: 'sgd',
  customer_account: '{{CUSTOMER_ACCOUNT_ID}}',
  payment_method: '{{PAYMENT_METHOD_ID}}',
});

// Customers v1
const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ['card'],
  amount: 1099,
  currency: 'sgd',
  customer: '{{CUSTOMER_ID}}',
  payment_method: '{{PAYMENT_METHOD_ID}}',
});
```

## Card Fingerprints

`card_present` PaymentMethods have a `fingerprint` attribute — same as `card` PaymentMethods — uniquely identifying the card number. Use to correlate in-person and online transactions by the same customer.

- **Mobile wallets** (Apple Pay, Google Pay): fingerprint differs from the underlying card's online fingerprint
- **Connect**: since API v2018-01-23, fingerprints are uniform across all connected accounts — usable for cross-account card lookups

## Compliance

When saving card details in-person, merchants must:

- State in checkout terms how payment details will be saved and allow customer opt-in
- For off-session charging, terms must cover: payment initiation authority, timing/frequency, amount determination, and cancellation policy (for subscriptions)
- Keep written records of customer agreement
- Only use saved methods for the purpose stated in terms
- If combining off-session charging with saving for future checkout display: collect explicit consent (e.g., checkbox)

## Sources

- [[source-stripe-terminal-save-payment-details]] — overview: generated_card mechanism, off-session, fingerprints, compliance
- [[source-stripe-terminal-save-directly]] — SetupIntent flow detail: CNP caveat, card networks, allow_redisplay, SDK compatibility matrix, mobile wallet caveats
- [[source-stripe-terminal-save-after-payment]] — Save after payment: setup_future_usage, allow_redisplay at collect time, generated_card retrieval, fallback when absent, SDK notes
