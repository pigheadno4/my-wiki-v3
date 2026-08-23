---
title: "Braintree Server SDK"
type: concept
category: technology
tags: [braintree, server-sdk, checkout, transactions, vault, subscriptions, webhooks]
---

## Braintree Server SDK

Braintree server SDKs connect a merchant backend to the Braintree Gateway. Client SDKs collect or approve a payment method and return a payment-method nonce or vaulted token; the server SDK uses that identifier for transaction, vault, subscription, and related gateway operations. A server SDK does not render checkout or establish that a payment method is enabled for a merchant or buyer.

## Shared Integration Model

The independently retained Node, PHP, and Ruby packages expose the same broad boundary through language-specific APIs:

- generate client tokens for browser or native SDK initialization;
- create and manage customers and vaulted payment methods;
- authorize transactions, submit them for settlement, partially settle, void, and refund;
- process PayPal and Venmo instruments returned by supported client integrations;
- create and manage plans and subscriptions; and
- verify and parse signed webhook notifications.

Exact methods, credential rules, transport behavior, supported runtime versions, and release changes remain package-qualified. Evidence from one language SDK must not be attributed to another without confirming it in that package's retained source.

## Checkout and Credential Boundary

Merchant backends must calculate trusted amounts and decide fulfillment from server-side state. A nonce is a short-lived processing input, while a vaulted token identifies a reusable payment method subject to product and merchant eligibility. Immediate settlement submission is optional; merchants can also authorize first and submit later.

Both retained SDKs support merchant API-key credentials and OAuth access tokens for ordinary gateway calls. The PHP implementation additionally makes the webhook boundary explicit: verification requires public/private API keys, so an access token alone is insufficient for webhook parsing.

## Versioned Evidence

- `braintree@3.39.0` at SHA `7a9270aaf31eb87819add64a768652243f90007c` is the retained Node.js baseline.
- `braintree_php@6.37.0` at SHA `0f53ece38397c9fed05b94620634a5a23ef8ee48` is the retained PHP baseline.
- `braintree@4.40.0` at SHA `1217992763cc13f33dbd8b6c51ad2ae058ddd2a8` is the retained Ruby baseline.

The Node and PHP baselines expose `preferredPaymentMethodToken` during client-token generation; the Ruby `4.40.0` client-token signature does not. All three warn that legacy Venmo SDK parameters are unsupported in favor of Pay with Venmo. This confirms the broad gateway contract while also demonstrating why optional fields must remain package-qualified. Current enablement and client experience still require client-SDK and product documentation evidence.

## Related

- [[source-github-braintree-node]] - Node.js server SDK implementation evidence
- [[changelog-github-braintree-node]] - Node.js package release ledger
- [[source-github-braintree-php]] - PHP server SDK implementation evidence
- [[changelog-github-braintree-php]] - PHP package release ledger
- [[source-github-braintree-ruby]] - Ruby server SDK implementation evidence
- [[changelog-github-braintree-ruby]] - Ruby package release ledger
- [[braintree-web-sdk]] - browser tokenization and nonce handoff
- [[braintree-android-sdk]] - native Android nonce handoff
- [[braintree-ios-sdk]] - native iOS nonce handoff
- [[paypal-braintree-integration]] - PayPal client approval and Braintree processing boundary
