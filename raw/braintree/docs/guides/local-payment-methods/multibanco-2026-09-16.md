<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/local-payment-methods/multibanco -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Multibanco
slug: /docs/guides/local-payment-methods/multibanco/
createTime: '2025-04-02T01:47:11.633Z'
updateTime: '2025-04-02T01:47:11.665Z'
---



# Multibanco


### Configuration


**AVAILABILITY**
Multibanco is currently in limited release and is available to pilot merchants in any [supported merchant country](https://www.braintreepayments.com/country-selection) except Brazil, Japan, and Russia. For customers, it is limited to buyers in Portugal only. If you want to participate in the pilot, please [contact us](/braintree/help/acceptPaymentTypes) .

Multibanco is a voucher-based payment scheme that is created online but is paid for at an ATM with a debit card, or using online banking. This payment scheme differs from other "instant" payments in that the buyer has up to 7 days to complete the payment. Before you can accept Multibanco, you will need to ensure you have completed the following steps:


- [Create, verify, and link](/braintree/articles/guides/payment-methods/paypal/setup-guide)your PayPal business account in the Braintree Control Panel. In order to process Local Payment Methods, you need to have a valid PayPal business account.


### Capturing Non-Instant Transaction

There is no capture call for non-instant transactions; Braintree will associate a transaction on behalf of the merchant once we receive confirmation that the voucher has been paid.


**NOTE**
In sandbox, use the approval URL to display a modal in which you can simulate a successful payment, an expired payment, or an unapproved payment. If successful payment is selected, a webhook will be sent to the merchant in 2-3 minutes and the payment context will update to show an associated transaction.


### Server Side with GraphQL


**NOTE**
Use [GraphQL](/braintree/graphql/integration_guides/non_instant_local_payments) to create a local payment transaction.


### Configure webhooks

A webhook integration is required for Multibanco. Webhooks serve as confirmation of a successful payment as well as notification of an expired payment voucher.[See the webhooks guide](/braintree/docs/guides/webhooks/overview)for a general overview on how to configure webhooks.

Below is an example of a Local Payment funded webhook for when the buyer has completed the payment:
### JSON
```javascript
{ 
    "local_payment_funded": { 
        "payment_id": "the_payment_id", 
        "payment_context_id": "the_payment_context_id", 
        "transaction": { 
            "id": "the_transaction_id", 
            "amount": 1.00, 
            "currency_iso_code": "EUR", 
            "created_at": "2021-07-28", 
            "order_id": "the_order_id", 
            "status": "settled" 
        } 
    } 
}
```
Below is an example of a Local Payment expired webhook for when the voucher has expired:
### JSON
```javascript
{ 
    "local_payment_expired": { 
        "payment_id": "the_payment_id", 
        "payment_context_id": "the_payment_context_id" 
    } 
}
```
[See the Local Payment Method webhooks reference](/braintree/docs/reference/general/webhooks/local-payment-methods)for details on the exact content of the Local Payment Method completed notification.