---
title: "Adyen Business Accounts"
type: concept
category: technology
tags: [adyen, business-accounts, platforms, financial-products]
---

## Definition

Adyen Business accounts are a separate Adyen for Platforms financial product for eligible platform users' business-related incoming/outgoing third-party transfers and direct receipt of platform payouts into an Adyen account. The 2023-modified overview describes API or Hosted Onboarding integration and calls the feature in development. These are dated product descriptions, not evidence that a specific user has an opened account or that any transfer settled. [[source-adyen-docs-business-accounts]]

## Evidence boundary

The captured overview conditions eligibility on user entity type, supported operating region, associated UBO/individual residence wording, and additional verification information. It lists US, mainland UK and Eurozone contexts with exclusions and US-specific onboarding detail, but those dated descriptions do not establish current regional availability, account approval, legal ownership, live balance, transfer completion or bank receipt. Keep Business accounts distinct from Capital grants and external-bank payouts; use child guides for verification, roles, consent and lifecycle.

## Sources

- [[source-adyen-docs-business-accounts-account-structure-resources-platform-account-structure]] — 2026-09-15 platform-versus-user resource map and distinct liable/user/instrument-linked balance-account roles; its multiple-Business-Accounts-per-balance-account statement conflicts with the captured one-number/one-bankAccount-instrument creation guides.


- [[source-adyen-docs-business-accounts-manage-access]] — 2023-modified, 2026-09-15-captured Business accounts Customer Area user and web-service credential role guide, including sole-proprietor IBAN PII and Transfers API v1 scope; roles do not prove access or operations.


- [[source-adyen-docs-business-accounts-verification-requirements]] — 2023-modified, 2026-09-15-captured Business Accounts additional verification-data and US onboarding-disclosure guide, with country/entity/conditional document scope and a linked US FATCA/CRS exception; data collection is not KYC or account-opening proof.


- [[source-adyen-docs-business-accounts-integration-checklist]] — 2023-modified, 2026-09-15-captured Business Accounts integration/go-live checklist for platform prerequisites, resource/credential/webhook setup, added verification and separately replicated live configuration with end-to-end checks; checklist steps are not live-operation proof.


- [[source-adyen-docs-business-accounts-verification-overview-capabilities]] — 2024-modified, 2026-09-15-captured Business Accounts account-holder capability guide for issueBankAccount and third-party flow permissions, requested/allowed/enabled flags, and pending/invalid verification deadline exceptions; flags do not prove an opened account.


- [[source-adyen-docs-business-accounts-onboard-users]] — 2024-modified, 2026-09-15-captured Business accounts API-only onboarding and v4 source-of-funds/country-data guidance; submission starts verification, not account opening.


- [[source-adyen-docs-business-accounts-manage-balance-accounts]] — 2026-09-15-modified Configuration API guide to create, view, update and permanently close account-holder-linked balance accounts; zero balance gates closure, while TEST resource/status/currency examples are not funded or usable Business Account proof.


- [[source-adyen-docs-business-accounts-verification-requirements-data-formats-per-country]] — 2024-modified, 2026-09-15-captured country/entity data-format tables for verification inputs across Platforms and Issuing; rows are examples, not Business Accounts eligibility or KYC approval.


- [[source-adyen-docs-business-accounts-verification-requirements-reference-additional-products]] — 2023-modified, 2026-09-15-captured FATCA/CRS, industry-code and SOF information guide for Business accounts (SOF also Issuing), with US exception, approval gates and field-path inconsistency; not KYC approval proof.


- [[source-adyen-docs-business-accounts-create-business-accounts]] — 2024-modified, 2026-09-15-captured Business Accounts guide for the verified-account-holder bankAccount payment-instrument creation flow, dated NL/US currency constraints and one-number-per-balance-account limit; examples are not live account or funds proof.


- [[source-adyen-docs-business-accounts-verification-overview]] — 2023-modified, 2026-09-15-captured Business Accounts KYC/capability process for asynchronous checks, data-review triggers, LEM-v3/v4 verification deadlines and permission loss.


- [[source-adyen-docs-business-accounts-verification-overview-data-review-process]] — 2023-modified, 2026-09-15-captured legal-entity periodic-review guide for deadline/capability webhooks, onboarding-v3/v4 proactive requests and user confirmation plus error resolution; request/confirmation is not KYC approval.


- [[source-adyen-docs-business-accounts-verify-account-holder]] — 2026-09-15 Open Banking/AISP route and report guide for an unregistered external individual's bank-account verification across Platforms, Marketplaces or Classic; it is not registered account-holder capability verification or Business Account opening proof.


- [[source-adyen-docs-business-accounts-kyc-verification-codes-remediating-actions]] — 2021-modified, 2026-09-15-captured KYC remediating-action code catalog for verificationErrors/subErrors, with conditional entity/field messages and duplicate `2_198` mapping; action codes do not prove approval or authorize retries.

- [[source-adyen-docs-business-accounts-kyc-verification-codes]] — 2021-modified, 2026-09-15-captured account-holder capability verification-code overview for Platforms/Issuing scope, three code layers, channels, roles and problems-array location; action availability is conditional and codes do not prove verification.



- [[source-adyen-docs-business-accounts-onboard-users-terms-of-service]] — 2026-09-15 Business Accounts onboarding ToS flow for webhook requirement, test/live document types, generated document IDs, authorized individual signer and acceptance-record readback.


- [[source-adyen-docs-business-accounts-kyc-verification-codes-general-verification-errors]] — 2023-modified, 2026-09-15-captured general verificationErrors code catalog under Business accounts KYC, also naming Platforms/Issuing scope and linking suberror/action references; not account-approval proof.


- [[source-adyen-docs-business-accounts-verification-requirements-document-requirements]] — 2023-modified, 2026-09-15-captured Business accounts document-upload reference for conditional KYC evidence by person/entity/bank, onboarding-v4 selfie, country/age/format exceptions and unresolved photo-ID file-count conflict.


- [[source-adyen-docs-business-accounts-manage-legal-entities]] — 2024-modified, 2026-09-15-captured LEM API v3/Customer Area guide to create, view, patch and type-change legal-entity resources for Business accounts onboarding, with PII role and verification-rerun limits; resource creation is not account-opening proof.


- [[source-adyen-docs-business-accounts-manage-account-holders]] — 2023-modified, 2026-09-15-captured Configuration API/Customer Area guide for legal-entity-linked account holders, capability/verification flags, zero-balance ordered closure and KYC roles; mixed capability examples and missing suspension section limit procedure inference.


- [[source-adyen-docs-business-accounts-kyc-verification-codes-sub-errors]] — 2023-modified, 2026-09-15-captured verification suberror family/table reference for Platforms or Issuing integrations, with code-specific remediating-action links and a setup-stop affiliation row.


- [[source-adyen-docs-business-accounts-account-structure-resources]] — 2021-modified, 2026-09-15-captured Business accounts resource map for regional balance platform, account holder/legal entity, balance accounts and bankAccount payment instrument; two-account prose conflicts with a one-account example, and setup is not account-opening proof.

- [[source-adyen-docs-business-accounts-account-structure-resources-legal-entity-management]] — 2026-09-15-captured Business Accounts LEM resource overview for legal entities, payout transfer instruments and supporting documents as verification inputs; resource creation is not verification, account-opening or payout proof.



- [[source-adyen-docs-business-accounts-get-started]] — 2022-modified, 2026-09-15-captured Business Accounts onboarding route for Platforms enablement, authentication, child implementation topics, test validation and separate live configuration; not proof of an opened account or transfer.


- [[source-adyen-docs-business-accounts]] — 2023-07-06-modified Business accounts landing page captured 2026-09-15 for product purpose, development warning, dated eligibility and child routes.

## Related

- [[adyen-financial-products]] — financial-products umbrella.
- [[adyen-platforms]] — platform integration context.
