---
title: "Braintree Control Panel"
type: concept
category: technology
tags: [braintree, control-panel, gateway-administration, sandbox, production, reporting]
---

## Braintree Control Panel

The Braintree Control Panel is the user interface for administering a Braintree gateway. Most functions can also be automated through the API, but the overview identifies payment-method enablement, fraud and recurring-billing configuration, email-receipt enablement, webhooks, users and roles, custom fields, and processing-credential access as tasks that must be completed in the Control Panel. [[source-braintree-control-panel-overview]]

## Dashboard and environment boundaries

The Dashboard provides sales and transaction volume, totals, averages, and routes to statements, summaries, and other reports. Successful transactions are expected to appear the day after settlement, but the Dashboard is for general sales patterns rather than reconciliation, and Braintree Marketplace transactions are excluded from its daily-sales graphs.

Sandbox and Production use mutually exclusive Control Panel environments that do not interact and may have different login credentials. Use the dedicated reporting documentation for reconciliation and the specific administration guides for task-level behavior. [[source-braintree-control-panel-overview]]

## Sources

- [[source-braintree-auth-configuration]] - closed-beta platform OAuth application configuration in the environment-specific Control Panel, including merchant-facing metadata, registered redirects and server-held client credentials
- [[source-braintree-payment-methods-paypal-funding-reconciliation]] - PayPal reconciliation route for details available in the PayPal console but not the Braintree Control Panel, plus the mapping from PayPal Transaction ID to Authorization Unique Transaction ID and its distinction from the Braintree transaction ID
- [[source-braintree-payment-methods-paypal-setup-guide]] - PayPal production enablement route through Business Account credential linking in the Braintree Control Panel, including the one-account-per-gateway boundary and generated REST API app dependency
- [[source-braintree-payment-methods-paypal-disputes]] - PayPal-specific Control Panel dispute management with full-integration and linked-account prerequisites, Add/Edit Processing Options permission, stage and deadline handling, retrieval actions, evidence routes and a separate credit-card-dispute workflow boundary
- [[source-braintree-control-panel-security-rotating-api-keys]] - exposure-driven API-key rotation, overlapping old/new key validity, per-user Control Panel generation and confirmation-before-deletion safety boundary, kept distinct from login and payment authentication
- [[source-braintree-fraud-tools-premium-fraud-protection]] - named Fraud Protection merchant-interface tuning, transaction risk-decision lookup and Premium Fraud Management Tools device-data diagnostic, distinct from processor approval and from Fraud Protection Advanced
- [[source-braintree-fraud-tools-basic-avs-cvv-rules]] - Control Panel configuration for credit-card AVS/CVV rules, including transaction scoping, post-issuer-approval gateway rejection and void behavior, Vault defaults and international AVS false-rejection boundaries
- [[source-braintree-fraud-tools-basic-risk-threshold-rules]] - Control Panel creation, criteria and enable/disable routes for credit-card and certain-Google-Pay velocity checks, with supporting-field and temporary-disable boundaries
- [[source-braintree-control-panel-security-two-factor-authentication]] - Control Panel 2FA access requirement, app/SMS and WebAuthn security-key routes, factor fallback, Account Admin-assisted lockout recovery and self-service reset limits, kept distinct from payment authentication and fraud tools
- [[source-braintree-get-started-try-it-out]] - Sandbox testing purpose, country-qualified behavior, material Sandbox-versus-Production differences, non-transfer of objects and settings, separate credentials and the delegated production-integration route
- [[source-braintree-get-started-overview]] - high-level route distinguishing manual Control Panel administration from API-based automation and customized gateway interaction
- [[source-braintree-control-panel-vault-overview]] - Vault purpose, encrypted tokenized payment-method storage, high-level record administration, Control Panel exports, CVV non-retention and the recurring-statement-indicator caveat, with create, update and verification procedures left to dedicated pages
- [[source-braintree-control-panel-users-roles-role-permissions]] - Control Panel permission categories and action scopes, including the Account Admin gate for granting user/role management, specialized Forward API and OAuth eligibility, broad connected-OAuth consent scope, and the collected Account Admin scope tension
- [[source-braintree-control-panel-vault-create]] - Control Panel creation of a new Vault customer with or without a credit card, with separate transaction-time and API routes, verification guidance, and the credit-card-only, conditional-CVV and never-store-CVV boundaries
- [[source-braintree-control-panel-users-roles-log-in-with-paypal]] - PayPal-credential login for separate Braintree Sandbox or Production accounts, with Braintree-credential and 2FA transition warnings and an explicit boundary from PayPal payment-method setup
- [[source-braintree-control-panel-custom-fields]] - Control Panel custom-field configuration route covering Pass Thru versus Store and Pass Back visibility, Add/Edit Processing Options permission, API-setup exclusion, never-used deletion eligibility, and the documented view of ACTIVE Fraud Protection Advanced fields
- [[source-braintree-control-panel-vault-update]] - Control Panel Vault customer, payment-method and address updates, with the high-volume API route and collected PCI, subscription, AVS and transaction-shipping boundaries
- [[source-braintree-control-panel-users-roles-managing-users-roles]] - Control Panel user and role creation/editing, role precedence, account activation, immutable usernames and permission-gated password-reset administration, with separate-user and account-security boundaries
- [[source-braintree-control-panel-important-gateway-credentials]] - Control Panel routes for environment-specific API keys, gateway and merchant-account identifiers, client tokenization keys and the legacy CSE key, with role and private-key security boundaries
- [[source-braintree-control-panel-vault-card-verification]] - Control Panel account-wide and vaulted-card verification for credit and debit cards, with $0/$1 authorization-and-void behavior, retry outcomes, CVV recollection and payment-method-versus-customer identity boundaries
- [[source-braintree-control-panel-search]] - Control Panel basic and advanced search routes for transactions, verifications, Vault records and subscriptions, with the collected 60-day and indexing-delay qualifications, object-specific result boundaries and CSV download limits
- [[source-braintree-control-panel-reporting-expiring-cards]] - Control Panel report for expired and soon-to-expire Vault cards, with date-range and all-expired views plus a boundary between report visibility, merchant reminders and separately enabled Account Updater requests
- [[source-braintree-control-panel-webhooks]] - role-gated Control Panel webhook creation and testing route, including destination and notification selection, separate server parsing, and the production test-kind caution
- [[source-braintree-control-panel-reporting-decline-analysis]] - Control Panel processor-decline search and CSV analysis by processor response or BIN, with separate verification-search and repeated-attempt skew boundaries and no imported retry policy
- [[source-braintree-control-panel-reporting-grant-api-report]] - limited-release beta Grant API report for recipient transaction count and volume grouped by currency, with OAuth-consent visibility and Control Panel execution boundaries
- [[source-braintree-control-panel-reporting-transaction-summary]] - Control Panel date-range and grouping route for current transaction-status totals, with the explicit processing-trend rather than reconciliation boundary
- [[source-braintree-control-panel-reporting-1099-k]] - qualified 1099-K eligibility and Control Panel access, prior-year availability and US Braintree Direct delivery fallback, with separate PayPal and direct-Amex form boundaries
- [[source-braintree-control-panel-reporting-settlement-batch-summary]] — Control Panel settlement-batch totals, report access and marketplace limits, account-specific cutoff behavior, funding-reconciliation exclusions, and daily email settings
- [[source-braintree-control-panel-audit-webhooks]] - collected select-partner Audit Webhook event catalog for API, Login, authorization, OAuth and fraud-protection administration changes; the article states neither a required Control Panel permission nor a setup procedure and does not establish equivalence to transaction events
- [[source-braintree-control-panel-reporting-transaction-level-fee-report]] - role-gated downloadable transaction-fee reporting with country, pricing-model, payment-method, data-availability and reconciliation boundaries
- [[source-braintree-control-panel-reporting-overview]] — Control Panel report categories, account/location and report-specific eligibility qualifications, and the boundary that this overview does not establish Dashboard behavior or reconciliation sufficiency
- [[source-braintree-control-panel-transaction-issues]] — rare transaction issues distinguished from standard processor declines and gateway rejections, with optional webhook delivery, Control Panel notification setup, role-scoped User Recipients, unrestricted-address Email Recipients, and no documented investigation workflow
- [[source-braintree-control-panel-descriptors]] — collected descriptor article covering soft, hard and dynamic statement visibility, bank and processor qualifications, Control Panel versus per-transaction API configuration, regional support routing, and the separate PayPal-console path
- [[source-braintree-control-panel-gateway-rejections]] — gateway-setting rejection versus customer-bank decline, pre-processor and post-authorization rejection timing, automatic void behavior, bank-acknowledgment warning, and `Gateway Rejected` reason routing
- [[source-braintree-control-panel-transaction-clone]] — Control Panel transaction cloning with copied payment information, payment-method/Vault/status eligibility limits, the narrow fraud/risk rejection exception, amount/CVV entry, and authorization-only settlement selection
- [[source-braintree-control-panel-transaction-create]] — manual Control Panel transaction creation, new-card versus Vault payment-method eligibility, authorization-only selection, and the industry-and-processor-qualified settlement-adjustment limit
- [[source-braintree-control-panel-duplicate-checking]] — default-enabled gateway duplicate screening for qualifying repeated transaction requests, payment-method-specific matching, immediate rejection behavior, and Account Admin Control Panel configuration boundaries
- [[source-braintree-control-panel-email-receipts]] — Control Panel gateway-receipt activation and configuration, submitted-for-settlement transaction/refund scope, customer-email and customization limits, duplicate PayPal receipts, and the separate subscription-failure-notification boundary
- [[source-braintree-control-panel-managing-authorizations]] — collected authorization-management article covering recommended Vault reuse, discouraged repeated authorizations, eligibility-qualified adjustments, and the boundary between its Control Panel documentation location and API/SDK operations
- [[source-braintree-control-panel-bank-identification-numbers]] — Control Panel and CSV BIN lookup, linked API retrieval, six-digit output boundaries during the 8-digit issuer-BIN expansion, and collected PCI qualifications

- [[source-braintree-control-panel-overview]] — Control Panel purpose, administration categories, Dashboard limitations, and Sandbox/Production isolation
