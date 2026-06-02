---
title: Accept Przelewy24 payments
slug: /docs/checkout/apm/przelewy24/
createTime: "2024-10-28T11:06:19.151Z"
updateTime: "2025-05-12T16:43:29.229Z"
---

# Accept Przelewy24 payments

Przelewy24 is a payment method in Poland.

| Countries                                                                     | Payment type  | Payment flow | Currencies | Minimum amount | Refunds         |
| ----------------------------------------------------------------------------- | ------------- | ------------ | ---------- | -------------- | --------------- |
| [](<#poland-(pl)bank-redirectredirectpln-eur1-plnwithin-180-days>)Poland (PL) | bank redirect | redirect     | PLN EUR    | 1PLN           | Within 180 days |

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

Use PayPal-hosted UI components called payment fields to collect payment information for alternative payment methods.

### Orders REST API

Integrate directly using the Orders API to fully customize the checkout experience.
