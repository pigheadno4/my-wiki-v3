---
title: Recurring payments module
slug: /docs/checkout/standard/customize/recurring-payments-module/
createTime: '2025-01-08T21:20:03.650Z'
updateTime: '2025-08-14T18:43:27.020Z'
---

# Recurring payments module

## Overview

The recurring payment module helps you display recurring payment information to the payer before they commit to the payment. This can increase payer conversion by building customer trust through transparency.

Pay with PayPal supports saving payment methods so that you can charge payers on a recurring basis through two integration patterns:

- **Save payment methods for purchase later**: Collect and store payment information for future transactions without processing an immediate payment.
- **Save payment methods during purchase**: Save payment details while simultaneously processing an initial transaction.

## Eligibility

- Available for buyers and merchants in the United States.
- To save for a purchase later: integrate using the Payment Methods Tokens v3 API.
- To save with a purchase: integrate using the Orders v2 API.
- Merchant must integrate using Save PayPal with the JavaScript SDK or have a server-side, direct-API integration with Orders API (save during purchase experience).
- Merchant must integrate using Save PayPal for purchase later with the JavaScript SDK or have a server-side, direct-API integration with Payment Method Tokens API (save for later experience).
- JavaScript SDK and API-only server-side integrations are supported.

## What are recurring payments?

Recurring payments are initiated by a merchant based on a schedule or other criteria. Examples:

- Subscriptions (streaming media, pet food delivery)
- Automatic bill payments (utilities, mobile phone bills)
- Auto reloads (road tolls, prepaid cards)

Industry classifications:

- Subscriptions
- Recurring
- Unscheduled account on file
- Merchant managed installments

These classifications are based on whether the amount or frequency varies and whether there is a fixed or open duration.

## How it works

When a payer signs up and adds PayPal as a payment method, they go through a PayPal flow where they are authenticated and consent to a billing agreement. The recurring payment module shows the payer billing terms on the PayPal review page.

Two types of information to provide:

- **Recurring payment type**: Flags the payment method token for future recurring payments; tailors PayPal flow content.
- **Recurring billing plan**: Shows the payer a summary of the billing agreement in PayPal.

## Recurring payment setup without purchase

Pass additional fields in the Create Setup Token and Create Payment Token API request using `payment_source.paypal` object. Useful for free trials, postpaid services, or scenarios where no immediate payment is required.

## Recurring payment setup with purchase

Flag the payment method in the Create Order request:
- Pass `ON_SUCCESS` in `payment_source.card.attributes.vault.store_in_vault`
- Set `MERCHANT` or `CUSTOMER` in `payment_source.card.attributes.vault.usage_type`
- Include all required metadata in the request body

## usage_pattern field

The field used depends on whether saving with or without purchase:

- **With purchase**: `payment_source.paypal.attributes.vault.usage_pattern` (setup); `payment_source.paypal.stored_credential.usage_pattern` (subsequent)
- **Without purchase**: `payment_source.paypal.usage_pattern` (Create Setup Token)

## usage_pattern values reference table

| Type | Amount | Frequency | Duration | usage_pattern values |
| ---- | ------ | --------- | -------- | -------------------- |
| **Subscription** — fixed amount, regular schedule, no end date (e.g. monthly streaming, weekly food delivery) | Fixed | Regular | None | `SUBSCRIPTION_PREPAID` (payment before delivery), `SUBSCRIPTION_POSTPAID` (payment after delivery) |
| **Recurring** — variable amount, regular schedule, no end date (e.g. monthly utility auto-pay) | Variable | Regular | None | `RECURRING_PREPAID` (upfront on fixed date), `RECURRING_POSTPAID` (after delivery based on usage) |
| **Unscheduled** — fixed or variable amount, variable frequency, no end date (e.g. prepaid auto-reload, app store spend threshold) | Fixed or variable | Variable | None | `UNSCHEDULED_POSTPAID` (merchant-managed, payment after delivery), `UNSCHEDULED_PREPAID` (merchant bills upfront per agreed logic, including auto-reload) |
| **Installment** — fixed amount, defined schedule, defined end date (e.g. merchant-assisted purchase in installments) | Fixed | Defined | Fixed | `INSTALLMENT_POSTPAID` (defined payments, after delivery), `INSTALLMENT_PREPAID` (defined payments, before delivery) |

## Recurring billing plan

Passed in `payment_source.paypal.billing_plan` (Create Setup Token) or `purchase_units.items[].billing_plan` (Create Order with purchase):

- `name`: Optional plan display name — shown in PayPal flow
- `billing_cycles`: Array of up to 3 billing cycles (trial or regular); each has `tenure_type`, `pricing_scheme`, `frequency`, `total_cycles`, `sequence`, `start_date`
- `one_time_charges`: One-time fees — `setup_fee`, `shipping_amount`, `taxes`, `product_price`, `total_amount`

## Merchant options for recurring metadata

| Option | Payer experience | Use case |
| ------ | ---------------- | -------- |
| Pass `usage_pattern` + `billing_plan.name` | Sees full plan details | Buyer subscribing to $5.99/month with 14-day free trial |
| Pass `usage_pattern` only | Recurring flow but no plan details | Complex plan structures hard to display; merchant communicates terms on site |
| Pass neither | Non-recurring PayPal approval flow | Not recommended for recurring transactions |

## User action button behavior

**Without purchase:**

| User action | Experience | Use case |
| ----------- | ---------- | -------- |
| `Setup Now` | Redirected to merchant confirmation page | Final approval step — typical flows |
| `Continue` | Redirected to merchant checkout | Buyer needs additional steps after approval |

**With purchase:**

| User action | Experience | Use case |
| ----------- | ---------- | -------- |
| `Pay Now` | Completes transaction on PayPal review page | Order total known and fixed |
| `Continue` | Returns to merchant to complete | Final amount may change after buyer leaves PayPal |

## Sample Create Setup Token API request

API: `POST /v3/vault/setup-tokens`

```curl
curl -v -k -X POST 'https://api-m.sandbox.paypal.com/v3/vault/setup-tokens' \
-H 'Authorization: Bearer ACCESS-TOKEN' \
-H 'PayPal-Request-ID: PAYPAL-REQUEST-ID' \
-H 'Content-Type: application/json' \
-d '{
    "customer": {
        "merchant_customer_id": "payer@example.com"
    },
    "payment_source": {
        "paypal": {
            "permit_multiple_payment_tokens": false,
            "usage_type": "MERCHANT",
            "customer_type": "CONSUMER",
            "usage_pattern": "RECURRING_PREPAID",
            "shipping": {
                "name": { "full_name": "Firstname Lastname" },
                "address": {
                    "address_line_1": "123 Main St.",
                    "admin_area_2": "Anytown",
                    "admin_area_1": "CA",
                    "postal_code": "12345",
                    "country_code": "US"
                }
            },
            "billing_plan": {
                "billing_cycles": [{
                    "tenure_type": "REGULAR",
                    "pricing_scheme": {
                        "pricing_model": "VARIABLE",
                        "price": { "value": "6.99", "currency_code": "USD" }
                    },
                    "frequency": { "interval_unit": "MONTH", "interval_count": 1 },
                    "total_cycles": 0,
                    "sequence": 1,
                    "start_date": "2024-04-16"
                }],
                "one_time_charges": {
                    "setup_fee": { "value": "10", "currency_code": "USD" },
                    "shipping_amount": { "value": "3", "currency_code": "USD" },
                    "taxes": { "value": "20", "currency_code": "USD" },
                    "product_price": { "value": "200", "currency_code": "USD" },
                    "total_amount": { "value": "233", "currency_code": "USD" }
                },
                "product": { "description": "Company yearly membership", "quantity": "1.0" },
                "name": "Company"
            },
            "experience_context": {
                "shipping_preference": "SET_PROVIDED_ADDRESS",
                "locale": "en-US",
                "return_url": "https://example.com/returnUrl",
                "cancel_url": "https://example.com/cancelUrl"
            }
        }
    }
}'
```

## Sample Create Setup Token API response

```json
{
  "id": "SETUP-TOKEN-ID",
  "customer": { "id": "CUSTOMER-ID" },
  "status": "PAYER_ACTION_REQUIRED",
  "payment_source": {
    "paypal": {
      "usage_pattern": "RECURRING_PREPAID",
      "shipping": {
        "name": { "full_name": "Firstname Lastname" },
        "address": {
          "address_line_1": "123 Main St.",
          "admin_area_2": "Anytown",
          "admin_area_1": "CA",
          "postal_code": "12345",
          "country_code": "US"
        }
      },
      "permit_multiple_payment_tokens": false,
      "usage_type": "MERCHANT",
      "customer_type": "CONSUMER"
    }
  },
  "links": [
    {
      "href": "https://api-m.sandbox.paypal.com/v3/vault/setup-tokens/SETUP-TOKEN-ID",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "https://sandbox.paypal.com/agreements/approve?approval_session_id=SETUP-TOKEN-ID",
      "rel": "approve",
      "method": "GET"
    }
  ]
}
```

Setup token expires after 3 days. Upgrade to payment method token by calling `POST /v3/vault/payment-tokens`.

## Sample Create Order API request (save during purchase)

API: `POST /v2/checkout/orders`

```curl
curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders/ \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ACCESS-TOKEN" \
-d '{
    "intent": "CAPTURE",
    "purchase_units": [{
        "amount": {
            "currency_code": "USD",
            "value": "238",
            "breakdown": {
                "item_total": { "currency_code": "USD", "value": "215" },
                "shipping": { "currency_code": "USD", "value": "3" },
                "tax_total": { "currency_code": "USD", "value": "20" }
            }
        },
        "items": [
            {
                "name": "iPhone 13",
                "description": "iPhone 13 with Verizon plan",
                "sku": "259483234816",
                "unit_amount": { "currency_code": "USD", "value": "200" },
                "tax": { "currency_code": "USD", "value": "20" },
                "quantity": "1",
                "category": "DIGITAL_GOODS"
            },
            {
                "name": "Billing Plan",
                "description": "Billing plan for subscriptions",
                "unit_amount": { "currency_code": "USD", "value": "15" },
                "quantity": "1",
                "billing_plan": {
                    "name": "Verizon",
                    "setup_fee": { "value": "10", "currency_code": "USD" },
                    "billing_cycles": [{
                        "tenure_type": "REGULAR",
                        "pricing_scheme": {
                            "price": { "value": "5", "currency_code": "USD" },
                            "pricing_model": "FIXED"
                        },
                        "frequency": { "interval_unit": "MONTH", "interval_count": 1 },
                        "total_cycles": 0,
                        "sequence": 1
                    }]
                }
            }
        ]
    }],
    "payment_source": {
        "paypal": {
            "attributes": {
                "vault": {
                    "store_in_vault": "ON_SUCCESS",
                    "usage_type": "MERCHANT",
                    "usage_pattern": "SUBSCRIPTION_PREPAID"
                }
            },
            "experience_context": {
                "return_url": "https://example.com/returnUrl",
                "cancel_url": "https://example.com/cancelUrl"
            }
        }
    }
}'
```

## Use payment method token with checkout

After creating a payment method token and buyer agrees to a payment schedule, use the token with the Create Orders endpoint to charge buyers for recurring payments.

Use the vault ID as `vault_id` in `payment_source.paypal`, add `stored_credential` with `payment_initiator`, `usage`, and `usage_pattern`.

## Next steps

- Retrieve a payment token: `GET /v3/vault/payment-tokens/{id}`
- List all payment tokens: `GET /v3/vault/customer/payment-tokens`
- Delete a payment token: `DELETE /v3/vault/payment-tokens/{id}`

## Resources

- Save PayPal for purchase later with the JavaScript SDK
- Payment Method Tokens API
- Create Order v2 API
