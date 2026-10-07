---
title: "Braintree Payment Request Setup and Integration (JavaScript v3)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/payment-request/setup-and-integration/javascript/v3"
raw_files:
  - "braintree/docs/guides/payment-request/setup-and-integration/javascript/v3-2026-09-16.md"
tags: [braintree, payment-request, javascript, google-pay, payment-method-nonce]
---

## Overview

Braintree-hosted JavaScript v3 setup guide for using the browser Payment Request API through Braintree's `PaymentRequestComponent`. It covers browser and transport prerequisites, payment-method configuration, component loading and initialization, tokenization, and the payment-method nonce handoff to a merchant server. This is a fetched website snapshot, not proof of current browser support, merchant enablement, successful authorization, transaction creation, settlement, or vaulting. See [[braintree]] and [[braintree-web-sdk]].

## Key takeaways

- The merchant should provide a fallback UI such as Hosted Fields when the browser does not support Payment Request, serve the site over HTTPS (with localhost allowed for sandbox testing), and check `window.PaymentRequest` before displaying the Payment Request button. The guide also warns that Braintree's implementation does not expose every feature of the underlying Payment Request API.
- Credit cards need no additional configuration when the merchant account is already configured to accept them. Google Pay requires Control Panel enablement, a completed client-side integration, and browser support; PayPal via Google Pay requires both PayPal and Google Pay enabled in the Control Panel. These are stated prerequisites and presentation conditions, not proof that a particular merchant or buyer is eligible.
- The illustrated flow creates a Braintree Payment Request component and invokes `tokenize` with payment details after a button click. The requested amount should reflect the amount intended for authorization and settlement, although the guide says transactions still process when that amount changes during order fulfillment. The callback and Promise examples are examples, not guarantees of outcome.
- After successful customer authorization, the client receives a payment-method nonce and passes it to the merchant server, where it can be used to create a transaction. Authorization and nonce receipt are therefore distinct from server-side transaction creation and settlement.
- Each unique Google Pay transaction requires checkout consent. The guide says vaulting Google Pay payment methods for future transactions results in declines and is not recommended, while distinguishing Google Pay cards used for recurring billing or split shipments after checkout consent; PayPal accounts from Google Pay cannot be vaulted.
- Snapshot ambiguity: under `Using direct links`, the prose says to load the Payment Request component, but the displayed script example loads `client.min.js` and `local-payment.min.js` at version `3.111.0`. The snapshot does not resolve whether the second script is correct, so consult an appropriate verified component reference before implementing that loading path.

## Detail locators

- `Before you get started` (raw lines 21–30): overview route, fallback UI, HTTPS/localhost condition, `PaymentRequestComponent` reference, and the warning that Braintree does not expose all Payment Request API functionality.
- `Configure payment methods` (raw lines 33–57): credit-card condition, Google Pay Control Panel steps and presentation conditions, and the dual-enablement condition for PayPal via Google Pay.
- `Load the component` (raw lines 60–84): direct-link and CommonJS examples; includes the unresolved `local-payment.min.js` direct-link example.
- `Initialize the component` → `Check browser capabilities and create Payment Request component` (raw lines 86–103): `window.PaymentRequest` capability check and fallback branch.
- `Initialize the component` → `Set up your Payment Request button` (raw lines 105–176): amount note plus callback and Promise examples for component creation and tokenization.
- `Send the payment method nonce to your server` (raw lines 178–186): successful-authorization nonce handoff, server-side transaction creation route, reuse guidance, and Google Pay vaulting/consent qualifications.

## Related

- [[braintree-web-sdk]] — modular browser SDK boundary and version-qualified Payment Request route
- [[braintree]] — provider capsule and source catalog

## Raw Sources

- [[raw/braintree/docs/guides/payment-request/setup-and-integration/javascript/v3-2026-09-16|Braintree Payment Request Setup and Integration — JavaScript v3 (fetched 2026-09-16)]]
