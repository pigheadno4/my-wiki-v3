---
title: "Adyen Payouts"
type: concept
category: technology
tags: [adyen, payouts, disbursements]
---

## Overview

The 2023-modified, 2026-09-15-captured [[source-adyen-docs-payouts]] landing page defines a broader Payouts umbrella: a Payments-combined Payout Service for an Adyen merchant of record paying a beneficiary not onboarded with Adyen, and a separate Adyen for Platforms route for payouts of processed payments to platform merchants or sub-merchants. This umbrella and its Payout Service child are distinct from the legacy Online Payout API material documented here; do not infer that API's integration, approval or staged-review rules for Payout Service from the landing page. The child routes own their distinct eligibility, APIs and payout lifecycle; the landing-page “real time” headline is not a completion guarantee.


Adyen's payout documentation covers outbound disbursements to suppliers, partners, or customers. The 2026-09-15 Online payouts snapshot describes a legacy Payout API with instant card and staged bank/PayPal-wallet paths, but says Adyen no longer accepts new Payout API integrations. New integrations are directed to the Transfers API; existing Payout API users are directed to their Adyen contact for migration information. Legacy Payout API use requires Adyen approval and configuration, and staged payouts require a separate reviewer to confirm and check each payout.

## Sources

- [[source-adyen-docs-payouts-payout-service-manage-access]] — 2026-09-15 Payout Service Customer Area team-access overview for signup admin roles and routes to users, API credentials, webhooks and reports; role listing is not live authorization or payout proof.


- [[source-adyen-docs-payouts-payout-service-manage-access-webservice-roles]] — 2023-modified, 2026-09-15-captured Payout Service-path, Platforms-prerequisite Balance Platform API credential role map for Transfers API v1-only bank initiation and separate TransferService Initiate/Retrieve actions; no actual grant or transfer proof.


- [[source-adyen-docs-payouts-payout-service-getting-paid-payout-amount]] — 2026-09-15 Payout Service available-balance guide for existing versus future-value-date booked changes; negative-total wording conflicts with its USD 100/−20 → USD 80 example, so no formula or payout outcome is established.


- [[source-adyen-docs-payouts-payout-service-enterprise-accounts]] — 2026-09-15 Payout Service enterprise-account overview for balance-account-linked account details, merchant-proceeds settlement and third-party transfer routes, with Adyen-contact setup and conditional EMI/PI license gate.


- [[source-adyen-docs-payouts-payout-service-account-structure-resources]] — 2026-09-15 Payout Service merchant-account/balance-platform resource guide for payment settlement into the business's balance account before own-bank or third-party bank/card transfer requests; example topology is not Platforms user/liable ownership or receipt proof.


- [[source-adyen-docs-payouts-payout-service-balance-updates-use-cases]] — 2026-09-15 Payout Service pilot balance-webhook threshold examples for balance-platform, holder and account scope; JPY narrative, numeric setting and sample event conflict and need unit clarification.


- [[source-adyen-docs-payouts-payout-service-balance-updates-manage-balance-webhook]] — 2026-09-15 pilot Payout Service Balance webhook Configuration API lifecycle for reading, PATCHing, deactivating and deleting settings; dropping the last condition broadens notifications.


- [[source-adyen-docs-payouts-payout-service-getting-paid-scheduled-payouts]] — 2022-modified, 2026-09-15-captured Payout Service Customer Area guide for role/capability-gated custom balance-account sweeps to a verified bank instrument; a configured or triggered schedule is not debit or bank-receipt proof.


- [[source-adyen-docs-payouts-payout-service-integration-checklist]] — 2026-09-15 Payout Service resource, TEST credential/webhook, payout/report and separate LIVE setup checklist; setup and GET 200 are not payout or bank-receipt proof.


- [[source-adyen-docs-payouts-payout-service-payout-lifecycle]] — 2026-09-15 Payout Service Transfers API lifecycle separating received/authorised/booked accounting events from optional review, post-booking screening, bank/card tracking and bank returns; distinct from the legacy Payout API.


- [[source-adyen-docs-payouts-payout-service-getting-paid-transfer-statement]] — 2026-09-15 Payout Service recipient-bank statement description/reference matrix, separating accepted characters from bank-visible characters by currency and priority, including zero-visibility routes.


- [[source-adyen-docs-payouts-payout-service-getting-paid]] — 2024-modified, 2026-09-15-captured Payout Service guide for merchant proceeds to company balance/payout account, scheduled/on-demand routes, irreversible instrument deletion, regional priorities and TEST fixtures; separate from legacy Payout API.


- [[source-adyen-docs-payouts-payout-service-get-started]] — 2026-09-15 Payout Service Transfers API onboarding overview for Adyen-contact design, TEST credentials/build/test and separately configured LIVE account; distinct from the legacy Payout API.


- [[source-adyen-docs-online-payments-online-payouts-payouts-to-a-bank-account]] — Adyen legacy Payout API bank-account request examples for SEPA and US recipients, with Transfers API migration direction (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-online-payments-online-payouts-payout-webhook]] — legacy Payout API webhook guide separating staged bank/wallet request acknowledgement and review events from instant-card payout events and financial-institution reversal (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-online-payments-online-payouts-payouts-to-bank-accounts-and-wallets]] — unversioned legacy Payout API guide to staged bank/PayPal-wallet payouts, separate submitter/reviewer roles, seven-day review expiry, and recipient-region limits (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-online-payments-online-payouts]] — Adyen Online payouts overview of the legacy Payout API, migration direction, payout paths, review requirement, and method-specific recipient-region table (webpage snapshot, 2026-09-15).
