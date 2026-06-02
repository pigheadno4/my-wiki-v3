---
title: "PayPal 3D Secure: Response Parameters"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-3ds-response-parameters.md"
tags: [paypal, 3d-secure, liability-shift, enrollment-status, authentication-status, response-parameters, reference]
---

## PayPal 3D Secure: Response Parameters

Definitive reference for all 3D Secure response parameters — `liability_shift`, `enrollment_status`, `authentication_status`, and the deprecated pre-June-2020 parameters.

Source URL: <https://developer.paypal.com/docs/checkout/advanced/customize/3d-secure/response-parameters/>

Last updated: 2025-12-10

## Key Takeaways

### JS SDK vs Orders API — parameter availability

| Parameter | JS SDK integration | Orders API integration |
| --------- | ------------------ | ---------------------- |
| `liability_shift` | ✓ (client + server) | ✓ (client + server) |
| `enrollment_status` | ✗ (server-side only) | ✓ |
| `authentication_status` | ✗ (server-side only) | ✓ |

### `liability_shift` — the decision parameter

| Value | Meaning | Action |
| ----- | ------- | ------ |
| `POSSIBLE` | Liability may shift to card issuer | **Continue** with authorization |
| `NO` | Liability stays with merchant | **Do not** continue |
| `UNKNOWN` | Auth system unavailable | **Do not** continue; ask buyer to retry |

### `enrollment_status` values

`Y` (enrolled) | `N` (not enrolled) | `U` (unavailable) | `B` (bypassed)

### `authentication_status` values

`Y` (success) | `N` (failed) | `R` (rejected) | `A` (attempted) | `U` (unable) | `C` (challenge required) | `I` (info only) | `D` (decoupled)

### Decision logic summary

- **Always proceed**: `enrollment_status = N`, `U`, `B` (card not enrolled or system bypassed — no auth required, proceed at merchant's discretion)
- **Proceed if `POSSIBLE`**: `enrollment_status = Y, authentication_status = Y` or `A`
- **Do not proceed**: `enrollment_status = Y, authentication_status = N` or `R`
- **Retry**: `authentication_status = U` or `C` (system issues or challenge pending)

### Deprecated parameters (pre-June 2020)

`liabilityShifted` / `authenticationStatus` / `AuthenticationReason` — still work server-side but unsupported. Key `AuthenticationReason` values:
- `SUCCESSFUL` — proceed
- `BYPASSED`, `ATTEMPTED`, `UNAVAILABLE`, `CARD_INELIGIBLE` — proceed but assume liability
- `FAILURE`, `SKIPPED_BY_BUYER`, `ERROR` — do not proceed

## Raw Sources

- [[paypal-3ds-response-parameters]] — verbatim webpage content with full decision table

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-expanded-checkout]] — Expanded Checkout concept page
- [[source-paypal-expanded-checkout-3ds-card-fields]] — CardFields 3DS integration (receives `liabilityShift` in `onApprove`)
- [[source-paypal-expanded-checkout-3ds-orders-api]] — Orders API 3DS integration (receives full `authentication_result`)
- [[source-paypal-expanded-checkout-3d-secure]] — 3DS eligibility by country
