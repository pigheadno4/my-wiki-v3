---
title: "Adyen Classic Platforms: Integration and go-live checklist"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/platforms-integration-checklist"
raw_files:
  - "adyen/docs/classic-platforms/platforms-integration-checklist/2026-09-15.md"
tags: [adyen, classic-platforms, integration, go-live, verification]
---

## Overview

This checklist is explicitly for **Classic Adyen for Platforms** integrations; teams starting a new implementation are directed to a separate new integration guide. It covers testing sub-merchant onboarding and verification, split payments, payouts, notifications, and reconciliation before separately configuring a live environment. This is a 2026-09-15 capture of a page marked last modified 2021-02-01. Use [[adyen-classic-platforms]] for the Classic model; its account-holder/account and Platforms API instructions do not establish the resource model of newer [[adyen-platforms]].

## Key takeaways

- The checklists assume an existing **test integration** and familiarity with Classic platform options. The platform chooses staggered or all-at-once sub-merchant data collection, Hosted Onboarding Page (HOP) or its own onboarding UI, and scheduled versus manual payouts before deciding what to test (raw lines 23–37). The first test requires an Adyen for Platforms test account and both platform and payment-processing API credentials (raw lines 50–63).
- The integration sequence is test account → onboarding/verification → payment splitting → payouts → notifications → reporting (raw lines 39–48). A sub-merchant is onboarded as an **account holder**. `/createAccountHolder` minimum information depends on legal-entity type and country; a HOP redirect is followed by verification-status notification checks and platform communication. In a custom UI, the platform submits collected data with `/updateAccountHolder` and likewise checks notifications (raw lines 65–124). The page says verification must be completed before payouts (raw line 75).
- When a customer pays on the platform, the Classic guide describes splitting funds among platform accounts, including the liable account, at authorization or capture and adjusting payment, capture, or refund allocations. It asks teams to test splits, refund handling, chargebacks and fund transfers; examples are tests, not executed-money-flow evidence (raw lines 126–141).
- Payout testing requires account-holder verification and an `accountCode`; manual payouts also require `accountHolderCode`. The checklist says a `/payoutAccountHolder` HTTP 200 response confirms payout success (raw lines 143–150), but separately says Platforms API requests are asynchronous and notifications are needed for final results (raw lines 154–165). Treat that as an unresolved distinction between the immediate response and final payout/bank outcome; do not use the 200 response alone as bank-receipt proof.
- For go-live, the page instructs teams to obtain an Adyen for Platforms contract and live account, update settings that are not fully copied (notifications, reports, API responses, statements, and applicable recurring details), configure risk/payout account/payment methods, switch credentials and endpoints, and test the full lifecycle including webhooks and reconciliation (raw lines 183–242). These are steps to perform, not evidence of live readiness or completed transactions.

## Detail locators

- Classic-only scope, prerequisites, integration choices and report list: raw lines 15–37.
- Six-step integration checklist and test credentials: raw lines 39–63.
- Verification notifications, HOP and custom onboarding responsibilities: raw lines 65–124.
- Split-payment test guidance: raw lines 126–141.
- Payout prerequisites, `200` wording and asynchronous notification boundary: raw lines 143–170.
- Test reports and separate go-live work: raw lines 172–242.

## Related

- [[adyen]] — provider context.
- [[adyen-classic-platforms]] — Classic platform model.
- [[adyen-platforms]] — newer integration route; keep resources and endpoints separate.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/platforms-integration-checklist/2026-09-15|Classic Platforms integration and go-live checklist, captured 2026-09-15]]
