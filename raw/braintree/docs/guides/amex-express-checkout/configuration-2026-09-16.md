<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/amex-express-checkout/configuration -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Configuration
slug: /docs/guides/amex-express-checkout/configuration/
createTime: '2025-04-02T01:57:23.552Z'
updateTime: '2025-04-02T01:57:23.571Z'
---



# Configuration


**AVAILABILITY**
Amex Express Checkout has been replaced with the latest unified checkout experience offered through Visa known as Secure Remote Commerce (SRC). If you were previously using Amex Express Checkout, you will need to [integrate with SRC](/braintree/docs/guides/secure-remote-commerce/overview) . SRC is currently in a limited release to [eligible merchants](/braintree/articles/guides/payment-methods/secure-remote-commerce#availability) , and the API is subject to change. It was introduced in Android v2, iOS v4, and JavaScript v3 of our Client SDKs. [Contact us](/braintree/help) to request access to the release.

In order to use this feature, you will first need to enable Amex Express Checkout in the Control
Panel.
## Enabling Amex Express Checkout


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on the gear icon in the top right corner
- Click**Processing**from the drop-down menu
- Scroll to the**Payment Methods**section
- Next to**Amex Express Checkout**, click the**Enable**button
- Complete the signup form
- Click the**Submit**button

After submitting the signup form, you will be redirected to a configuration page containing yourclient_idandclient_key, which you'll need in order to configure the Amex
Express Checkout tag on your checkout page. You'll need to follow the same steps in your sandbox
account in order to test your integration.