---
title: "Adyen for Platforms"
type: concept
category: technology
tags: [adyen, platforms, onboarding, split-payments, payouts]
---

## Definition

Adyen for Platforms is Adyen's current platform-integration overview for commerce, ordering/POS, retail-management and SaaS businesses that process online and/or in-person payments on behalf of their users. The 2026-09-15 snapshot routes to user onboarding and Adyen verification, split payment processing, managed/custom payouts, risk, and reports. It points to a separate marketplace integration guide when that model fits better. [[source-adyen-docs-platforms]]

## Evidence boundary

The landing page does not define the detailed legal-entity/account-holder/balance/liable/reserve/transfer-instrument model, API roles, verification capabilities or status transitions. A platform and its users are distinct actors, but “on behalf of” does not identify a merchant of record, legal seller, payee or fund owner for a particular transaction. Country and acquiring-region lists are dated and distinct; the Channel Islands and Isle of Man are excluded for in-person payments and store creation. Issuing, business accounts and Capital are separate optional products with additional availability and verification. The page is not proof of onboarding approval, payment authorization, split execution, payout or bank receipt.

## Sources

- [[source-adyen-docs-platforms-financial-products]] — 2023-modified, 2026-09-15-captured platform product hub orienting business accounts, Capital, Issuing and Payouts; product-specific eligibility and activation belong to their guides.


- [[source-adyen-docs-platforms-verification-requirements-reference-additional-products-brand-specific-industry-codes]] — 2026-09-15 brand-specific IC/MCC classification and conditional approval-contact guide for Platforms business accounts; the pinned export has no accepted-code list or eligibility proof.


- [[source-adyen-docs-platforms-verification-requirements-reference-additional-products-industry-codes]] — 2026-09-15 Platforms IC/MCC selection and approval-contact reference; captured code table is absent and does not prove industry or business-account eligibility.


- [[source-adyen-docs-platforms-onboard-users-onboarding-steps]] — 2026-09-15 onboarding-step filter export with hosted/on-invite/v4 selected but Location and entity-type filters missing; no concrete step result is present.


- [[source-adyen-docs-platforms-account-structure-resources-legal-entity-management]] — 2026-09-15 Platforms LEM resource orientation naming legal entities, transfer instruments, supporting documents and business lines for user verification; creation is not approval or payout proof.


- [[source-adyen-docs-platforms-manage-access]] — 2023-modified, 2026-09-15-captured Platforms Customer Area/team-access overview for admin email activation, role-assigned users and separate payments/balance/financial-product credential routes; no operation-level permission proof.


- [[source-adyen-docs-platforms-manage-reserve-account]] — 2026-09-15 Platforms reserve-account guide for liable-holder-linked collateral against transfer-caused negative user balances, distinct from refund/chargeback reserved compensation; request and block are not payout proof.


- [[source-adyen-docs-platforms-manage-liable-accounts]] — 2026-09-15 guide to platform-owned main, incorrect-splits and compensation liable balances, including conditional negative-balance handling; not account-specific fund or bank-receipt proof.


- [[source-adyen-docs-platforms-kyc-verification-codes]] — 2021-modified, 2026-09-15-captured Platforms/Issuing verification-code taxonomy and account-holder capability problems retrieval route; actions are conditional suggestions, not verification outcomes.


- [[source-adyen-docs-platforms-quickstart-guide-customer-area]] — 2026-09-15 Platforms Customer Area quickstart for operational views, company/merchant-account access and user-role hygiene; UI visibility does not prove financial outcomes.


- [[source-adyen-docs-platforms-manage-access-webservice-roles]] — 2023-modified, 2026-09-15-captured Balance Platform API credential role catalog for configuration, optional Issuing, and Transfers API permissions, including BCL PCI sensitivity and v1-only transfer-initiation role; no actual grant or operation proof.


- [[source-adyen-docs-platforms-verification-overview-verification-types]] — 2026-09-15 Platforms guide comparing upfront verification with payment-facilitator-only staggered verification, tier-change payout conditions and country-specific tier currencies.


- [[source-adyen-docs-platforms-account-structure-resources-financial-products]] — 2026-09-15 Platforms example separating regional platform accounts, liable/grant resources and user account holders, balance accounts, payment instruments, transfer instruments, legal entities and business lines; examples do not prove product grants or money movement.


- [[source-adyen-docs-platforms-account-structure-resources-platform-structure]] — 2026-09-15 Adyen for Platforms payment-facilitator structure example separating platform and user merchant, balance, liable, legal-entity and transfer-instrument resources, with an illustrative split-to-payout path.


- [[source-adyen-docs-platforms-account-structure-resources]] — 2021-modified, 2026-09-15-captured current Platforms account-resource map for company/merchant/store, region-specific balance platforms, user account-holder/balance/legal-entity links and platform liable resources; it does not prove account or fund state.


- [[source-adyen-docs-platforms-quickstart-guide]] — 2026-09-15 Platforms quickstart orienting Adyen team roles, account/balance/legal-entity resources and next-step guides; not operational or financial-outcome proof.


- [[source-adyen-docs-platforms-account-holder-status]] — 2026-09-15 Platforms guide to active/suspended/closed account-holder state, Adyen-initiated inheritance and post-settlement split routing by pay-in capability; status guidance is not verification, settlement or payout proof.


- [[source-adyen-docs-platforms-verification-requirements-upload-bank-document]] — 2026-09-15 limited-availability Hosted Onboarding bank-document upload/feedback guide with name, file and manual-review conditions; upload acceptance is not verification approval.


- [[source-adyen-docs-platforms-manage-account-holder-risk]] — 2026-09-15-captured Platforms Score guide for role-gated account-holder cases, risk rules/actions, payout controls, irreversible identity exclusions and conditional risk webhooks; flags are not fraud or payout proof.


- [[source-adyen-docs-platforms-identify-account-holder-risk]] — 2026-09-15 Score overview for platform-user risk signals, weighted scores, linked-account grouping, platform-selected controls and limited device-data pilot.


- [[source-adyen-docs-platforms-manage-balance-accounts]] — 2026-09-15 Configuration API/Customer Area guide to account-holder-linked balance-account creation, viewing, description update and permanent zero-balance closure; examples do not prove funded state or payout.


- [[source-adyen-docs-platforms-manage-access-api-credentials-web-service]] — 2023-modified, 2026-09-15-captured balance-platform web service/LEM credential, role, test/live, rotation and deactivation guide; possession does not prove permission or operation.


- [[source-adyen-docs-platforms-onboard-users]] — 2024-modified, 2026-09-15-captured Platforms hosted/invite/API-only onboarding overview, with entity/country and capability gates; data collection is not verification approval.


- [[source-adyen-docs-platforms-onboard-users-onboarding-versions]] — dated onboarding-version overview and v2-to-v4 Hosted/API-only migration conditions; its v4 stable statement conflicts with a later v3 stable reference.


- [[source-adyen-docs-platforms-verification-requirements-reference-additional-products]] — 2023-modified, 2026-09-15-captured Platforms additional-capabilities data reference for conditional financial-account FATCA/CRS, business-account industry codes and business-account/issuing source of funds; no eligibility or enabled-capability proof.


- [[source-adyen-docs-platforms-kyc-verification-codes-general-verification-errors]] — 2023-modified, 2026-09-15-captured general KYC verification-error code mapping for Adyen for Platforms and Issuing, with possible suberrors, missing-data/contract categories, and illustrative error-object shape; no verification or eligibility proof.


- [[source-adyen-docs-platforms-quickstart-guide-support]] — 2026-09-15 Platforms support quickstart assigning user-facing support to the platform and Adyen escalation to its business, with KYC/payout troubleshooting and ticket routes; examples and typical timing are not response or financial-outcome guarantees.


- [[source-adyen-docs-platforms-kyc-insights]] — 2026-09-15 Customer Area balance-platform KYC analytics guide for dated onboarding cohorts, verification metrics and historical errors; aggregate trends are not individual current-eligibility proof.


- [[source-adyen-docs-platforms-verification-overview]] — 2023-modified, 2026-09-15-captured Platforms verification overview for capability requests, data-change/review checks, version-qualified deadlines and asynchronous status; a deadline or request is not capability approval.


- [[source-adyen-docs-platforms-verification-overview-data-review-process]] — 2023-modified, 2026-09-15-captured periodic user-data review process: webhook/deadline, optional v3/v4 proactive request, hosted/API-only confirmation, and subsequent valid/invalid verification results; no account-specific outcome proof.


- [[source-adyen-docs-platforms-verification-overview-capabilities]] — 2024-modified, 2026-09-15-captured account-holder capability guide for requested/allowed/enabled settings, verification statuses, product-specific capability tables and deadline exceptions.


- [[source-adyen-docs-platforms-onboard-users-pci-forms]] — 2026-09-15 Platforms guide to sales-channel-dependent user SAQs, hosted/custom-UI signing and Legal Entity Management API document/status routes; submission is not independent PCI or capability approval.


- [[source-adyen-docs-platforms-onboard-users-customize-hosted-onboarding]] — 2024-modified, 2026-09-15-captured Platforms/Issuing hosted-onboarding theme, link-setting, test and debug guide; UI controls do not establish verification approval.


- [[source-adyen-docs-platforms-quickstart-guide-onboarding-and-kyc]] — 2026-09-15 Platforms user-onboarding/KYC quickstart for hosted and API-only methods, conditional verification, Terms/PCI and support; guidance does not prove capability activation or payout.


- [[source-adyen-docs-platforms-onboard-users-terms-of-service]] — 2026-09-15 Adyen for Platforms Terms guide for main-entity document generation, individual or authorized-signatory acceptance, test/live type differences and acceptance-info retrieval; examples do not prove actual legal consent or capability enablement.


- [[source-adyen-docs-platforms-kyc-verification-codes-remediating-actions]] — 2021-modified, 2026-09-15-captured Platforms/Issuing verification remediation-code catalog with parent/suberror placement, object-specific messages, conditional missing-data codes and duplicated `2_198` wording.


- [[source-adyen-docs-platforms-onboard-users-components]] — 2026-09-15 Adyen Platforms transfer-instrument Onboarding components guide for LEM v3/v4 entities, server-scoped session roles, bank-data entry/management and user-flow events; submission and status display do not prove verification or payout.


- [[source-adyen-docs-platforms-manage-stores]] — 2025-modified, 2026-09-15-captured Platforms Customer Area/Management API store guide for legal-entity business-line linking, country/role prerequisites, optional splits and irreversible store closure.


- [[source-adyen-docs-platforms-verification-requirements-onboarding-guidelines]] — 2026-09-15 in-development Platforms onboarding guide for general KYC and selected country/entity-specific ID, organization and bank-document conditions; dated guidance does not prove current eligibility or granted capabilities.


- [[source-adyen-docs-platforms-manage-transfer-instruments]] — 2023-modified, 2026-09-15-captured Legal Entity Management API/Customer Area guide distinguishing user bank-account instruments from liable-account company payout accounts, verification state and deletion effects.


- [[source-adyen-docs-platforms-verification-requirements-document-requirements]] — 2023-modified, 2026-09-15-captured conditional document-upload reference for platform verification, with entity, country, business-account/issuing and onboarding-v4 limits; submission is not verification approval.


- [[source-adyen-docs-platforms-manage-account-holders]] — 2023-modified, 2026-09-15-captured Configuration API/Customer Area guide for platform account-holder creation, status, closure and capabilities; legal entities and balance accounts remain distinct.


- [[source-adyen-docs-platforms-manage-legal-entities]] — 2024-modified, 2026-09-15-captured Adyen for Platforms Legal Entity Management API v3 guide for creating, viewing and updating legal entities, with role, region and verification-rerun boundaries.


- [[source-adyen-docs-platforms-verification-requirements]] — 2023-modified guide captured 2026-09-15 for platform user-verification inputs by country, legal-entity type and financial product, with minor-user, business-account, issuing and Capital qualifications; requirements do not prove verification or capability approval.


- [[source-adyen-docs-platforms-onboard-users-onboarding-versions-onboarding-v4]] — 2025-modified, 2026-09-15-captured Platforms onboarding v4 change guide for hosted/API-only legal-entity validation, country/entity exceptions and separate issuing/business-account source-of-funds requirements; historical rules do not prove verification or capability activation.


- [[source-adyen-docs-platforms-verification-requirements-data-formats-per-country]] — 2024-modified, 2026-09-15-captured country/entity data-format reference for Adyen for Platforms and issuing, with onboarding-version and document-verification exceptions.


- [[source-adyen-docs-platforms-get-started]] — 2022-modified, 2026-09-15-captured Platforms onboarding overview from Adyen contact/design through test integration, live application and separately replicated live setup; no activation or money-movement proof.


- [[source-adyen-docs-platforms-integration-checklist]] — 2023-modified, 2026-09-15-captured Adyen for Platforms resource, API, onboarding, splits, payout, reporting and go-live checklist; test examples and steps do not prove verified capabilities or financial outcomes.


- [[source-adyen-docs-platforms]] — 2026-09-15 current Adyen for Platforms landing page for platform/user model, verification, split-payments and payout routes, regional lists and separate optional financial products.

## Related

- [[adyen-payments]] — general channel orientation.
- [[adyen-mirakl]] — connector using Adyen for Platforms; distinct from the platform overview.
- [[adyen-reporting]] — reporting route.
- [[adyen]] — provider profile.
