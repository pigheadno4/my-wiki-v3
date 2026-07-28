---
title: "Braintree Web Drop-in"
type: concept
category: technology
tags: [braintree, drop-in, checkout, javascript-sdk, hosted-fields, wallets, deprecation]
---

## Braintree Web Drop-in

Braintree Web Drop-in is a prebuilt browser checkout UI layered on the modular Braintree Web SDK. It renders an opinionated payment selector, tokenizes the buyer's selected method, and returns a Braintree payment-method nonce for server-side processing.

## Integration Model

Merchants create Drop-in inside an empty container or use its script-tag form integration. Card entry uses Hosted Fields; optional payment views cover PayPal, PayPal Credit, Venmo, Apple Pay, and Google Pay. Method configuration and browser checks determine what is actually displayed.

The instance exposes `requestPaymentMethod()` for nonce creation, requestability and view events, available-payment-option inspection, selected-method clearing, limited configuration updates, and teardown. Optional Data Collector output and 3D Secure verification are attached to the nonce request flow.

## Vault Boundary

A customer-scoped client token can display supported vaulted cards and PayPal accounts and control whether newly entered methods are vaulted. Apple Pay, Google Pay, and Venmo vaulted records are hidden from new authorization selection in this implementation. Clearing a selection does not delete a vaulted method; deletion is a separate Vault Manager operation.

## Version and Migration Boundary

The first retained release is `braintree-web-drop-in@1.47.0` at SHA `ec1c7c533c2e878545f2b25505c56b7e22dc1c17`. It pins `braintree-web@3.123.2`, so it must not inherit claims from the independently collected `braintree-web@3.144.0` source.

The repository schedules deprecated status for 2026-09-01 and unsupported status for 2027-09-01, and directs merchants to migrate to the Braintree SDK. The notice says processing will be supported for one year after deprecation, while processing on unsupported SDKs may be suspended at any time. These statements describe the retained snapshot; current operational status should be rechecked when answering time-sensitive questions.

## Related

- [[source-github-braintree-web-drop-in]] - cumulative exact-SHA implementation evidence
- [[changelog-github-braintree-web-drop-in]] - package-qualified release ledger
- [[braintree-web-sdk]] - modular SDK and migration target
- [[braintree]] - company page
