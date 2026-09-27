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
