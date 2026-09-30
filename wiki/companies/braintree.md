---
title: "Braintree"
type: company
tags: [braintree, payments, checkout, graphql, javascript-sdk, node-js-sdk, php-sdk, ruby-sdk, android-sdk, ios-sdk, popup-bridge, webview, card-brand-detection, input-formatting, uuid, secure-random, developer-tooling, github-actions]
source_count: 202
---

## Overview

Braintree is represented in this wiki by seventeen independently tracked repositories: the GraphQL API contract, Node.js, PHP, and Ruby server SDKs, modular Braintree Web SDK, prebuilt Braintree Web Drop-in UI, native Braintree Android and iOS SDKs, separately versioned Android and iOS Drop-in UIs, independent Android and iOS PopupBridge WebView transports, the standalone `credit-card-type` detector, the `restricted-input` formatter, the shared `@braintree/uuid` utility, mobile SDK review tooling, and web SDK release automation. Client SDKs produce payment-method nonces for server processing; the server SDKs perform gateway operations; PopupBridge only transports browser popup results; `credit-card-type` infers likely card brands; `restricted-input` formats browser input; `@braintree/uuid` generates internal identifiers; and SDK tooling concerns engineering operations. The GraphQL schema describes a separate API contract. Their commit or package identities and evidence histories remain separate.

## Website Documentation

One hundred eighty-five independently reviewed website sources complement the seventeen repository
sources. Their collected documentation scope remains separate from exact-SHA
implementation evidence:

### Marketplace documentation

- [[source-braintree-marketplace-article-overview]] - article-level Marketplace model, scope and eligibility qualifications
- [[source-braintree-marketplace-guide-overview]] - developer-guide orientation, constraints and operation routes
- [[source-braintree-marketplace-article-onboarding]] - applicant, business and verification roles distinct from Node procedure
- [[source-braintree-marketplace-guide-onboarding-node]] - Node sub-merchant account creation, conditional information and pending result
- [[source-braintree-marketplace-guide-confirmation-node]] - Node post-verification approval/decline webhook confirmation
- [[source-braintree-marketplace-guide-create-node]] - Node sub-merchant transaction creation and service-fee route
- [[source-braintree-marketplace-article-processing]] - article-level service fees, escrow, refunds and chargeback responsibility
- [[source-braintree-marketplace-article-funding]] - article-level disbursement, escrow and exception-notification boundaries
- [[source-braintree-marketplace-guide-update-node]] - Node sub-merchant account updates and unchanged omitted attributes
- [[source-braintree-marketplace-guide-testing-go-live-node]] - sandbox simulations, production transition and real-payment cautions

The collected Marketplace overviews and recurring-billing overview state incompatibility, while the testing/go-live guide discusses recreating recurring-billing settings. The sources retain this unresolved conflict; none proves current Marketplace support or recurring-billing compatibility. See [[braintree-marketplace]].

### Other website documentation

- [[source-braintree-payment-methods-ach]] - ACH verification, delayed/reversible settlement, returns and internally conflicting void guidance
- [[source-braintree-payment-methods-venmo]] - Venmo checkout/vaulting, merchant and customer eligibility, profile setup and refund window
- [[source-braintree-payment-methods-apple-pay]] - conditional Apple Pay platform scope, DPAN model, consent guidance and certificate setup
- [[source-braintree-payment-methods-google-pay]] - Android/web eligibility and method-specific card, fraud and vaulting boundaries
- [[source-braintree-payment-methods-local-payment-methods]] - regional methods, PayPal-account prerequisite, redirect contexts and unsupported recurring/dispute routes
- [[source-braintree-payment-methods-secure-remote-commerce]] - Click to Pay guide with unresolved end-of-support versus limited-release conflict
- [[source-braintree-payment-methods-paypal-credit]] - deprecated credit-line guide and separate Pay Later successor route
- [[source-braintree-payment-methods-unionpay]] - dedicated integration deprecation/limited-release tension, SMS verification and qualified card behavior
- [[source-braintree-payment-methods-paypal-pay-later-offers]] - country-qualified offers, Checkout with Vault enablement and messaging restrictions
- [[source-braintree-payment-methods-sepa-direct-debit]] - pilot-only mandate/setup, post-disbursement returns and recurring support

- [[source-braintree-payment-methods-paypal-best-practices]] - PayPal integration practices and their qualified platform, checkout and vaulting boundaries
- [[source-braintree-payment-methods-paypal-disputes]] - PayPal-specific dispute access, deadlines and evidence routes distinct from card disputes
- [[source-braintree-paypal-pay-later-offers-javascript-v3]] - JavaScript v3 Pay Later presentation and setup route with conflicting same-date offer-table warning
- [[source-braintree-payment-methods-paypal-setup-guide]] - PayPal Business Account and Braintree production setup sequence and prerequisites
- [[source-braintree-paypal-checkout-with-vault-javascript-v3]] - JavaScript v3 checkout-plus-vault consent, token handoff and returning-customer distinction
- [[source-braintree-payment-methods-paypal-processing]] - PayPal authorization, capture, settlement transition, partial-settlement and legacy-vault boundaries
- [[source-braintree-payment-methods-paypal-funding-reconciliation]] - PayPal funding and Settlement Withdrawal route separate from reconciliation and deposit proof
- [[source-braintree-payment-methods-paypal-overview]] - PayPal payment-method orientation, availability and One-Time/Vaulted/Recurring routes
- [[source-braintree-payment-methods-paypal-shared-data]] - PayPal account creation/linking data-sharing categories and consent boundary
- [[source-braintree-paypal-messaging-javascript-v3]] - JavaScript v3 URL whose captured body covers native iOS/Android Pay Later Messaging eligibility and Drop-in exclusion

- [[source-braintree-control-panel-security-two-factor-authentication]] - Control Panel 2FA requirement, method order and account-recovery boundaries, not payment authentication
- [[source-braintree-control-panel-security-rotating-api-keys]] - API-key exposure response and safe overlapping-validity cutover
- [[source-braintree-fraud-tools-basic-risk-threshold-rules]] - velocity-check configuration, supported methods, required submitted fields and override limit
- [[source-braintree-fraud-tools-basic-avs-cvv-rules]] - credit-card AVS/CVV post-approval gateway rejection and Vault/international qualifications
- [[source-braintree-fraud-tools-3d-secure]] - cardholder authentication, enrollment and conditional liability shift, not authorization proof
- [[source-braintree-fraud-tools-premium-fraud-protection]] - named Fraud Protection approve/decline decision route, distinct from Advanced
- [[source-braintree-fraud-tools-premium-fraud-protection-advanced]] - Advanced eligibility, review flow and Not Evaluated fallback
- [[source-braintree-fraud-tools-premium-kount-custom]] - Kount risk-decision handoff, finality/discrepancy and responsibility split
- [[source-braintree-fraud-tools-premium-chargeback-protection]] - two named tools, conditional protection and eligibility, unresolved bypass support conflict and indemnity direction
- [[source-braintree-fraud-tools-premium-effortless-chargeback-protection]] - reason-code-specific evidence, conditional fee/amount waiver and non-waived fee limits

- [[source-braintree-get-started-overview]] - merchant/gateway roles, Direct/Extend/Auth orientation and Control Panel/API interaction routes
- [[source-braintree-get-started-explore]] - getting-started navigation map without importing linked-guide behavior
- [[source-braintree-get-started-try-it-out]] - Sandbox versus Production testing, isolation and non-transfer boundaries
- [[source-braintree-get-started-get-paid]] - post-settlement funding guidance distinct from payment acceptance and deposit proof
- [[source-braintree-get-started-payment-methods]] - collected method categories, eligibility limits and unresolved SRC support-status conflict
- [[source-braintree-get-started-currencies]] - presentment/settlement currencies and qualified multi-currency setup
- [[source-braintree-get-started-data-migration-overview]] - import/export orientation and migration scope limits
- [[source-braintree-get-started-data-migration-imports]] - inbound secure transfer, identifier mapping and two-import limit
- [[source-braintree-get-started-data-migration-exports]] - outbound Vault export, PCI/key prerequisites and two-export limit
- [[source-braintree-get-started-data-migration-public-key]] - public-key encryption route with current-key acquisition boundary

- [[source-braintree-control-panel-important-gateway-credentials]] - environment-specific gateway credentials and merchant-account identifiers with role and private-key security boundaries
- [[source-braintree-control-panel-search]] - basic and advanced Control Panel searches with object-specific results, indexing delays and CSV limits
- [[source-braintree-control-panel-users-roles-managing-users-roles]] - user and role administration, account activation and password-reset safety boundaries
- [[source-braintree-control-panel-vault-update]] - Vault customer, payment-method and address updates with PCI, subscription, AVS and shipping boundaries
- [[source-braintree-control-panel-vault-card-verification]] - card-verification purpose and outcomes, distinct from payment authorization and customer identity
- [[source-braintree-control-panel-custom-fields]] - custom-field configuration, visibility and permission boundaries
- [[source-braintree-control-panel-users-roles-log-in-with-paypal]] - PayPal-credential access to Braintree Control Panel, distinct from PayPal payment setup
- [[source-braintree-control-panel-vault-create]] - Control Panel Vault customer creation, card and CVV boundaries, distinct from payment authorization
- [[source-braintree-control-panel-users-roles-role-permissions]] - role-permission action scopes and the preserved Account Admin versus Forward API scope tension
- [[source-braintree-control-panel-vault-overview]] - Vault administration, export and CVV boundaries with routes to dedicated operation pages

- [[source-braintree-control-panel-reporting-overview]] - Control Panel report categories and account/location qualifications, with dedicated report pages for eligibility detail
- [[source-braintree-control-panel-reporting-settlement-batch-summary]] - processor batch totals, report access, exclusions, cutoff and email settings without funding proof
- [[source-braintree-control-panel-reporting-transaction-level-fee-report]] - pricing-model fee report, country-eligibility conflict, post-disbursement availability and reconciliation limits
- [[source-braintree-control-panel-reporting-transaction-summary]] - current-status trend report that must not be used for reconciliation
- [[source-braintree-control-panel-reporting-decline-analysis]] - decline-rate views and data-skew boundaries, not a retry policy
- [[source-braintree-control-panel-reporting-expiring-cards]] - Vault expiry report and separate card-update/action boundary
- [[source-braintree-control-panel-reporting-1099-k]] - qualified 1099-K access, timing and processor-specific form boundaries in the collected page
- [[source-braintree-control-panel-reporting-grant-api-report]] - beta Grant API recipient count and volume report with limited visibility
- [[source-braintree-control-panel-webhooks]] - Control Panel webhook configuration, permission, test and production-caution routes
- [[source-braintree-control-panel-audit-webhooks]] - select-partner authentication/admin notification catalog distinct from transaction webhooks

- [[source-braintree-control-panel-managing-authorizations]] - verify/store versus repeated authorization, qualified amount adjustments, and conflicting region availability in the collected page
- [[source-braintree-control-panel-email-receipts]] - transaction/refund email-receipt activation, configuration, manual generation and custom-receipt boundaries
- [[source-braintree-control-panel-bank-identification-numbers]] - Control Panel/CSV BIN lookup, six-digit availability and dated PCI qualifications
- [[source-braintree-control-panel-duplicate-checking]] - conditional duplicate matching, default time window, gateway rejection and Control Panel configuration
- [[source-braintree-control-panel-transaction-create]] - manual creation and payment-method eligibility with authorization/settlement boundaries
- [[source-braintree-control-panel-transaction-clone]] - copied transaction data, compatibility restrictions, CVV and permission boundaries
- [[source-braintree-transaction-lifecycle]] - authorization, settlement submission, settling and merchant-account settlement without inferred bank funding
- [[source-braintree-control-panel-gateway-rejections]] - gateway-rule versus bank decline, pre/post-authorization rejection and automatic-void limits
- [[source-braintree-control-panel-transaction-issues]] - separate issue category, notification/recipient routes and absent investigation workflow
- [[source-braintree-control-panel-descriptors]] - soft, hard and dynamic descriptors with bank, region and Control Panel/API boundaries

- [[source-braintree-best-practices-node]] - Node server-SDK response-code, timeout-uncertainty and transport-security guidance with historical version and certificate-table qualifications
- [[source-braintree-authorization-responses]] - processor authorization response classes, gateway-rejection distinction and card-network retry restrictions
- [[source-braintree-exceptions-node]] - Node server-SDK exception categories and distinct timeout boundaries without inferred transaction failure or retry safety
- [[source-braintree-result-objects-node]] - Node result-wrapper versus collection behavior, and validation-only error details distinct from other failed results
- [[source-braintree-server-sdk-deprecation-policy]] - server-SDK lifecycle categories and maintenance routes without inferring a current version's status
- [[source-braintree-server-sdk-migration-guide-node]] - historical Node 2.24.0-or-earlier to v3 migration changes and damaged legacy-function rendering
- [[source-braintree-upgrade]] - historical Server-to-Server, Transparent Redirect and Braintree.js migration routes to client SDKs and payment-method nonces
- [[source-braintree-settlement-responses]] - capture-request processor responses distinguishing settled, pending and declined outcomes
- [[source-braintree-avs-cvv-responses]] - AVS postal/street and CVV response categories, with damaged response-object naming and no inferred transaction outcome
- [[source-braintree-merchant-advice-codes]] - optional Mastercard advice codes, stop/no-retry instructions and exact wait durations under separate retry restrictions

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

- [[source-braintree-plan-update-node]] — plan updates, omission warning and override/trial guidance
- [[source-braintree-plan-create-node]] — merchant prerequisite and plan-creation input routes
- [[source-braintree-plan-find-node]] — single-plan lookup and result forms
- [[source-braintree-add-on-all-node]] — add-on collection retrieval and SDK-language boundary
- [[source-braintree-discount-all-node]] — discount collection retrieval and result access
- [[source-braintree-credit-card-update-node]] — stored-card update and nonce/raw-card precedence
- [[source-braintree-credit-card-create-node]] — card creation and qualified PCI/input guidance
- [[source-braintree-credit-card-expiring-between-node]] — expiry-date retrieval and incomplete-example boundaries
- [[source-braintree-credit-card-find-node]] — card-token lookup and qualified alternative guidance
- [[source-braintree-credit-card-delete-node]] — card-token deletion without imported downstream effects
- [[source-braintree-address-create-node]] — customer-scoped Vault address creation and limits
- [[source-braintree-webhooks-dispute-node]] — dispute notification triggers and attribute routes
- [[source-braintree-address-update-node]] — address-ID/customer-ID updates and error routes
- [[source-braintree-address-delete-node]] — address deletion and payment-method reference removal
- [[source-braintree-plan-all-node]] — callback/Promise retrieval of a Plan collection
- [[source-braintree-customer-update-node]] — customer updates and payment-method update boundaries
- [[source-braintree-transaction-find-node]] — transaction lookup and Marketplace-qualified escrow example
- [[source-braintree-subscription-cancel-node]] — subscription cancellation and billing-effect guidance
- [[source-braintree-webhooks-subscription-node]] — subscription notification triggers and payload limits
- [[source-braintree-subscription-find-node]] — subscription lookup, result handling and policy notice
- [[source-braintree-customer-create-node]] — Node customer creation and verification variants with retained evidence gaps
- [[source-braintree-payment-method-find-node]] — stored payment-method lookup and result-limitation notice
- [[source-braintree-webhooks-payment-method-node]] — scoped payment-method revocation and customer-data update events
- [[source-braintree-customer-delete-node]] — customer deletion and cascading consequences
- [[source-braintree-customer-find-node]] — customer-ID lookup with an explicit missing-code limitation
- [[source-braintree-tokenization-key-javascript-v3]] — reduced-privilege client authorization and JavaScript initialization
- [[source-braintree-webhooks-testing-go-live-node]] — sample versus delivered webhook testing and limitations
- [[source-braintree-payment-method-nonce-find-node]] — non-consuming nonce lookup and risk-check information
- [[source-braintree-payment-method-nonce-create-node]] — nonce creation with source-qualified usage guidance
- [[source-braintree-payment-method-delete-node]] — deletion and associated-subscription consequences
- [[source-braintree-transaction-submit-for-settlement-node]] — explicit Node settlement submission and availability-qualified adjustment/data routes
- [[source-braintree-authorization-overview]] — client-authorization capability comparison and selection guidance
- [[source-braintree-client-token-generate-node]] — Node token generation and customer-ID variant
- [[source-braintree-transaction-void-node]] — void eligibility and conditional reversal
- [[source-braintree-authorization-client-token]] — signed-token roles and validity boundaries
- [[source-braintree-hosted-fields-events-javascript-v3]] — JavaScript Hosted Fields events and field-state retrieval
- [[source-braintree-transaction-refund-node]] — Node refund requirements and failure distinctions
- [[source-braintree-webhooks-parse-node]] — webhook parsing, ordering and retry qualifications
- [[source-braintree-payment-method-nonces]] — nonce/single-use naming, use and lifespan boundaries
- [[source-braintree-webhooks-create-node]] — webhook configuration and destination requirements
- [[source-braintree-get-started]] — initial integration and client/server flow; preserves the website-versus-repository Drop-in lifecycle-date conflict
- [[source-braintree-transaction-sale-node]] — Node transaction creation and raw-detail routes, including the risk/fraud prerequisite and an inconsistent example
- [[source-braintree-webhooks-overview]] — notification overview, permissions and volume boundaries
- [[source-braintree-control-panel-overview]] — administrative UI, reporting limitations and environment isolation
- [[source-braintree-credit-cards-client-javascript-v3]] — version-qualified Card Fields/Hosted Fields support boundary

## GraphQL API Contract

The `braintree/graphql-api` baseline at exact commit `3a89f42` exposes the GraphQL contract for transaction authorization, charge, capture, partial capture, refunds and voids; client tokens, tokenization and vaulting; PayPal one-time payments and billing agreements; Venmo payment contexts; 3D Secure; and recurring billing plans and subscriptions.

The schema is field-level contract evidence, not proof of merchant enablement or client-SDK support. Integration questions should combine it with the appropriate Web, Android, iOS, or server SDK source rather than treating schema presence as an end-to-end capability claim.

## Node.js Server SDK Surface

`braintree@3.39.0` provides gateway configuration, client-token generation, customer and payment-method vault operations, transaction authorization and settlement, refunds and voids, PayPal and Venmo instruments, card verification and 3DS data, plans and subscriptions, and signed webhook parsing.

The server SDK does not render checkout. Browser or native SDKs collect approval or payment data and return a nonce or token to the merchant server. PayPal customer sessions are restricted to authorized merchants, and legacy Venmo SDK transaction parameters warn merchants to migrate to Pay with Venmo.

## PHP Server SDK Surface

`braintree_php@6.37.0` provides PHP gateway configuration, client-token generation, customer and payment-method vault operations, transaction authorization and settlement, refunds and voids, PayPal and Venmo instruments, plans and subscriptions, and signed webhook parsing.

The PHP package requires PHP 7.3 or later and supports key credentials or OAuth credentials without mixing them. Webhook signature verification specifically requires public/private API keys. The exact release hardens Address and Dispute path IDs, adds PayPal email validation codes, and adds preferred-payment-method context to client-token generation.

## Ruby Server SDK Surface

`braintree@4.40.0` provides Ruby gateway configuration, client-token generation, customer and payment-method vault operations, transaction authorization and settlement, refunds and voids, PayPal and Venmo instruments, plans and subscriptions, and signed webhook parsing.

The active 4.x package requires Ruby 2.6 or later and supports key credentials or OAuth credentials without mixing them. Its exact release hardens Address and Dispute path IDs, adds PayPal email validation codes, and adds network-qualified 3DS pass-through fields. Unlike the retained Node and PHP baselines, its client-token signature does not expose `preferredPaymentMethodToken`.

## Web SDK Surface

- Hosted Fields provides merchant-styled, Braintree-hosted card inputs.
- 3D Secure verifies card nonces and reports liability-shift outcomes.
- PayPal Checkout v6, Venmo, Fastlane, Apple Pay, and Google Pay connect external wallet experiences to Braintree processing.
- Local Payment, SEPA, US bank account, and Instant Verification cover additional payment and bank-verification paths.
- Data Collector, Payment Ready, and preferred-method signals support risk and presentation decisions but do not themselves prove eligibility.

## Card Brand Detection Utility

`credit-card-type@10.3.0` is a standalone CommonJS utility that infers likely card brands from partial or complete number prefixes and supplies expected number lengths, formatting gaps, and security-code metadata. Its exact release adds Troy; the retained v10 changelog also records Naranja and Verve additions.

The package has no runtime dependencies and can be used independently of Braintree processing. It does not validate a PAN, choose a co-badged processing network, tokenize a card, establish merchant acceptance, or authorize a payment. Its mutable custom-card and ordering APIs affect subsequent detector calls in the same loaded module.

## UUID Utility

`@braintree/uuid@2.0.0` is a zero-argument CommonJS UUID v4 generator used in Braintree's JavaScript SDK ecosystem. It tries global `crypto.randomUUID()`, falls back to `crypto.getRandomValues()` with explicit version and variant bits, and throws when neither secure source is available; it has no insecure random fallback or runtime dependency.

The retained `braintree-web@3.144.0` package pins UUID `2.0.0`, while `braintree-web-drop-in@1.47.0` pins UUID `1.0.1`. The v2 implementation therefore cannot be projected onto that Drop-in baseline. UUID generation is internal utility behavior, not payment-resource creation, API idempotency, tokenization, eligibility, or transaction processing.

## Input Formatting Utility

`braintree/restricted-input` at `default-branch@8dcc6ea` contains package metadata for `restricted-input@4.2.0` and provides pattern-driven filtering and formatting for browser inputs. It accepts alpha, digit, and wildcard placeholders, inserts permanent characters, preserves selection state, handles paste and autofill events, and exposes the unformatted value and runtime pattern changes.

The utility uses separate iOS, Android Chrome or ChromeOS, KitKat WebView, IE9, and base strategies. Detected Samsung browser cases disable active formatting because the source notes that digits can be dropped. Exact classification is delegated to `@braintree/browser-detection@^2.1.1`. The package does not detect a card brand, validate a PAN, mask sensitive data, tokenize a card, establish merchant acceptance, or process a payment.

## Drop-in Surface

The additive `braintree-web-drop-in@1.48.0` update hardens the displayed card suffix through numeric conversion, truncation, and zero-padding; it retains the HTML template and the same runtime dependencies. This is not new checkout functionality or a digits-only validator. Its September 10 release leaves the September 1 no-updates notice unchanged, while the website guide gives October lifecycle dates; retain this unresolved source-specific conflict rather than infer renewed support. [[source-github-braintree-web-drop-in]] [[changelog-github-braintree-web-drop-in]] [[source-braintree-get-started]]

`braintree-web-drop-in@1.47.0` provides an opinionated UI for cards, PayPal, PayPal Credit, Venmo, Apple Pay, and Google Pay, with vaulted-method display, optional Data Collector output, and 3D Secure verification. It pins `braintree-web@3.123.2`, not the separately retained `3.144.0` modular SDK.

The repository schedules Drop-in deprecation for 2026-09-01 and unsupported status for 2027-09-01 and directs merchants to migrate to the modular Braintree SDK. Its notice says processing will be supported for one year after deprecation, while processing on unsupported SDKs may be suspended at any time. Current support status should be rechecked for time-sensitive guidance.

## Android SDK Surface

`braintree-android@5.30.0` provides modular native clients for cards, PayPal, Venmo, Google Pay, local payments, SEPA, 3D Secure, fraud data, and payment-method presentation. Redirect-capable methods use a request/launcher/result pattern with app-link or deep-link return handling before nonce tokenization.

PayPal and Venmo are separate Braintree modules. Venmo can launch the Venmo app or a mobile browser and supports conditional multi-use vaulting with a customer-scoped client token. This is distinct from the standalone `paypal/paypal-android` SDK, whose retained `2.3.0` source does not establish a native Venmo path.

## Android Drop-in Surface

`drop-in@6.17.0` provides a prebuilt Android payment-selection experience for cards, PayPal, Venmo, Google Pay, saved methods, vault management, card 3D Secure, and device-data collection. It requires Android API 21+ and pins Braintree Android `4.50.0`, so behavior from the independently retained `braintree-android@5.30.0` modular SDK cannot be attributed to it.

Most selections return a nonce for server processing. PayPal defaults to a vault request, Venmo defaults to single use, and Venmo visibility requires remote enablement plus an available Venmo app switch at this baseline. Customer-scoped client tokens enable saved-method retrieval and deletion.

## iOS SDK Surface

`braintree-ios@7.9.0` provides modular native clients for cards, PayPal, Venmo, Apple Pay, local payments, SEPA, 3D Secure, fraud data, Shopper Insights, messaging, and payment UI. It requires iOS 16+, Xcode 16.2+, and Swift 5.10+.

PayPal supports separate checkout and vault requests, including billing-agreement consent and recurring metadata. Venmo is a separate native Braintree module using universal-link app switch with browser fallback and conditional multi-use vaulting. Apple Pay support creates and tokenizes a native payment request; the demo's recurring sheet does not by itself establish later merchant charges.

## iOS Drop-in Surface

`BraintreeDropIn@9.14.0` provides a prebuilt UIKit payment-selection experience for cards, PayPal, Venmo, Apple Pay, saved methods, vault management, and card 3D Secure. It supports iOS 12+ and requires `braintree_ios` 5.27.0, so behavior from the independently retained `braintree-ios@7.9.0` modular SDK cannot be attributed to it.

Most selections return a nonce for server processing. Apple Pay selection returns only a method type and requires the merchant to present and tokenize the Apple Pay sheet separately. Venmo visibility additionally requires remote enablement and an installed Venmo app at this baseline.

## iOS PopupBridge Surface

`PopupBridge@3.1.0` adapts PayPal or Braintree web checkout running inside `WKWebView`: JavaScript requests a popup, native code opens `ASWebAuthenticationSession`, and the validated return URL is delivered to the page. It requires iOS 16+, Xcode 16.2+, and Swift 5.10+.

Exact release `3.1.0` adds a merchant return-scheme initializer for Venmo app switch. The bridge reports whether Venmo is installed and can advertise the merchant scheme to Braintree Web, but it does not enable Venmo, create a payment session, tokenize a payment, or process a transaction. Its README lists PayPal SDK v5 as supported and v6 or later as unsupported.

The retained podspec, privacy manifest, and PayPal data-collector guide conflict with the exact runtime: the podspec names the replaced browser controller, the privacy manifest has blank declarations despite analytics metadata transmission, and the guide uses delegate callbacks removed in v2. See [[source-github-popup-bridge-ios]] for the exact boundaries.

## Android PopupBridge Surface

`popup-bridge@5.3.0` adapts a web checkout running inside an Android WebView by exposing a JavaScript interface, opening popup URLs through Braintree Browser Switch, persisting the pending request, and returning deep-link data to the page. The exact build requires Android API 23+, targets API 37, and uses Browser Switch `3.5.1`.

The host activity owns the deep link, must use `PopupBridgeWebViewClient`, and must forward return intents through `handleReturnToApp()`. Venmo installation state is injected after page load. As on iOS, this is transport evidence rather than payment-session, tokenization, merchant-enablement, or processing evidence.

The retained Android README and migration guides conflict with the exact runtime on minimum SDK, lifecycle handling, version status, and data-collector APIs. See [[source-github-popup-bridge-android]] for the exact `5.3.0` behavior.

## Mobile SDK Developer Tooling

`braintree/mobile-sdk-tooling` at `default-branch@a3b0ffe` provides a shared GitHub Actions review digest for configured Braintree mobile SDK repositories. It authenticates with a GitHub App, reduces each reviewer's full history to the latest decisive state, applies CODEOWNER-aware approval counting and inner-source routing, and posts qualifying pull requests to Slack.

This is engineering-operations evidence only. It does not establish SDK implementation behavior, release readiness, merchant eligibility, or payment processing. Its current limitations include a 100-open-pull-request cap per repository, manual daylight-saving cron maintenance, individual-only CODEOWNER extraction, and Ubuntu/GNU shell assumptions.

## Web SDK Release Automation

`braintree/web-sdk-github-actions` at `default-branch@e9c8ae9` retains CI, version/changelog preparation, branch/PR creation, publication, release-note and cleanup wiring. It is engineering tooling, not a payment SDK. README full-pipeline claims exceed the retained implementation; change detection has a confirmed shell syntax error, and dry-release jobs do not transfer the bumped artifact. Older pinned actions and excluded generated bundles remain unverified. See [[source-github-web-sdk-github-actions]], [[changelog-github-web-sdk-github-actions]] and [[braintree-sdk-release-automation]].

## Versioned Implementation Knowledge

The retained history begins with `braintree-web@3.143.0` and currently reaches `3.146.0` at exact SHA `893d4e786f4161c3b96c5d34425752c5b63ff84d`. Version 3.144.0 added non-v6 PayPal View/Edit Funding Instrument, expanded PayPal Checkout v6 session options, and prevented failed incognito detection from aborting Venmo creation. Version 3.145.0 fixes v6 checkout-with-vault tokenization, adds ECD-gated Venmo desktop address requests and QR rescan UI, and improves client loading and popup recovery. Version 3.146.0 adds v6 View/Edit Saved Payment with a preferred vaulted-token client context, presentation-option forwarding, and Hosted Fields/frame-message hardening. The supplemental sandbox helper is not production credential-handling guidance. Recovery analytics and approval do not prove payment success; delegated SDK and gateway behavior remain outside the retained implementation evidence. See [[source-github-braintree-web]] and [[changelog-github-braintree-web]].

Repository evidence is not current enablement guidance. PayPal, Venmo, and Fastlane modules have configuration or delegated-runtime boundaries, and legacy source modules should not be treated as recommendations for new integrations.

## Knowledge Status

- Ingested website-document sources: 185 (Braintree C01–C23; raw snapshots collected 2026-09-16)
- Ingested cumulative GitHub repository sources: 17
- Ingested package releases: 15
- Latest retained GraphQL API ref: `default-branch@3a89f42` at `3a89f427466a0a978dbfcfd953913f4e76c3264a`
- Latest retained Braintree Node release: `braintree@3.39.0` at `7a9270aaf31eb87819add64a768652243f90007c`
- Latest retained Braintree PHP release: `braintree_php@6.37.0` at `0f53ece38397c9fed05b94620634a5a23ef8ee48`
- Latest retained Braintree Ruby release: `braintree@4.40.0` at `1217992763cc13f33dbd8b6c51ad2ae058ddd2a8`
- Latest retained Braintree Web release: `braintree-web@3.146.0` at `893d4e786f4161c3b96c5d34425752c5b63ff84d`
- Latest retained card-brand detector release: `credit-card-type@10.3.0` at `fbd8ed80a411fa9b238055208c19a7323cd38e21`
- Latest retained UUID utility release: `@braintree/uuid@2.0.0` at `d134a2ca93d12705a76ff036baeba568016f9b13`
- Latest retained input formatter ref: `default-branch@8dcc6ea` at `8dcc6ea9e6cea44eef2b02fbc3f7569a602fa089` (`package.json` 4.2.0)
- Latest retained Drop-in release: `braintree-web-drop-in@1.47.0` at `ec1c7c533c2e878545f2b25505c56b7e22dc1c17`
- Latest retained Android release: `braintree-android@5.30.0` at `51f183a48557d0fd00eefa541712df0c4f21ee28`
- Latest retained Android Drop-in release: `drop-in@6.17.0` at `da8a702bb37e3a4567e5ba4dd8cbc2257acc37c7`
- Latest retained iOS release: `braintree-ios@7.9.0` at `4e987ca19f03b65a0d303b4c3ec95e0c723be971`
- Latest retained iOS Drop-in release: `BraintreeDropIn@9.14.0` at `d951d104ac960188824bda191be2f57c57351a31`
- Latest retained iOS PopupBridge release: `PopupBridge@3.1.0` at `00256b4b8c58367287fe35a442a33cd7c010a94f`
- Latest retained Android PopupBridge release: `popup-bridge@5.3.0` at `f30654168b997ea1dd95ebc61901582ae00bebb0`
- Latest retained mobile SDK tooling ref: `default-branch@a3b0ffe` at `a3b0ffe7931cde179f8b0dfdd5162979adf81683`
- Latest retained web SDK automation ref: `default-branch@e9c8ae9` at `e9c8ae99ae5365f91f8e5372ae2d9d2dc7a427e0`

## Sources

- [[source-github-web-sdk-github-actions]] - web SDK release-automation contracts and caveats
- [[changelog-github-web-sdk-github-actions]] - commit-qualified automation history
- [[source-github-graphql-api]] - commit-qualified GraphQL API contract
- [[changelog-github-graphql-api]] - GraphQL schema history
- [[source-github-braintree-node]] - cumulative Node.js server SDK implementation baseline
- [[changelog-github-braintree-node]] - package-qualified Node.js release ledger
- [[source-github-braintree-php]] - cumulative PHP server SDK implementation baseline
- [[changelog-github-braintree-php]] - package-qualified PHP release ledger
- [[source-github-braintree-ruby]] - cumulative Ruby server SDK implementation baseline
- [[changelog-github-braintree-ruby]] - package-qualified Ruby release ledger
- [[source-github-braintree-web]] — cumulative Braintree Web implementation baseline
- [[changelog-github-braintree-web]] — package-qualified release ledger
- [[source-github-credit-card-type]] - cumulative card-brand detection implementation baseline
- [[changelog-github-credit-card-type]] - package-qualified card-brand detector release ledger
- [[source-github-uuid]] - cumulative secure UUID generation baseline
- [[changelog-github-uuid]] - package-qualified UUID utility release ledger
- [[source-github-restricted-input]] - cumulative browser input-formatting implementation baseline
- [[changelog-github-restricted-input]] - commit-qualified formatter and package-history ledger
- [[source-github-braintree-web-drop-in]] - cumulative Drop-in implementation baseline
- [[changelog-github-braintree-web-drop-in]] - package-qualified Drop-in release ledger
- [[source-github-braintree-android]] - cumulative native Android implementation baseline
- [[changelog-github-braintree-android]] - package-qualified Android release ledger
- [[source-github-braintree-android-drop-in]] - cumulative prebuilt Android Drop-in implementation baseline
- [[changelog-github-braintree-android-drop-in]] - package-qualified Android Drop-in release ledger
- [[source-github-braintree-ios]] - cumulative native iOS implementation baseline
- [[changelog-github-braintree-ios]] - package-qualified iOS release ledger
- [[source-github-braintree-ios-drop-in]] - cumulative prebuilt iOS Drop-in implementation baseline
- [[changelog-github-braintree-ios-drop-in]] - package-qualified iOS Drop-in release ledger
- [[source-github-popup-bridge-ios]] - cumulative iOS WebView popup transport baseline
- [[changelog-github-popup-bridge-ios]] - package-qualified iOS PopupBridge release ledger
- [[source-github-popup-bridge-android]] - cumulative Android WebView popup transport baseline
- [[changelog-github-popup-bridge-android]] - package-qualified Android PopupBridge release ledger
- [[source-github-mobile-sdk-tooling]] - cumulative mobile SDK review-automation baseline
- [[changelog-github-mobile-sdk-tooling]] - commit-qualified mobile SDK tooling history

## Related

- [[braintree-sdk-release-automation]] - release preparation, publication and evidence boundaries
- [[braintree-fraud-tools]] - Basic velocity and AVS/CVV controls
- [[braintree-3d-secure]] - cardholder authentication and conditional liability shift
- [[braintree-fraud-protection]] - named Fraud Protection risk decisions
- [[braintree-fraud-protection-advanced]] - Advanced review and risk-decision route
- [[braintree-kount-custom]] - Kount decision handoff and finality
- [[braintree-chargeback-protection]] - conditional protection-tool and eligibility route
- [[braintree-effortless-chargeback-protection]] - Effortless evidence and fee boundaries
- [[braintree-webhooks]] — website-document notification entry
- [[braintree-control-panel]] — website-document administration entry
- [[braintree-index]] — Braintree catalog and operations links
- [[braintree-log]] — collection and ingest history
- [[braintree-web-sdk]] — browser SDK concept
- [[card-brand-detection]] - generic brand inference, ambiguity, UI metadata, and validation boundary
- [[payment-input-formatting]] - generic pattern, browser-event, paste, caret, and validation boundaries
- [[braintree-server-sdk]] - shared server integration boundary and package-qualified evidence rules
- [[braintree-web-drop-in]] - prebuilt checkout UI and migration boundary
- [[braintree-android-sdk]] - native Android request, launcher, nonce, PayPal, and Venmo model
- [[braintree-ios-sdk]] - native iOS nonce, PayPal, Venmo, Apple Pay, and migration model
- [[braintree-popup-bridge]] - WebView popup transport and payment-processing boundary
- [[paypal-braintree-integration]] — Braintree PayPal v6 processing boundary
