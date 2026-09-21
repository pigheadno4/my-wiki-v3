<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/venmo/testing-go-live -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Testing and Go Live
slug: /docs/guides/venmo/testing-go-live/
createTime: '2025-04-02T02:10:07.337Z'
updateTime: '2025-04-02T02:10:07.355Z'
---



# Testing and Go Live


## Sandbox testing

Sandbox behavior is limited to testing the app switch flow that returns a payment method nonce. As a
result:
- The app switch flow will show a test merchant with Braintree's logo instead of your own business's details
- A successful app switch will always return a nonce for a test user named VenmoJoe
- Purchases made in sandbox will**not**be reflected in the Venmo app
- [Removing a connection from Venmo](/braintree/docs/guides/venmo/server-side#removing-connections)to a sandbox app is not allowed. Attempting to do so will result in a 400 response.

If you would like to[use a test nonce](/braintree/docs/reference/general/testing#payment-method-nonces)in
the Braintree sandbox, please usefake-venmo-account-nonce.
##### Creating test disputes

When creating a Venmo transaction in the sandbox with thefake-venmo-account-nonce, the
following transaction amounts will create a dispute:AmountDispute Status| 62.00 | Under Review |
| 62.01 | Open |

You can test responding to Venmo disputes[in the Control Panel](/braintree/docs/reference/general/testing/ruby#venmo-disputes)and[via our SDKs](/braintree/docs/guides/disputes/testing-go-live/ruby#simulating-a-won-dispute)by submitting specific evidence when responding to the dispute.
## Go live

Once you’ve finished testing your integration and you’re ready to go live, you’ll need to[set up Venmo in your production Control Panel and complete your application](/braintree/articles/guides/payment-methods/venmo#go-live). We will review your application and enable Venmo payments for your production environment upon
approval.