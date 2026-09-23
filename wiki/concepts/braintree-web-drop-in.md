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

> [!warning] Website lifecycle date conflict
> The Braintree Get Started website snapshot says Drop-in deprecation starts October 1, 2026, payment processing remains supported until October 1, 2027, and unsupported status begins on October 1, 2027. Those dates differ from the September milestones retained in both `braintree-web-drop-in@1.47.0` and `1.48.0`. The latter was released September 10 despite its unchanged README saying updates stop September 1; do not infer a support extension. Treat the schedules as source-specific and verify current status before migration planning. [[source-braintree-get-started]] [[source-github-braintree-web-drop-in]]

The first retained release is `braintree-web-drop-in@1.47.0` at SHA `ec1c7c533c2e878545f2b25505c56b7e22dc1c17`. It pins `braintree-web@3.123.2`, so it must not inherit claims from the independently collected `braintree-web@3.144.0` source.

It also pins `@braintree/uuid@1.0.1`. The independently retained UUID source is `2.0.0`, so its secure-random implementation and explicit no-secure-source error must not be attributed to this Drop-in release without exact v1 evidence.

The repository schedules deprecated status for 2026-09-01 and unsupported status for 2027-09-01, and directs merchants to migrate to the Braintree SDK. The notice says processing will be supported for one year after deprecation, while processing on unsupported SDKs may be suspended at any time. These statements describe the retained snapshot; current operational status should be rechecked when answering time-sensitive questions.

## Card Label Hardening in 1.48.0

`braintree-web-drop-in@1.48.0` adds numeric conversion, first-four-character truncation, and zero-padding to the card `lastFour` display. It preserves `0012` and `0000`, but malformed text produces `0NaN`; this is output normalization, not strict card-data validation. The payment-method template still uses `innerHTML`. PayPal email and Venmo username escaping are unchanged, as are the pinned `braintree-web@3.123.2` and `@braintree/uuid@1.0.1` dependencies. No new wallet or nonce behavior is established by this delta. [[source-github-braintree-web-drop-in]] [[changelog-github-braintree-web-drop-in]]

## Related

- [[source-braintree-upgrade]] - historical guidance that routes Transparent Redirect to Drop-in and changes the server handoff from redirect confirmation to a payment-method nonce; consult the separately retained lifecycle evidence before current migration planning

- [[source-github-braintree-web-drop-in]] - cumulative exact-SHA implementation evidence
- [[changelog-github-braintree-web-drop-in]] - package-qualified release ledger
- [[braintree-web-sdk]] - modular SDK and migration target
- [[source-github-uuid]] - independently versioned UUID utility and v1/v2 evidence boundary
- [[braintree]] - company page
