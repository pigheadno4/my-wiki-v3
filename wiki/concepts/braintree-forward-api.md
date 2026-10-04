---
title: "Braintree Forward API"
type: concept
category: technology
tags: [braintree, braintree-extend, forward-api, payment-data-forwarding, vault]
---

## Braintree Forward API

Braintree Forward API is the Braintree Extend route for constructing outbound requests to a destination from Braintree payment-method data and caller-supplied values. The collected examples demonstrate functions, transformations, overrides, conditional paths, XML construction, multiple payment methods and transformation-local variables. Production use is subject to eligibility. [[source-braintree-extend-forward-api-examples]]

This forwarding route is distinct from evidence that a destination authorized the merchant, accepted the request, executed a payment, or settled funds. The retained examples use Braintree's sandbox forwarding endpoint and `httpbin.org`; their returned request/debug representations are configuration examples, not payment outcomes. Destination-specific authority, credentials, request semantics and execution must be established by their own documentation and evidence.

## Vault and CVV boundary

Braintree states that vaulted payment methods do not retain CVV. When a destination requires CVV with vaulted card data, the documented example combines a long-lived payment-method token with a separately collected CVV-only payment-method nonce and uses Forward API variable suffixing. This is a data-construction path, not proof that the destination permits or successfully processes the request. [[source-braintree-extend-forward-api-examples]]

## Related

- [[braintree]] - provider company and exhaustive source catalog
- [[braintree-payment-platform]] - provider product-orientation route

## Sources

- [[source-braintree-extend-forward-api-worldpay]] - 2026-09-16 collected Braintree-hosted destination guide for the `worldpay_shared` configuration, optional JSON/XML override bodies, production eligibility and the logged-data/PII caution
- [[source-braintree-extend-forward-api-pgp-key]] - 2026-09-16 collected unversioned Forward API PGP public-key retrieval page for encrypting secrets sent during communication with the Forward API team
- [[source-braintree-extend-forward-api-stripe]] - 2026-09-16 Braintree-hosted destination guide naming Stripe Payment Methods, Tokens and Charges configs, with a sandbox Payment Methods request example, production eligibility and logged-override cautions; not Stripe API authority or payment-execution proof
- [[source-braintree-extend-forward-api-braintree-api-forwarding]] - 2026-09-16 Braintree Extend guide to forwarding alternate-Braintree-API nonces or stored payment-method tokens through sandbox request examples, with production-eligibility and payment-outcome-evidence boundaries
- [[source-braintree-extend-forward-api-adyen]] - Braintree-hosted destination guide for `adyen_payments` and `adyen_authorise`, Basic-auth/API-key sandbox request examples, production eligibility, and logged-override cautions; not Adyen authority or payment-execution proof
- [[source-braintree-extend-forward-api-transformations]] - collected Braintree Extend guide to ordered Forward API transformation paths, DSL evaluation and type constraints, with production-eligibility and destination-execution boundaries

- [[source-braintree-extend-forward-api-examples]] - sandbox examples for functions, transformation and override behavior, multi-payment-method construction, transformation-local variables, eligibility and the Vault/CVV boundary
