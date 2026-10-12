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
