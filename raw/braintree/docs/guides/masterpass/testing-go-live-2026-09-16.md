<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/masterpass/testing-go-live -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Testing and Go Live
slug: /docs/guides/masterpass/testing-go-live/
createTime: '2025-04-02T00:19:56.680Z'
updateTime: '2025-04-02T00:19:56.697Z'
---



# Testing and Go Live


**AVAILABILITY**
Masterpass has been replaced with the latest unified checkout experience offered through Visa known as Secure Remote Commerce (SRC). If you were previously using Masterpass, you will need to [integrate with SRC](/braintree/docs/guides/secure-remote-commerce/overview) . SRC is currently in a limited release to [eligible merchants](/braintree/articles/guides/payment-methods/secure-remote-commerce#availability) , and the API is subject to change. It was introduced in Android v2, iOS v4, and JavaScript v3 of our Client SDKs. [Contact us](/braintree/help) to request access to the release.


## Testing

The sandbox environment only accepts[test credit card numbers](/braintree/docs/reference/general/testing#credit-card-numbers). Vaulting or transacting with any other credit card numbers will result in a validation error.
### Nonces

In order to simplify testing your server-side code, you can use the static nonces below to simulate
a credit card originating from Masterpass.| Nonce | Description |
| --- | --- |
| `fake-masterpass-amex-nonce` | A nonce representing an American Express card from Masterpass |
| `fake-masterpass-discover-nonce` | A nonce representing a Discover card from Masterpass |
| `fake-masterpass-mastercard-nonce` | A nonce representing a Mastercard card from Masterpass |
| `fake-masterpass-visa-nonce` | A nonce representing a Visa card from Masterpass |

