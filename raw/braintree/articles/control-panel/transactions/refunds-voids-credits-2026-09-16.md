<!-- Source URL: https://developer.paypal.com/braintree/articles/control-panel/transactions/refunds-voids-credits -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: 'Refunds, Voids, and Detached Credits'
slug: /articles/control-panel/transactions/refunds-voids-credits/
createTime: '2025-04-02T01:49:00.517Z'
updateTime: '2025-04-02T01:49:00.698Z'
---



# Refunds, Voids, and Detached Credits

When you need to return funds to a customer, there are a few different options:


- [**Refund**](#refunds): Transfers settled funds from your merchant account to the customer’s account
- [**Void**](#voids): Cancels the transfer of funds from the customer to you before the transaction settles
- [**Detached credit**](#detached-credits): Allows you to send funds to a customer without the original associated transaction, but is not always available as an option


## Refunds

You can only refund a transaction with a Settling or Settled status. If you need to cancel a transaction that has an Authorized, Submitted for Settlement, or Settlement Pending status, you may be able to issue a [void](#voids) instead.

You can choose to [issue a refund via the Control Panel](#issuing-a-refund-within-the-control-panel) or the [API](/braintree/docs/reference/request/transaction/refund). For most payment methods, transactions can be refunded any time after the transaction has settled, as long as the associated method is still active. PayPal and Venmo transactions can only be refunded within 180 days of receiving payment.

A refunded transaction goes through the [typical settlement process](/braintree/articles/get-started/transaction-lifecycle). As soon as the refund settles, the funds are sent back to the customer’s bank account. The customer's bank may take a couple of days to deposit these funds, so it is normal for your customer to experience a small delay.


**NOTE**
 Refunds go through a real-time refund authorization for select merchants in US and Australia. For more details, please refer to the [Refund Authorization guide](/braintree/articles/guides/refund-authorizations).

 


**IMPORTANT**
 If a customer makes a purchase in a currency other than their home currency and later requests a refund of that transaction, their refund amount may not exactly match their original transaction amount due to variable exchange rates. [See our article on single-currency setups](/braintree/articles/get-started/currencies#single-currency-setups) for more information.

 


### Issuing a refund within the Control Panel

To issue a refund in the Control Panel:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Transactions**in the navigation bar
- Scroll to the**Transaction Search**section
- Define your desired parameters and click the**Search**button
- Click on the desired transaction**ID**link
- Click the**Refund**button at the top of the page
- Make any adjustments to the amount (if needed)
- Click the**Refund**button


**NOTE**
 If you don't see the **Refund** button, it may be because you have already issued a refund or your user does not have the appropriate [role permissions](/braintree/articles/control-panel/users-roles/role-permissions). If the transaction was created through a merchant account that is no longer active, you’ll need to [issue a detached credit](#detached-credits) through an active merchant account.

 


### Finding a missing refund

Occasionally, a customer’s bank may have trouble routing a refund to the customer's account, particularly when the card used has been lost, stolen, or closed since the time of the original transaction. When this happens, depending on the bank, they might attempt to re-route the funds to the appropriate account, mail the customer a check, or return the funds to your merchant account.

If you are using Braintree Direct, you can further assist your customer by providing them with the [Acquirer Reference Number (ARN)](#acquirer-reference-numbers) to pass along to their bank. If you are using the Braintree gateway only and do not have a merchant account with us, you will need to contact your merchant account provider directly for a transaction's ARN.


#### Acquirer Reference Numbers

An Acquirer Reference Number (ARN), also referred to as a Trace ID, is a unique value assigned to a credit or debit card transaction once it has been processed. The ARN is used to track the transaction's movement – allowing card brands, card issuing banks, and processors to locate the transaction and confirm its handling.

ARNs can be useful in confirming a refund was processed for concerned customers. If you provide your customer with the ARN, their bank can trace the transaction using this value.

If your customer has contacted their bank with the ARN and is still unable to locate the funds, please [contact us](/braintree/help/TransactionProcessingQuestion).


##### Acquirer Reference Numbers in the Control Panel


**AVAILABILITY**
 ARNs are currently available for most Braintree Direct merchants located in the US or EU. If your account setup does not support ARNs in the Control Panel and you are integrated with Braintree Direct, [contact us](/braintree/help/TransactionProcessingQuestion) and we may be able to retrieve this value for you. ARNs are available for credit and debit card purchases – including those made with digital wallets or mobile devices.

 

A transaction's ARN is typically generated within 3 business days of the transaction moving to the [Settledstatus](/braintree/articles/get-started/transaction-lifecycle#settled). To find a transaction's Acquirer Reference Number:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Transactions**in the navigation bar
- Scroll to the**Transaction Search**section
- Define your desired parameters and click the**Search**button
- Click on the desired transaction**ID**link
- Scroll to the**Transaction Information**section

The Acquirer Reference Number can be found at the bottom of the **Transaction Information** section. Alternatively, ARNs are also listed in the [transaction search CSV download](/braintree/articles/control-panel/search#transactions).


**NOTE**
 If it has been more than 3 business days since the transaction moved to the Settled status, and the ARN has still not populated, [contact us](/braintree/help) for assistance.

 


## Voids

**Credit card**

In general, voids can only be issued if the transaction has a status of Authorized or Submitted for Settlement. PayPal transactions that have been submitted as [multiple partial settlements](/braintree/docs/reference/request/transaction/submit-for-partial-settlement), however, can also be voided with the status of Settlement Pending.

When a transaction is voided, the original authorization should disappear from the customer’s statement within 24 to 48 hours. You can choose to void a transaction either within the [Control Panel](#issuing-a-void-within-the-control-panel) or via the [API](/braintree/docs/reference/request/transaction/void).


**NOTE**
 Some banks don't recognize void requests immediately. It's possible that after you issue the void, your customer will still see the pending charge. If this happens, have your customer call their bank; the bank should be able to see the void request and update your customer's bank statement.

 

**ACH**

Voids cancel transactions and prevent money from being sent to the ACH network. This allows for a transaction to be reversed without any transfer of funds.

**Void timings**


- For a transaction on any day before 9:15 PM ET:
- Voidable: Until 9:15 PM ET
- Not voidable or refundable: Between 9:15 PM ET and 12:00 AM ET
- Not voidable or refundable: Transaction will move to aSettlement pendingstate at 10:00 PM ET
- Refundable: Transaction will move to aSettledstate after 12:00 AM ET


- For a transaction on any day between 9:15 PM and 9:45 PM ET:
- Not voidable nor refundable: Between 9:15 PM ET and 12:00 AM ET
- Not voidable or refundable: Transaction will move to aSettlement pendingstate at 10:00 PM ET
- Refundable: Transaction will move to aSettledstate after 12:00 AM ET


- For transactions on any day after 9:45 PM ET:
- Voidable: All transactions created after 9:45 PM ET are voidable till the following day at 9:15 PM ET




### Issuing a void within the Control Panel

To void a transaction in the Control Panel:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Transactions**in the navigation bar
- Scroll to the**Transaction Search**section
- Define your desired parameters and click the**Search**button
- Click on the desired transaction**ID**link
- Click the**Void**button at the top of the page
- Click**Continue**to confirm the void


**NOTE**
 If you don't see the **Void** button, it may be because the transaction has already settled or your user does not have the appropriate [role permissions](/braintree/articles/control-panel/users-roles/role-permissions).

 


## Detached credits


**NOTE**
 Depending on your account setup, you may not be able to issue detached credits.

 

Detached credits, also known as blind credits, are disabled by default because it is generally against card association (e.g. Visa, Mastercard) rules for a merchant to transfer funds to a credit card without a pre-existing sale transaction. However, there are instances in which you might have a legitimate sale transaction but are not able to issue a refund – making it necessary to issue a detached credit. Here are the most common situations:


- You are a new Braintree merchant and need to refund a transaction that was issued through your previous processor
- You are an existing Braintree merchant and need to refund a transaction that was issued through a Braintree merchant account that is no longer active
- ​Your customer has closed the account associated with their original payment method

Keep these rules in mind when considering detached credits:


- Detached credits cannot exceed the amount of the original sale transaction
- Credits cannot be enabled in your account permanently, because they increase the potential impact of a security breach


### Issuing detached credits

Before you can issue a detached credit, we'll need to temporarily enable them on your Braintree account. To request that we temporarily enable detached credits, have the authorized signer on your Braintree gateway account [contact us](/braintree/help/TransactionProcessingQuestion).

Once enabled, you'll be able to issue detached credits to new payment methods and payments methods that are already saved in your Vault.


#### New payment methods

To issue a detached credit to a new payment method:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Transactions**in the navigation bar
- Under the**Transaction Create**section, click the**New Transaction**button
- Scroll to the**Transaction Information**section
- In theTransaction Typedrop-down menu, choose**credit**
- Enter all required and any optional values
- Click the**Create Transaction**button


**NOTE**
 If you don't see the **Credit** option, but we’ve enabled detached credits on your account, it's possible that your user doesn’t have the appropriate [role permissions](/braintree/articles/control-panel/users-roles/role-permissions).

 


#### Existing payment methods

To issue a detached credit to an existing Vault record:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Transactions**in the navigation bar
- Under the**Transaction Create**section, click the**New Transaction**button
- Locate the customer you'd like to charge using the search bar under the**Want to create a transaction for an existing customer?**section
- Click the**Charge**link located to the right of your customer of choice to create a transaction using their default payment method
- If you want to charge a different payment method other than the customer's default, click on the desired payment method token**ID**instead and click the**New Transaction**button on the top of the Payment Method page


- In theTransaction Typedrop-down menu, choose**credit**
- Enter all required and any optional values
- Click the**Create**button


**NOTE**
 If you don't see the **Credit** option, but we’ve enabled detached credits on your account, it's possible that your user doesn’t have the appropriate [role permissions](/braintree/articles/control-panel/users-roles/role-permissions).

 

