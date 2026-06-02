---
title: Accept MyBank payments
slug: /docs/checkout/apm/mybank/
createTime: "2024-10-28T13:33:39.160Z"
updateTime: "2025-05-13T15:35:04.447Z"
---

# Accept MyBank payments

MyBank is a payment method in Europe.

| Countries                                                                                                                   | Payment type  | Payment flow | Currencies | Minimum amount | Refunds         |
| --------------------------------------------------------------------------------------------------------------------------- | ------------- | ------------ | ---------- | -------------- | --------------- |
| [](<https://developer.paypal.com/docs/checkout/apm/mybank/#italy-(it)bank-redirectredirecteurn/awithin-180-days>)Italy (IT) | bank redirect | redirect     | EUR        | N/A            | Within 180 days |

## How it works

![Alternative,payment,methods,diagram](assets/paypal-apm-unbranded-flow.svg)

- Your checkout page offers alternative payment methods.
- The buyer enters their personal details and selects an alternative payment method from your checkout page.
- The buyer is redirected to their selected issuing bank to confirm the purchase.
- The buyer authorizes and completes the payment.
- The buyer returns to your website to see the confirmation of the purchase.
- The merchant completes the payment process. PayPal transfers the funds to the merchant, and the transaction shows up in your PayPal account with the buyer's chosen payment method.

## Eligibility

- Available to merchants globally, except in Russia, Japan, and Brazil.
- Billing agreements, multiple seller payments, and shipping callback aren't supported.
- Support for order capture only (order authorize is not supported). See [authorized and captured payments](https://developer.paypal.com/api/nvp-soap/paypal-payments-standard/integration-guide/authcapture/) .
- Chargebacks aren't supported.
- Transaction must be an online purchase (buy online, pay in store is not supported).

## Integration methods

### JavaScript SDK

Use PayPal-hosted UI componentscalled payment fields to collect payment information for alternative payment methods.

### Orders REST API

Integrate directly usingthe Orders API to fully customize the checkout experience.
