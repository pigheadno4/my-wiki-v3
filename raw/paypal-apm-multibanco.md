---
title: Accept Multibanco payments
slug: /docs/checkout/apm/multibanco/
createTime: "2024-10-25T05:21:33.575Z"
updateTime: "2025-05-14T10:19:59.078Z"
---

# Accept Multibanco payments

Multibanco is an interbank network in Portugal.

| Country       | Payment type | Payment flow | Currency | Maximum amount | Refunds |
| ------------- | ------------ | ------------ | -------- | -------------- | ------- |
| Portugal (PT) | voucher      | redirect     | EUR      | 99,999.99      | N/A     |

##

## How it works

![Alternative,payment,methods,diagram](assets/paypal-apm-unbranded-flow-non-instant.svg)

- The buyer chooses to pay with Multibanco.
- The buyer provides their first name and last name.
- The payment instruction is presented to the buyer.
- The buyer completes the payment via online banking or at a Multibanco ATM.
- The merchant receives the successful payment completion webhook notification and PayPal moves the funds to the merchant account.
- The merchant ships the goods.

## Integration methods

### JavaScript SDK

Use PayPal-hosted UI components called payment fields to collect payment information for alternative payment methods.

### Orders REST API

Integrate directly using the Orders API to fully customize the checkout experience.
