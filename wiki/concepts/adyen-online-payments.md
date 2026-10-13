---
title: "Adyen Online Payments"
type: concept
category: technology
tags: [adyen, online-payments, checkout, webhooks]
---

## Overview

Adyen Online Payments is Adyen's documentation area for accepting card, wallet, and local payment methods on websites and mobile apps.

## Integration architecture

At overview level, the integration is divided among a payments server that calls Checkout API endpoints, a client website or app that collects shopper payment details and passes payment information to the server, and a webhook server that receives payment-status and other payments-related activity. The overview recommends API Libraries and Drop-in/Components; it does not state that those choices are mandatory. Library/API updates and the product lifecycle remain qualifications when applying the overview to a specific implementation.

## Sources

- [[source-adyen-docs-online-payments-payments-india-compliance-guide]] — Adyen India local-acquiring guide for account setup, card-data limits, saved-card models, and recurring mandate and pre-debit steps (webpage snapshot, 2026-09-15; excludes cross-border payments).


- [[source-adyen-docs-online-payments-payments-india-compliance-guide-go-live-india]] — India-specific live account and endpoint checklist, following compliance and KYC steps, with real-payment testing and fee qualifications (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-online-payments-analytics-and-data-tracking]] — 2026-09-15 Adyen webpage snapshot on Drop-in/Components telemetry, checkout attempt identifier, analytics version and configuration boundaries, privacy-policy counsel note, and optional separate Web fraud-data script.


- [[source-adyen-docs-online-payments-go-live-checklist]] — Adyen live-environment setup and real-payment testing checklist covering account, finance, risk, API, and webhook readiness (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-online-payments-upgrade-your-integration]] — 2026-09-15 Adyen webpage upgrade hub for version policy, Drop-in/Components and Checkout API lifecycle, upgrade routes, and mobile compatibility matrices.


- [[source-adyen-docs-online-payments-upgrade-your-integration-upgrade-to-web-v6]] — Web Drop-in/Components v5-to-v6 migration guide (webpage snapshot, 2026-09-15) for Checkout API v69+, configuration, constructors, payment callbacks, and conditional method-specific upgrades.


- [[source-adyen-docs-online-payments-upgrade-your-integration-upgrade-to-web-v6-from-v4]] — v4-to-v6 Web Drop-in/Components migration guide for the Checkout API v69 minimum, import and initialization changes, event handling, and optional method or styling migrations (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-online-payments-upgrade-your-integration-upgrade-to-web-v6-from-v3]] — 2026-09-15 Web Drop-in/Components v3.x.x-to-v6.0.0 migration guide covering Checkout API v69+, imports, configuration, constructors, callbacks, styling, and conditional method-specific changes.


- [[source-adyen-docs-online-payments-auto-rescue-sepa]] — 2026-09-15 SEPA Auto Rescue guide for AM04/MS03 chargeback-triggered shopper-not-present retries, two-attempt limit, and webhook, cancellation, test, and report routes; its title calls the case refused while the body starts from `AUTHORISED` then `CHARGEBACK`.


- [[source-adyen-docs-development-resources-error-codes]] — unversioned Adyen API error-code catalog for an online-payments integration, covering generic, Checkout, 3DS2, wallet, and network-token diagnostics (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-online-payments-auto-rescue]] — 2026-09-15 Adyen Auto Rescue overview for retrying selected shopper-not-present card refusals and SEPA direct debit failures within a rescue window, with webhook setup required and a terminology difference in the SEPA navigation.


- [[source-adyen-docs-online-payments-donations]] — Adyen Giving online-donation guide covering campaign setup, shopper opt-in, eligible methods and currencies, and integration routes (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-online-payments-integration-checklist]] — unversioned Adyen website checklist routing test-account setup, payment lifecycle and state handling, testing, reconciliation, and approval-qualified go-live steps (webpage snapshot, 2026-09-15)

- [[source-adyen-docs-online-payments-accessibility]] — Adyen website accessibility and VPAT overview for Web Drop-in/Components, recording WCAG 2.1 test scope and Adyen's version-qualified `v5.49.0`-or-later Level AA statement (webpage snapshot, 2026-09-15)

- [[source-adyen-docs-online-payments-two-step-checkout]] — unversioned Advanced-flow Web Drop-in/Components guide for adding a pre-payment review page, retaining validated payment data server-side for up to one hour, and submitting `/payments` from the review step (webpage snapshot, 2026-09-15)

- [[source-adyen-docs-online-payments-build-your-integration-payment-result-codes]] — unversioned Adyen website guide to synchronous payment result codes, intermediate versus final state, and later webhook status (webpage snapshot, 2026-09-15)

- [[source-adyen-docs-online-payments-checkout-settings]] — Adyen Customer Area guide to per-merchant-account manual or dynamic payment-method ordering, checkout-session linkage, and analytics (webpage snapshot, 2026-09-15).

- [[source-adyen-docs-development-resources-response-handling]] — online-payments HTTP response semantics covering request processing versus payment execution, qualified retry/error handling, and diagnostic routes (webpage snapshot, 2026-09-15)

- [[source-adyen-docs-online-payments-web-best-practices]] — unversioned Web Drop-in/Components best-practices guide covering browser lifecycle, custom-button safeguards, secure hosting, embedding and testing (webpage snapshot, 2026-09-15)

- [[source-adyen-docs-online-payments-cancel]] — webpage guide for cancelling eligible authorized, uncaptured online payments through Customer Area or Checkout API, including PSP-reference versus merchant-reference routes and path-specific webhook outcomes (webpage snapshot, 2026-09-15)

- [[source-adyen-docs-online-payments-partial-authorizations]] — Adyen guide to issuer-approved partial card amounts, Advanced-flow requirements, response interpretation, and qualified follow-up routes (webpage snapshot, 2026-09-15)

- [[source-adyen-docs-online-payments-partial-payments]] — unversioned website guide to multi-method orders, rolling `orderData`, completion by final payment states plus `ORDER_CLOSED`, and cancellation paths (webpage snapshot, 2026-09-15)

- [[source-adyen-docs-online-payments-build-your-integration]] — server-side flow selection guide covering one-request Sessions, Sessions with additional methods, and three-request Advanced.

- [[source-adyen-docs-online-payments]] — Adyen website overview of online-payment use cases, integration roles, lifecycle guidance, and next-step routes (webpage snapshot, 2026-09-15)
