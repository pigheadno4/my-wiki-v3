---
title: "Adyen Platforms onboarding versions and v4 migration"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/onboard-users/onboarding-versions"
raw_files:
  - "adyen/docs/platforms/onboard-users/onboarding-versions/2026-09-15.md"
tags: [adyen, platforms, onboarding, legal-entity-management, versioning]
---

## Overview

This Adyen Platforms page explains how onboarding versions package breaking changes in the Legal Entity Management (LEM) API, hosted onboarding, and KYC verification checks, and gives a v2-to-v4 update route for Hosted and API-only integrations. It calls v4 the latest stable version at the top and in the update steps, but a later sunset paragraph calls v3 the latest stable version; treat that sentence as an unresolved inconsistency in this 2026-09-15 snapshot rather than a current-version claim. The page was last modified 2025-02-10. See [[adyen]] and [[adyen-platforms]] for provider and Platforms context.

## Key takeaways

- An onboarding release can change one or more of LEM API, hosted onboarding, and KYC checks. Adyen says immediate updating is unnecessary and it will give approximately 6–12 months' notice before sunsetting a version; after an API version's sunset it can no longer be used. Both API-only and Hosted integrations must update their API version before the applicable sunset. Older stable versions receive no additional updates. An API-only release candidate is a changeable pilot preview obtained through an Adyen account manager, not the stable Hosted release.
- The stated update sequence is to contact Adyen, update the server integration to LEM API v4, review and implement features, test, then go live. Hosted onboarding remains on LEM v2 until its integration is updated and then uses LEM v4. The page describes v2-to-v4 differences; it does not provide a separate v3-to-v4 migration matrix.
- For older users after v2-to-v4 updating, verification deadlines become available, but capabilities invalid in the older version do not automatically receive them. PCI and Terms of Service acceptance are backfilled; sales-channel changes may require a new PCI questionnaire and newly requested capabilities require additional ToS. New users face the listed PCI enforcement and ToS requirement. Updating alone does not immediately rerun verification checks: a user data update or required data review triggers new checks. These conditions do not establish a completed verification or enabled capability.
- Both migration tabs call for required-data-review notification, verification-deadline logic, country/region compliance review, updated verification-error and webhook structures, required data and name/address validation review. Verification errors move from per-capability placement to an array of affected capabilities; `/checkVerificationErrors` is an additional endpoint. The `sendToTransferInstrument` capability is checked at transfer-instrument and legal-entity levels. Business-line creation uses `service` in place of deprecated `capability`, with `paymentProcessing`/`banking`/`issuing` mapping to receivePayments/issueBankAccount/issueCard; source of funds is required for card issuing and business accounts. These are integration instructions, not proof of a transfer.
- API-only onboarding additionally calls for collection of user support phone and email, and a transfer-instrument `type` that distinguishes IBAN from local bank account and changes required information. Adyen recommends transfer-instrument components, describing instant bank-account verification when details are added or updated; the recommendation is not a universal requirement or a verified status for an individual account. For API-only users, capability status remains visible at legal-entity level until a data update or required data review.
- Before testing, Adyen says to contact it to ensure new features are enabled in the test environment, then test major features and unsuccessful-verification error handling. The page does not name a specific API credential or role; country, entity, and capability requirements vary by linked detail guides. Its migration directions are historical guidance, not evidence that a particular integration was upgraded, approved, live, or compliant today.

## Detail locators

- Scope, stable-version assertion, sunset notice, and nonbreaking-versus-breaking changes: raw lines 19–47. Stable/release-candidate and sunset guidance, including conflicting v3 wording: lines 51–67. Update sequence: lines 69–77.
- v2-to-v4 older/new user differences and verification trigger: lines 79–89. Hosted migration requirements: lines 91–117. API-only migration requirements and components: lines 119–149. Test prerequisites and error handling: lines 151–153.

## Related

- [[adyen]] — provider context.
- [[adyen-platforms]] — Platforms onboarding, legal-entity and verification context.
- [[source-adyen-docs-platforms-onboard-users-onboarding-versions-onboarding-v4]] — the separate v4 overview linked for detailed requirements.

## Related raw API references

- The snapshot links to the v4 overview, country/region compliance, required-data, verification, API Diff, and release-note guides. Those linked pages own their detailed requirements; this page alone does not establish current account settings or permissions.

## Raw Sources

- [[raw/adyen/docs/platforms/onboard-users/onboarding-versions/2026-09-15|Adyen Docs: Onboarding versions (2026-09-15 snapshot; page last modified 2025-02-10)]]
