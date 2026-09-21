<!-- Source URL: https://developer.paypal.com/braintree/articles/guides/payment-methods/secure-remote-commerce -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Secure Remote Commerce
slug: /articles/guides/payment-methods/secure-remote-commerce/
createTime: '2025-04-01T22:36:44.524Z'
updateTime: '2026-01-23T10:25:26.393Z'
---



**NOTE**
Effective January 20, 2026, Visa Click to Pay (Secure Remote Commerce) will no longer be supported. After this date, any transaction attempted with Visa Click to Pay will receive a "Payment method not supported" error and risk payment decline.


# Secure Remote Commerce


## Availability

Amex Express Checkout, Masterpass, and Visa Checkout have been replaced with the latest unified checkout experience offered through Visa known as Secure Remote Commerce (SRC). If you were previously using Amex Express Checkout or Masterpass, you will need to integrate with SRC following the instructions below. If you were using Visa Checkout, you do not have to change your integration as SRC is an updated version of Visa Checkout. As such, you may see Visa Checkout referenced elsewhere in our documentation. SRC is currently in a limited release. [Learn more.](/braintree/articles/guides/payment-methods/secure-remote-commerce#availability)

Secure Remote Commerce, which your customers will experience as Click to Pay, is a digital wallet that allows customers to store all of their major debit and credit cards in one account. With this single sign-in experience through Visa, customers can easily make purchases on your website or mobile app using any of the cards saved in their wallet.


## Availability

SRC is currently in limited release and is only available for merchants that are based in the following locations:


- Australia
- Canada
- France*
- Hong Kong
- Ireland
- Malaysia
- New Zealand
- Poland
- Singapore
- Spain
- United Kingdom
- United States

Eligible merchants must be using our iOS v4 or JavaScript v3 SDKs.

[Contact us](/braintree/help) to request access to the limited release.


## Customer availability

Customers can store the following card types in their SRC wallets:


- Visa
- Mastercard
- American Express
- Discover
- UnionPay


## Processing

Transactions using SRC process and settle just like credit card transactions. You can identify SRC transactions in the Control Panel by their unique payment type logo, which includes the credit card brand name at the bottom.


### Fees

There are no additional fees for processing SRC transactions – pricing for these transactions are the same as your other credit card transactions.


### Disputes

[Chargebacks, retrievals, and pre-arbs](/braintree/articles/risk-and-security/chargebacks-retrievals/overview) on SRC transactions behave the same way as your credit card disputes, and should be responded to according to your merchant account setup. If you’re unsure how to handle a dispute, [Contact us](/braintree/help/ChargebackDisputeInfo) for assistance.


### Fraud tools

SRC transactions are compatible with our AVS and risk threshold [Basic Fraud Tools](/braintree/articles/guides/fraud-tools/basic/overview), our [Premium Fraud Management Tools](/braintree/articles/guides/fraud-tools/premium/overview), and [3D Secure](/braintree/articles/guides/fraud-tools/3d-secure).


### Recurring billing and vaulting

SRC payment methods can be [vaulted](/braintree/articles/control-panel/vault/overview) and used for [recurring billing](/braintree/articles/guides/recurring-billing/overview).


## Setup

SRC is currently in a limited release. [Contact us](/braintree/help) if you're interested in accepting SRC using PayPal Braintree. Full integration instructions are available in our [developer docs](/braintree/docs/guides/secure-remote-commerce/overview).

