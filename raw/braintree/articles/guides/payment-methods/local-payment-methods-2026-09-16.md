<!-- Source URL: https://developer.paypal.com/braintree/articles/guides/payment-methods/local-payment-methods -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Local Payment Methods
slug: /articles/guides/payment-methods/local-payment-methods/
createTime: '2025-04-02T00:50:34.218Z'
updateTime: '2025-04-02T00:50:34.240Z'
---



# Local Payment Methods

Local Payment Methods allow customers to pay with banks, wallets, or other means that operate only in specific regions of the world. For example, your customer in the Netherlands might want to pay using iDEAL, which is used by more than 60% of consumers in the Netherlands for online purchases, whereas customers in Belgium on the same website might want to pay using Bancontact, a popular payment method there.


## Availability

Local Payment Methods are available to eligible merchants in [all countries that Braintree supports](https://www.braintreepayments.com/country-selection). In order to offer Local Payment Methods you must first add [PayPal](/braintree/articles/guides/payment-methods/paypal/setup-guide) to your Braintree integration. Transactions will be automatically presented to customers in Euros and the funds will settle into your PayPal business account in your primary currency. Any applicable currency conversion will be added to the customer’s payment amount.


### Customer Availability

Different Local Payment Methods are available to customers depending on their locality. To see which payment schemes are supported in each country, please refer to our [developer docs](/braintree/docs/guides/local-payment-methods/overview#supported-payment-methods). The Custom UI integration gives you full control over which payment methods you display on your checkout page based on the country your customers are located in.


## Setup

The only setup required for Local Payment Methods is to ensure you have [created, verified, and linked](/braintree/articles/guides/payment-methods/paypal/setup-guide) a valid PayPal business account in the Braintree Control Panel. You can then complete your client and server integrations. See our [developer docs](/braintree/docs/guides/local-payment-methods/overview) for full instructions.


## Processing


### Fees

Braintree does not charge additional processing fees for Local Payment Methods; you are only subject to the pricing and fee rates established by PayPal as per your user agreement. If you are unsure of these rates, you will need to [check with PayPal directly](/braintree/articles/guides/payment-methods/paypal/setup-guide#contacting-paypal-support).


### Funding

Funds for Local Payment Methods will be settled into your PayPal account once your customer confirms a payment.


### Disputes

Disputes are currently not supported for Local Payment Methods. Customers will need to work directly with their bank to handle disputes.


### Recurring transactions and vaulting support

Vaulting payment methods and creating recurring transactions are currently not supported with Local Payment Methods.


## Payment Contexts

Since most Local Payment Methods require you to redirect your customer to the Local Payment Method’s checkout flow, you can lose sight of customer activity as they are going through their checkout journey. Payment Contexts help provide more visibility into the payment lifecycle by capturing the payment initiation and Local Payment Method type details ahead of the transaction being created. Some possible uses for this information include allowing you to look for general conversion improvement, measure performance by payment method, and troubleshoot failed transactions.

Payment Contexts reflect the state of payment and stages that your customer goes through before you attempt to complete the [transaction](/braintree/docs/guides/transactions). This additional context includes steps such as when your customer starts a payment, if they abandon it, or when they finish the amount approval. This feature can be used when customers are completing checkout steps in the checkout flow of the payment method they selected rather than on your website.

Currently, this feature is available as a search function in your Braintree gateway.

To locate Payment Contexts:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Transactions**in the navigation bar
- Select the**Payment Contexts**tab
- Define your desired parameters and click the**Search**button


### Statuses

When a buyer clicks on a payment method, a Payment Context is created. Once created, each Payment Context goes through a series of stages, which are reflected in the Payment Context’s status.

Below are the possible statuses a Payment Context can fall into:

| Status | Description |
| --- | --- |
| Created | Payment has been initiated by customer |
| Expired | Payment has been abandoned/cancelled by customer |
| Approved | Payment has been completed on the Local Payment Method’s checkout flow by customer |
| Transacted | Merchant has attempted to complete the payment. At this point the Payment Context can show up in the**Transaction Search**asSettled. |

You can use these Payment Context statuses to gain insight into specific scenarios:


- See how many customers do not approve the payment by looking for Payment Contexts that have changed statuses fromCreatedtoExpired
- Check whether you have failed to transact by looking for Payment Contexts that have changed statuses fromCreatedtoApprovedtoExpired

