---
title: "Adyen Classic Platforms"
type: concept
category: technology
tags: [adyen, classic-platforms, marketplaces, sub-merchants]
---

## Definition

Adyen Classic Platforms is the older Adyen for Platforms integration for marketplace and other platform models. In the 2023-modified overview captured 2026-09-15, the platform onboards sellers, service providers or contractors as sub-merchants/account holders, accepts buyer payments on their behalf, can split payment funds among sub-merchants and deduct costs, move funds between its account and sub-merchant accounts, then schedule or initiate payouts. [[source-adyen-docs-classic-platforms]]

## Evidence boundary

The Classic overview explicitly directs a new implementation to a separate new-integration guide. Keep Classic account-holder/account and workflow terminology separate from the current [[adyen-platforms]] balance-platform/API model; this overview does not establish that their resources or endpoints are interchangeable. Its country list and point-of-sale country condition are dated snapshot guidance, not current eligibility. Descriptions of immediate acceptance after signup, held funds, transfers and payout options do not prove verification approval, an executed split, payment capture, settlement, payout or bank receipt for a particular sub-merchant.

## Sources

- [[source-adyen-docs-classic-platforms-api]] — 2019-modified, 2026-09-15-captured Classic Platforms API Explorer directory for Account, Fund, notification configuration and delivery, and hosted onboarding references; new implementations are directed elsewhere.


- [[source-adyen-docs-classic-platforms-reconciliation-use-cases]] — 2021-modified, 2026-09-15-captured Classic reconciliation hub routing report preparation to accounts-receivable, ledger, scheduled-payout and fee guides; this page contains no worked rows or completed reconciliation.


- [[source-adyen-docs-classic-platforms-identify-account-holder-risk-configure-notifications-for-risk-signals]] — 2022-modified, 2026-09-15-captured Classic Score webhook setup for `SCORE_SIGNAL_TRIGGERED`, with Adyen activation step and conflicting create-example `active` values.


- [[source-adyen-docs-classic-platforms-payouts-payout-notifications]] — 2022-modified, 2026-09-15-captured Classic `ACCOUNT_HOLDER_PAYOUT` status reference for Initiated/Confirmed/Failed, possible post-confirmation bank return and scheduled-return recovery.


- [[source-adyen-docs-classic-platforms-kyc-action-required-snapshot-report]] — 2019-modified, 2026-09-15-captured Classic scheduled CSV for recently active sub-merchants with incomplete KYC, with notification preference and an entity-type list narrower than the creation guide.


- [[source-adyen-docs-classic-platforms-account-structure-example-structures]] — 2019-modified, 2026-09-15-captured Classic company/merchant/platform account illustration and one-to-one versus multiple account/bank-account payout mapping.


- [[source-adyen-docs-classic-platforms-notification-types]] — 2020-modified, 2026-09-15-captured Classic event-purpose catalog for account holders, payouts, transfers, refunds and liable-account compensation; request/Initiated labels are not completion or bank-receipt proof.


- [[source-adyen-docs-classic-platforms-account-holders-and-accounts-change-legal-entity]] — 2020-modified, 2026-09-15-captured Classic Account API v5+ legal-entity change guide preserving account codes/history, with migrate-versus-new-details verification and one-shareholder migration limit.


- [[source-adyen-docs-classic-platforms-onboard-users-hosted-onboarding-page-hop-appearance]] — 2026-09-15 Classic Customer Area HOP appearance guide for role-gated header, logo, background and FAQ controls with asset limits.


- [[source-adyen-docs-classic-platforms-payouts]] — 2023-modified, 2026-09-15-captured Classic scheduled-full-bank versus manual-partial-bank/eligible-card payout overview with tier, country, bank-count and currency limits; US example absent from table.


- [[source-adyen-docs-classic-platforms-onboard-users-hosted-onboarding-page-customize-experience]] — 2022-modified, 2026-09-15-captured Classic HOP customization guide for check/page selection, locale fallback, verified-data editing and return redirect; source flags `returnURL` versus companion `returnUrl` casing.


- [[source-adyen-docs-classic-platforms-configure-notifications-signing-notifications-with-hmac]] — 2023-modified, 2026-09-15-captured Classic Notifications v5+ HMAC guide for configuration, raw-body verification and key-rotation boundary; key-size and example-event text conflict.


- [[source-adyen-docs-classic-platforms-payouts-manual-payout]] — 2020-modified, 2026-09-15-captured Classic Customer Area/Fund API manual-payout guide for balance and role gates, asynchronous status, regional speed conditions and descriptor example conflict.


- [[source-adyen-docs-classic-platforms-top-up-accounts]] — 2023-modified, 2026-09-15-captured Classic Fund API direct-debit top-up guide: holder bank to merchant settlement to split credits, consent/rail/limit gates, asynchronous results and USD/EUR sample mismatch.


- [[source-adyen-docs-classic-platforms-prepare-reports]] — 2023-modified, 2026-09-15-captured Classic report configuration, download and reconciliation-join guide, including period/time-zone alignment and nonunique merchant-reference caveat.


- [[source-adyen-docs-classic-platforms-configure-notifications]] — 2021-modified, 2026-09-15-captured Classic Notification API setup, update/delete, acknowledgment, retry and test guide; examples conflict on API version, protocol and one configuration ID.


- [[source-adyen-docs-classic-platforms-identify-account-holder-risk]] — 2020-modified, 2026-09-15-captured Classic Score overview for account-holder risk signals, shared identity scores, review-led actions and default no payout/processing disablement.


- [[source-adyen-docs-classic-platforms-onboard-users-custom-onboarding]] — 2020-modified, 2026-09-15-captured Classic custom account-holder onboarding guide for upfront/staggered collection, Account API v6 updates, notification-gated verification and asynchronous documents.


- [[source-adyen-docs-classic-platforms-onboard-users-hosted-onboarding-page]] — 2021-modified, 2026-09-15-captured Classic HOP guide for enabled hosted verification, one-time redirect timing, session recovery and webhook result gates.


- [[source-adyen-docs-classic-platforms-payouts-scheduled-payout]] — 2020-modified, 2026-09-15-captured Classic daily/per-account payout schedules, HOLD/manual behavior, notification-confirmed updates and conditional regional same-day speed.


- [[source-adyen-docs-classic-platforms-fund-transfer]] — 2020-modified, 2026-09-15-captured Classic account-to-account transfer and full/partial reversal guide for Fund API/Customer Area, with account-status gates and asynchronous webhook outcomes.


- [[source-adyen-docs-classic-platforms-quick-start]] — 2021-modified, 2026-09-15-captured Classic TEST integration walk-through across onboarding, Checkout split, capture, payout, notifications and reports; basic fields predate later verification requirements.


- [[source-adyen-docs-classic-platforms-verification-process-check-verification-results]] — 2021-modified, 2026-09-15-captured Classic notification, Account API and Customer Area verification-result guide with per-check status, versioned payout-method type and conditional retry/document steps.


- [[source-adyen-docs-classic-platforms-test-scenarios]] — 2020-modified, 2026-09-15-captured Classic Account API/HOP test fixtures for payout, failed KYC and refund-timing states; the invalid-data owner-city field path differs from earlier examples.


- [[source-adyen-docs-classic-platforms-identify-account-holder-risk-review-and-manage]] — 2020-modified, 2026-09-15-captured Classic Score guide for role-gated identity review, manual/automated risk actions and permanent linked-KYC-value exclusion.


- [[source-adyen-docs-classic-platforms-onboard-users]] — 2020-modified, 2026-09-15-captured Classic account-holder verification guide for upfront versus staggered onboarding, payout-tier transitions, and the distinct Payout/Processing `/checkAccountHolder` prechecks.


- [[source-adyen-docs-classic-platforms-verification-process]] — 2023-modified, 2026-09-15-captured Classic account-holder verification/deadline guide for payout gates, inactive/suspended refunds, conditional unsuspension and final closure.


- [[source-adyen-docs-classic-platforms-payouts-track-payouts]] — 2026-09-15 Classic payout tracking guide for Initiated/Confirmed/Failed notifications, post-confirmation bank returns, timing estimates and manual versus scheduled recovery routes.

- [[source-adyen-docs-classic-platforms-payouts-manual-payout-payout-to-cards]] — 2021-modified, 2026-09-15-captured Classic manual payout-to-card guide with Support/PCI/eligibility gates, stored payout method and asynchronous update/payout notifications; request receipt does not prove card credit.



- [[source-adyen-docs-classic-platforms-verification-process-verification-codes]] — 2019-modified, 2026-09-15-captured Classic Platforms v5+ account-holder verification-code catalog for identity, document, bank and company errors, with internal-only descriptions and explicit no-retry cases.


- [[source-adyen-docs-classic-platforms-account-holders-and-accounts]] — 2021-modified, 2026-09-15-captured Classic Account API v6 guide to sub-merchant account-holder creation, automatic and optional accounts, asynchronous notification gates, and separate payment-versus-payout verification.


- [[source-adyen-docs-classic-platforms-processing-payments]] — 2021-modified, 2026-09-15-captured Classic split-payment, capture and refund guide for seller accountCode versus liable-account allocation and precedence.


- [[source-adyen-docs-classic-platforms-verification-process-accepted-data-format]] — 2023-modified, 2026-09-15-captured Classic identity, organization registration/TIN and payout-bank format reference with conditional verification inputs and country examples.

- [[source-adyen-docs-classic-platforms-verification-process-document-requirements]] — 2021-modified, 2026-09-15-captured Classic failed-verification document guide for individual ID, organization registration and bank evidence, with category-specific screenshot, age, page and size limits.



- [[source-adyen-docs-classic-platforms-verification-process-requirements-update]] — 2022-modified, 2026-09-15-captured Classic sub-merchant verification changes: shareholder/signatory identity, regional data, versioned Account API shapes, notifications and cohort-specific onboarding actions.


- [[source-adyen-docs-classic-platforms-verification-process-legal-arrangements]] — 2021-modified, 2026-09-15-captured Classic Account API v6 legal-arrangements verification guide for association, partnership, sole proprietorship and trust; conditional documents, asynchronous results and example/region conflicts.


- [[source-adyen-docs-classic-platforms-error-codes]] — 2019-modified, 2026-09-15-captured Classic Platforms response/notification error-code catalog, with separate general and account-holder lists and duplicated account-holder code `125`.


- [[source-adyen-docs-classic-platforms-account-structure]] — 2021-modified, 2026-09-15-captured Classic Platforms resource and money-flow guide for merchant accounts, sub-merchant account holders/accounts, liable pair, splits, verified-bank payouts and refunds.


- [[source-adyen-docs-classic-platforms]] — 2023-modified, 2026-09-15-captured Classic Platforms overview of sub-merchant onboarding, payment splitting, internal funds transfers, payouts, reconciliation and dated region scope.

- [[source-adyen-docs-classic-platforms-platforms-integration-checklist]] — 2021-modified, 2026-09-15-captured Classic test and go-live checklist for account-holder verification, split payments, payout prerequisites, asynchronous notifications and reconciliation; its payout-200 wording needs the final-result webhook boundary.


## Related

- [[adyen-platforms]] — newer Adyen for Platforms model and its separate integration guide.
- [[adyen]] — provider context.
