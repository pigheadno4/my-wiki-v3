---
title: "Stripe — Payments for Existing Customers"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-payments-existing-customers-2026.md"
tags: [stripe, checkout, saved-payment-methods, existing-customers, allow-redisplay, customer-session, elements]
---

## Summary

4 integration paths for showing saved payment methods to existing customers at checkout. Common rules govern `allow_redisplay`, prefill behavior, and key events.

## 4 Integration Paths

| Path | Parameter | UI mode |
| --- | --- | --- |
| Stripe-hosted Checkout | `customer`/`customer_account` | Default (redirect) |
| Embedded Checkout page | `customer`/`customer_account` | `ui_mode: 'embedded_page'` |
| Elements (Checkout Session) | `customer`/`customer_account` | `ui_mode: 'elements'` |
| Custom flow (Payment Element) | CustomerSession with `payment_method_redisplay` feature | Direct PI + CustomerSession |

## Common Rules

**`allow_redisplay`**: Default shows only `always`. Use `allow_redisplay_filters: ['always', 'limited', 'unspecified']` to show more. If filters specified, must include `always` to see those PMs.

**Apple Pay / Google Pay**: Cannot be reused in Checkout Session — must display fresh each time.

**Max saved cards shown**: 50.

**Prefill conditions**: payment or subscription mode only (not setup); card PMs only; 30-minute timeout after session creation.

**Prefill priority**: payment mode = newest card; subscription mode = default PM (if card) else newest.

**Allow remove**: `saved_payment_method_options[payment_method_remove]: 'enabled'`.

## Supported Saved PM Types (Custom Flow)

`card`, `link`, `us_bank_account`, `acss_debit`, `sepa_debit`, `bacs_debit`, `au_becs_debit`, `nz_bank_account`, `ideal`, `sofort`, `bancontact`.

## Key Events

`checkout.session.completed`, `checkout.session.async_payment_succeeded`, `checkout.session.async_payment_failed`.

## Related Pages

- [[stripe-saved-payment-methods]] — concept page (updated with existing customer flow)
- [[stripe-checkout]] — Stripe Checkout concept page

## Raw Sources

- [[stripe-payments-existing-customers-2026]] — verbatim existing customers payments guide (1616 lines, 2 screenshots)
