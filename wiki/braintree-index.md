# Braintree Index

> Braintree-specific catalog. Cross-cutting pages are in the root [[index]].

Operations history: [[braintree-log]]

## Company

- [[braintree]]

## Sources

### Website documentation

- [[source-braintree-payment-method-create-node]] - Node.js existing-customer payment-method creation with required customer ID and nonce, default and billing-address behavior, payment-type limits on duplicate rejection, card-verification and Premium Fraud Management Tools guidance, and nonce-versus-raw-card precedence
- [[source-braintree-payment-method-update-node]] - Node.js stored-payment-method updates by token, including shared or replacement billing-address behavior, PayPal/default-method restrictions, card verification with the AVS-update transaction/CVV rejection condition, and nonce-association and precedence rules
- [[source-braintree-subscription-search-node]] - Node.js subscription search through `gateway.subscription.search()`, with callback and stream result consumption, qualified filter-example routes, the preserved results-limitation policy notice, and no reconstructed SDK version from the damaged rendering
- [[source-braintree-subscription-retry-charge-node]] - Node.js manual retry of a past-due subscription charge, with the explicit example amount, displayed success access, and separate transaction-settlement submission route
- [[source-braintree-payment-method-grant-node]] - limited-release Node.js Grant API route for giving another Braintree merchant controlled access to one customer payment method through a recipient access token and returned nonce
- [[source-braintree-payment-method-revoke-node]] - limited-release Node.js revocation of a payment-method grant, deleting the granted version from the receiving merchant's Vault without importing the separate payment-method deletion cascade
- [[source-braintree-webhooks-transaction-node]] - Node.js ACH and SEPA Direct Debit transaction settlement notification kinds, qualified post-settled decline wording, and damaged availability/attribute-rendering boundaries
- [[source-braintree-webhooks-account-updater-node]] - feature-restricted Account Updater daily-report webhook, including its 24-hour updated-method scope, no-updates suppression, payload-category route, and one-week report-link expiry
- [[source-braintree-webhooks-fraud-protection-node]] - Node.js `transaction_reviewed` notification for an accepted or rejected Fraud Protection Dashboard review, with requested-not-completed void/refund scope and review payload categories
- [[source-braintree-address-find-node]] - Node.js lookup of one address by customer ID plus address ID, with `err`/`address` callback evidence, separate response-object navigation, and a shared customer-or-address not-found route

- [[source-braintree-plan-update-node]] — plan-ID updates, destructive modification omission warning and override/trial routes
- [[source-braintree-plan-create-node]] — plan creation prerequisite, required-input and add-on/discount routes
- [[source-braintree-plan-find-node]] — single-plan lookup with code-grounded method and callback/Promise forms
- [[source-braintree-add-on-all-node]] — Node add-on collection/result access and Ruby-reference boundary
- [[source-braintree-discount-all-node]] — Node discount collection/result access without inferred creation/application behavior
- [[source-braintree-credit-card-update-node]] — stored-card updates, conditional verification and nonce/raw-card precedence
- [[source-braintree-credit-card-create-node]] — card creation, qualified PCI advisory and nonce/raw-card input guidance
- [[source-braintree-credit-card-expiring-between-node]] — date-range retrieval, callback and incomplete stream example boundaries
- [[source-braintree-credit-card-find-node]] — card-token lookup and qualified payment-method alternative guidance
- [[source-braintree-credit-card-delete-node]] — card-token deletion, error-only callback and qualified PCI advisory
- [[source-braintree-address-create-node]] — customer-scoped Vault address creation, generated IDs and per-customer limit
- [[source-braintree-webhooks-dispute-node]] — dispute notification triggers and qualified attribute/deprecation routes
- [[source-braintree-address-update-node]] — customer/address-ID updates, callback and alternative update routes
- [[source-braintree-address-delete-node]] — address deletion and removal of billing/shipping references from Vault payment methods
- [[source-braintree-plan-all-node]] — Plan collection retrieval through callback and Promise examples
- [[source-braintree-customer-update-node]] — customer-ID updates, omitted attributes and existing versus new payment-method boundaries
- [[source-braintree-transaction-find-node]] — transaction-ID lookup, result-limitation notice and Marketplace escrow example
- [[source-braintree-subscription-cancel-node]] — subscription cancellation, billing effect and result/error routes
- [[source-braintree-webhooks-subscription-node]] — subscription notification kinds, qualified triggers and payload limits
- [[source-braintree-subscription-find-node]] — subscription-ID lookup, callback/Promise code and result-limitation notice
- [[source-braintree-customer-create-node]] — Node customer creation variants, verification qualifications, custom fields and raw evidence gaps
- [[source-braintree-payment-method-find-node]] — stored-token lookup, result-limitation notice and separate PayPal-account examples
- [[source-braintree-webhooks-payment-method-node]] — current PayPal/Venmo revocation and enabled customer-data update notification scope
- [[source-braintree-customer-delete-node]] — customer-ID deletion with associated payment-method and recurring-subscription consequences
- [[source-braintree-customer-find-node]] — single-customer ID lookup and missing Node invocation evidence
- [[source-braintree-tokenization-key-javascript-v3]] — static reduced-privilege client authorization, lifecycle, environment and JavaScript initialization routes
- [[source-braintree-webhooks-testing-go-live-node]] — Node sample payloads versus Braintree-delivered tests, dummy-object and handler-kind warnings
- [[source-braintree-payment-method-nonce-find-node]] — non-consuming Node nonce lookup and available 3D Secure information
- [[source-braintree-payment-method-nonce-create-node]] — Node nonce creation, token input and Braintree's should-only usage guidance
- [[source-braintree-payment-method-delete-node]] — Node payment-method deletion with immediate subscription cancellation and paid-days forfeiture
- [[source-braintree-transaction-submit-for-settlement-node]] — Node settlement submission, amount adjustments and availability-qualified supplemental data
- [[source-braintree-authorization-overview]] — client tokens versus tokenization keys, capability conditions and selection routes
- [[source-braintree-client-token-generate-node]] — Node token generation and customer-scoped Drop-in saved-payment presentation
- [[source-braintree-transaction-void-node]] — Node void eligibility, PayPal-specific state and conditional authorization reversal
- [[source-braintree-authorization-client-token]] — signed client-token purpose, server/client roles and validity boundaries
- [[source-braintree-hosted-fields-events-javascript-v3]] — JavaScript Hosted Fields events and field-state lookup, with version-qualified reference links
- [[source-braintree-transaction-refund-node]] — Node refund eligibility, omitted amounts, partial-refund restrictions and failure routes
- [[source-braintree-webhooks-parse-node]] — Node signature/payload parsing, ordering warning and response-conditioned retries
- [[source-braintree-payment-method-nonces]] — SDK nonce versus GraphQL single-use payment method, use and lifespan boundaries
- [[source-braintree-webhooks-create-node]] — Control Panel webhook creation, Manage Webhooks permission and HTTPS destination requirements
- [[source-braintree-get-started]] — Braintree Direct sandbox integration, client-token/nonce flow, and source-qualified Drop-in lifecycle conflict
- [[source-braintree-transaction-sale-node]] — Node transaction sale, payment-source choices, settlement submission, risk/fraud data prerequisites, and raw example inconsistency
- [[source-braintree-webhooks-overview]] — HTTPS notifications, ACH Direct Debit transaction-status scope, permissions, and burst-volume warning
- [[source-braintree-control-panel-overview]] — gateway administration, Dashboard versus reconciliation, and Sandbox/Production isolation
- [[source-braintree-credit-cards-client-javascript-v3]] — JavaScript v3 Hosted Fields versus Card Fields and named native SDK alternatives

### Versioned GitHub implementation evidence

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
- [[source-github-braintree-web]] — cumulative `braintree-web` implementation knowledge through `3.145.0`, including PayPal v6 checkout-with-vault, Venmo desktop address requests and QR rescan, and loader/popup recovery (github-repo, 2026-09-16)
- [[changelog-github-braintree-web]] — package-qualified Braintree Web release ledger from `3.143.0` through `3.145.0` (github-repo, 2026-09-16)
- [[source-github-credit-card-type]] - `credit-card-type@10.3.0` partial brand detection, ambiguity resolution, formatting/security-code metadata, mutable custom-card APIs, and validation boundary (github-repo, 2026-08-29)
- [[changelog-github-credit-card-type]] - package-qualified card-brand detector release ledger beginning at `10.3.0` (github-repo, 2026-08-29)
- [[source-github-uuid]] - `@braintree/uuid@2.0.0` secure UUID v4 generation, global Web Crypto fallback chain, explicit failure behavior, and consumer-version boundary (github-repo, 2026-08-31)
- [[changelog-github-uuid]] - package-qualified UUID utility release ledger beginning at `2.0.0` (github-repo, 2026-08-31)
- [[source-github-restricted-input]] - commit-qualified `restricted-input@4.2.0` pattern formatting, paste, caret, browser strategies, and validation boundary at `default-branch@8dcc6ea` (github-repo, 2026-08-30)
- [[changelog-github-restricted-input]] - commit-qualified `4.1.3` to `4.2.0` transition and retained package-history statements (github-repo, 2026-08-30)
- [[source-github-braintree-web-drop-in]] - `braintree-web-drop-in@1.48.0` card-label hardening and lifecycle conflict; preserves `1.47.0` UI, vault, 3DS, and localization baseline (github-repo, updated 2026-09-20)
- [[changelog-github-braintree-web-drop-in]] - package-qualified Drop-in release ledger from `1.47.0` through `1.48.0` (github-repo, updated 2026-09-20)
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

- [[braintree-webhooks]] — gateway notification purpose, setup routes, permissions, and volume boundaries
- [[braintree-control-panel]] — gateway administration, Dashboard limits, and separate environments

- [[braintree-server-sdk]] - shared server-side gateway boundary with independent Node.js, PHP, and Ruby package evidence
- [[braintree-web-sdk]] — modular client/nonce architecture and exact-version evidence boundaries
- [[braintree-web-drop-in]] - prebuilt checkout UI, pinned SDK dependency, and scheduled deprecation
- [[braintree-android-sdk]] - native Android request/launcher/result architecture, PayPal/Venmo behavior, and independently versioned Drop-in boundary
- [[braintree-ios-sdk]] - native iOS authorization/nonce architecture, PayPal/Venmo/Apple Pay, and independently versioned Drop-in boundary
- [[braintree-popup-bridge]] - WebView popup transport, Venmo app-switch return, and payment-eligibility boundary

## Cross-Cutting Concepts

- [[card-brand-detection]] - generic brand inference, ambiguity, UI metadata, and validation/acceptance boundary
- [[payment-input-formatting]] - generic pattern, paste, caret, browser-compatibility, and validation boundaries
- [[paypal-braintree-integration]] — PayPal Web SDK v6 sessions converted to Braintree payment-method nonces

## Operations

- [[braintree-log]] — provider-specific collection and ingest history
- [GitHub collection status](../tracking/github/status.md)
