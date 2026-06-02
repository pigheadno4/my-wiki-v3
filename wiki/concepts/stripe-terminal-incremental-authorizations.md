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

Additional restrictions:

- POS and reader must be **fully online** (no offline transactions)
- Maximum **10 attempts per payment**, including declines

Cardholder experience: depending on issuing bank, may see one authorization that increases in place, or separate pending authorizations for each increment. After capture, appears as a single charge.

## Integration Flow

### 1. Create PaymentIntent with incremental auth support

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

After confirming the PaymentIntent (collect + processPayment/confirmPaymentIntent), check `incremental_authorization_supported` on `latest_charge`. Not guaranteed even if requested — actual eligibility depends on card network and MCC at transaction time.

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

**Exception**: merchants eligible for on-receipt tipping (overcapture) — `amount_to_capture` above authorized amount does NOT trigger incremental auth; capture always succeeds (overcapture applies instead).

## Relationship to On-Receipt Tipping

On-receipt tipping uses **overcapture** (a separate mechanism) rather than incremental authorization. If overcapture is eligible, it takes precedence and the auto-increment behavior at capture does not apply. See [[stripe-terminal-tipping]] for details.

For online (non-Terminal) incremental authorization, see [[stripe-incremental-authorization]] — different availability rules and no auto-increment-at-capture behavior.

## Sources

- [[source-stripe-terminal-incremental-authorizations]] — primary source: availability table, setup flow, incrementAuthorization API, capture behavior
- [[source-stripe-terminal-on-receipt-tipping]] — mentions incremental auth as fallback when overcapture limits are exceeded
- [[stripe-terminal-extended-authorizations]] — related: extends the capture window (vs increasing the amount)
