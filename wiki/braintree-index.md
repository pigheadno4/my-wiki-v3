# Braintree Index

> Braintree-specific catalog. Cross-cutting pages are in the root [[index]].

Operations history: [[braintree-log]]

## Company

- [[braintree]]

## Sources

- [[source-github-mobile-sdk-tooling]] - shared mobile SDK pull-request review digest, GitHub App authentication, CODEOWNER-aware review reduction, Slack routing, and operational limits at `default-branch@a3b0ffe` (github-repo, 2026-08-27)
- [[changelog-github-mobile-sdk-tooling]] - commit-qualified mobile SDK tooling history beginning at `default-branch@a3b0ffe` (github-repo, 2026-08-27)
- [[source-github-graphql-api]] - commit-qualified GraphQL contract for transactions, vaulting, PayPal, Venmo, 3DS, recurring billing, and broader API inventory at `default-branch@3a89f42` (github-repo, 2026-08-11)
- [[changelog-github-graphql-api]] - commit-qualified GraphQL schema history through `3a89f42` (github-repo, 2026-08-11)
- [[source-github-braintree-node]] - cumulative `braintree@3.39.0` server-side gateway knowledge: client tokens, vault, transactions, PayPal/Venmo, 3DS, subscriptions, webhooks, and error semantics (github-repo, 2026-08-09)
- [[changelog-github-braintree-node]] - package-qualified Braintree Node release ledger beginning at `3.39.0` (github-repo, 2026-08-09)
- [[source-github-braintree-php]] - cumulative `braintree_php@6.37.0` PHP gateway knowledge: client tokens, vault, transactions, PayPal/Venmo, subscriptions, webhooks, credentials, and error semantics (github-repo, 2026-08-19)
- [[changelog-github-braintree-php]] - package-qualified Braintree PHP release ledger beginning at `6.37.0` (github-repo, 2026-08-19)
- [[source-github-braintree-ruby]] - cumulative `braintree@4.40.0` Ruby gateway knowledge: client tokens, vault, transactions, PayPal/Venmo, 3DS, subscriptions, webhooks, runtime, and error semantics (github-repo, 2026-08-23)
- [[changelog-github-braintree-ruby]] - package-qualified Braintree Ruby release ledger beginning at `4.40.0` (github-repo, 2026-08-23)
- [[source-github-braintree-web]] — cumulative `braintree-web` implementation knowledge through `3.144.0`: Hosted Fields, 3DS, PayPal v6, View/Edit Funding Instrument, Venmo, wallets, local payments, and decision-support components (github-repo, 2026-07-28)
- [[changelog-github-braintree-web]] — package-qualified Braintree Web release ledger from `3.143.0` through `3.144.0` (github-repo, 2026-07-28)
- [[source-github-credit-card-type]] - `credit-card-type@10.3.0` partial brand detection, ambiguity resolution, formatting/security-code metadata, mutable custom-card APIs, and validation boundary (github-repo, 2026-08-29)
- [[changelog-github-credit-card-type]] - package-qualified card-brand detector release ledger beginning at `10.3.0` (github-repo, 2026-08-29)
- [[source-github-braintree-web-drop-in]] - `braintree-web-drop-in@1.47.0` prebuilt UI, payment methods, vault behavior, 3DS, localization, and migration boundary (github-repo, 2026-07-28)
- [[changelog-github-braintree-web-drop-in]] - package-qualified Drop-in release ledger beginning at `1.47.0` (github-repo, 2026-07-28)
- [[source-github-braintree-android]] - `braintree-android@5.30.0` native clients, nonce flow, PayPal, Venmo, cards, 3DS, redirect handling, and exact release changes (github-repo, 2026-08-01)
- [[changelog-github-braintree-android]] - package-qualified Braintree Android release ledger beginning at `5.30.0` (github-repo, 2026-08-01)
- [[source-github-braintree-android-drop-in]] - `drop-in@6.17.0` prebuilt native payment selection, nonce handoff, cards, PayPal, Venmo, Google Pay, vaulting, 3DS, device data, and 4.50 dependency boundary (github-repo, 2026-08-13)
- [[changelog-github-braintree-android-drop-in]] - package-qualified Android Drop-in release ledger beginning at `6.17.0` (github-repo, 2026-08-13)
- [[source-github-braintree-ios]] - `braintree-ios@7.9.0` modular native clients, nonce flow, PayPal, Venmo, Apple Pay, cards, 3DS, UI, and v7 migration boundary (github-repo, 2026-08-01)
- [[changelog-github-braintree-ios]] - package-qualified Braintree iOS release ledger beginning at `7.9.0` (github-repo, 2026-08-01)
- [[source-github-braintree-ios-drop-in]] - `BraintreeDropIn@9.14.0` prebuilt native payment selection, nonce handoff, cards, PayPal, Venmo, Apple Pay, vaulting, 3DS, and 5.27 dependency boundary (github-repo, 2026-08-13)
- [[changelog-github-braintree-ios-drop-in]] - package-qualified iOS Drop-in release ledger beginning at `9.14.0` (github-repo, 2026-08-13)
- [[source-github-popup-bridge-ios]] - `PopupBridge@3.1.0` iOS WebView-to-`ASWebAuthenticationSession` transport, Venmo return scheme, PayPal/Braintree boundary, analytics, and retained documentation conflicts (github-repo, 2026-08-27)
- [[changelog-github-popup-bridge-ios]] - package-qualified iOS PopupBridge release ledger beginning at `3.1.0` (github-repo, 2026-08-27)
- [[source-github-popup-bridge-android]] - `popup-bridge@5.3.0` Android WebView-to-Browser-Switch transport, persisted return handling, Venmo detection, analytics, and retained lifecycle conflicts (github-repo, 2026-08-27)
- [[changelog-github-popup-bridge-android]] - package-qualified Android PopupBridge release ledger beginning at `5.3.0` (github-repo, 2026-08-27)

## Concepts

- [[braintree-server-sdk]] - shared server-side gateway boundary with independent Node.js, PHP, and Ruby package evidence
- [[braintree-web-sdk]] — modular client/nonce architecture and exact-version evidence boundaries
- [[braintree-web-drop-in]] - prebuilt checkout UI, pinned SDK dependency, and scheduled deprecation
- [[braintree-android-sdk]] - native Android request/launcher/result architecture, PayPal/Venmo behavior, and independently versioned Drop-in boundary
- [[braintree-ios-sdk]] - native iOS authorization/nonce architecture, PayPal/Venmo/Apple Pay, and independently versioned Drop-in boundary
- [[braintree-popup-bridge]] - WebView popup transport, Venmo app-switch return, and payment-eligibility boundary

## Cross-Cutting Concepts

- [[card-brand-detection]] - generic brand inference, ambiguity, UI metadata, and validation/acceptance boundary
- [[paypal-braintree-integration]] — PayPal Web SDK v6 sessions converted to Braintree payment-method nonces

## Operations

- [[braintree-log]] — provider-specific collection and ingest history
- [GitHub collection status](../tracking/github/status.md)
