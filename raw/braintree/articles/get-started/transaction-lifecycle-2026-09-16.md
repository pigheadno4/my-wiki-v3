<!-- Source URL: https://developer.paypal.com/braintree/articles/get-started/transaction-lifecycle -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Transaction Lifecycle
slug: /articles/get-started/transaction-lifecycle/
createTime: '2025-04-01T21:37:02.127Z'
updateTime: '2025-04-01T21:37:02.146Z'
---



# Transaction Lifecycle

As money travels from the customer to your bank account, the transaction is given a series of statuses. A **successful** transaction will go through the following statuses:

![transaction,statuses](https://www.paypalobjects.com/btdevdoc/braintree/img/articles/transaction-status.png)

Transaction statuses can help you understand where your money is in the transaction lifecycle.


## Authorized

When a purchase is first submitted by a customer, we start by checking with the customer’s bank to see if the payment method is legitimate and has sufficient funds to pay for your product or service. If the customer's bank approves, the transaction will be given an Authorized status. An authorization puts a hold on the funds in the customer’s account, but doesn’t remove any funds just yet.


## Submitted for Settlement

Eventually, authorizations will expire. In order to collect funds, a transaction needs to be submitted for settlement – which happens by default when creating transactions via the Control Panel. Transactions with the Submitted for Settlement status (also known in the payments industry as captured or capturing) indicate that the process of removing money from the customer's account has been initiated.

In most cases, you’ll want to submit a transaction for settlement at the same time that you authorize the payment. Some merchants that ship physical goods wait to submit for settlement until after the product has shipped in order to reduce chargebacks. [Learn more about extended authorizations.](/braintree/articles/control-panel/transactions/managing-authorizations)


## Settling

When we begin communicating with the processor about the settlement request, the transaction will move from Submitted for Settlement to Settling. The amount of time a transaction spends in the Settling state depends on the processing bank. [Contact us](/braintree/help/TransactionProcessingQuestion) if you have questions on transactions with a Settling status.


## Settled

This is when the money moves from your customer’s bank through your merchant account. Once the money hits your merchant account, the transaction will display as Settled, and the funds will be routed to your bank account.


## Other statuses

If the transaction is unsuccessful, or is interrupted in some way, there are other transaction statuses that can indicate what is happening. [Learn more about all of the possible statuses transactions can have.](/braintree/docs/reference/general/statuses#transaction)

