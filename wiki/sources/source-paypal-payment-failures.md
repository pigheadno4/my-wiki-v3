---
title: "PayPal Payment Failures — Handling & Recovery"
type: source
date_ingested: 2026-04-19
original_format: webpage
raw_files:
  - "paypal-rest-api-payment-failures-2025.md"
tags: [paypal, payment-failures, error-handling, subscriptions, orders-api, webhooks, intelligent-retry]
---

## Summary

Cross-cutting guide for detecting and recovering from payment failures across PayPal's Orders v2 API and Subscriptions API. Covers 19 error codes, `actions.restart()` pattern, asynchronous failures, intelligent retry for subscriptions, and relevant webhook events.

## Key Takeaways

- Some failures are **asynchronous** — bank may initially authorize then later decline; use webhooks to track
- `INSTRUMENT_DECLINED` → call `actions.restart()` to restart payment flow (not `actions.order.capture()` again)
- PayPal **intelligent retry** for subscriptions: proprietary algorithm considers payment history, risk signals, bank availability — no merchant action required
- Manual subscription retries available via PayPal Dashboard or Subscriptions API

## Payment Failure Error Codes (19)

| Code | Meaning | Fix |
| --- | --- | --- |
| `INSTRUMENT_DECLINED` | Payment method declined | `actions.restart()` |
| `CARD_EXPIRED` | Card expired | Ask for new card |
| `AMOUNT_MISMATCH` / `ITEM_TOTAL_MISMATCH` | Totals don't add up | Fix totals in request |
| `CURRENCY_NOT_SUPPORTED` | Unsupported currency | Use supported currency |
| `ORDER_NOT_APPROVED` | Buyer didn't approve | Redirect to re-approve |
| `MAX_NUMBER_OF_PAYMENT_ATTEMPTS_EXCEEDED` | Too many failed attempts | Use different payment method |
| `REDIRECT_PAYER_FOR_ALTERNATE_FUNDING` | Funding source failed | Choose different method |
| `VALIDATION_ERROR` / `UNPROCESSABLE_ENTITY` | Invalid/missing data | Correct and retry |
| `PAYMENT_DENIED` | Denied by PayPal | Contact PayPal support |
| `PAYER_CANNOT_PAY` | Payer can't pay with this method | Different method or support |
| `CANNOT_BILL_PAST_DUE_BALANCE` | Subscription suspended; past due balance exceeded max | Contact PayPal support |
| `REJECTED_DUE_TO_RISK_REVERSAL` | Rejected due to chargeback/dispute | Investigate; contact support |
| `TRANSACTION_REFUSED` | Refused by processor | Different method or contact bank |
| `INVALID_ACCOUNT_STATUS` | Payer account locked/inactive | Contact PayPal support |
| `INVALID_REQUEST` | Malformed request | Fix parameters |
| `AUTHENTICATION_FAILURE` | Invalid credentials | Verify API credentials |
| `NOT_AUTHORIZED` | No permission | Check account permissions |
| `RESOURCE_NOT_FOUND` | Resource doesn't exist | Verify ID |
| `UNPROCESSABLE_ENTITY` | Semantic errors | Review request data |

## Webhook Events for Payment Failures

**Orders API:**
- `PAYMENT.CAPTURE.COMPLETED` — successful capture
- `PAYMENT.CAPTURE.DENIED` — failed capture

**Subscriptions API:**
- `BILLING.SUBSCRIPTION.PAYMENT.FAILED` — failed subscription payment
- `BILLING.SUBSCRIPTION.PAYMENT.SUCCEEDED` — successful subscription payment

## `actions.restart()` Pattern

```javascript
paypal.Buttons({
  onApprove: (data, actions) => {
    return actions.order.capture().catch(err => {
      if (err.name === "INSTRUMENT_DECLINED") {
        return actions.restart(); // buyer picks another method
      }
      alert("Payment could not be completed. Please try again.");
    });
  }
}).render('#paypal-button-container');
```

## Related Pages

- [[paypal]] — company page
- [[paypal-checkout]] — checkout integration concept
- [[paypal-subscriptions]] — subscriptions concept

## Raw Sources

- [[paypal-rest-api-payment-failures-2025]] — full payment failures guide: 19 error codes, actions.restart(), intelligent retry, webhook events, manual retry
