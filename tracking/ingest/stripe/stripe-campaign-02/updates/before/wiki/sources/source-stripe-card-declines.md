---
title: "Stripe Card Declines"
type: source
date_ingested: 2026-05-09
original_format: webpage
raw_files:
  - "stripe-card-declines-2026.md"
tags: [stripe, declines, card-declines, radar, network-codes, retries, on-session, off-session, advice-code]
---

## Summary

Detailed guide on card-specific declines: common causes, network codes, retry strategy, programmatic handling, and on-session vs off-session scenarios.

## Common Decline Causes

- **Insufficient funds** — suggest BNPL as alternative
- **Incorrect card data** — ask customer to re-enter; check CVC + postal code
- **Suspected fraud** — customer must call issuer to confirm identity

Most declines return `generic_decline` — exact reason is opaque. Card issuers only discuss specifics with their cardholders.

## Network Codes

Two codes accompany every decline (null if network doesn't return one):

| Field | Description |
|---|---|
| `network_decline_code` | 2-4 digit bank code; meaning differs by card brand |
| `network_advice_code` | 2-4 digit bank code; guidance on managing the decline. Mastercard calls this MAC (Merchant Advice Code) |

## `advice_code` Values and Retry Behavior

| `advice_code` | Meaning | Next steps |
|---|---|---|
| `do_not_try_again` | Don't retry this card for this transaction | See decline code; customer may need to call issuer |
| `try_again_later` | Temporary decline; retry permitted | Ask customer to try again |
| `confirm_card_data` | Some card data is wrong | Customer must verify card info |

**Max 8 retries** recommended — excess retries can be flagged as fraud by issuers.

## Reducing Declines

- Collect CVC + postal code (reduces fraud-based declines)
- Implement [3D Secure](https://docs.stripe.com/payments/3d-secure) to lower declines in supported countries
- For `generic_decline` / `do_not_honor`: examine CVC and AVS check results
- Cross-country IP/card mismatch → likely legitimate geographic decline; customer contacts issuer
- FSA/HSA cards restricted to eligible merchant categories — customer must call issuer
- Global customer base → consider local Stripe accounts per region

## Programmatic Handling

- `PaymentIntent.last_payment_error.decline_code` — why the issuer declined
- Iterate `PaymentIntent` attempted charges → inspect `failure_message`
- Webhook `payment_intent.payment_failed` → monitor failed attempts

### On-session vs Off-session

| Scenario | Handling |
|---|---|
| On-session | Prompt customer to retry or use different payment method |
| Off-session | Notify customer (email/push) to return and update payment method; SCA may require `authentication_required` handling |

## Related Pages

- [[stripe-declines]] — concept page (updated with card-specific details)
- [[stripe-3d-secure]] — 3DS to reduce issuer declines
- [[source-stripe-declines-overview]] — parent declines overview

## Raw Sources

- [[stripe-card-declines-2026]] — verbatim Stripe card declines page
