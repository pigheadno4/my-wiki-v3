<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/ach/testing-go-live -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Testing and Go Live
slug: /docs/guides/ach/testing-go-live/
createTime: '2025-04-01T21:56:33.485Z'
updateTime: '2025-04-01T21:56:33.518Z'
---



# Testing and Go Live


**AVAILABILITY**
ACH Direct Debit is available to [eligible merchants](/braintree/articles/guides/payment-methods/ach#availability) who can implement a custom client-side integration using our [JavaScript v3 SDK](/braintree/docs/guides/client-sdk/setup/javascript/v3) . It's currently not available in our Drop-in UI.


## Test values for sandbox verifications


### Routing numbers

When testing verification methods that require routing numbers, you can use any real 9-digit bank routing number (e.g. 011000015).
### Account numbers


#### For network check verifications

Use the test account numbers below to simulate the corresponding network check verification responses in the sandbox:

| Account Number | Verification Status | Processor Response Code | Additional Processor Response |
| --- | --- | --- | --- |
| 1000000000 |  | 1000 - Approved | N/A |
| 1000000001 |  | 1003 - Approved With Risk | N/A |
| 1000000002 |  | 3000 - Processor Network Unavailable – Try Again | N/A |
| 1000000004 |  | 2046 - Declined | N/A |
| 1000000005 |  | 2061 - Invalid Transaction Data | Invalid routing number |
| 1000000006 |  | 2092 - No Data Found - Try Another Verification Method | N/A |
| 1000000007 |  | 2092 - No Data Found - Try Another Verification Method | N/A |
| 1000000008 |  | 2061 - Invalid Transaction Data | Invalid account number |
| 1000000009 |  | 2061 - Invalid Transaction Data | Invalid account type (if selected account is of type 'checking') |
| Any other number |  | 2038 - Processor Declined | N/A |


#### For micro-transfer verifications

Use the test account numbers and micro-deposit amounts below to simulate the corresponding verification responses:

| Account Number | Verification Status | Micro-Deposit Amounts | Processor Response Code | Instant Settlement |
| --- | --- | --- | --- | --- |
| 1000000000 |  | 17 and 29 | 1000 - Approved | yes |
| 1000000001 |  | 17 and 29 | 1000 - Approved | no |
| 1000000002 |  | n/a | 3000 - Processor Network Unavailable – Try Again | no |
| 1000000003 |  | n/a | 2005 - Invalid Credit Card Number | no |
| Any other number |  | Random | 1000 - Approved | no |

Using account number 1000000000, once you pass the corresponding micro-deposit amounts, the verification will move to astate immediately.

Using account number 1000000001, the verification will go through a more realistic settlement simulation: the micro-transfers will take 3 business days to settle, and the verification will only move to astate once the micro-transfers have settled and you’ve passed the corresponding micro-deposit amounts.

If you use an account number outside of any of the above, the verification will move to thestate successfully, but the micro-deposit amounts will be random and not available to you, as would be the case in production.
#### For independent check verifications

The sandbox will return a successful verification using any number with 4-17 digits (e.g. 1000000000).
## Test values for sandbox transactions

Once a bank account has been markedin sandbox, you can create test transactions that simulate various processor responses you might receive on real-world transaction requests.
### Amounts for unsuccessful transactions

In sandbox, the transaction amount determines whether or not a transaction will be successful. Use the following amounts with a verified bank account to simulate unsuccessful transactions:

| Test Amount | Initial Status | Final Status |
| --- | --- | --- |
| 33333.33 | Failed | n/a |
| 44444.44 | Settlement Pending | Settlement Declined(insufficient funds)* |
| 55555.55 | Settlement Pending | Settlement Declined(unauthorized transaction)* |
| 6666.66 | Settlement Pending | Settlement Declined(account closed)* |
| 7777.77 | Settlement Pending | Settlement Declined(account not found)* |

See[Transaction Statuses](/braintree/articles/guides/payment-methods/ach#transaction-statuses)for more information about initial and final states.

*You'll receive a webhook notification if a transaction reaches a final status of Settlement Declined due to non-sufficient funds or unauthorized transaction (also known as an[unauth](/braintree/articles/guides/payment-methods/ach#disputes)).
### Amounts for successful transactions

Transactions in the sandbox will be successful as long as you use:


- A verified bank account payment method.
- A transaction amount**not**listed in the[test amounts table](#amounts-for-unsuccessful-transactions)above.


## Go live


- Make sure your production account settings mirror the ones in your tested sandbox configuration.
- If you've created any[Transaction webhooks](/braintree/docs/reference/general/webhooks/transaction)in sandbox, be sure to recreate them in your production account and point them to your production environment.
- [Contact us](/braintree/help/acceptPaymentTypes)to enable ACH Direct Debit payments in your production account.

