<!-- Source URL: https://developer.paypal.com/braintree/articles/wells-flat/transactions/accepted-payment-methods -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Accepted Payment Methods
slug: /articles/wells-flat/transactions/accepted-payment-methods/
createTime: '2025-04-02T00:58:47.892Z'
updateTime: '2025-04-02T00:58:47.914Z'
---



# Accepted Payment Methods


## Card types

Your account is configured to accept the following card types as long as the card does not require a PIN or password:


- Visa
- Mastercard
- American Express
- Discover/Diners Club*
- JCB

*Diners Club cards are processed as Discover cards.


### Special note on American Express

If you process less than $1 million in annual volume on American Express, you can use Braintree's aggregated Amex. This is the easiest way to accept Amex and is enabled on your account by default, but it’s important to note that you will have less flexibility with your [descriptors](/braintree/articles/wells-flat/transactions/descriptors#american-express-descriptors).

Alternatively, you can apply for your own account directly through Amex. If you choose this option, your funding, descriptors, and chargebacks will be managed by Amex and you’ll need to contact them for support on these issues.


## Alternative payment methods

Most merchants can accept the following alternative payment methods. If you are a Braintree Marketplace merchant, [contact us](/braintree/help/acceptPaymentTypes) for more information on which payment methods are available to you.


### PayPal

Most merchants can accept [PayPal](/braintree/articles/guides/payment-methods/paypal/overview) transactions by entering their PayPal Business Account credentials into the Braintree Control Panel.


### ACH Direct Debit

[ACH Direct Debit](/braintree/articles/guides/payment-methods/ach) is currently available for eligible merchants located in the US.


### Apple Pay

Merchants with an iOS mobile app can enable [Apple Pay](/braintree/articles/guides/payment-methods/apple-pay) for [eligible customers](/braintree/articles/guides/payment-methods/apple-pay#customer-availability) to make purchases using their iOS devices.


### Google Pay

Most merchants can enable [Google Pay](/braintree/articles/guides/payment-methods/google-pay) for [eligible customers](/braintree/articles/guides/payment-methods/google-pay#customer-availability) to make purchases using Android devices.


### Pay with Venmo

Select US merchants can enable [Venmo](/braintree/articles/guides/payment-methods/venmo) as a payment method for customers using a personal Venmo account on an iOS or Android device.


### Samsung Pay

Samsung Pay has been deprecated.


**IMPORTANT**
 This guide has been deprecated. Please use the [pay later offers guide](/braintree/articles/guides/payment-methods/paypal-pay-later-offers) instead.

 


### Secure Remote Commerce

[Secure Remote Commerce (SRC)](/braintree/articles/guides/payment-methods/secure-remote-commerce) is currently available in limited release for eligible merchants located in the US to accept payments from customers using their SRC digital wallet.


## Currencies

Regardless of the currency of your customer’s bank account, they should be able to purchase from you. The transaction will be processed in the currency associated with your merchant account, and the customer’s bank will convert the charge to the customer's bank account currency. While this method requires no additional work to set up, customers may be charged a conversion fee or other fees by their banks. In addition, refunds become more difficult to process, which can lead to an increase in chargebacks.

You can reduce this friction for your customers by requesting an additional merchant account to charge customers directly in [one of the other currencies](/braintree/docs/reference/general/currencies) that we support. Our [Customer Success team](/braintree/help/acceptCurrencies) will guide you through this process and help you determine which presentment and settlement currencies apply to your account setup.

Once your additional currency is set up, the last step is updating your integration to [specify the new merchant account ID](/braintree/docs/reference/request/transaction/sale/ruby#specify-merchant-account-id) for your additional currency. You may need to check in with your developers for this part.


### Billing address

Merchants are recommended to collect and pass billing address information when storing payment methods and/or creating transactions. Passing billing address details (postal code at minimum) can help increase the likelihood of a successful authorization.

