<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/amex-express-checkout/testing-go-live -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Testing and Go Live
slug: /docs/guides/amex-express-checkout/testing-go-live/
createTime: '2025-04-02T01:48:58.091Z'
updateTime: '2025-04-02T01:48:58.194Z'
---



# Testing and Go Live


**AVAILABILITY**
Amex Express Checkout has been replaced with the latest unified checkout experience offered through Visa known as Secure Remote Commerce (SRC). If you were previously using Amex Express Checkout, you will need to [integrate with SRC](/braintree/docs/guides/secure-remote-commerce/overview) . SRC is currently in a limited release to [eligible merchants](/braintree/articles/guides/payment-methods/secure-remote-commerce#availability) , and the API is subject to change. It was introduced in Android v2, iOS v4, and JavaScript v3 of our Client SDKs. [Contact us](/braintree/help) to request access to the release.


## Sandbox Testing

Amex Express Checkout is different from traditional credit card processing which affects the testing
process. The card details are sent to Braintree by Amex and stored securely on our servers. You can
use the following Amex test account to perform test transactions against the Braintree sandbox. To
use the account, be sure to set the JavaScriptenvparameter of theamex:inittag toqa.
- **Username**: test_user
- **Password**: password
- **One-time access code**: 123456
- **CID**: 1234

If you would like to[use a test nonce](/braintree/docs/reference/general/testing#payment-method-nonces)in
the Braintree sandbox, please usefake-amex-express-checkout-nonce.
## Go live


- Change your JavaScriptenvparameter of theamex:inittag fromqatoproduction
- If possible, test your integration with a real American Express account

As always, please[contact us](/braintree/help/acceptPaymentTypes)if you have any
questions or concerns!