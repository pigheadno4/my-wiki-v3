---
title: "PayPal: Refund a Payment"
type: source
date_ingested: 2026-04-17
original_format: webpage
raw_files:
  - "paypal-refund-payment.md"
tags: [paypal, refunds, payments-api, capture, negative-testing]
---

## Summary

Integration guide for refunding captured PayPal payments using **Payments API v2** (`/v2/payments/captures/{capture_id}/refund`). Covers full and partial refunds, error handling, negative testing, best practices, and go-live guidance. Builds on the [[source-paypal-payments-quickstart]] integration.

## Key takeaways

- **Endpoint**: `POST /v2/payments/captures/{capture_id}/refund`
- **Full refund**: omit `amount` from the request body
- **Partial refund**: include `amount.value` and `currency_code`
- **Status check**: `GET /v2/payments/refunds/{refund_id}`
- Refunds always go back to the original payment method — no redirecting to a different method
- No currency conversion: always refund in the same currency as the original payment

## Timing

- Sandbox: refunds complete instantly
- Production: 3–5 business days (varies by payment method)
- **180-day window**: refunds must be processed within 180 days of capture; after expiry requires manual PayPal support intervention; customer's bank may have shorter windows

## Error codes

| Error code | HTTP status | Meaning |
| --- | --- | --- |
| `CAPTURE_FULLY_REFUNDED` | 422 | Already fully refunded |
| `REFUND_AMOUNT_EXCEEDED` | 422 | Amount exceeds refundable balance |
| `REFUND_NOT_ALLOWED_AFTER_180_DAYS` | 422 | Refund period expired |
| `PERMISSION_DENIED` | 403 | No refund permission on the account |
| `INTERNAL_SERVER_ERROR` | 500 | Generic server error |

## Webhooks

- Event: `PAYMENT.CAPTURE.REFUNDED` — subscribe for real-time refund status updates
- Always verify webhook signatures for security

## Best practices

- Store capture IDs immediately on payment capture — required for future refunds
- Use idempotency keys to avoid duplicate refunds on network retries
- Log all refunds with initiator, timestamp, and reason (compliance requirement)
- Track cumulative refunded amounts per capture to prevent over-refunding
- Build approval workflows for large refunds — processed refunds cannot be cancelled
- Include clear `note_to_payer` for customer communication

## Tip: void vs refund

If a payment was authorized but not yet captured, use **void** instead of refund to avoid processing fees. See [[source-paypal-standard-payments]] for the authorization vs. capture distinction.

## Related pages

- [[paypal-checkout]] — PayPal Checkout concept page
- [[disputes]] — Disputes and chargebacks (related but distinct from refunds)
- [[source-paypal-payments-quickstart]] — Base integration this builds on

## Raw Sources

- [[paypal-refund-payment]] — verbatim refund integration guide
