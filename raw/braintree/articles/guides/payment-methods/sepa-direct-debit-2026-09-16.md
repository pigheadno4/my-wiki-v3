<!-- Source URL: https://developer.paypal.com/braintree/articles/guides/payment-methods/sepa-direct-debit -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: SEPA Direct Debit
slug: /articles/guides/payment-methods/sepa-direct-debit/
createTime: '2025-04-01T22:34:38.866Z'
updateTime: '2025-04-01T22:34:38.884Z'
---



# SEPA Direct Debit


**AVAILABILITY**
 SEPA Direct Debit is currently in limited release and is only available to pilot merchants. If you want to participate in the pilot, please [contact us](/braintree/help?issue=acceptPaymentTypes).

 

The Single Euro Payments Area (SEPA) is a payment-integration initiative of the European Union for simplification of bank transfers denominated in euro between member countries. SEPA enables customers to make cashless payments to any EUR bank account located in the area using a single bank account. To debit from SEPA bank accounts, the bank account holder must accept a mandate that gives debtors the authorization to debit the account.


## Setup

The first step to integrate with SEPA Direct Debit is to ensure you have [created, verified, and linked](/braintree/articles/guides/payment-methods/paypal/setup-guide) a valid PayPal business account in the Braintree Control Panel. Contact your account manager configure your PayPal account to process SEPA direct debit. You can then complete your client and server integrations. See our [developer docs](/braintree/docs/guides/sepa-direct-debit/overview) for full instructions.


## Processing


### Fees

Braintree does not charge additional processing fees for SEPA Direct Debit; you are only subject to the pricing and fee rates established by PayPal as per your user agreement. If you are unsure of these rates, you will need to [check with PayPal directly](/braintree/articles/guides/payment-methods/paypal/setup-guide#contacting-paypal-support). Transactions will be automatically presented to customers in Euros and the funds will settle into your PayPal business account in your primary currency. Any applicable currency conversion will be added to the customer’s payment amount.


### Returns

SEPA Direct Debit transactions can be returned for a variety of reasons. Although a majority of returns are received in 3 business days, returns can also be received after disbursement. In those cases, we deduct the amount from the next business day's disbursement and will display the transaction with a SEPA Direct Debit Return Code followed by Failed After Settlement in the Control Panel. For a full list of common SEPA Direct Debit return codes and associated descriptions, please refer to [SEPA Return Reason Code PDF](https://www.europeanpaymentscouncil.eu/sites/default/files/kb/file/2018-09/EPC135-18%20v1.0%20Guidance%20on%20Reason%20Codes%20for%20SCT%20R-transactions.pdf).


### Funding

Funds for SEPA Direct Debit will be settled into your PayPal account once your customer confirms a payment.


### Recurring transactions and vaulting support

Vaulting payment methods and creating recurring transactions is supported with SEPA Direct Debit. See our [vaulting docs](/braintree/docs/guides/sepa-direct-debit/vaulting) for full instructions.

