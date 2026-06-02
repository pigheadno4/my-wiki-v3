---
title: "PayPal Expanded Checkout: Real-Time Account Updater (RTAU)"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-expanded-checkout-rtau.md"
tags: [paypal, expanded-checkout, rtau, real-time-account-updater, vault, recurring-payments, card-on-file, mastercard, visa]
---

## PayPal Expanded Checkout: Real-Time Account Updater (RTAU)

Integration guide for PayPal's Real-Time Account Updater — automatically recovers declined card-on-file payments by fetching updated card info from Mastercard/Visa before retrying.

Source URL: <https://developer.paypal.com/docs/checkout/advanced/customize/rtau/>

Last updated: 2025-03-11

## Key Takeaways

### What it is

RTAU intercepts declined card-on-file payments, queries the card network for updated card details, and retries the payment — all transparently. Only applies to **vaulted/saved cards** (payment tokens); not applicable to Apple Pay, Google Pay, or Samsung Pay.

### Eligibility

- Limited early access program
- Requires **both**: Advanced credit and debit card payments (Expanded Checkout) + Save payment methods (vault)
- Only triggers on **subsequent payments** using a card on file — not first-time card entries
- Issuers/cardholders can opt out; no guarantee of update even for eligible cards

### Supported networks and countries

| Network | Card types | Issuing countries (partial) | Merchant countries (partial) |
| ------- | ---------- | -------------------------- | --------------------------- |
| Mastercard | Credit + debit | 33 countries (major EU, US, CA, AU) | 34 countries (+ CN) |
| Visa | Credit + debit | 35 countries (major EU, US, AU, HK, SG) | 33 countries (+ CN) |

Notable difference: Visa issuing includes **HK, SG, CH**; Mastercard issuing includes **LI**. Full country tables in raw file.

### Mastercard flow (reactive — decline then update)

1. Payment submitted → Mastercard sends to issuer → issuer declines (expired/cancelled/changed card)
2. Mastercard notifies PayPal of decline
3. PayPal checks RTAU eligibility → requests updated card from Mastercard
4. Mastercard returns updated card info
5. PayPal resubmits payment with updated card
6. PayPal returns updated info to merchant; updates vault token if applicable

### Visa flow (proactive — flag before decline)

1. Payment submitted → PayPal flags for Visa to check updates
2. Visa checks for card updates before sending to issuer
3. If update available: Visa submits with updated card → returns updated info to PayPal
4. If no update available: Visa submits with original card → issuer approves or declines normally
5. PayPal returns updated info to merchant; updates vault token if applicable

Key difference: **Mastercard is reactive** (update happens after decline); **Visa is proactive** (update happens before issuer attempt).

### API response fields added by RTAU

Token-based payment responses include two additional fields in the `card` object:

| Field | Description |
| ----- | ----------- |
| `expiry` | New expiration date used for payment (e.g. `"2040-12"`) |
| `last_digits` | Last 4 digits of the card number used (reflects new PAN if card was replaced) |

These fields reflect the **actual card used**, which may differ from the stored token's original values. PayPal also updates the vault token automatically.

### 3 card change scenarios

| Scenario | Result |
| -------- | ------ |
| **Expired token** | Payment succeeds; response has updated `expiry` (same `last_digits`) |
| **Updated token** (card replaced) | Payment succeeds; response has new `expiry` and new `last_digits` |
| **Closed token** (card closed by issuer) | HTTP 422 `CARD_CLOSED` error — no recovery possible |

### `CARD_CLOSED` error

```json
{
  "issue": "CARD_CLOSED",
  "description": "The card is closed."
}
```

HTTP 422 `UNPROCESSABLE_ENTITY` — the card account is permanently closed, updater cannot provide new info. Must request new card from cardholder.

### Tip: detect RTAU updates

Before submitting `POST /v2/checkout/orders`, call `GET /v3/vault/payment-tokens/{id}` to get the stored `expiry`/`last_digits`. Compare those values to the ones in the capture response — if they differ, RTAU updated the card.

## Raw Sources

- [[paypal-expanded-checkout-rtau]] — verbatim webpage content with Mastercard/Visa flow diagrams, full country tables, 3 sample request/response scenarios

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-expanded-checkout]] — Expanded Checkout concept page
- [[paypal-vault]] — vault/payment tokens (RTAU updates vaulted tokens automatically)
- [[recurring-payments]] — recurring payments (primary RTAU use case)
- [[source-paypal-expanded-checkout-customize-overview]] — full customization catalog (14 features)
