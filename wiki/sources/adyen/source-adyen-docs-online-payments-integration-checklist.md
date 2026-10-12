---
title: "Adyen Online Payments Integration Checklist"
type: source
date_ingested: 2026-10-11
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/integration-checklist"
raw_files:
  - "adyen/docs/online-payments/integration-checklist/2026-09-15.md"
tags: [adyen, online-payments, integration, testing, webhooks, reconciliation]
---

## Overview

This [[adyen]] checklist routes an online-payments integration from test-account setup through implementation, testing, reconciliation, and applying to go live. Its central implementation concern is accepting payments while handling subsequent states. See [[adyen-online-payments]] for the provider-level architecture.

## Key takeaways

- Test setup covers creating an account, choosing an initial company/merchant-account structure, adding team users, obtaining a test API key and client key, and adding payment methods. The page says the account structure can be finalized again when going live.
- The build checklist routes webhook handling, client/server integration guidance, errors and refused payments, refunds and cancellations, additional payment methods, result codes including `pending`, optional additional features, and transaction testing.
- Webhooks are the checklist's route for payment statuses, refund outcomes, some local-payment-method results, and other events; the page therefore treats later payment state as part of the integration, not only the initial payment request.
- Reconciliation work includes automatically retrieving the Settlement details report, which the page calls the main reconciliation report generated for each payout, and building a settlement-reconciliation process.
- Accepting shopper payments live requires applying for a live account. Only if that application is approved does the checklist direct the merchant to the go-live checklist.
- This is a webpage snapshot fetched 2026-09-15 whose embedded metadata says it was last modified in 2019. It is a navigation checklist, not proof of current account approval, payment-method or feature availability, regulatory sufficiency, successful test coverage, payment execution, authorization, capture, payout, or settlement. Follow the linked current guides for implementation detail and current requirements.

## Detail locators

- Test-account setup, account structure, users, credentials, and initial payment methods: `Set up your test account`, lines 21–32.
- Core lifecycle and webhooks: `Build your integration`, lines 34–41.
- Errors, refused payments, modifications, payment methods, result codes, additional features, 3D Secure 2, and testing: `Build your integration`, lines 42–51.
- Settlement report and reconciliation routes: `Reporting and reconciliation`, lines 53–60.
- Live-account application and approval-qualified go-live route: `Go live`, lines 62–66.

## Related

- [[adyen]] — provider page.
- [[adyen-online-payments]] — provider-level online-payments architecture and source route.

## Raw Sources

- [[raw/adyen/docs/online-payments/integration-checklist/2026-09-15|Adyen Integration checklist (2026-09-15)]]
