<!-- Source URL: https://developer.paypal.com/braintree/articles/adyen/transactions/accepted-payment-methods -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: '''Accepted Payment Methods'''
slug: /articles/adyen/transactions/accepted-payment-methods/
createTime: '2025-04-01T22:26:14.235Z'
updateTime: '2025-04-01T22:26:14.253Z'
---



# Accepted Payment Methods


## Card types

By default, your account is configured to accept the following card types:


- Visa
- Mastercard
- [American Express](/braintree/articles/adyen/pricing-fees#american-express)*

*Amex is available for a limited number of currencies – [contact us](/braintree/help) to see if the available options meet your needs.


## Currencies

Regardless of the currency of your customer’s bank account, they should be able to purchase from you. The transaction will be processed in the currency associated with your merchant account, and the customer’s bank will convert the charge to the customer's bank account currency. While this method requires no additional work to set up, customers may be charged a conversion fee or other fees by their banks. In addition, refunds become more difficult to process, which can lead to an increase in chargebacks.

You can reduce this friction for your customers by requesting an additional merchant account to charge customers directly in [one of the other currencies](/braintree/docs/reference/general/currencies) that we support. Our [Customer Success team](/braintree/help/acceptCurrencies) will guide you through this process and help you determine which presentment and settlement currencies apply to your account setup.

Once your additional currency is set up, the last step is updating your integration to [specify the new merchant account ID](/braintree/docs/reference/request/transaction/sale/ruby#specify-merchant-account-id) for your additional currency. You may need to check in with your developers for this part.

