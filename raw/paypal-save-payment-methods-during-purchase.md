<!-- Source URL: https://developer.paypal.com/docs/checkout/save-payment-methods/during-purchase/ -->
<!-- Fetched: 2026-04-14 -->

---
title: Save payment methods during purchase
slug: /docs/checkout/save-payment-methods/during-purchase/
createTime: '2024-05-15T17:40:40.419Z'
updateTime: '2025-03-11T23:21:39.014Z'
---


# Save payment methods during purchase

PayPal's JavaScript, iOS, and Android SDKs as well as the Orders API support saving payment methods during checkout.



## Choose your integration 

### JavaScript SDK
Integrate client-side or server-side. Saves PayPal, Venmo, and credit or debit cards.


### Orders API
Integrate server-side. Saves PayPal and credit or debit cards.


### Android SDK
Saves PayPal and credit or debit cards.


### iOS SDK
Saves PayPal and credit or debit cards.


**warning**
**Warning:** To continue providing a Pay Later option at checkout, it is essential that you integrate Billing With Purchase. This solution offers the same functionalities as Billing Agreement and is compatible with your existing payment options.



## JavaScript SDK best practice 
If you have a [client-side integration](/docs/checkout/standard/) , you can only save PayPal Wallets. We recommend a [client-side and server-side integration](/docs/checkout/advanced/) to save more payment methods.
