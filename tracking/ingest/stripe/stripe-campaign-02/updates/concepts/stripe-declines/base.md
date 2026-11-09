---
title: "Stripe Declines"
type: concept
category: technology
tags: [stripe, declines, card-declines, radar, fraud, issuer-declines, adaptive-acceptance, payment-failure, outcome, network-codes, retries]
---

## Overview

Stripe surfaces three types of payment failure, each requiring different handling. The key API field is the `Charge.outcome` object, which identifies the failure type and reason regardless of the payment method.

## Three Failure Types

| Type | `outcome.type` | `network_status` | Who decides |
| --- | --- | --- | --- |
| Issuer decline | `issuer_declined` | `declined_by_network` | Card issuer / payment provider |
| Blocked payment | `blocked` | `not_sent_to_network` | Stripe Radar or Adaptive Acceptance |
| Invalid API call | `invalid` | `not_sent_to_network` | Stripe (malformed request) |

Non-card payment methods use the same decline structure and response codes.

## The `outcome` Object

Fields on `Charge.outcome`:

| Field | Description |
| --- | --- |
| `type` | `issuer_declined`, `blocked`, or `invalid` |
| `network_status` | `declined_by_network` or `not_sent_to_network` |
| `reason` | Specific reason (e.g. `expired_card`, `highest_risk_level`) |
| `advice_code` | What to do next (e.g. `do_not_try_again`, `confirm_card_data`) |
| `network_decline_code` | Raw network code (e.g. `"54"` = expired card) |
| `network_advice_code` | Network-level advice |
| `risk_level` | `normal`, `elevated`, or `highest` |
| `seller_message` | Human-readable explanation |

## Issuer Declines

The card issuer's systems evaluate spending habits, balance, card data (expiry, address, CVC) and decline if criteria aren't met. Stripe surfaces the result as a [Stripe decline code](https://docs.stripe.com/declines/codes) and optionally a [network decline code](https://docs.stripe.com/declines/network-codes).

**Most common card decline causes**: insufficient funds, incorrect card data, suspected fraud. Most declines come back as `generic_decline` — the exact reason is opaque, and card issuers only discuss specifics with their cardholders.

### Network Codes

Two codes accompany every card decline (null if the network doesn't return one):

| Field | Description |
| --- | --- |
| `network_decline_code` | 2-4 digit bank code; meaning differs by card brand |
| `network_advice_code` | 2-4 digit bank code for managing the decline; Mastercard calls this MAC (Merchant Advice Code) |

### `advice_code` and Retry Behavior

| `advice_code` | Meaning | Action |
| --- | --- | --- |
| `do_not_try_again` | Don't retry this card for this transaction | See decline code; customer may need to call issuer |
| `try_again_later` | Temporary decline; retry permitted | Ask customer to try again |
| `confirm_card_data` | Some card data is wrong | Customer must verify card info |

**Max 8 retries** recommended — excessive retries signal fraud to issuers.

### Reducing Card Declines

- Collect CVC + postal code at checkout
- Implement [[stripe-3d-secure]] in supported countries
- For `generic_decline`/`do_not_honor`: check CVC and AVS results
- FSA/HSA cards restricted to eligible merchant categories
- Cross-country IP/card mismatch → geographic decline; customer contacts issuer
- Global customer base → consider local Stripe accounts per region

### Programmatic Handling

- `PaymentIntent.last_payment_error.decline_code` — specific decline reason
- Iterate attempted charges → inspect `failure_message`
- Webhook `payment_intent.payment_failed` → monitor failed attempts

**On-session**: prompt customer to retry or use a different payment method.
**Off-session**: notify customer to return and update payment method; SCA may require `authentication_required` handling.

```json
outcome: {
  network_decline_code: "54",
  network_status: "declined_by_network",
  reason: "expired_card",
  advice_code: "confirm_card_data",
  type: "issuer_declined"
}
```

## Blocked Payments

Stripe Radar blocks payments before sending to the network — no authorization is attempted and no funds are held (though some card types may briefly show a pending authorization that resolves within a few days).

**Blocked by Radar rule or high risk score:**

```json
outcome: {
  network_status: "not_sent_to_network",
  reason: "highest_risk_level",
  advice_code: "do_not_try_again",
  risk_level: "highest",
  type: "blocked"
}
```

**Blocked by Adaptive Acceptance** (IC+ pricing only — avoids excessive retry penalties and low-probability network costs):

```json
outcome: {
  network_status: "not_sent_to_network",
  reason: "low_probability_of_authorization",
  advice_code: "do_not_try_again",
  risk_level: "normal",
  type: "blocked"
}
```

**Allow list**: To unblock a legitimate payment, find it in the Dashboard and click **Add to allow list**. This overrides all matching Radar rules for future attempts — it does not retry the current payment.

## Invalid API Calls

Malformed API calls (wrong CVC, invalid card number, bad parameters) produce a `card_error` with `outcome.type = "invalid"`. These usually don't appear in the Dashboard.

```json
{
  "error": {
    "code": "incorrect_cvc",
    "message": "Your card's security code is incorrect.",
    "type": "card_error"
  }
}
```

## Network Decline Codes

Raw bank/network codes (e.g. ACH `R01`, SEPA `MD01`) map to Stripe decline codes. Full tables in [[source-stripe-network-decline-codes]].

**Payment methods with network code tables**: ACH Direct Debit, Australia BECS, Bacs (ADDACS/ARUDD/AUDDIS), Cash App Pay, NZ BECS, Canadian PAD, SEPA Direct Debit.

Common patterns across all bank debit methods: `debit_not_authorized` (missing mandate), `recipient_deceased`, `insufficient_funds`, `account_closed`, `refer_to_customer`.

## Decline Codes Reference

Stripe uses its own decline codes that expand on raw issuer codes. Full list in [[source-stripe-decline-codes]].

**Codes to mask from customers** (show as `generic_decline`): `fraudulent`, `lost_card`, `stolen_card`, `merchant_blacklist`

**Deprecated codes** (now `advice_code` values): `do_not_try_again`, `try_again_later`

**LPM-specific codes** (19 total, not on cards): `compliance_violation`, `payment_disputed`, `partner_high_risk_customer`, `recurring_not_supported_by_bank`, etc. — see [[source-stripe-decline-codes]] for full table.

## Related Concepts

- [[stripe-authorization-boost]] — Adaptive Acceptance and network token strategies to reduce issuer declines
- [[stripe-3d-secure]] — 3DS authentication to pre-validate high-risk payments
- [[disputes]] — what happens after a disputed charge

## Sources

- [[source-stripe-declines-overview]] — Stripe declines overview page
