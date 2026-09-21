<!-- Source URL: https://developer.paypal.com/braintree/articles/get-started/payment-methods -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Payment Methods
slug: /articles/get-started/payment-methods/
createTime: '2025-04-01T23:10:45.911Z'
updateTime: '2026-01-23T10:24:44.924Z'
---



**NOTE**
Effective January 20, 2026, Visa Click to Pay (Secure Remote Commerce) will no longer be supported. After this date, any transaction attempted with Visa Click to Pay will receive a "Payment method not supported" error and risk payment decline.


# Payment Methods

Integrating with Braintree offers your customers many different ways to pay – and we’re always working on adding more. Here's a quick list of what we currently offer, and whom they are available to. For an overview of how to add payment method types to your integration, [see our developer docs](/braintree/docs/guides/payment-method-types-overview).


## ACH Direct Debit

Most merchants in the US can accept ACH Direct Debit transactions from participating customers. [Learn more about ACH Direct Debit.](/braintree/articles/guides/payment-methods/ach)


## Apple Pay

Most merchants located in the US, Canada, Europe, Australia, and APAC regions can accept Apple Pay transactions from participating customers – depending on your processor settings. [Learn more about Apple Pay.](/braintree/articles/guides/payment-methods/apple-pay)


## Google Pay

Most merchants located in the US, Canada, Europe, Australia, and APAC regions can accept Google Pay transactions from participating customers – with approval from Google. [Learn more about Google Pay.](/braintree/articles/guides/payment-methods/google-pay)


## Samsung Pay

Samsung Pay has been deprecated.


**IMPORTANT**
 This guide has been deprecated. Please use the [pay later offers guide](/braintree/articles/guides/payment-methods/paypal-pay-later-offers) instead.

 


## Card types


### Credit cards

Braintree’s US merchant accounts bundle Visa, Mastercard, Discover, UnionPay, JCB, and sometimes American Express as the default accepted payment types. Most of our international merchant accounts bundle Visa and Mastercard as the default accepted payment types. All merchants interested in accepting Amex should either indicate this on their application, or [contact us](/braintree/help/acceptPaymentTypes).


### Debit cards

When processing payments online, credit and debit cards are handled the same, as long as they are issued by a major card brand. Because PINs can't be accepted online, debit cards will always be run as credit.


### Dual-branded cards

Dual-branded cards include two different card brand logos and can be processed through either brand's network. Merchants can process these cards on whichever network is supported in their region. For example, some cards, such as Elo, are dual-branded as Discover cards. This means that even if Elo cards are not supported by your setup, dual-branded cards can be run on Discover's network, and will be reflected as Discover card transactions.


### Special-use cards

Credit and debit cards issued for specific purchases – like [HSAs and FSAs](https://usa.visa.com/run-your-business/commercial-solutions/enterprise-government-cards/healthcare-card.html) or [P-Cards](http://en.wikipedia.org/wiki/Purchasing_card) – can only be accepted if your merchant account is associated with the appropriate MCC (Merchant Category Code). If you aren’t sure what your MCC is, [contact us](/braintree/help/acceptPaymentTypes) for assistance.


## PayPal

Braintree is the only payment platform that allows you to accept both cards **and** PayPal through a single integration. PayPal is available to most of our merchants. [Learn more about PayPal.](/braintree/articles/guides/payment-methods/paypal/overview)


## Local Payment Methods

In addition to PayPal and cards, you can now offer the most relevant Local Payment Methods for your customers with a single Braintree integration. This will allow your cross-border customers to pay in their preferred Local Payment Methods while all payments settle into your PayPal account. [Learn more about Local Payment Methods.](/braintree/articles/guides/payment-methods/local-payment-methods)


## Venmo

Venmo allows customers on iOS and Android devices or on the desktop site to connect their Venmo account to your mobile app or desktop website – making it easy for them to make purchases using their bank account, credit and debit cards, or Venmo balance. Paying with Venmo is currently available for merchants in the US – [see our Venmo support article](/braintree/articles/guides/payment-methods/venmo) for more information.


## Secure Remote Commerce

Secure Remote Commerce (SRC) is a digital wallet that allows customers to store all of their major debit and credit cards in one account. With this single sign-in experience through Visa, customers can easily make purchases on your website or mobile app using any of the cards saved in their wallet. SRC is currently available in a limited release to eligible merchants – [see our SRC guide](/braintree/articles/guides/payment-methods/secure-remote-commerce) for more information.

[Next Page: Currencies](/braintree/articles/get-started/currencies)