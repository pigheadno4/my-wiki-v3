---
title: "PayPal Orders API — Troubleshooting & Error Reference"
type: source
date_ingested: 2026-04-19
original_format: webpage
raw_files:
  - "paypal-rest-api-common-errors-2025.md"
  - "paypal-error-resource-not-found-2025.md"
  - "paypal-error-unprocessable-entity-2025.md"
  - "paypal-error-agreement-cancelled-2025.md"
  - "paypal-error-cannot-pay-self-2025.md"
  - "paypal-error-currency-mismatch-2025.md"
  - "paypal-error-currency-not-allowed-2025.md"
  - "paypal-error-duplicate-transaction-2025.md"
  - "paypal-error-merchant-reference-transaction-2025.md"
  - "paypal-error-not-authorized-2025.md"
  - "paypal-error-unsupported-payee-currency-2025.md"
  - "paypal-error-validation-error-2025.md"
tags: [paypal, orders-api, troubleshooting, error-codes, error-handling, debugging]
---

## Summary

Aggregated troubleshooting and error reference for the PayPal Orders v2 API. Covers 31 error codes with specific fixes, HTTP status code → error name mapping (including 503), and 4 full curl+JSON error samples.

## Key Takeaways

- **503/SERVICE_UNAVAILABLE** — exists in addition to the standard 400/401/403/404/422/500
- **`ORDER_ALREADY_AUTHORIZED`** — do NOT re-create; call capture. If authorization >3 days old, reauthorize first
- **`PAYER_ACTION_REQUIRED`** — redirect to `'rel':'payer-action'` HATEOAS link BEFORE authorizing or capturing; some payment methods require webhook subscription for background payer actions
- **`PAYEE_NOT_CONSENTED`** — requires `PARTNER_FEE` capability in seller onboarding signup link
- **`debug_id`** — always include when contacting PayPal support
- Error response shape: `{name, details[{field, location, issue, description}], message, debug_id, links}`

## HTTP Status Codes (Orders v2)

| Code | Error name | Meaning |
| --- | --- | --- |
| 400 | `INVALID_REQUEST` | Wrong format |
| 401 | `AUTHENTICATION_FAILURE` | Missing/invalid token |
| 403 | `NOT_AUTHORIZED` | Insufficient permissions |
| 404 | `RESOURCE_NOT_FOUND` | Resource doesn't exist |
| 422 | `UNPROCESSABLE_ENTITY` | Business rule failure |
| 500 | `INTERNAL_SERVER_ERROR` | Server error |
| 503 | `SERVICE_UNAVAILABLE` | Service unavailable |

## Key Error Codes (31 total)

| Code | Fix |
| --- | --- |
| `AMOUNT_MISMATCH` | Total must equal sum of line items + taxes + discounts |
| `CANNOT_BE_NEGATIVE` / `CANNOT_BE_ZERO_OR_NEGATIVE` | Positive amount, max 2 decimal places |
| `DECIMAL_PRECISION` / `DECIMALS_NOT_SUPPORTED` | Round to 2 decimals; match currency's supported decimals |
| `DUPLICATE_INVOICE_ID` | Use unique `invoice_id`; contact support with `debug_id` if must reuse |
| `INCOMPATIBLE_PARAMETER_VALUE` | Check parameters match expected data types |
| `INVALID_PARAMETER_SYNTAX` / `INVALID_PARAMETER_VALUE` | Fix JSON format/values |
| `INVALID_RESOURCE_ID` | Check ID; verify scopes if cross-account |
| `INVALID_STRING_LENGTH` | Check field length limits in Orders API docs |
| `ITEM_TOTAL_MISMATCH` | Item totals must match quantity total |
| `MISSING_REQUIRED_PARAMETER` | Add all required parameters |
| `ORDER_ALREADY_AUTHORIZED` | Call capture; if >3 days old, reauthorize first |
| `ORDER_ALREADY_CAPTURED` | No action; GET order for capture/transaction ID; use `AUTHORIZE` intent for multi-capture |
| `ORDER_NOT_APPROVED` | Redirect buyer to `'rel':'approve'` HATEOAS URL or provide valid `payment_source` |
| `PAYEE_ACCOUNT_RESTRICTED` | Contact PayPal support to lift restrictions |
| `PAYEE_NOT_CONSENTED` | Add `PARTNER_FEE` capability during seller onboarding signup |
| `PAYEE_NOT_ENABLED_FOR_CARD_PROCESSING` | Contact PayPal support for account config |
| `PAYER_ACTION_REQUIRED` | Redirect to `'rel':'payer-action'` HATEOAS link BEFORE capture; some methods need webhook for background actions |
| `PERMISSION_DENIED` | Check permissions/scopes; grant necessary permissions if cross-account |
| `POSTAL_CODE_REQUIRED` | Add postal code to request |
| `REDIRECT_PAYER_FOR_ALTERNATE_FUNDING` | Redirect buyer to choose different payment method |
| `REFERENCED_CARD_EXPIRED` | Buyer must update card info |
| `SHIPPING_ADDRESS_INVALID` | Fix address; ask buyer for correct address if using saved details |
| `TOKEN_ID_NOT_FOUND` | Validate payment token; check cross-account permissions |
| `UNPROCESSABLE_ENTITY` | Contact support with `debug_id` or `correlation_id` from response header |
| `VALIDATION_ERROR` | Card number incorrect — ask buyer to re-enter |

## Error Sample Highlights

**500**: `INTERNAL_SERVER_ERROR` — no specific field details; just `debug_id` and info link

**422**: `UNPROCESSABLE_ENTITY` — includes `details[].field` path (e.g. `/payment_source/card/expiry`), `location: body`, specific `issue` (e.g. `CARD_EXPIRED`), and `description`

**400**: `INVALID_REQUEST` — includes `details[].field`, `value` that was rejected, and `issue` (e.g. `INVALID_PARAMETER_VALUE`)

**403**: `NOT_AUTHORIZED` — includes `details[].issue` (e.g. `PERMISSION_DENIED_FOR_DONATION_ITEMS`) and `description` explaining required account manager approval

## Related Pages

- [[paypal]] — company page
- [[paypal-checkout]] — checkout integration concept
- [[source-paypal-payment-failures]] — broader payment failures guide (19 codes, intelligent retry, webhook events)

## Raw Sources

- [[paypal-rest-api-common-errors-2025]] — Orders v2 common errors: 31 codes with fixes, HTTP status table (incl. 503), 4 curl+JSON error samples (500/422/400/403)
- [[paypal-error-validation-error-2025]] — VALIDATION_ERROR (Orders v2 + Payments v1): 6 causes incl. outdated API version (validation rules change between versions); check details[].field + issue in error response
- [[paypal-error-unsupported-payee-currency-2025]] — UNSUPPORTED_PAYEE_CURRENCY (Payments V1): payee account doesn't support currency (vs platform-level CURRENCY_NOT_SUPPORTED); causes: account restrictions, disabled in payee settings, region limits; contact payee to enable
- [[paypal-error-not-authorized-2025]] — NOT_AUTHORIZED (403) sub-codes: PAYEE_ACCOUNT_NOT_VERIFIED (verify email/bank/card); PAYEE_NOT_CONSENTED (add payee to purchase_units.payee + PARTNER_FEE for Complete Payments); PERMISSION_DENIED (sandbox vs live env mismatch, expired tokens, personal account using business tools)
- [[paypal-error-merchant-reference-transaction-2025]] — MERCHANT_NOT_ENABLED_FOR_REFERENCE_TRANSACTION (Payments V1): not enabled by default; contact customer support to enable; may require additional account info; see reference transactions guide
- [[paypal-error-duplicate-transaction-2025]] — DUPLICATE_TRANSACTION (Payments V2): network latency/payer double-click/no response retry; use idempotency key per transaction; check transaction history before retrying
- [[paypal-error-currency-not-allowed-2025]] — CURRENCY_NOT_ALLOWED (Payments V1): unsupported/unconfigured/region-restricted/disabled currency; change to supported currency + configure merchant account
- [[paypal-error-currency-mismatch-2025]] — CURRENCY_MISMATCH (Payments V2): currency mismatch between account config, payer/payee accounts, or different fields in same request; verify all fields use same currency + confirm merchant account accepts that currency
- [[paypal-error-cannot-pay-self-2025]] — CANNOT_PAY_SELF (Payments V1): sender and receiver are same account; use distinct PayPal IDs/emails; add validation to prevent self-payment
- [[paypal-error-agreement-cancelled-2025]] — AGREEMENT_ALREADY_CANCELLED (Orders V2 variant): manual/auto cancellation (payment failures or account issues) or logic error; check agreement status before operations
- [[paypal-error-unprocessable-entity-2025]] — UNPROCESSABLE_ENTITY sub-codes (24): Billing Agreements (AGREEMENT_ALREADY_CANCELLED, BILLING_AGREEMENT_NOT_FOUND, CANNOT_PAY_SELF, MERCHANT_NOT_ENABLED_FOR_REFERENCE_TRANSACTION, NOT_ENABLED_FOR_CHANNEL_INITIATED_BILLING, PAYER_ACCOUNT_LOCKED_OR_CLOSED, PREVIOUS_REQUEST_IN_PROGRESS, UNSUPPORTED_PAYEE_CURRENCY) + Orders v2/Payments v1 codes
- [[paypal-error-resource-not-found-2025]] — INVALID_RESOURCE_ID: cause (bad/missing ID or no permission), impact (payment stopped), resolution (verify ID + check caller permissions); from Payments v1 or Orders v2
