---
title: Accept Bancontact payments
slug: /docs/checkout/apm/bancontact/
createTime: "2024-10-25T09:21:13.959Z"
updateTime: "2025-05-09T15:39:34.060Z"
---

# Accept Bancontact payments

Bancontact is the most widely used, accepted and trusted electronic payment method in Belgium, with over 15 million Bancontact cards issued, and 150,000 online transactions processed a day. Bancontact makes it possible to pay directly through the online payment systems of all major Belgian banks and can be used by all customers with a Bancontact branded payment card. Bancontact cards are issued by more than 20 Belgian banks and exists solely in Belgium.

| Countries   | Payment type  | Payment flow | Currencies | Minimum amount | Refunds         |
| ----------- | ------------- | ------------ | ---------- | -------------- | --------------- |
| Belgium(BE) | bank redirect | redirect     | EUR        | 1EUR           | Within 180 days |

## How it works

![Alternative,payment,methods,diagram](assets/paypal-apm-unbranded-flow.svg)

- Your checkout page offers alternative payment methods.
- The buyer provides their personal details and selects an alternative payment method from your checkout page.
- The buyer is transferred from your checkout page to the third-party bank to confirm the purchase.
- The buyer authorizes and confirms payment.
- The buyer returns to your site to see confirmation of purchase.
- The merchant initiates completion of payment. PayPal moves the funds to the merchant. Transaction shows in your PayPal account with the payment method the buyer used.

## Eligibility

- Available to merchants globally (excluding Russia, Japan, and Brazil).
- Billing agreements, multiple seller payments, and shipping callbacks are not supported.
- Only supports order capture (order authorization is not supported). See [authorised and captured payments](https://developer.paypal.com/api/nvp-soap/paypal-payments-standard/integration-guide/authcapture/) for details.
- Chargebacks are not supported.
- Transactions must be online purchases (buy online, pay in-store is not supported).

## Integration methods

### JavaScript SDK

Use PayPal-hosted UI componentscalled payment fields to collect payment information for alternative payment methods.

### Orders REST API

Integrate directly using the Orders API to fully customize the checkout experience.
