---
title: "Stripe — Partial Authorization"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-partial-authorization-2026.md"
tags: [stripe, partial-authorization, capture, payment-intents, ic-plus, debit, prepaid]
---

## Summary

IC+ feature (requires contacting sales/support) allowing card issuers to approve a portion of the requested amount when the cardholder's available balance is insufficient. Used for debit/prepaid cards to allow customers to pay what's available and cover the remainder with another payment method.

## Availability

- IC+ pricing required; must contact sales/support to enable (not self-serve)
- Online card payments only: Visa, Mastercard, Discover, Amex
- Issuer and card type determine actual support at transaction time
- **AmEx (as of May 2024)**: debit/prepaid only; no recurring or cross-border
- **Visa**: must apply across card types

## Restrictions

- Overcapture cannot be used on partially authorized transactions
- Connect `transfer_amount` capped at partially authorized amount if set higher
- Stripe enforces minimum charge amount — declines if partial auth falls below minimum

## Status Field

`charge.payment_method_details.card.partial_authorization.status`:
- `partially_authorized` — issuer approved less than requested
- `fully_authorized` — issuer approved the full amount
- `declined` — issuer declined
- `not_requested` — feature wasn't requested

Also: `amount_requested` (original) and `amount_authorized` (approved) on the charge.

## Manual vs Auto-Capture

**Manual capture (recommended)**: set `request_partial_authorization: 'if_available'` + `capture_method: 'manual'`; allows reviewing partial amount before committing to capture.

**Auto-capture**: set `request_partial_authorization: 'if_available'` + `capture_method: 'automatic'`; automatically captures whatever was partially authorized — use with caution.

## Combining with Incremental Authorization

Can combine partial auth + incremental auth: pass `request_partial_authorization: 'if_available'` on the `increment_authorization` endpoint. The opt-in is retained from PI confirmation for subsequent increments unless explicitly set to `never`.

## Test Cards

| Number | Payment Method | Behavior |
| --- | --- | --- |
| 4000058400000071 | pm_card_debit_partialAuthorization | Authorizes 70% of amount (rounded down) when partial auth requested; otherwise declines with insufficient funds |
| 4000058400000816 | pm_card_debit_partialIncrement | Full auth initially; 70% for increments when partial auth requested; otherwise insufficient funds |

## Related Pages

- [[stripe-partial-authorization]] — concept page
- [[stripe-incremental-authorization]] — combinable with partial auth
- [[stripe-overcapture]] — cannot be used together with partial authorization

## Raw Sources

- [[stripe-partial-authorization-2026]] — verbatim partial authorization guide (296 lines)
