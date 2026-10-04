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
- [[source-braintree-reference-forward-api-server-errors]] - 2026-09-16 collected unversioned Forward API server-error reference for illustrative failure-body shape, timeout/TLS 502/504 mappings, production eligibility, and the destination-5xx boundary where Forward API returns HTTP 200 while carrying the destination error in the body; not Orchestration, retry-policy, destination-success, payment-lifecycle, or current-enablement evidence
- [[source-braintree-reference-forward-api-vault-errors]] - 2026-09-16 collected unversioned Forward API Vault-error reference for the illustrative response body, `401`/`403` access failures, field-specific `404` cases, `422` data/export/binding failures and the PayPal Vault-flow prerequisite; production remains eligibility-gated, the example is not a guaranteed schema, and the catalog does not define Orchestration, general retry policy or downstream payment-lifecycle behavior
- [[source-braintree-reference-forward-api-config]] - 2026-09-16 collected unversioned Forward API config reference for destination request templates, production review/approval/load versus sandbox inline or file submission, and post-load name lookup; not a universal config schema, credential guide, Orchestration flow, or evidence of destination acceptance, payment execution, settlement, or current eligibility
- [[source-braintree-reference-forward-api-transformation-errors]] - 2026-09-16 collected unversioned Forward API transformation-error reference for the illustrative response-body shape, exact failure identity, pre-execution type checking, serializable-result and function-input catalog, multiple-type-error condition, and production eligibility boundary; not Orchestration, required-schema, retry, downstream-processing, or payment-lifecycle evidence
- [[source-braintree-reference-forward-api-variables]] - 2026-09-16 collected unversioned variable-substitution reference covering global precedence, partial-template serialization, non-serialized local variables, Apple Pay DPAN qualification and payment-method suffix binding; production eligibility remains qualified, and the captured global-variable inventory is empty
- [[source-braintree-reference-forward-api-tokenization-errors]] - 2026-09-16 collected unversioned Forward API tokenization error catalog for JSON failure bodies, HTTP 400/422/500 mappings, the risk-reason disclosure restriction and sandbox negative-test fixtures; production remains eligibility-gated and the catalog does not define Orchestration or downstream retry/payment lifecycle behavior
- [[source-braintree-reference-forward-api-functions]] - 2026-09-16 sparse functions reference identifying the intentionally minimal Forward API DSL and production eligibility, but containing no function/signature/error inventory and embedding an example RSA keypair that must not be reused as credential material
- [[source-braintree-reference-forward-api-validation-errors]] - 2026-09-16 collected unversioned Forward API validation-error reference for the response-body failure shape, common `message` validation flag, request/config/security error catalog and production eligibility/config/debug boundaries; not Orchestration or destination/payment-lifecycle evidence
- [[source-braintree-reference-forward-api-forward]] - 2026-09-16 Forward API incoming-request reference for sandbox endpoint and controls, trace identity, required merchant/method fields, production naming and eligibility, debug no-send behavior, and the `sensitive_data` logging boundary
- [[source-braintree-reference-forward-api-direct-tokenization]] - 2026-09-16 direct `/tsp` reference for generating tokenized PAN data, with endpoint pre-approval, PAN-equivalent PCI handling, Discover-qualified restrictions, sandbox outputs and a Visa cryptogram example that must not be generalized into the sibling forwarding-support flow
- [[source-braintree-reference-forward-api-overview]] - 2026-09-16 collected unversioned Forward API overview for Vault-to-PCI-compliant-destination identity, production eligibility, config-based HTTPS request delegation and destination-response relay; an outbound forwarding route distinct from Orchestration processor connections and transaction lifecycle operations
- [[source-braintree-reference-forward-api-tokenization]] - 2026-09-16 collected unversioned Forward API tokenization reference with Discover and Mastercard sandbox TPAN request examples, Discover generated-CVV and AVS behavior, the invalid-instrument error route and the production-eligibility boundary; distinct from Orchestration transaction lifecycle operations

- [[source-braintree-extend-forward-api-worldpay]] - 2026-09-16 collected Braintree-hosted destination guide for the `worldpay_shared` configuration, optional JSON/XML override bodies, production eligibility and the logged-data/PII caution
- [[source-braintree-extend-forward-api-pgp-key]] - 2026-09-16 collected unversioned Forward API PGP public-key retrieval page for encrypting secrets sent during communication with the Forward API team
- [[source-braintree-extend-forward-api-stripe]] - 2026-09-16 Braintree-hosted destination guide naming Stripe Payment Methods, Tokens and Charges configs, with a sandbox Payment Methods request example, production eligibility and logged-override cautions; not Stripe API authority or payment-execution proof
- [[source-braintree-extend-forward-api-braintree-api-forwarding]] - 2026-09-16 Braintree Extend guide to forwarding alternate-Braintree-API nonces or stored payment-method tokens through sandbox request examples, with production-eligibility and payment-outcome-evidence boundaries
- [[source-braintree-extend-forward-api-adyen]] - Braintree-hosted destination guide for `adyen_payments` and `adyen_authorise`, Basic-auth/API-key sandbox request examples, production eligibility, and logged-override cautions; not Adyen authority or payment-execution proof
- [[source-braintree-extend-forward-api-transformations]] - collected Braintree Extend guide to ordered Forward API transformation paths, DSL evaluation and type constraints, with production-eligibility and destination-execution boundaries

- [[source-braintree-extend-forward-api-examples]] - sandbox examples for functions, transformation and override behavior, multi-payment-method construction, transformation-local variables, eligibility and the Vault/CVV boundary
