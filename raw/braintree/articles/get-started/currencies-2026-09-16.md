<!-- Source URL: https://developer.paypal.com/braintree/articles/get-started/currencies -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Currencies
slug: /articles/get-started/currencies/
createTime: '2025-04-02T01:04:36.775Z'
updateTime: '2025-04-02T01:04:36.794Z'
---



# Currencies

When it comes to payment processing, we look at currencies in two different contexts: **presentment** and **settlement**. It’s important to understand the difference between the two, because your presentment and settlement currencies can affect your reporting, feature availability, currency conversion, and more.


## Presentment currency

Your presentment currency is the currency that relates to your customer when they purchase from you. It can be the currency you show on your website or mobile app, and the currency that your customer is charged in. Depending on your account setup, you may be able to present in more than one currency.

We support more than [130 local currencies](/braintree/docs/reference/general/currencies) in 44 countries.


## Settlement currency

Your settlement currency is the currency in which your funds will be deposited into your business bank account. Depending on your account setup, you may only be able to settle in your home currency, or you may have the option to settle in multiple currencies. Typically, available settlement currencies are limited to the major currencies in your region.


## Currency setups

We offer options for both single currency and multi-currency setups. If you transact mostly with local customers, we recommend using the default [single currency setup](#single-currency-setups). If you transact with a larger international customer base, we recommend a [multi-currency setup](#multi-currency-setups).


### Single currency setups

By default, transactions will be presented and settled in your home currency. This method requires no additional work to set up, and if most of your transaction volume is domestic, this is all you need.

Regardless of the currency you present in, customers in our supported countries should be able to purchase from you. If a customer makes a purchase using a different currency, the customer's bank will convert the charge to their home currency, and they will be subject to their bank’s currency conversion rates.


**NOTE**
 If you sell to international customers, it can be tempting to display a converted price to those customers while still charging the transaction in your home currency. We do not recommend this approach, as conversion rates change frequently and it's possible for your customer to be charged a different amount than what you displayed at the time of the purchase. [Learn how to set up your account for multi-currency transactions.](#multi-currency-setups)

 


#### Refunds

Refunds with single currency setups can cause friction when you transact with international customers. Often times, the exchange rate will change in between the time that you process a transaction and when you issue the refund. As a result, the customer's refund may not match the amount they originally paid. To avoid these complications, we recommend [setting up your account for multi-currency transactions](#multi-currency-setups) if you have a large international base.


### Multi-currency setups

If you serve a large international customer base, we recommend a multi-currency setup. You can typically choose to present **or** settle in multiple currencies, subject to approval from any relevant banking partners and you successfully completing the integration of the required multi-currency accounts.


**IMPORTANT**
 Your account is not automatically configured to accept multiple currencies. By default, your merchant account will only be set up in your home currency. We will discuss your options for presentment and settlement currencies during our onboarding process, and it is your responsibility to ensure that you have received approval from any relevant banking partners and have successfully completed integration of the required multi-currency accounts before accepting multiple currencies.

 


#### Presentment

You can reduce currency conversion issues for your customers by requesting additional merchant accounts that present in any of our other supported currencies. When a customer makes a purchase in a presentment currency that's different from your settlement currency, the transaction amount will be converted to your settlement currency before being deposited.


#### Settlement

If the bulk of your processing is always in the same few presentment currencies (e.g. USD, GBP, and EUR), you may want to consider settling in those currencies as well. Depending on where and with whom you bank, you may need to have a different bank account for each settlement currency.


#### Integrating with multiple currencies

Once your additional currency is set up for your account, you must update your integration to [specify the new merchant account ID](/braintree/docs/reference/request/transaction/sale/ruby#specify-merchant-account-id) for each of your additional currencies. You may need to check in with your developers for this part.


**IMPORTANT**
 Before processing live transactions with a multi-currency setup, it is important to confirm that all of your desired currencies have been correctly configured by creating test transactions in the sandbox. Unless you have clearly specified during your onboarding process and in your integration, have received approval from any relevant banking partners, and have successfully completed integration of the required multi-currency accounts, live transactions will process only in your home currency, regardless of the pricing you present to your customers in your checkout flow.

 


## Testing currencies

You can try out processing other currencies by creating new merchant accounts in our testing environment, the Braintree sandbox. [Learn more about testing currencies in the sandbox.](/braintree/articles/get-started/try-it-out#testing-currencies)

