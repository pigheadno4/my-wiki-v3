<!-- Source URL: https://developer.paypal.com/braintree/articles/guides/payment-methods/google-pay -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Google Pay
slug: /articles/guides/payment-methods/google-pay/
createTime: '2025-04-01T21:37:08.139Z'
updateTime: '2026-01-13T15:15:44.873Z'
---



# Google Pay

Google Pay includes access to Google's payment method vault, allowing customers to quickly and securely make purchases on their Android mobile devices. Businesses can accept Google Pay on [multiple browsers](#supported-browsers), making it quick and easy for customers to buy on both mobile and the web.

By selecting Google Pay in your Android app or web checkout, customers can pay using any cards or PayPal accounts associated with their Google accounts.


## Availability

Where your business is located dictates your ability to accept Google Pay. Most merchants based in the following regions – contingent on their processing settings – can accept Google Pay transactions from [eligible customers](#customer-availability) with the indicated payment method types:


- APAC - Visa, Mastercard, American Express*,[PayPal](#paypal-via-google-pay)
- Australia - Visa, Mastercard, American Express*,[PayPal](#paypal-via-google-pay)
- Canada - Visa, Mastercard, American Express*,[PayPal](#paypal-via-google-pay)
- Europe - Visa, Mastercard, American Express*,[PayPal](#paypal-via-google-pay)
- New Zealand - Visa, Mastercard, American Express*,[PayPal](#paypal-via-google-pay)
- United States - Visa, Mastercard, American Express, Discover,[PayPal](#paypal-via-google-pay)

*To be eligible to accept Google Pay with American Express in this region, you must be processing with your own Amex account.

If you are unsure of your setup, [contact us](/braintree/help/acceptPaymentTypes) for assistance.


**IMPORTANT**
 All merchants processing Google Pay transactions are subject to Google's terms of service. Keep in mind that Google has [detailed payment content policies](https://support.google.com/faqs/answer/75724), so you’ll want to make sure your specific goods or services are supported before setup.

 


### Customer availability

Google Pay customer availability depends on where a customer stores their payment methods: in a Google account or to an Android device.


#### Google accounts

Google Pay is available for all customers worldwide to make purchases using cards or PayPal accounts saved to their Google accounts.


#### Android devices

Some customers can make Google Pay purchases using payment methods saved directly to their Android devices. At this time, our eligible merchants can process this type of Google Pay transaction for customers in all countries and regions supported by Google Pay. For a complete list of locations where customers can pay with Google Pay payment methods stored to a device, [see Google's Help Center](https://support.google.com/pay/answer/9023773).


**IMPORTANT**
 Google's documentation only identifies the countries where customers can pay with this payment method. To accept Google Pay, merchants must be located in a country that is [eligible to onboard with Braintree](https://www.braintreepayments.com/country-selection) and [compatible with Google Pay](#availability).

 


### Supported browsers

Google Pay is now available across multiple browsers. See [Google's documentation](https://developers.google.com/pay/api/web/guides/setup#get-started) for a full list of supported web browsers.


## Processing

Google Pay card transactions process and settle just like credit card transactions, but can be identified in the Control Panel by their unique payment type logo.

Google Pay transactions settle like PayPal transactions and can be identified in the Control Panel by the Transaction Source of Google and Payment Type of PayPal Account.


### Fees

There are no additional standard fees for processing Google Pay transactions. Pricing for Google Pay cards is the same as your other credit card transactions and is priced similarly to your other PayPal transactions.


### Disputes

Chargebacks, retrievals, and pre-arbitrations on Google Pay transactions behave in the same way as your credit card or PayPal disputes, and should be responded to according to your merchant account setup. If you’re unsure how to handle a dispute, [Contact us](/braintree/help/ChargebackDisputeInfo) for assistance.


### Fraud tools

We recommend collecting billing address information, at minimum billing postal code, and passing that billing postal code with all Google Pay transactions as a best practice.

Our support for fraud checks on these transactions varies based on the type of Google Pay payment method:


- Cards from a customer's Google account are compatible with both our[risk threshold rules](/braintree/articles/guides/fraud-tools/basic/risk-threshold-rules)and our[Premium Fraud Management Tools](/braintree/articles/guides/fraud-tools/premium/overview).
- Cards added by the user directly to their Android device are not compatible with our[Basic Fraud Tools](/braintree/articles/guides/fraud-tools/basic/overview)but are compatible with our[Premium Fraud Management Tools](/braintree/articles/guides/fraud-tools/premium/overview).
- Google Pay transactions are not compatible with either our[Basic Fraud Tools](/braintree/articles/guides/fraud-tools/basic/overview)or[Premium Fraud Management Tools](/braintree/articles/guides/fraud-tools/premium/overview), but are covered by[PayPal Seller Protection](https://www.paypal.com/us/webapps/mpp/security/seller-protection). To qualify for Seller Protection and avoid certain types of chargebacks, you must:
- Pass a properly-formatted[shipping address](/braintree/docs/reference/request/transaction/sale/ruby#shipping)with each PayPal transaction.
- Meet PayPal's Seller Protection requirements.
- PayPal will not assess you a chargeback fee if the transaction is[eligible](https://www.paypal.com/us/webapps/mpp/ua/useragreement-full#seller-protection).




### Recurring billing and vaulting

Our support for vaulting Google Pay payment methods varies based on the payment method type:


- Google Pay cards stored to a Google account can be vaulted for future transactions,[recurring billing](/braintree/articles/guides/recurring-billing/overview), and split shipment transactions.
- Google Pay cards that were added directly to an Android device can only be vaulted for recurring billing and split shipment transactions. Each unique Google Pay transaction made with a card stored on a customer's Android device requires consent from the customer during checkout; as such, vaulting these payment methods for future transactions will result in declines and is not recommended.
- Google Pay accounts cannot be vaulted and are not supported for recurring billing or split shipment transactions.


## Setup

To add Google Pay to your Braintree integration, you'll need to update your application code and make sure Google Pay is enabled in your Control Panel. Whether you're adding Google Pay to an Android app or integrating for web, you need to receive approval from Google before moving to production. [See our developer docs for full details](/braintree/docs/guides/google-pay/overview).

