---
title: "Stripe Declines Overview"
type: source
date_ingested: 2026-05-09
original_format: webpage
raw_files:
  - "stripe-declines-2026.md"
tags: [stripe, declines, radar, fraud, issuer-declines, adaptive-acceptance, payment-failure]
---

## Summary

Overview of the three types of payment failures in Stripe and how to handle each. Covers the `outcome` API object, Stripe Radar blocking behavior, and Adaptive Acceptance.

## Three Types of Payment Failure

| Type | `outcome.type` | `network_status` | Who decides |
|---|---|---|---|
| Issuer decline | `issuer_declined` | `declined_by_network` | Card issuer/payment provider |
| Blocked payment | `blocked` | `not_sent_to_network` | Stripe Radar or Adaptive Acceptance |
| Invalid API call | `invalid` | `not_sent_to_network` | Stripe (malformed request) |

## The `outcome` Object

Key fields on the `Charge.outcome` attribute:

- `type` — failure category: `issuer_declined`, `blocked`, `invalid`
- `network_status` — `declined_by_network` or `not_sent_to_network`
- `reason` — e.g. `expired_card`, `highest_risk_level`, `low_probability_of_authorization`
- `advice_code` — e.g. `do_not_try_again`, `confirm_card_data`
- `network_decline_code` — raw code from card network (e.g. `"54"` for expired)
- `network_advice_code` — network-level advice code
- `risk_level` — `normal`, `elevated`, `highest`
- `seller_message` — human-readable explanation

## Issuer Declines

Issuer's automated systems analyze spending habits, account balance, card data (expiry, address, CVC). Stripe surfaces the decline as a [Stripe decline code](https://docs.stripe.com/declines/codes) and (when provided) a [network decline code](https://docs.stripe.com/declines/network-codes).

```json
outcome: {
  network_decline_code: "54",
  network_status: "declined_by_network",
  reason: "expired_card",
  advice_code: "confirm_card_data",
  type: "issuer_declined"
}
```

## Blocked Payments (Stripe Radar)

Stripe Radar blocks high-risk payments before sending to the network — no authorization attempt is made. Two block reasons:

**High risk (Radar rule or score):**
```json
outcome: {
  network_status: "not_sent_to_network",
  reason: "highest_risk_level",
  advice_code: "do_not_try_again",
  risk_level: "highest",
  type: "blocked"
}
```

**Low authorization probability (Adaptive Acceptance, IC+ only):**
```json
outcome: {
  network_status: "not_sent_to_network",
  reason: "low_probability_of_authorization",
  advice_code: "do_not_try_again",
  risk_level: "normal",
  type: "blocked"
}
```

**Allow list**: If a Radar-blocked payment is legitimate, add it to the allow list via Dashboard → overrides all matching rules for future attempts (does not retry the blocked payment).

## Invalid API Calls

Malformed or invalid API calls (wrong CVC, bad card number, etc.) generate a `card_error` response. These typically don't appear in the Dashboard. The `outcome.type` is `invalid`.

## Related Pages

- [[stripe-declines]] — concept page
- [[stripe-authorization-boost]] — Adaptive Acceptance detail
- [[stripe-3d-secure]] — authentication to reduce issuer declines
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-declines-2026]] — verbatim Stripe declines overview page
