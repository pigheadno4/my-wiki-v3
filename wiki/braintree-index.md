# Braintree Index

> Braintree-specific catalog. Cross-cutting pages are in the root [[index]].

Operations history: [[braintree-log]]

## Company

- [[braintree]]

## Sources

### Website documentation

- [[source-braintree-best-practices-node]] - Node response-code, timeout-uncertainty and transport-security routes with collected-version qualifications
- [[source-braintree-authorization-responses]] - processor approval/decline/network classes and scoped retry restrictions
- [[source-braintree-exceptions-node]] - Node exception categories and distinct timeout boundaries
- [[source-braintree-result-objects-node]] - result wrapper, collection and validation-error distinctions
- [[source-braintree-server-sdk-deprecation-policy]] - server-SDK lifecycle categories and maintenance routes
- [[source-braintree-server-sdk-migration-guide-node]] - historical Node 2.24.0-or-earlier to v3 migration route
- [[source-braintree-upgrade]] - historical Server-to-Server, Transparent Redirect and Braintree.js upgrade routes
- [[source-braintree-settlement-responses]] - capture-request settled, pending and declined response routes
- [[source-braintree-avs-cvv-responses]] - AVS street/postal and CVV category reference with rendering caveat
- [[source-braintree-merchant-advice-codes]] - optional Mastercard advice and scoped retry-wait routes

- [[source-braintree-recurring-billing-manage-node]] - Node.js subscription-management guide covering status-qualified updates, proration and failed-charge behavior, past-due retries, version-qualified retry settlement, and transaction-based refunds
- [[source-braintree-recurring-billing-testing-go-live-node]] - Braintree Node.js route for sandbox recurring-billing setup and test-value locators, plus the separate production credentials, recreated settings and plans, environment switch, and limited real-payment settlement checks
- [[source-braintree-recurring-billing-create-node]] - Braintree Node.js guide to stored-payment-method and plan prerequisites, plan-derived subscription setup, and start-date or trial-dependent creation, charge and status timing
- [[source-braintree-recurring-billing-overview]] - Braintree recurring-billing availability, plan-and-Vault setup flow, and `Pending`, `Active`, `Past Due`, `Expired` and `Canceled` subscription meanings
- [[source-braintree-recurring-billing-plans-node]] - Braintree plan-template inheritance, EU price and dormant-customer notice qualification, and Control Panel/API boundaries for recurring-billing add-ons and discounts
- [[source-braintree-transactions-guide-node]] - Node.js transaction guide distinguishing sale authorization, settlement submission, pre-settlement void, refund, parameter-scoped validation errors, and account-qualified dispute retrieval
- [[source-braintree-webhooks-disbursement-node]] - Node.js `disbursement` and deprecated `transaction_disbursed` notification conditions for Braintree-funded merchant accounts, with broad payload-category and bank-departure boundaries
- [[source-braintree-webhooks-sub-merchant-account-node]] - Node.js Braintree Marketplace sub-merchant approval and decline notification conditions, with notification-kind, trigger-time and `MerchantAccount` payload routes
- [[source-braintree-webhooks-test-node]] - Node.js `check` test notification triggered in the Control Panel, with only notification kind and UTC trigger time documented and no business-object payload established
- [[source-braintree-webhooks-braintree-auth-node]] - Closed-beta Node.js Braintree Auth notifications for connected-merchant underwriting/application and PayPal link-status events, with connected-merchant and OAuth-application payload routes

- [[source-braintree-subscription-create-node]] - Node.js subscription creation using a vaulted payment-method token or conditional nonce, with 3DS-first-transaction, merchant-account currency, plan-modification and start-date qualifications routed to exact raw sections
- [[source-braintree-subscription-update-node]] - Node.js updates to an existing subscription, including add-on and discount add-update-remove scope, conditional 3DS-enriched nonce guidance for the next transaction, and the option that removes all existing add-ons and discounts
- [[source-braintree-transaction-search-node]] - Node.js transaction search through `gateway.transaction.search()`, with callback `response.each()` consumption, criteria routes, the preserved policy limitation, refund-versus-credit scope, and timezone-qualified date searches
- [[source-braintree-transaction-submit-for-partial-settlement-node]] - Node.js multiple partial settlement against one parent authorization, with separate child transactions and child-only refund restrictions, plus a preserved payment-method availability conflict and damaged lifecycle-status rendering
- [[source-braintree-transaction-adjust-authorization-node]] - Node.js adjustment of an `authorized` transaction's amount, with lower-amount partial-reversal attempts, higher-amount incremental-authorization attempts, and the some-market merchant-fee qualification
- [[source-braintree-transaction-clone-transaction-node]] - Node.js creation of a new transaction by copying all original attributes except amount, with required amount and settlement-submission option input plus Braintree's preferred Vault-reuse alternative
- [[source-braintree-transaction-hold-in-escrow-node]] - Braintree Marketplace-specific Node.js hold-in-escrow invocation by transaction ID, limited to `authorized` or `submitted_for_settlement` transactions and preserving the empty-handler result boundary
- [[source-braintree-transaction-release-from-escrow-node]] - Braintree Marketplace-specific Node.js escrow release by transaction ID, with the `held` prerequisite, master/sub-merchant fund distribution, next-business-day timing, and empty-handler evidence boundary
- [[source-braintree-transaction-cancel-release-node]] - Braintree Marketplace-specific Node.js cancellation of a previously requested escrow release while `escrow_status` is `release_pending`, explicitly distinct from refund evidence
- [[source-braintree-transaction-line-item-find-all-node]] - Node.js transaction-ID retrieval of a Transaction Line Item collection, with callback and Promise result variables, the preserved policy notice, and unreconstructed damaged explanatory prose

- [[source-braintree-dispute-add-text-evidence-node]] - Braintree Node.js text-evidence addition for `open` disputes, restricted to merchants with Control Panel dispute access, with plain and categorized evidence routes and a separate finalization boundary for submission to the banks
- [[source-braintree-merchant-account-create-node]] - Node.js merchant-account creation examples covering individual/business identity, bank-oriented funding, terms acceptance, master-merchant association, callback arguments and a Promise-resolved result value, without establishing universal onboarding eligibility
- [[source-braintree-merchant-account-create-for-currency-node]] - Braintree Node.js currency-specific merchant-account creation for Braintree Auth merchants, with callback and Promise result handling plus unsupported-currency validation routes
- [[source-braintree-merchant-account-update-node]] - Node.js merchant-account update example using an account identifier, an individual first-name change and a `result.success` callback check, with a separate not-found route and no inferred wider update effects
- [[source-braintree-merchant-account-all-node]] - Node.js merchant-account collection retrieval through `gateway.merchantAccount.all()`, with callback `forEach` consumption and displayed `currencyIsoCode` access, without importing account-creation or update behavior
- [[source-braintree-merchant-account-find-node]] - Node.js single merchant-account lookup by ID through `gateway.merchantAccount.find()`, with callback arguments and separate response-object and not-found routes
- [[source-braintree-webhooks-grant-api-node]] - Node.js Grant API notifications for updates to previously granted payment instruments and grantor revocation, with side-qualified update kinds and broad payload-category routes
- [[source-braintree-webhooks-oauth-node]] - Node.js OAuth access-revocation notification for connected merchants, with production closed-beta and sandbox open-beta qualifications plus payload and parsing routes
- [[source-braintree-webhooks-local-payment-methods-node]] - Node.js instant local-payment completion and reversal versus non-instant funding and expiry events, with the completion event's separate nonce-based Transaction Sale route
- [[source-braintree-settlement-batch-summary-generate-node]] - Node.js date-scoped settlement batch summary reporting with single-custom-field grouping examples and callback or Promise access to summary records

- [[source-braintree-search-fields-node]] - Node.js search-field categories and operators, including the 255-character text limit and distinct non-time versus time-range boundary semantics
- [[source-braintree-search-results-node]] - Node.js search-result consumption through version-qualified no-callback object-mode streams or callback-provided `each` iteration, with lazy-fetch race behavior, maximum-count guidance and transaction-versus-other-search caps
- [[source-braintree-customer-search-node]] - Node.js customer search through `gateway.customer.search()`, with callback `response.each()` consumption, raw routes for filter examples and operator restrictions, the preserved results-limitation notice, and the unavailable all-customers Node call
- [[source-braintree-credit-card-verification-search-node]] - Node.js credit-card-verification search by verification, customer, card, payment-method, billing-address or creation-time criteria, with callback iteration, qualified timezone behavior and a preserved policy-based result-limitation notice
- [[source-braintree-dispute-accept-node]] - Braintree Node.js dispute acceptance by ID, restricted to merchants with Control Panel dispute access, with the prior-refund do-not-accept warning and an unreconstructed missing status-eligibility value
- [[source-braintree-dispute-finalize-node]] - Braintree Node.js dispute finalization for `Open` disputes, restricted to merchants with Control Panel dispute access, requiring the finalize call to submit evidence to the banks and transition status to `Disputed`
- [[source-braintree-dispute-find-node]] - Braintree Node.js single-dispute lookup by dispute ID, restricted to merchants with Control Panel dispute access and preserving the results-limitation policy notice
- [[source-braintree-dispute-search-node]] - Braintree Node.js dispute search with callback `response.forEach()` result access, raw routes for criteria and operators, Control Panel access qualification, and the preserved results-limitation notice
- [[source-braintree-document-upload-create-node]] - Node.js document-upload creation with an `EvidenceDocument` kind and file-stream example, preserving the displayed result-variable mismatch and no inference that upload creation submits dispute evidence
- [[source-braintree-dispute-remove-evidence-node]] - Braintree Node.js removal of one evidence item by dispute and evidence IDs while the dispute is `Open`, restricted to merchants with Control Panel dispute access and distinct from evidence submission or finalization

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
