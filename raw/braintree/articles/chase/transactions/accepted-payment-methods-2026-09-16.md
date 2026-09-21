<!-- Source URL: https://developer.paypal.com/braintree/articles/chase/transactions/accepted-payment-methods -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Accepted Payment Methods
slug: /articles/chase/transactions/accepted-payment-methods/
createTime: '2025-04-01T22:58:43.370Z'
updateTime: '2025-04-01T22:58:43.393Z'
---



# Accepted Payment Methods


## Card types

By default, your account is set up to accept the following card types:


- Visa
- Mastercard
- Discover/Diners Club* (US only)

*Diners Club cards are processed as Discover cards.


### American Express

Your account is not configured to process American Express transactions by default. If you would like to accept this card type, you will need to apply for your own account directly through Amex.

Amex will manage funding, descriptors, chargebacks, and technical support for all Amex transactions.


#### Fees

We charge a per transaction fee for all Amex transactions in addition to any processing fees that are assessed by Amex directly. Amex will provide a separate statement for the fees they assess.


#### Setup

If you already process with Amex independently, you'll need to provide us with your Service Establishment Numbers (SE#s) and the currencies they correspond with. If you do not already have an Amex account, you’ll need to coordinate with us and Amex directly to set up an account and get your SE#s. [Contact us](/braintree/help/acceptPaymentTypes) to start this process.


**NOTE**
 Before we can enable Amex as an accepted payment method in your gateway, we will need to confirm that Amex pricing was specified in your original pricing agreement; if it was not, we will provide you with an Amex pricing agreement form to complete and sign.

 


## Alternative payment methods


### PayPal

Most merchants can accept PayPal transactions by entering their PayPal Business Account credentials into the Braintree Control Panel. Check out our [PayPal support article](/braintree/articles/guides/payment-methods/paypal/overview) to learn more about how to accept PayPal as a payment method with your Braintree account.


### Apple Pay

Most Chase merchants with an iOS mobile app can enable [Apple Pay](/braintree/articles/guides/payment-methods/apple-pay) for customers in [compatible countries](/braintree/articles/guides/payment-methods/apple-pay#location-requirements) to make purchases using their iOS devices. Chase currently supports Visa, Mastercard, Discover, and American Express credit cards on Apple Pay.


### Google Pay

Most merchants can enable [Google Pay](/braintree/articles/guides/payment-methods/google-pay) for [eligible customers](/braintree/articles/guides/payment-methods/google-pay#customer-availability) to make purchases using Android devices. Chase currently supports Visa, Mastercard, Discover, and American Express credit cards on Google Pay.


## Currencies

Regardless of the currency of your customer’s bank account, they should be able to purchase from you. The transaction will be processed in the currency associated with your merchant account, and the customer’s bank will convert the charge to the customer's bank account currency. While this method requires no additional work to set up, customers may be charged a conversion fee or other fees by their banks. In addition, refunds become more difficult to process, which can lead to an increase in chargebacks.

You can reduce this friction for your customers by requesting an additional merchant account to charge customers directly in [one of the other currencies](/braintree/docs/reference/general/currencies) that we support. Our [Customer Success team](/braintree/help/acceptCurrencies) will guide you through this process and help you determine which presentment and settlement currencies apply to your account setup.

Once your additional currency is set up, the last step is updating your integration to [specify the new merchant account ID](/braintree/docs/reference/request/transaction/sale/ruby#specify-merchant-account-id) for your additional currency. You may need to check in with your developers for this part.


**NOTE**
 Merchants domiciled in Canada are currently only able to present and settle in CAD – multi-currency setups are not available.

 

