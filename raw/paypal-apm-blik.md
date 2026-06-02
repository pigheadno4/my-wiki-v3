---
title: Accept BLIK payments
slug: /docs/checkout/apm/blik/
createTime: "2024-10-25T11:16:22.465Z"
updateTime: "2025-05-09T11:13:59.384Z"
---

# Accept BLIK payments

BLIK is a payment method in Poland.

| Countries  | Payment type  | Payment flow | Currencies | Minimum amount | Refunds         |
| ---------- | ------------- | ------------ | ---------- | -------------- | --------------- |
| Poland(PL) | bank redirect | redirect     | PLN        | 1PLN           | Within 180 days |

## How it works

![Alternative,payment,methods,diagram](assets/paypal-apm-unbranded-flow.svg)

- Your checkout page offers alternative payment methods.
- The buyer enters their personal details and selects an alternative payment method from your checkout page.
- The buyer is redirected to their selected issuing bank to confirm the purchase.
- The buyer authorizes and completes the payment.
- The buyer returns to your website to see the confirmation of the purchase.
- The merchant completes the payment process. PayPal transfers the funds to the merchant, and the transaction shows up in your PayPal account with the buyer's chosen payment method.

## Eligibility

- Available to merchants globally (excluding Russia, Japan, and Brazil).
- Billing agreements, multiple seller payments, and shipping callbacks are not supported.
- Only supports order capture (order authorization is not supported). See [authorised and captured payments](https://developer.paypal.com/api/nvp-soap/paypal-payments-standard/integration-guide/authcapture/) for details.
- Chargebacks are not supported.
- Transactions must be online purchases (buy online, pay in-store is not supported).

## Integration methods

### JavaScript SDK

Use PayPal-hosted UI components called payment fields to collect payment information for alternative payment methods.

### Orders REST API

Integrate directly using the Orders API to fully customize the checkout experience.
