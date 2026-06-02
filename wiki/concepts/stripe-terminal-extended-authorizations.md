---
title: "Stripe Terminal: Extended Authorizations"
type: concept
category: technology
tags: [stripe, stripe-terminal, extended-authorization, payment-intents, card-present]
---

## Definition

Extended authorizations allow merchants to capture a confirmed Terminal PaymentIntent beyond the standard window (48 hours for most cards, 5 days for Visa), up to 30 days depending on card brand and merchant category.

**Canonical use case**: a hotel authorizes in full at check-in, captures at check-out.

## Availability

Available on Visa, Mastercard, Amex, and Discover. **Not available** on single-message payment methods (Interac, eftpos).

| Card brand | Eligible merchant categories | Window |
| --- | --- | --- |
| Visa | Hotel, lodging, vehicle rental, cruise line | 30 days (actual: 29d 18h, to allow clearing) |
| Visa | Aircraft/bicycle/boat/clothing/DVD/equipment/furniture/motor home/motorcycle rental, trailer parks & campgrounds | 10 days (actual: 9d 18h) |
| Mastercard (excl. Maestro/Cirrus) | All | 30 days |
| American Express | Lodging and vehicle rental | 30 days* |
| Discover | Airline, bus/tour, car rental, cruise, local transport (incl. ferries), hotel, lodging, passenger railway | 30 days |

\* Amex: must capture by end of customer's stay or rental period even if within 30 days.

## Integration

Set at PaymentIntent creation:

```javascript
const paymentIntent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: 'usd',
  payment_method_types: ['card_present'],
  capture_method: 'manual',
  payment_method_options: {
    card_present: {
      request_extended_authorization: true,
    },
  },
});
```

## Determining the Validity Window

After confirming the PaymentIntent, check `capture_before` on the Charge object — it gives the exact expiry timestamp. Always use this field rather than relying on card brand rules, which can change without notice.

If not captured by `capture_before`: the authorization expires, funds are released, and the PaymentIntent transitions to `canceled`.

## Relationship to Incremental Authorizations

- **Extended authorizations**: extend *when* you can capture (more time)
- **Incremental authorizations**: increase *how much* you can capture (higher amount)

Both require `capture_method: manual`. See [[stripe-terminal-incremental-authorizations]].

For online (non-Terminal) extended authorizations, see [[stripe-extended-authorization]] — different network availability rules apply.

## Sources

- [[source-stripe-terminal-extended-authorizations]] — primary source: availability table, setup, capture_before field behavior
