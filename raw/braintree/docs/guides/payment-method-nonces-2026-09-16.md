<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/payment-method-nonces -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Payment Method Nonces and Single-Use Payment Methods
slug: /docs/guides/payment-method-nonces/
createTime: '2025-04-02T02:10:28.122Z'
updateTime: '2025-04-02T02:10:28.136Z'
---



# Payment Method Nonces and Single-Use Payment Methods

In the SDKs, a payment method nonce is a secure, one-time-use reference to payment information. It's the key element that allows your server to communicate sensitive payment information to Braintree without ever touching the raw data.     In the GraphQL API, a payment method nonce is refered to as a single-use payment method and has the same functionality.     In this article, a single-use token will refer to both a payment method nonce and single-use payment method.


## Payment method types

A single-use token can reference any payment method. This can help keep your integration simple and lightweight; for example, you could use the same server-side code for creating a PayPal transaction as you use for creating a credit card transaction.


## Security

Security is important for all payment method types, but it's particularly critical for cards.     The Payment Card Industry Security Standards Council mandates compliance with their Data Security Standard (PCI DSS), and the less exposure your business has to raw card data, the easier it is to demonstrate compliance. Using single-use tokens in place of raw card data helps keep your PCI compliance burden to a minimum.      [Learn more about security and PCI compliance in our support articles.](/braintree/articles/risk-and-security/compliance/pci-compliance)


## Functionality

Braintree's servers will generate single-use tokens in response to requests from merchant clients and servers.     In general, your client will be responsible for handling the responses from Braintree and sending them to your server. Your server is then responsible for sending those single-use tokens back to Braintree on requests to perform certain actions.     You'll need a single-use token for two main purposes:


- To create transactions with the[SDK](/braintree/docs/guides/transactions)or[GraphQL API](/braintree/graphql/guides/transactions/#creating-transactions)
- To create or update payment methods in your Vault for repeat use with the[SDK](/braintree/docs/guides/payment-methods)or[GraphQL API](/braintree/graphql/guides/payment_methods/)


## Lifespan

A single-use token may only be used once. If it is not used, it expires 3 hours after being created.


## Learn more

See more documentation on single-use tokens.


- Basic Braintree-client-server interaction in our[Get Started guide](/braintree/docs/start/overview)
- Simple transaction sale calls in our[credit cards](/braintree/docs/guides/credit-cards/server-side#creating-transactions)and[PayPal](/braintree/docs/guides/paypal/server-side#creating-transactions)guides
- Simple payment method create call in our[API reference](/braintree/docs/reference/request/payment-method/create)
- Advanced payment method nonce usage in our[3D Secure guide](/braintree/docs/guides/3d-secure/overview)and[API reference](/braintree/docs/reference/request/payment-method-nonce/create)
- Sandbox testing details including[static payment method nonce test values](/braintree/docs/reference/general/testing#payment-method-nonces)

