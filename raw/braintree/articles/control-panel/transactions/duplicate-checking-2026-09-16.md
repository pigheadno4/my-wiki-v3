<!-- Source URL: https://developer.paypal.com/braintree/articles/control-panel/transactions/duplicate-checking -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Duplicate Transaction Checking
slug: /articles/control-panel/transactions/duplicate-checking/
createTime: '2025-04-01T22:36:46.682Z'
updateTime: '2025-04-01T22:36:46.701Z'
---



# Duplicate Transaction Checking

Duplicate transactions can happen if a customer refreshes your checkout page or clicks your buy button multiple times, issuing a new API request with each click. Duplicate transaction checking prevents transaction requests from accidentally processing more than once.

Duplicate transaction checking logic is enabled in your gateway by default, but can be [turned off or updated in the Control Panel](#configuring-duplicate-transaction-checking).


**NOTE**
 While duplicate checking can help prevent repeat transactions from going through, we recommend talking with your developers to see if changes can be made to your form to reduce the likelihood of this occurring (e.g. disabling your buy button after it’s clicked).

 


## Duplicate checking logic

Our duplicate checking logic runs within a specific time frame. If all of the general and relevant payment method-specific conditions are met within the designated timeframe, any suspected duplicate transactions will be [Gateway Rejected](/braintree/articles/control-panel/transactions/gateway-rejections).

The timeframe for duplicate checking logic is set to 30 seconds by default, but can be updated to meet your needs in the [Control Panel](#configuring-duplicate-transaction-checking).


### General conditions

In order for a transaction to be Gateway Rejected as a duplicate transaction, it must meet all of the following conditions within the designated timeframe:


- Amount is the same as the initial transaction
- Order ID is the same (**if**collected and**if**the transaction**was not**created by Braintree's recurring billing functionality)
- Subscription ID is the same (**if**the transaction**was**created by Braintree's recurring billing functionality)
- The initial transaction was successful (status can beAuthorized,Submitted for Settlement,Settling,Settled, orVoided)


**NOTE**
 A duplicate transaction request is immediately rejected and will not wait on any in-flight transactions that are still pending a response from the card processing network. If the initial transaction is subsequently declined, neither transaction will be automatically retried.

 


### Payment method-specific conditions

In addition to the general conditions listed above, there are conditions specific to supported payment methods. For the following payment methods, the listed condition must also be true in order for our duplicate transaction logic to reject the transaction:


- Google Pay or Apple Pay – DPAN is the same
- PayPal – payer email address is the same
- Credit card – number and expiration date are the same


## Configuring duplicate transaction checking

Duplicate transaction checking is enabled by default with a 30 second window in both the sandbox and production environments. These settings can be updated or disabled by users with Account Admin permissions.


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on the gear icon in the top right corner
- Click**Processing**from the drop-down menu
- Scroll to the**Transactions**section
- Next to**Duplicate Transaction Checking**, you can:
- Click the toggle to enable or disable this feature
- Click the**Options**link below the toggle to make changes to the timeframe



