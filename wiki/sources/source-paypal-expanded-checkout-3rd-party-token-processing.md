---
title: "PayPal Expanded Checkout: Third-Party Network Token Processing"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-expanded-checkout-3rd-party-token-processing.md"
tags: [paypal, expanded-checkout, network-token, tokenization, tsp, eci, card-on-file, orders-api, bin-details]
---

## PayPal Expanded Checkout: Third-Party Network Token Processing

Integration guide for processing payments using network tokens created outside of PayPal (by the merchant, partner, or a third-party Token Service Provider). Covers the `network_token` object, ECI flag mapping, and test cards.

Source URL: <https://developer.paypal.com/docs/checkout/advanced/3rd-party-token-processing/>

Last updated: 2025-05-30

## Key Takeaways

### What it is

Third-party network token processing lets PayPal process a payment using a token that **PayPal did not create** — the token was created and stored by the merchant, partner, or an external Token Service Provider (TSP). PayPal treats it like a regular card payment.

Contrast with PayPal vault tokens (`payment_source.token.id`) which are PayPal-created and stored.

### Availability

32 countries including US, CA, AU, UK, and most of EU. Full list in raw file.

### Key constraints

- Requires **Expanded Checkout** integration
- **No reference or future transactions** — do not use `payment_source.token.id` with third-party tokens
- Tokens are **not stored by PayPal** — cannot be created, mapped, unmapped, or validated against PAN
- Merchant is **solely liable** for any third-party vaulting functionality

### API: `network_token` object

Passed under `payment_source.card.network_token`:

| Field | Required | Description |
| ----- | -------- | ----------- |
| `number` | Yes | Network token number (replaces PAN) |
| `expiry` | Yes | Token expiration date |
| `cryptogram` | Yes (CIT) / Optional (MIT) | Cryptogram from TSP |
| `eci_flag` | Yes (CIT) / Optional (MIT) | ECI string (see mapping below) |
| `token_requestor_id` | No | TSP-assigned ID |

### ECI flag mapping

TSPs provide a 2-digit numeric ECI code — must be converted to the string PayPal expects:

| Numeric ECI | String value |
| ----------- | ------------ |
| `00` | `MASTERCARD_NON_3D_SECURE_TRANSACTION` |
| `07` | `NON_3D_SECURE_TRANSACTION` |

### Combined with `stored_credential`

For merchant-initiated charges using third-party tokens, also pass `stored_credential`:

```json
"stored_credential": {
  "payment_initiator": "MERCHANT",
  "payment_type": "UNSCHEDULED",
  "usage": "SUBSEQUENT",
  "previous_network_transaction_reference": {
    "id": "NETWORK-TRANSACTION-REFERENCE-ID",
    "network": "VISA"
  }
}
```

### Response additions

Two extra objects appear in the response vs a standard card payment:

| Object | Location | Contents |
| ------ | -------- | -------- |
| `bin_details` | `payment_source.card` | `issuing_bank`, `bin_country_code`, `products` |
| `network_transaction_reference` | `captures[]` | `id` + `network` — save for future `stored_credential` |

> [!info] Visa capture response
> The Visa network does **not** return an expiration date in the capture response — unlike Mastercard.

### Test cards (sandbox)

All share the same cryptogram: `ApIPtIgAMyrMgTx1RSnAMAACAAA=`

| Brand | Test card number |
| ----- | ---------------- |
| Visa | 4034772286582057 / 4556871409493313 |
| Mastercard | 5530238208956601 / 5419720028804901 |
| Amex | 379015087078375 |
| Discover | 6011390662682995 |

ECI flag: `MASTERCARD_NON_3D_SECURE_TRANSACTION` for Mastercard; `NON_3D_SECURE_TRANSACTION` for all others.

## Raw Sources

- [[paypal-expanded-checkout-3rd-party-token-processing]] — verbatim webpage content with full create order + capture request/response samples and test card table

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-expanded-checkout]] — Expanded Checkout concept page
- [[paypal-vault]] — PayPal-native vault tokens (contrast: PayPal creates and stores the token)
- [[source-paypal-expanded-checkout-sca-payment-indicators]] — stored_credential reference (used alongside network_token for MIT flows)
- [[source-paypal-expanded-checkout-customize-overview]] — full customization catalog
