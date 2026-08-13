---
title: "PayPal Subscriptions & Recurring Payments"
type: concept
category: technology
tags: [paypal, recurring-payments, subscriptions, vault, stored-credentials, billing-cycles, usage-pattern]
---

## Overview

PayPal offers two paths for recurring payments:

1. **Orders API + Vault** — flexible merchant-initiated charges using stored payment tokens; the Vault token describes the usage pattern, while Orders describes each subsequent charge; works with cards, PayPal Wallet, and contract-modeled Venmo subject to product eligibility
2. **Subscriptions API** — structured subscription management with billing plans, trial periods, and automated lifecycle (pause, cancel, reactivate); dashboard or REST API

## Vault-Based Recurring (Orders API)

PayPal's vault stores buyer payment methods for future merchant-initiated charges.

**Token lifecycle**:
1. Setup token created during buyer consent (expires in 3 days)
2. Payment token (vault ID) created on approval — persistent stored credential
3. Merchant uses `vault_id` in Orders API for subsequent charges

See [[paypal-vault]] for full token lifecycle details.

### `stored_credential` fields (required on every MIT)

```json
{
  "payment_initiator": "MERCHANT",
  "payment_type": "RECURRING",
  "usage": "SUBSEQUENT"
}
```

`usage_pattern` does not belong in the Orders `stored_credential` object. It belongs to the Payment Method Tokens wallet contract used while establishing the stored payment method.

### 8 `usage_pattern` values

| Pattern | Type | Amount | Frequency |
| --- | --- | --- | --- |
| `SUBSCRIPTION_PREPAID` | Subscription | Fixed | Regular |
| `SUBSCRIPTION_POSTPAID` | Subscription | Fixed | Regular |
| `RECURRING_PREPAID` | Recurring | Variable | Regular |
| `RECURRING_POSTPAID` | Recurring | Variable | Regular |
| `UNSCHEDULED_PREPAID` | Unscheduled | Fixed/variable | Irregular |
| `UNSCHEDULED_POSTPAID` | Unscheduled | Fixed/variable | Irregular |
| `INSTALLMENT_PREPAID` | Installment | Fixed | Defined |
| `INSTALLMENT_POSTPAID` | Installment | Fixed | Defined |

PREPAID = charged before delivery; POSTPAID = charged after delivery.

## Subscriptions API

6-step flow: create product → create plan → show plan to buyer → buyer subscribes → activate subscription → charge automatically.

### TypeScript server SDK baseline at `2.3.0`

`@paypal/paypal-server-sdk@2.3.0` exposes a broad `SubscriptionsController`: product create/list/get/update; plan create/list/get/patch/activate/deactivate/pricing updates; and subscription create/list/get/patch/revise/suspend/cancel/activate/capture/transaction listing. This is typed API-surface evidence, not proof of merchant eligibility or a complete production billing implementation. See [[source-github-paypal-typescript-server-sdk]].

The independent exact REST-contract baseline at `90e8041` separates Catalog Products 1.0 from Subscriptions 1.8. Catalog owns product create/list/get/patch; Subscriptions owns plan management and the subscription create/get/patch/revise/suspend/cancel/activate/outstanding-balance/transaction lifecycle. See [[source-github-paypal-rest-api-specifications]].

### v6 sample baseline at `b5f2df2`

The current sample initializes `paypal-subscriptions`, requests `RECURRING_PAYMENT` eligibility, and starts `createPayPalSubscriptionPaymentSession()`. Its Node server uses `PAYPAL_SUBSCRIPTION_PLAN_ID` when supplied; otherwise it creates a sample service product, an active USD 9.99 monthly plan, and then the subscription. This is a creation and approval example, not evidence of lifecycle management, retries, cancellation, or production eligibility.

### Historical create, activate, and revise samples at `5409a3b`

The September 2023 `paypal-examples/paypal-sdk-server-side-integration` baseline shows three JS SDK 5.1.x paths. The ordinary flow creates a subscription with a configured plan and defaults `application_context.user_action` to `SUBSCRIBE_NOW`. A `CONTINUE` example activates the approved subscription through `POST /v1/billing/subscriptions/{id}/activate`. A revise example sends another configured plan ID to `POST /v1/billing/subscriptions/{id}/revise`.

> [!warning] Historical sample validation gaps
> These examples are illustrative rather than production-ready. Their Fastify schemas require neither `subscriptionId` nor plan configuration; missing plan values become the literal string `"undefined"`. The revise browser ignores the server response, returns the original subscription ID, and then displays success. Use current Subscriptions documentation for supported lifecycle semantics and validation requirements.

### Postman lifecycle baseline at `7f7240a`

The Public APIs collection provides runnable examples for product and plan setup, plan activation/deactivation and pricing changes, and subscription create, show, update, revise, suspend, activate, cancel, balance capture, authorized-amount capture, and transaction listing. Its revise operation covers plan, quantity, shipping amount, and shipping-address changes and explicitly requires buyer consent. Stored responses are commit-qualified examples, so current lifecycle constraints and errors must still be checked against the API contract and current documentation.

### Billing plan structure (`billing_cycles` array)

- Up to **3 cycles** per plan (e.g. trial → discounted → regular)
- Each cycle: `tenure_type` (TRIAL/REGULAR), `pricing_scheme` (FIXED/variable), `frequency` (DAY/WEEK/MONTH/YEAR + count), `total_cycles`, `start_date`
- `one_time_charges`: setup fees, product price, shipping, taxes — displayed but not recurring

### 4 pricing models

Fixed, quantity-based, volume, tiered. Volume vs tiered distinction: volume applies one rate to all units based on total; tiered applies different rates to each tier bracket.

### Key constraints

- Single currency per plan
- Cannot change currency after plan created
- Dashboard integration available (no code) vs REST API (full control)
- 12 customization capabilities including trial periods, custom billing cycles, subscriber management

## Relevant Concepts

- [[recurring-payments]] — generic concept: dunning, retry logic, stored credentials standard, SCA
- [[paypal-vault]] — token lifecycle (setup token → payment token)

## Payment Failure & Recovery

**Intelligent retry**: PayPal automatically retries failed subscription payments using a proprietary algorithm (considers payment history, risk signals, bank availability). No merchant action required. Configure retry schedules in the PayPal dashboard.

**Manual retry**: via PayPal Dashboard or Subscriptions API.

**Key failure codes for subscriptions**:

- `CANNOT_BILL_PAST_DUE_BALANCE` — subscription suspended; past due balance exceeded maximum
- `REJECTED_DUE_TO_RISK_REVERSAL` — rejected due to chargeback or dispute

**Webhook events**:

- `BILLING.SUBSCRIPTION.PAYMENT.FAILED` — failed subscription payment
- `BILLING.SUBSCRIPTION.PAYMENT.SUCCEEDED` — successful subscription payment

See [[source-paypal-payment-failures]] for full error code reference.

## Sources

- [[source-paypal-checkout-recurring-payment]] — Orders API recurring: vault flow, `stored_credential` fields, billing agreement
- [[source-paypal-subscriptions-overview]] — Subscriptions API: 6-step flow, billing plan structure, 4 pricing models, 12 customization capabilities
- [[source-paypal-checkout-recurring-payments-module]] — Full `usage_pattern` table, billing plan constraints, setup vs purchase paths
- [[source-paypal-checkout-save-payment-methods-recurring]] — Save payment methods for recurring: field-level RBA schema, 7 use cases, 422 errors
- [[source-github-v6-web-sdk-sample-integration]] — runnable v6 subscription session and sample product/plan creation
- [[source-github-paypal-sdk-server-side-integration]] — historical create, `CONTINUE` activation, and plan-revise sample with documented validation gaps
- [[source-github-paypal-typescript-server-sdk]] — package-qualified `2.3.0` controller and model surface for products, plans, and subscription lifecycle operations
- [[source-github-paypal-rest-api-specifications]] — exact-SHA Catalog Products 1.0 and Subscriptions 1.8 contracts
- [[source-github-postman-collections]] — runnable product, plan, and subscription lifecycle examples at exact commit
