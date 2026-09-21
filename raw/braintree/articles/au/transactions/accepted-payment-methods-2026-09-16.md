<!-- Source URL: https://developer.paypal.com/braintree/articles/au/transactions/accepted-payment-methods -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Accepted Payment Methods
slug: /articles/au/transactions/accepted-payment-methods/
createTime: '2025-04-01T21:50:04.845Z'
updateTime: '2025-04-01T21:50:04.864Z'
---



# Accepted Payment Methods

In addition to credit and debit cards, you can process a variety of payment methods through your Braintree account. Here is a quick breakdown of the payment method options you can offer your customers.


## Card types

By default, your account is set up to accept the following card types:


- Visa
- Mastercard


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

Most merchants can accept [PayPal](/braintree/articles/guides/payment-methods/paypal/overview) transactions by entering their PayPal Business Account credentials into the Braintree Control Panel.


### Apple Pay

Most merchants with an iOS mobile app can enable [Apple Pay](/braintree/articles/guides/payment-methods/apple-pay) for [eligible customers](/braintree/articles/guides/payment-methods/apple-pay#customer-availability) to make purchases using their iOS devices.


### Google Pay

Most merchants can enable [Google Pay](/braintree/articles/guides/payment-methods/google-pay) for [eligible customers](/braintree/articles/guides/payment-methods/google-pay#customer-availability) to make purchases using Android devices.

