---
title: "PayPal Expanded Checkout: Card Decline Errors"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-expanded-checkout-card-decline-errors.md"
tags: [paypal, expanded-checkout, card-decline, avs, cvv, processor-response, orders-api, maestro, error-codes]
---

## PayPal Expanded Checkout: Card Decline Errors

Reference tables for AVS and CVV error codes returned in the `processor_response` object of the Orders v2 API capture response. Covers Visa/Mastercard/Discover/Amex (alphabetical codes) and Maestro (numeric codes).

Source URL: <https://developer.paypal.com/docs/checkout/advanced/card-decline-errors/>

Last updated: 2025-05-14

## Key Takeaways

### Where these codes appear

In the Orders v2 API capture response under `processor_response`:

```json
"processor_response": {
  "avs_code": "Y",
  "cvv_code": "M",
  "response_code": "0000"
}
```

### Two code systems

| Network | Code format |
| ------- | ----------- |
| Visa, Mastercard, Discover, Amex | Alphabetical (`A`–`Z`) |
| Maestro | Numeric (`0`–`4`) |

### AVS codes — Visa/Mastercard/Discover/Amex

| Code | Meaning | Match |
| ---- | ------- | ----- |
| `Y` | Yes | Address + 5-digit ZIP ✓ |
| `X` | Exact match | Address + 9-digit ZIP ✓ |
| `M` | Address | Address + Postal Code ✓ |
| `D` / `F` | International X / UK X | Address + Postal Code ✓ |
| `A` / `B` | Address only | Address only (no ZIP) |
| `W` | Whole ZIP | 9-digit ZIP only |
| `Z` | ZIP | 5-digit ZIP only |
| `P` | Postal | Postal code only |
| `N` | No | None — **transaction declined** |
| `C` | International N | None — **transaction declined** |
| `E` | MOTO not allowed | N/A — **transaction declined** |
| `G` / `I` | Global/International unavailable | N/A |
| `R` | Retry | N/A |
| `S` | Service not supported | N/A |
| `U` | Unavailable | N/A |

### CVV codes — Visa/Mastercard/Discover/Amex

| Code | Meaning |
| ---- | ------- |
| `M` | Match ✓ |
| `N` | No match |
| `E` | Error / unrecognized |
| `I` | Invalid or null |
| `P` | Not processed |
| `S` | Service not supported |
| `U` | Unknown (issuer not certified) |
| `X` | No response |

### Maestro AVS codes (numeric)

| Code | Meaning |
| ---- | ------- |
| `0` | All address info matched ✓ |
| `1` | None matched — **transaction declined** |
| `2` | Partial match |
| `3` | Not provided / not processed |
| `4` or `U` | Not checked / service unavailable |
| Null | No AVS response obtained |

### Maestro CVV codes (numeric)

| Code | Meaning |
| ---- | ------- |
| `0` | Matched ✓ |
| `1` | No match |
| `2` | Merchant hasn't implemented CVV2 handling |
| `3` | CVV2 not present on card |
| `4` or `X` | Service not available |

### Codes that always decline

- AVS `N` (no match), `C` (international N), `E` (MOTO not allowed)
- Maestro AVS `1` (none matched)
- CVV `N` (no match) does not itself force a decline in all cases — the issuer may still approve

## Raw Sources

- [[paypal-expanded-checkout-card-decline-errors]] — verbatim webpage content with full AVS and CVV tables for both code systems

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-expanded-checkout]] — Expanded Checkout concept page
- [[source-paypal-checkout-handle-errors]] — general error handling patterns (onError, script guard)
- [[source-paypal-checkout-handle-funding-failures]] — INSTRUMENT_DECLINED handling (funding failures vs AVS/CVV declines)
