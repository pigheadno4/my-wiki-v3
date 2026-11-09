---
title: "Stripe Decline Codes"
type: source
date_ingested: 2026-05-09
original_format: webpage
raw_files:
  - "stripe-decline-codes-2026.md"
tags: [stripe, declines, decline-codes, card-declines, lpm, radar, authentication-required, fraud]
---

## Summary

Complete reference table of Stripe decline codes for card payments (50 codes) and Local Payment Methods (19 codes). Stripe's decline codes expand on raw issuer codes with more specific reasons and next steps.

## Card Decline Codes (50 total)

See raw file for complete table. Key groupings:

**Authentication:**
- `authentication_required` — needs 3DS; Stripe frontends auto-trigger auth flow; off-session needs customer retry
- `authentication_not_handled` — 3DS/SCA flow was skipped; run it before retrying

**Card data errors** (customer can fix):
- `incorrect_cvc` / `invalid_cvc`, `incorrect_number` / `invalid_number`, `incorrect_zip`, `incorrect_address`, `incorrect_pin` / `invalid_pin`
- `invalid_expiry_month`, `invalid_expiry_year`, `expired_card`

**Issuer decisions** (opaque to merchant):
- `generic_decline`, `do_not_honor`, `call_issuer`, `no_action_taken`, `not_permitted`, `transaction_not_allowed` — all route to "contact card issuer"
- `card_velocity_exceeded`, `withdrawal_count_limit_exceeded` — spending/limit exceeded
- `insufficient_funds` — use alternative payment method
- `card_not_supported`, `currency_not_supported` — card type/currency mismatch

**Fraud / security (mask from customer — show as `generic_decline`):**
- `fraudulent` — Stripe suspects fraud
- `lost_card` — present as `generic_decline`
- `stolen_card` — present as `generic_decline`
- `merchant_blacklist` — payment matches block list; present as `generic_decline`

**PIN / card reader only:**
- `offline_pin_required`, `online_or_offline_pin_required`, `pin_try_exceeded`, `mobile_device_authentication_required`

**Other:**
- `duplicate_transaction` — identical amount + card submitted recently; check for recent payment
- `processing_error` / `reenter_transaction` / `issuer_not_available` — retry
- `testmode_decline` — test card used in live mode
- `pickup_card`, `restricted_card` — contact issuer

**Deprecated** (now `advice_code` values, not decline codes):
- `do_not_try_again`, `try_again_later`

## LPM Decline Codes (19 total)

LPM codes have 4 columns: decline code, `charge.outcome.reason`, seller message, API error message.

| Decline code | Notes |
| --- | --- |
| `partner_generic_decline` | Generic LPM decline |
| `invalid_customer_account` | Customer must fix account issue |
| `payment_limit_exceeded` | Over customer account limit |
| `invalid_billing_agreement` | Retries won't succeed |
| `expired_card` | Card registered with LPM expired |
| `processing_error` | Partner processing error |
| `insufficient_funds` | Customer has insufficient funds |
| `currency_not_supported` | Retries won't succeed |
| `invalid_amount` | Retries won't succeed |
| `invalid_business_account` | Business account deactivated |
| `partner_high_risk_customer` | Customer flagged by partner |
| `compliance_violation` | ToS/program rules/laws violation; retries won't succeed |
| `payment_disputed` | Active dispute; retry if resolved in merchant's favor |
| `invalid_authorization` | Auth invalid or revoked; retries won't succeed |
| `invalid_payment_information` | Retries won't succeed |
| `partner_payment_not_found` | Payment not found by provider |
| `expired_payment_information` | Customer must update payment info |
| `duplicate_transaction` | Identical recent transaction |
| `recurring_not_supported_by_bank` | Customer must switch to a bank that supports recurring |

## Related Pages

- [[stripe-declines]] — concept page (updated with decline code reference)
- [[source-stripe-card-declines]] — card decline handling guide
- [[source-stripe-declines-overview]] — top-level declines overview

## Raw Sources

- [[stripe-decline-codes-2026]] — verbatim Stripe decline codes reference page
