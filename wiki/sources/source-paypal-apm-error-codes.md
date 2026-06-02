---
title: "Error Codes (APM Reference)"
type: source
date_ingested: 2026-04-14
original_format: webpage
raw_files:
  - "paypal-apm-error-codes.md"
tags: [paypal, apm, error-codes, cancel-url, reference]
---

## Overview

Error codes returned as query parameters in the `cancel_url`: `?errorcode=XXX&token=XXX`. Query parameters are not case sensitive.

Source URL: <https://developer.paypal.com/docs/checkout/apm/reference/error-codes/>

Last updated: 2025-04-21

## Key Error Codes (19 total)

| Error code | Cause |
| --- | --- |
| `order_not_confirmed` | Order not in `PAYER_ACTION_REQUIRED` or no payment method attached |
| `system_config_error` | Auth failure or invalid request |
| `invalid_payment_method` | Wrong order ID attached to payment method |
| `payee_not_enabled_for_payment_method` | Not authorized to accept this APM |
| `payment_method_change_not_allowed` | Idempotency check — `PayPal-Request-Id`/payload issue |
| `processing_error` | Idempotency — order no longer in PENDING state |
| `min_amount_required_by_payment_method` | Below APM minimum transaction amount |
| `payment_method_error` | Transaction declined by payment method |
| `declined_by_payment_method` | Transaction declined by payment method (duplicate of above) |
| `currency_not_supported_by_payment_method` | Currency/country mismatch |
| `country_not_supported_by_payment_method` | Country not supported |
| `invalid_expiry_date` | Expiry date not in future / exceeds threshold |
| `unsupported_processing_instruction` | `processing_instruction` not supported for this `payment_source` |
| `order_complete_on_payment_approval` | `ORDER_COMPLETE_ON_PAYMENT_APPROVAL` required for this `payment_source` |
| `order_completion_in_progress` | Auto-capture still in progress — retry request |
| `internal_server_error` | Encryption, DB, timeout, or unknown errors |
| `not_enabled_for_payment_source` | API caller/payee not set up — allow 2 business days |
| `payment_error` | All other errors (catch-all) |

## Raw Sources

- [[paypal-apm-error-codes]] — verbatim reference page

## Relevant Wiki Pages

- [[paypal-apm]] — APM overview
- [[source-paypal-apm-subscribe-webhooks]] — Webhook reference (related APM reference page)
