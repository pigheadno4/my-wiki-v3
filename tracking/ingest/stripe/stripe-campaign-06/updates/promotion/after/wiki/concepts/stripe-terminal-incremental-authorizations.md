---
title: "Stripe Terminal: Incremental Authorizations"
type: concept
category: technology
tags: [stripe, stripe-terminal, incremental-authorization, payment-intents, card-present]
---

## Definition

Incremental authorizations allow merchants to increase the authorized amount on a confirmed Terminal PaymentIntent before capture. The initial authorization is a card-present transaction; increments authorize the additional difference between the previous and new amounts.

## Availability

| Card brand | Eligible merchant categories |
| --- | --- |
| Visa | All |
| Mastercard | All |
| American Express | All |
| Discover | Transportation, hospitality, food service, car rental, recreation (restricted — see source for full list) |
| China UnionPay (November 2026 private preview) | Car rental and automobile rental agencies, hotels, motels, resorts and steamship or cruise lines. Selected Asia-Pacific and European markets. Request access through Stripe Sales. |

Additional restrictions:

- POS and reader must be **fully online** (no offline transactions)
- Maximum **10 attempts per payment**, including declines

Cardholder experience: depending on issuing bank, may see one authorization that increases in place, or separate pending authorizations for each increment. After capture, appears as a single charge.

## Integration Flow

For iOS `StripeTerminal@6.0.0`, SDK-side `PaymentIntentParametersBuilder` defaults to `.automaticAsync`. Explicitly choose `.setCaptureMethod(.manual)` for incremental authorization, as the retained versioned example does when that feature is selected. See [[source-github-stripe-terminal-ios]] and [[changelog-github-stripe-terminal-ios]].

For Android `stripeterminal@6.0.0`, the SDK builder defaults to `CaptureMethod.AutomaticAsync`; explicitly choose `CaptureMethod.Manual` for incremental authorization. The changed Java/Kotlin examples enforce this when incremental authorization is selected; eligibility and authoritative backend state still govern later capture. See [[source-github-stripe-terminal-android]] and [[changelog-github-stripe-terminal-android]].

### 1. Create PaymentIntent with incremental auth support

The November 2026 guide also requires explicit `captureMethod: 'manual'` for React Native SDK `0.0.1-beta.34` and later. The Swift and Kotlin creation snippets and the Swift confirmation setup omit the manual setting. Set it explicitly alongside the incremental authorization request flag. The Node example below is from the May 2026 capture. November’s server example uses `allowed_payment_method_types[]=card_present`. See [[stripe-payment-intents]] for the separate versioned Node request boundary.

```javascript
const paymentIntent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: 'usd',
  payment_method_types: ['card_present'],
  capture_method: 'manual',
  payment_method_options: {
    card_present: {
      request_incremental_authorization_support: true,
    },
  },
});
```

UI effect: reader shows `Pre-authorization` instead of `Total` on the payment screen.

### 2. Confirm and check eligibility

After confirming the PaymentIntent, inspect `payment_method_details.card_present.incremental_authorization_supported` on `latest_charge`. Eligibility depends on card network and merchant category at transaction time. In the May React Native example, collect and process use the PaymentIntent ID. November passes the object for collection, then uses `confirmPaymentIntent` with the collected object. The November confirmation example omits the incremental authorization request flag, which is part of the creation prerequisites.

### 3. Perform incremental authorization (server-side)

```javascript
const paymentIntent = await stripe.paymentIntents.incrementAuthorization(
  '{{PAYMENT_INTENT_ID}}',
  { amount: 1500 }  // new total, not the increment
);
```

Pass the new **total** amount — Stripe authorizes the **difference**. Can call multiple times up to the 10-attempt limit.

- **Success**: PaymentIntent updated with new amount
- **Failure**: `card_declined` error; PaymentIntent remains at original amount; other field updates not saved

### 4. Capture

```javascript
const paymentIntent = await stripe.paymentIntents.capture(
  '{{PAYMENT_INTENT_ID}}',
  { amount_to_capture: 2000 }
);
```

Capturing with `amount_to_capture` higher than the current authorized amount triggers an **automatic** incremental authorization attempt.

**Capture outcome.** If an automatic increment returns `card_declined`, the previous amount stays authorized and accompanying field updates are unsaved. Check for possible capture failures. For eligible on-receipt tips, overcapture skips the automatic increment. The November on-receipt guide requires checking the latest Charge’s `payment_method_details.card_present.overcapture_supported` and limits the excess to 50% of the authorized amount or USD 50, whichever is greater. See [[source-stripe-terminal-on-receipt-tipping]].

## Relationship to On-Receipt Tipping

On-receipt tipping uses **overcapture** (a separate mechanism) rather than incremental authorization. If overcapture is eligible, it takes precedence and the auto-increment behavior at capture does not apply. See [[stripe-terminal-tipping]] for details.

For online (non-Terminal) incremental authorization, see [[stripe-incremental-authorization]] — different availability rules and no auto-increment-at-capture behavior.

## Sources

- [[source-stripe-terminal-incremental-authorizations]] — May and November 2026 Terminal guides for payment eligibility, versioned manual capture setup, increment, and capture outcomes.
- [[source-stripe-terminal-on-receipt-tipping]] — mentions incremental auth as fallback when overcapture limits are exceeded
- [[stripe-terminal-extended-authorizations]] — related: extends the capture window (vs increasing the amount)
