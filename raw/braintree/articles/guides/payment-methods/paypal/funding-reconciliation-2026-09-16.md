<!-- Source URL: https://developer.paypal.com/braintree/articles/guides/payment-methods/paypal/funding-reconciliation -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Funding and Reconciliation
slug: /articles/guides/payment-methods/paypal/funding-reconciliation/
createTime: '2025-04-02T01:11:11.557Z'
updateTime: '2025-04-02T01:11:11.575Z'
---



# Funding and Reconciliation


## Funding


**NOTE**
 Using PayPal **will not** affect your funding process for credit card transactions.

 

By default, PayPal transactions are funded by PayPal to your PayPal Business Account’s balance. If you’d like to deposit these funds into your bank account, you have two options:


- Manually withdraw the funds using your[PayPal console](https://www.paypal.com/login)
- [Contact PayPal](/braintree/articles/guides/payment-methods/paypal/setup-guide#contacting-paypal-support)to set up Settlement Withdrawal

Settlement Withdrawal automatically sends the previous day's transactions to your bank within 2-3 business days. With this feature enabled, you’ll be able to go to your PayPal console and download a daily report of the transactions that were included in each withdrawal.


## Reconciliation

PayPal has [many reports](https://www.paypal.com/cgi-bin/webscr?cmd=p/xcl/rec/reports-products-outside) available to reconcile your account. For larger merchants, the PayPal Transaction Details and PayPal Settlement Report are both popular reconciliation options. For small to medium merchants, PayPal recommends using the PayPal Monthly Financial Summary report.

Regardless of your business's size, all of these reports can be used in conjunction with Braintree's [Settlement Batch Summary](/braintree/articles/control-panel/reporting/settlement-batch-summary) report in order to reconcile your account.


### Searching for specific transactions

When reconciling PayPal transactions, we recommend looking up the transaction details in the PayPal console; there you will find additional details that aren’t available in the Braintree Control Panel (e.g. fees assessed, net deposit amount). You can locate specific transactions in the PayPal console by searching for either the customer’s PayPal email address or the Transaction ID.

The Transaction ID in the PayPal console is a unique identifier for an individual transaction set by PayPal; within the Braintree Control Panel, we refer to this value as the Authorization Unique Transaction ID. It’s important to note that this value is different from the Braintree transaction ID.

To find the Authorization Unique Transaction ID:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Transactions**in the navigation bar
- Scroll to the**Transaction Search**section
- Define your desired parameters and click the**Search**button
- Click on the desired transaction**ID**link
- Scroll to the**Payment Information**section
- Locate theAuthorization Unique Transaction IDfield; this value will match the Transaction ID in the PayPal console

Alternatively, you can [search for the transaction details via the API](/braintree/docs/reference/request/transaction/search).

