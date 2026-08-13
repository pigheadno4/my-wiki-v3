# Braintree Index

> Braintree-specific catalog. Cross-cutting pages are in the root [[index]].

Operations history: [[braintree-log]]

## Company

- [[braintree]]

## Sources

- [[source-github-graphql-api]] - commit-qualified GraphQL contract for transactions, vaulting, PayPal, Venmo, 3DS, recurring billing, and broader API inventory at `default-branch@3a89f42` (github-repo, 2026-08-11)
- [[changelog-github-graphql-api]] - commit-qualified GraphQL schema history through `3a89f42` (github-repo, 2026-08-11)
- [[source-github-braintree-node]] - cumulative `braintree@3.39.0` server-side gateway knowledge: client tokens, vault, transactions, PayPal/Venmo, 3DS, subscriptions, webhooks, and error semantics (github-repo, 2026-08-09)
- [[changelog-github-braintree-node]] - package-qualified Braintree Node release ledger beginning at `3.39.0` (github-repo, 2026-08-09)
- [[source-github-braintree-web]] — cumulative `braintree-web` implementation knowledge through `3.144.0`: Hosted Fields, 3DS, PayPal v6, View/Edit Funding Instrument, Venmo, wallets, local payments, and decision-support components (github-repo, 2026-07-28)
- [[changelog-github-braintree-web]] — package-qualified Braintree Web release ledger from `3.143.0` through `3.144.0` (github-repo, 2026-07-28)
- [[source-github-braintree-web-drop-in]] - `braintree-web-drop-in@1.47.0` prebuilt UI, payment methods, vault behavior, 3DS, localization, and migration boundary (github-repo, 2026-07-28)
- [[changelog-github-braintree-web-drop-in]] - package-qualified Drop-in release ledger beginning at `1.47.0` (github-repo, 2026-07-28)
- [[source-github-braintree-android]] - `braintree-android@5.30.0` native clients, nonce flow, PayPal, Venmo, cards, 3DS, redirect handling, and exact release changes (github-repo, 2026-08-01)
- [[changelog-github-braintree-android]] - package-qualified Braintree Android release ledger beginning at `5.30.0` (github-repo, 2026-08-01)
- [[source-github-braintree-ios]] - `braintree-ios@7.9.0` modular native clients, nonce flow, PayPal, Venmo, Apple Pay, cards, 3DS, UI, and v7 migration boundary (github-repo, 2026-08-01)
- [[changelog-github-braintree-ios]] - package-qualified Braintree iOS release ledger beginning at `7.9.0` (github-repo, 2026-08-01)
- [[source-github-braintree-ios-drop-in]] - `BraintreeDropIn@9.14.0` prebuilt native payment selection, nonce handoff, cards, PayPal, Venmo, Apple Pay, vaulting, 3DS, and 5.27 dependency boundary (github-repo, 2026-08-13)
- [[changelog-github-braintree-ios-drop-in]] - package-qualified iOS Drop-in release ledger beginning at `9.14.0` (github-repo, 2026-08-13)

## Concepts

- [[braintree-web-sdk]] — modular client/nonce architecture and exact-version evidence boundaries
- [[braintree-web-drop-in]] - prebuilt checkout UI, pinned SDK dependency, and scheduled deprecation
- [[braintree-android-sdk]] - native Android request/launcher/result architecture and PayPal/Venmo boundary
- [[braintree-ios-sdk]] - native iOS authorization/nonce architecture, PayPal/Venmo/Apple Pay, and independently versioned Drop-in boundary

## Cross-Cutting Concepts

- [[paypal-braintree-integration]] — PayPal Web SDK v6 sessions converted to Braintree payment-method nonces

## Operations

- [[braintree-log]] — provider-specific collection and ingest history
- [GitHub collection status](../tracking/github/status.md)
