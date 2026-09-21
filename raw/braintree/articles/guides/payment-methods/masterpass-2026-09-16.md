<!-- Source URL: https://developer.paypal.com/braintree/articles/guides/payment-methods/masterpass -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Masterpass
slug: /articles/guides/payment-methods/masterpass/
createTime: '2025-04-01T23:51:19.437Z'
updateTime: '2026-01-23T10:33:50.757Z'
---



# Masterpass


**AVAILABILITY**
 Masterpass has been replaced with the latest unified checkout experience offered through Visa known as Secure Remote Commerce (SRC). If you were previously using Masterpass, you will need to [integrate with SRC](/braintree/articles/guides/payment-methods/secure-remote-commerce).

 


**NOTE**
Effective January 20, 2026, Visa Click to Pay (Secure Remote Commerce) will no longer be supported. After this date, any transaction attempted with Visa Click to Pay will receive a "Payment method not supported" error and risk payment decline.

Masterpass by Mastercard is a digital wallet service that allows customers to store all of their payment and shipping information in one central, secure location. With Masterpass, customers can shop, click, and check out faster on your website.


### Customer availability

Your customers can store the following card types in their Masterpass wallet:


- American Express
- Diners Club
- Discover
- JCB
- Maestro
- Mastercard
- Visa


## Processing

Masterpass transactions process and settle just like credit card transactions. You can identify Masterpass transactions in the Control Panel by their unique payment type logo, which includes the credit card brand name at the bottom.


### Fees

There are no additional fees for processing Masterpass transactions – pricing for Masterpass is the same as your other credit card transactions.


### Disputes

[Chargebacks, retrievals, and pre-arbs](/braintree/articles/risk-and-security/chargebacks-retrievals/overview) on Masterpass transactions behave the same way as your credit card disputes, and should be responded to according to your merchant account setup. If you’re unsure how to handle a dispute, [Contact us](/braintree/help/ChargebackDisputeInfo) for assistance.


### Fraud tools

Masterpass transactions are compatible with our AVS and risk threshold [Basic Fraud Tools](/braintree/articles/guides/fraud-tools/basic/overview), and our [Premium Fraud Management Tools](/braintree/articles/guides/fraud-tools/premium/overview). CVV rules are bypassed for all Masterpass transactions, as Masterpass wallets do not save CVV values.


### Recurring billing and vaulting

Vaulting can only be used to support recurring transactions and you will need to obtain approval from Masterpass in order to do so. Masterpass does not support split shipments or one-off transactions with vaulted payment information.


## Setup

Full integration instructions are available in our [developer docs](/braintree/docs/guides/masterpass/overview).

