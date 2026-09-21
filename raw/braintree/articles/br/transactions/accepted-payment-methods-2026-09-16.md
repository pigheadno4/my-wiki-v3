<!-- Source URL: https://developer.paypal.com/braintree/articles/br/transactions/accepted-payment-methods -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Accepted Payment Methods
slug: /articles/br/transactions/accepted-payment-methods/
createTime: '2025-04-01T22:46:53.529Z'
updateTime: '2025-04-01T22:46:53.543Z'
---



# Accepted Payment Methods


## Card types

By default, your account is set up to accept the following card types:


- Visa
- Mastercard
- Amex
- Elo
- Hipercard


### Combo cards

Brazilian issuers support combo cards, which can be used either as credit or debit cards. You can specify the card type of a combo card by using the account_type field in the 3DS and/or in the transaction sale call. Unlike other types of cards, there is not a specific indicator to determine if a card is a combo card, so you will need to ensure Brazilian customers have the ability to select an account type as needed.


### American Express

Your American Express processing will be done with local acquirers in Brazil and your account is configured to process American Express transactions by default. You will **not** need to apply for your own Amex merchant account.

Braintree will manage funding, descriptors, chargebacks, and technical support for all Amex transactions. Along with transactions from other card brands, Amex transactions will be included in the statement provided by Braintree.


## Currencies

Presentment in Brazilian Reals (BRL) is supported in Brazil. Regardless of the currency of your customer’s bank account, they should be able to purchase from you. The transaction will be processed in the currency associated with your merchant account, which will be in BRL. The customer’s bank will convert the charge to the customer's bank account currency. While this method requires no additional work to set up, customers may be charged a conversion fee or other fees by their banks. In addition, refunds become more difficult to process, which can lead to an increase in chargebacks.

