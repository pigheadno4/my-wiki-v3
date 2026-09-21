<!-- Source URL: https://developer.paypal.com/braintree/articles/aib-af/transactions/authorizations -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Authorizations
slug: /articles/aib-af/transactions/authorizations/
createTime: '2025-04-01T23:38:20.474Z'
updateTime: '2025-04-01T23:38:20.488Z'
---



# Authorizations

When a transaction is in the [Authorized](/braintree/articles/get-started/transaction-lifecycle#authorized) status, your customer’s bank puts a hold on the funds needed to cover the cost of that transaction. If the transaction is later submitted for settlement, those funds will be debited from the customer’s bank account and routed into your merchant account.

If a pending authorization is not submitted for settlement in time, it will expire, and the customer’s bank will release the held funds. Authorization expiration timelines differ by card type; [learn more in our developer docs](/braintree/docs/reference/general/statuses#authorization-expired).

In the case of [voids](#voids) and [gateway rejections](#gateway-rejections), your customers may have to wait until authorizations expire before they will see held funds released back into their bank accounts.


## Voids

[Voids](/braintree/articles/control-panel/transactions/refunds-voids-credits#voids) occur when you cancel the transfer of held funds from a customer's bank account before the transaction settles. Typically, you can only void a transaction that has the status of [Authorized](/braintree/articles/get-started/transaction-lifecycle#authorized) or [Submitted for Settlement](/braintree/articles/get-started/transaction-lifecycle#submitted-for-settlement). When you void an Authorized transaction, the authorization should disappear from your customer’s bank account, and any held funds will be released within 24 to 48 hours.

If you are set up to automatically submit all authorized transactions for settlement, however, you will only be able to void transactions once they enter the Submitted for Settlement status.


### VoidingSubmitted for Settlementtransactions

When you void a Submitted for Settlement transaction, the funds held on the original authorization will not be released automatically. Instead, your customer will continue to see a pending authorization until it eventually [expires](/braintree/docs/reference/general/statuses#authorization-expired). When this happens, you can have your customer contact their bank; the bank should be able to see the void request and update your customer's bank statement.


## Gateway Rejections

A transaction will be [gateway rejected](/braintree/articles/control-panel/transactions/gateway-rejections) if it does not pass certain rules or settings in your Braintree gateway. Gateway rejections can occur after a transaction moves into the Authorized status, and your cardholder’s bank has already put a hold on the customer’s funds. When this happens, the gateway will then void the original authorization and the cardholder’s bank will release the funds.

If you are set up to automatically submit all authorized transactions for settlement, gateway rejections will be voided after the transaction has already entered the Submitted for Settlement status. [Learn more about voidingSubmitted for Settlementtransactions.](#voiding-submitted-for-settlement-transactions)

