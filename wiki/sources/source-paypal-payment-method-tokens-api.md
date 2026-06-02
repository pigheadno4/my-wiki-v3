---
title: "Save Payment Methods with the Payment Method Tokens API (docs.paypal.ai)"
type: source
date_ingested: 2026-04-17
original_format: webpage
raw_files:
  - "paypal-payment-method-tokens-api.md"
  - "paypal-payment-method-tokens-test.md"
tags: [paypal, vault, payment-tokens, setup-token, cards, paypal-wallet, 3d-secure, orders-api, billing-agreements, avs, cvv]
---

## Summary

Direct API integration guide for saving payment methods using **Payment Method Tokens API v3** (`/v3/vault/setup-tokens` → `/v3/vault/payment-tokens`). No JavaScript SDK required. Covers both cards and PayPal Wallet in one document. Same 35-country availability as JS SDK vault integration.

## Key differences: cards vs PayPal Wallet

| Dimension | Cards | PayPal Wallet |
| --- | --- | --- |
| Payer interaction | None required | Must approve billing agreement |
| PCI requirement | SAQ D | None |
| Verification methods | None / smart auth / 3DS | N/A |
| Setup token status | `PAYER_ACTION_REQUIRED` (3DS) or immediate | `PAYER_ACTION_REQUIRED` |

## Flow: setup token → payment token → order

1. `POST /v3/vault/setup-tokens` — create temporary token (expires 3 days)
2. For PayPal: redirect to `approve` HATEOAS link for billing agreement approval
3. For cards with 3DS: redirect to `approve` HATEOAS link for challenge
4. `POST /v3/vault/payment-tokens` with `{"payment_source": {"token": {"id": "SETUP_ID", "type": "SETUP_TOKEN"}}}` → permanent payment token
5. Use token: `payment_source.card.vault_id` in Orders API — no payer present needed

## HATEOAS links on setup token response

| Rel | Method | Cards | PayPal |
| --- | --- | --- | --- |
| `approve` | GET | 3DS only | All |
| `confirm` | POST | All verification methods | All |
| `self` | GET | All | All |

## Account enablement requirements

- Business account: **Account Settings** → **Payment Preferences** → **Save PayPal and Venmo payment methods** → **Get Started** → awaits PayPal review
- Developer Dashboard: **Apps & Credentials** → app → **Features** → **Vault** must be checked
- Migration from Billing Agreements API: must contact PayPal support first

## Card verification methods

- **No verification**: checks format only
- **Smart authorization**: zero/minimal-value auth to validate card is real
- **3D Secure** (`SCA_WHEN_REQUIRED` or `SCA_ALWAYS`): two-factor challenge

## Related pages

- [[paypal-vault]] — Vault concept page
- [[source-paypal-save-cards-payment-tokens-api]] — Cards-only Payment Method Tokens API (developer.paypal.com)
- [[source-paypal-save-paypal-payment-tokens-api]] — PayPal Wallet Payment Method Tokens API (developer.paypal.com)
- [[source-paypal-save-cards-js-sdk]] — JS SDK vault integration (card fields approach)

## Raw Sources

- [[paypal-payment-method-tokens-api]] — verbatim Payment Method Tokens API integration guide
- [[paypal-payment-method-tokens-test]] — Testing guide: 3 verification scenarios (no-verify/smart-auth/3DS) with request+response samples; AVS test table (21 address values); CVV test codes (6 values 115-130); 3DS eci_flag + pares_status in response
