---
title: "Braintree Payment Methods"
type: concept
category: technology
tags: [braintree, payment-methods, cards, digital-wallets, eligibility]
---

## Braintree Payment Methods

Braintree's collected getting-started page is a provider-wide route to its stated payment-method categories and eligibility qualifications. The page covers ACH Direct Debit, Apple Pay, Google Pay, cards, PayPal, Local Payment Methods, Venmo and Secure Remote Commerce, while recording Samsung Pay as deprecated and a dated end-of-support notice for Visa Click to Pay. Detailed setup belongs to the dedicated method guides rather than this overview. [[source-braintree-get-started-payment-methods]]

## Eligibility boundaries

Availability is not uniform across the listed methods. The page qualifies methods by combinations of merchant region, customer participation, processor settings, third-party approval, merchant-account card bundles, supported regional card networks, merchant category code, US merchant status and limited-release eligibility. Its collected current-tense wording is snapshot evidence, not proof of present support, merchant enablement or buyer eligibility. [[source-braintree-get-started-payment-methods]]

Card scope also varies by account and use case: the page distinguishes US from most international default card-brand bundles, treats major-brand online debit as credit because PINs cannot be accepted online, allows dual-branded routing only on a network supported in the merchant's region, and requires an appropriate MCC for special-use cards. Use the source and its raw detail locators to select the applicable qualification before following a dedicated integration route. [[source-braintree-get-started-payment-methods]]

> [!warning] Contradiction
> The page's opening note equates Visa Click to Pay with Secure Remote Commerce and gives a January 20, 2026 end-of-support date, while its final section calls Secure Remote Commerce a current limited release for eligible merchants. The snapshot does not resolve the conflict; use the source and raw locators rather than inferring current support.

## Sources

- [[source-braintree-articles-au-transactions-accepted-payment-methods]] - 2026-09-16 Braintree-hosted AU-path account article for default Visa and Mastercard acceptance, direct Amex setup with currency and pricing prerequisites, and qualified PayPal, Apple Pay and Google Pay availability; not current support, universal merchant eligibility, fixed pricing or payment-execution proof, with the narrower mobile-only wallet wording versus dedicated web-capable guides preserved as an unresolved channel-scope difference

- [[source-braintree-articles-apac-transactions-accepted-payment-methods]] - 2026-09-16 Braintree-hosted APAC-path account article for default Visa and Mastercard acceptance, Hong Kong/Singapore-only direct Amex setup and pricing prerequisites, qualified PayPal and wallet availability, and merchant-account currency handling; not current regional support, universal merchant eligibility, fixed pricing or payment-execution proof, with the known SRC/Click to Pay support-status conflict left unresolved

- [[source-braintree-articles-aib-bf-transactions-accepted-payment-methods]] - 2026-09-16 Braintree-hosted exact AIB BF account article for configured card brands, consequential Maestro 3D Secure and Control Panel conditions, separately enabled JCB/Discover/Diners Club, qualified alternative methods, and merchant-account currency selection with conversion-fee/refund warnings; not AIB AF, current independent authority, a merchant-specific agreement, or payment-execution proof

- [[source-braintree-articles-aib-af-transactions-accepted-payment-methods]] - 2026-09-16 Braintree-hosted AIB AF account article for default Visa, Mastercard and Maestro acceptance, separately configured Amex with pricing prerequisites, 3D-Secure-qualified Maestro constraints, qualified alternative methods, and merchant-account currency setup; not AIB BF, independent current bank authority, universal availability, fixed pricing or payment-execution proof

- [[source-braintree-articles-wells-ic-transactions-accepted-payment-methods]] - 2026-09-16 Braintree-hosted Wells IC article for account-scoped card acceptance, qualified alternative methods, American Express account and support choices, and merchant-account currency setup; not current independent bank policy, Wells Flat evidence, universal availability, fixed pricing or payment-execution proof

- [[source-braintree-articles-wells-flat-transactions-accepted-payment-methods]] - 2026-09-16 Braintree-hosted Wells Flat account article for PIN/password-qualified card acceptance, aggregated-versus-direct Amex account responsibilities, conditionally available alternative methods and ambiguous deprecation wording; not a Wells IC, provider-wide or current support guarantee
- [[source-braintree-articles-adyen-transactions-accepted-payment-methods]] - 2026-09-16 Braintree-hosted Adyen-processor article for account-default Visa, Mastercard and American Express acceptance, with American Express currency limits and merchant-account currency setup; not universal Adyen availability or a Braintree Orchestration guide
- [[source-braintree-articles-chase-transactions-accepted-payment-methods]] - 2026-09-16 Braintree-hosted Chase accepted-payment-methods article for default card scope, separately configured Amex acceptance and pricing, qualified PayPal/Apple Pay/Google Pay availability, and currency-account limitations; not independent Chase authority, universal availability or payment-execution evidence
- [[source-braintree-local-payment-methods-alipay]] - collected unversioned Alipay method route for limited-release applicability, geography, currency-code and transaction-limit retrieval, preserving the unresolved umbrella Euro-presentment relationship and snapshot/execution-evidence boundaries
- [[source-braintree-local-payment-methods-pay-upon-invoice-ios-v7]] - iOS v7-routed Pay Upon Invoice availability notice that directs integration to JavaScript v3 and provides no iOS procedure
- [[source-braintree-local-payment-methods-pay-upon-invoice-android-v5]] - Android v5-routed Pay Upon Invoice availability notice stating that the method is only available for the JavaScript v3 SDK, without an Android integration procedure
- [[source-braintree-local-payment-methods-satispay]] - collected Satispay route for limited-release Italy-buyer applicability, captured seller/currency/transaction-limit labels and separate platform integration-guide navigation, without implying merchant enablement or payment execution
- [[source-braintree-local-payment-methods-grabpay]] - collected unversioned GrabPay method notice for limited-release and applicability retrieval, preserving its unresolved seller-country conflict
- [[source-braintree-local-payment-methods-configuration-javascript-v3]] - JavaScript v3 Local Payment Methods configuration checklist for linked PayPal Business Account, server-generated client token, client integration, server transaction creation, webhooks and Sandbox-or-Production success, without treating setup as execution proof
- [[source-braintree-local-payment-methods-configuration-android-v5]] - Android v5 configuration checklist for the linked PayPal business account, server-generated client token, client and server integration, webhooks and successful environment processing, with a historical mobile-certificate warning and no account-setup or execution-proof inference
- [[source-braintree-local-payment-methods-configuration-ios-v7]] - iOS v7-routed Local Payment Methods configuration checklist for PayPal business-account linking, server-generated client authorization, separate client/server/webhook responsibilities and a Sandbox-or-Production success prerequisite, with historical certificate and execution-evidence boundaries
- [[source-braintree-local-payment-methods-oxxo]] - unversioned collected OXXO guide for Mexico-pilot applicability and non-instant cash-voucher lifecycle retrieval, with the umbrella EUR-presentment wording versus the method-page MXN example left unresolved
- [[source-braintree-local-payment-methods-overview]] - unversioned Local Payment Methods developer overview for customer-country inventory, transaction-limit locators, non-instant labels, client/server routes, unsupported vaulting and recurring use, method-specific access and deprecation qualifications, and unresolved same-date EUR-versus-limit-currency tension
- [[source-braintree-local-payment-methods-boleto-bancario]] - unversioned Boleto Bancário developer guide for method-specific pilot applicability and non-instant lifecycle retrieval
- [[source-braintree-local-payment-methods-multibanco]] - collected Multibanco route for limited-release merchant and Portugal-buyer applicability, voucher-based ATM or online-banking payment, linked-PayPal setup, seven-day non-instant no-capture lifecycle, server-side GraphQL routing and required outcome webhooks
- [[source-braintree-local-payment-methods-trustly]] - collected Trustly route for direct bank-account initiation, method-specific `EUR`/`DKK`/`GBP`/`NOK`/`SEK` applicability, non-instant post-settlement transaction association, server-side GraphQL, required success/expiry webhooks and sandbox-only timing, preserving unresolved family-guide conflicts over blanket euro presentment and customer-confirmation funding
- [[source-braintree-local-payment-methods-client-side-custom-ios-v7]] - iOS v7 custom-client document route with method-specific request and initiation locators, preserving the unresolved umbrella-versus-method currency conflict and bounded webhook-versus-Payment-Context-GraphQL tension
- [[source-braintree-local-payment-methods-server-side-node]] - Node.js server-side Local Payment Methods guide for client-return and webhook-delivered nonce paths, one-time Transaction Sale submission, duplicate-sale rejection, and no-return refund and reversal boundaries
- [[source-braintree-local-payment-methods-mbway]] - collected MB WAY guide for limited-release applicability, JavaScript-client and server-side SDK scope, and the payment-ID-to-webhook nonce handoff without inferring settlement, funding or instant completion
- [[source-braintree-local-payment-methods-client-side-custom-android-v5]] - Android v5 custom client-side Local Payment Methods guide for merchant-owned UI, request/return handling and nonce handoff to separate server responsibilities, with unresolved client-page webhook versus server-page Payment Context API alternative wording
- [[source-braintree-local-payment-methods-testing-go-live-node]] - Node.js Local Payment Methods testing/go-live guide distinguishing mocked and linked-PayPal Sandbox approaches from separate Production credentials, server configuration and limited real-payment checks
- [[source-braintree-local-payment-methods-pay-upon-invoice-javascript-v3]] - JavaScript v3 Pay Upon Invoice route for pilot-only Germany/EUR B2C scope, linked PayPal onboarding, `startPayment` and payment-ID correlation, no-capture transaction association, required outcome webhooks, and shipment/dispute safeguards
- [[source-braintree-local-payment-methods-bancomatpay]] - collected BANCOMAT Pay guide for limited-release applicability, JavaScript-client and server-side SDK scope, and the payment-ID-to-webhook single-use-token handoff without inferring settlement, funding or instant completion
- [[source-braintree-credit-cards-server-side-node]] - collected Node.js-routed website guide for server-side card transaction and pre-Vault verification routes, with snapshot, package-version and execution-evidence boundaries
- [[source-braintree-credit-cards-client-side-ios-v7]] - website iOS v7 Card Fields guide for client-side card collection and tokenization, merchant-owned submission, server nonce handoff and sandbox testing
- [[source-braintree-credit-cards-client-side-android-v5]] - Android v5 website guide to Card Fields card-data collection and tokenization, merchant-owned surrounding checkout controls, authorization prerequisites and nonce return for server processing
- [[source-braintree-credit-cards-overview]] - unversioned website overview of the Card Fields card-entry description, client-token prerequisite and nonce handoff, with platform/version selection routed to the retained JavaScript v3 boundary
- [[source-braintree-credit-cards-configuration]] - collected credit-card configuration snapshot for the default setup posture, qualified Amex exception, and separate card-verification and AVS/CVV protection routes
- [[source-braintree-paypal-messaging-javascript-v3]] - Braintree Pay Later Messaging route preserving the captured native iOS/Android eligibility, Drop-in exclusion and promotional-content restrictions while flagging the absence of JavaScript v3 setup content
- [[source-braintree-payment-methods-paypal-shared-data]] - Braintree PayPal account creation/linking data-sharing route covering the article's contact, business-entity, credential, consent and approved-volume categories plus its TLS/SSL transport statement
- [[source-braintree-payment-methods-paypal-overview]] - Braintree PayPal overview route for One-Time, Vaulted and Recurring Payments selection, Braintree Direct and qualified availability boundaries, PayPal-owned pricing, dispute-management options and sandbox-testing paths
- [[source-braintree-payment-methods-paypal-processing]] - Braintree PayPal processing route for separate authorization/capture, PayPal's non-batch settlement transition, PayPal-and-Venmo partial settlements, refund timing and the article's legacy Vault warning
- [[source-braintree-payment-methods-paypal-setup-guide]] - Braintree PayPal setup route for eligibility-first prerequisites, verified Business Account and production Control Panel linking, the generated REST app dependency, unsupported eChecks and PayPal multi-currency setup
- [[source-braintree-payment-methods-paypal-best-practices]] - Braintree Pay with PayPal experience route distinguishing One-Time Checkout, sub-$40 mobile-first Vaulted Payments and Recurring Payments review-page guidance, with User Agreement presentation requirements and upstream shipping-callback qualifications
- [[source-braintree-paypal-pay-later-offers-javascript-v3]] - JavaScript v3 Pay Later route for the existing PayPal client-side prerequisite, dynamic messaging restrictions, amount-driven message rendering, standalone-button funding configuration and per-button eligibility checks

- [[source-braintree-payment-methods-sepa-direct-debit]] - pilot-only SEPA Direct Debit availability, mandate and linked-PayPal setup prerequisites, customer-confirmation funding statement, post-disbursement return exposure, and supported vaulting and recurring transactions

- [[source-braintree-payment-methods-paypal-pay-later-offers]] - Braintree PayPal Pay Later route for country-dependent offer identity, merchant-versus-customer eligibility, Checkout with Vault enablement, and messaging/button and promotional-content boundaries

- [[source-braintree-payment-methods-unionpay]] - UnionPay-specific deprecation and limited-release tension; European-merchant, SDK-version and settlement-currency conditions; SMS verification and vaulted-card behavior; processing, chargeback-fee and CVV/AVS-bypass boundaries

- [[source-braintree-payment-methods-paypal-credit]] - deprecated PayPal Credit guide covering the legacy reusable credit-line identity, US/UK currency and regulatory qualifications, customer credit approval, named financing options and existing-PayPal-setup boundary, with a separate Pay Later offers redirect

- [[source-braintree-payment-methods-secure-remote-commerce]] - SRC/Click to Pay identity, limited-release merchant and SDK prerequisites, credit-card-like processing routes, and the guide's unresolved January 2026 end-of-support versus current-tense availability conflict

- [[source-braintree-payment-methods-google-pay]] - dedicated Google Pay route for Android and web setup, merchant-versus-customer availability, card-or-account distinctions, method-specific fraud-tool and vaulting boundaries, and Google production approval

- [[source-braintree-payment-methods-local-payment-methods]] - regional bank, wallet and other local-method scope; eligible-merchant and PayPal-account prerequisites; locality-based display; euro presentment and primary-currency PayPal settlement; redirect-qualified Payment Context visibility; and unsupported dispute, vaulting and recurring-transaction boundaries

- [[source-braintree-payment-methods-apple-pay]] - dedicated Braintree Apple Pay route for conditional merchant and customer availability, mobile/web platform requirements, DPAN processing, vaulting consent guidance, integration roles and certificate renewal

- [[source-braintree-payment-methods-venmo]] - Venmo checkout and vaulting route with unsupported-business-model, US-entity, SDK-version, customer-version, production-profile and 180-day refund qualifications from the collected guide

- [[source-braintree-payment-methods-ach]] - ACH Direct Debit merchant eligibility, required bank-account verification, delayed batch settlement and late-return exposure, conflicting void guidance, and bank-account vaulting versus recurring-billing boundary

- [[source-braintree-get-started-payment-methods]] - provider-wide payment-method categories, merchant and customer qualifications, card scope, and collected deprecation boundaries
