---
title: "Adyen Account Structure"
type: concept
category: technology
tags: [adyen, account-structure, company-account, merchant-account, account-groups]
---

## Overview

Adyen's account-structure guide describes one company account with one or more merchant accounts, optional account groups when several merchant accounts exist, and optional stores under merchant accounts for in-person locations. This is an account and access hierarchy, not by itself a merchant-of-record, legal-entity, contractual-liability, ownership, or full funds-flow model.

## Account levels

For Adyen's framework entity onboarding route, a common holding entity is the main contracting entity added as a company account, while affiliated processing entities are added as merchant accounts. The guide says the holding entity generally does not process payments; this route-specific mapping does not establish a particular merchant of record, contractual allocation, or live eligibility. [[source-adyen-docs-account-define-account-structure-framework-onboarding]]


The defining-structure guide adds that each payment-processing legal entity needs at least one merchant account, a merchant account cannot span two legal entities, and each merchant account has one acquiring region. It links the merchant account to the legal entity owning the ultimate settlement bank account and permits only one bank account per settlement currency. These are Adyen account/settlement configuration rules in a dated guide; they do not determine the merchant of record or full funds flow. [[source-adyen-docs-account-define-account-structure]]


A separate organization layer groups legally related company accounts for one Customer Area login after Adyen-side setup. Membership does not grant access to every company by default, and roles remain distinct for each company account. This access layer does not itself define merchant-account processing, contracts, seller identity, or fund flow. [[source-adyen-docs-account-manage-account-structure-create-an-organization]]


The company account represents the core business to Adyen, holds merchant accounts and users, and receives the monthly invoice by default. Merchant accounts process payments and are where the guide locates payouts and reconciliation reports; payment methods, processing currencies, and overrides of company-level risk rules are configured there. The guide says one merchant account is enough for many customers, while more may be useful or required depending on their business. Its regional example is illustrative.

With multiple merchant accounts, account groups can grant role-qualified users access to search payments and view/download reports across grouped merchant accounts. A merchant account may belong to only one group. For point-of-sale payments, stores can be placed under merchant accounts to represent physical locations; separate in-person documentation owns store-setup details. Account grouping is not evidence that merchant-account payouts combine.

## Evidence boundary

This is a 2023-last-modified Adyen page captured 2026-09-15. It does not identify the legal seller or merchant of record, establish an organization entity, decide current account eligibility, or prove a live payout or payment outcome. Use the source and linked selection/management guides for applicable setup details.

## Sources

- [[source-adyen-api-explorer-balancecontrol-latest-get-balanceoverview-merchants-merchantaccountcode-balances]] — 2026-11-07 Balance Control API v2 merchant/currency balance GET; optional minor-unit balance objects, with available-funds definition, response-envelope and live-base-path conflicts.

> [!warning] Contradiction
> This API page describes available funds as settled, while [[source-adyen-docs-account-balances]] defines available funds as an adjustable aggregate including unsettled Pending, Next payout, Reserve and conditional Negative refund allowance. Do not equate API `availableFund` with that aggregate. This merchant-scoped endpoint's flat response table also conflicts with its two-merchant `merchantBalancesOverview` example; its listed live base path conflicts with the Going live paragraph in [[source-adyen-api-explorer-balancecontrol-latest-overview]]. The captures do not resolve these differences.


- [[source-adyen-api-explorer-balancecontrol-latest-get-balanceoverview-companies-companyaccountcode-balances]] — 2026-11-07-captured Balance Control API v2 company-path GET for per-merchant balance categories and required currency; optional row/amount fields and prospective next payout are not bank-receipt proof. The operation lists a Live `/balance-control/api/v2` base, while the family overview also states a shorter Live `/api/v2` base in prose.

> [!warning] Contradiction
> The Balance Control API v2 company and merchant balance GET references describe available funds as settled and pending balance as separate and unsettled; the account-balances guide defines total available funds as including unsettled Pending, Next payout, Reserve, and conditional Negative refund allowance. The captures do not reconcile the API `availableFund` field with the guide's broader total. [[source-adyen-api-explorer-balancecontrol-latest-get-balanceoverview-companies-companyaccountcode-balances]] [[source-adyen-api-explorer-balancecontrol-latest-get-balanceoverview-merchants-merchantaccountcode-balances]] [[source-adyen-docs-account-balances]]


- [[source-adyen-api-explorer-management-latest-get-merchants-merchantid-paymentmethodsettings-paymentmethodid]] — 2026-11-05-captured Management API v3 Test, role-gated read of one merchant-account payment-method setting by merchant and method IDs; optional `allowed`, `enabled`, and `verificationStatus` readback remain distinct from a payment outcome.


- [[source-adyen-api-explorer-management-latest-patch-companies-companyid-users-userid]] — 2026-11-03 Management API v3 TEST company-user detail update by `companyId` and `userId`, requiring Users read and write; returned user details do not prove login or merchant processing.


- [[source-adyen-api-explorer-management-latest-delete-merchants-merchantid-payoutsettings-payoutsettingsid]] — 2026-11-03-captured Management API v3 TEST deletion of a merchant-scoped payout setting by two path IDs, with Adyen-set access and payout-settings role; 204 is request-status evidence, not payout or bank-receipt proof.


- [[source-adyen-api-explorer-management-latest-get-merchants-merchantid-payoutsettings-payoutsettingsid]] — 2026-11-03-captured Management API v3 TEST, role-gated merchant payout-setting GET by merchant and setting IDs; readback distinguishes verification-derived `allowed` from configurable `enabled` and does not prove bank receipt.


- [[source-adyen-api-explorer-management-latest-get-merchants-merchantid-payoutsettings]] — 2026-11-03-captured Management API v3 TEST merchant payout-settings list, requiring Adyen-set access and a payout-settings-read role; bank verification and enabled configuration are distinct, and readback does not prove payout or bank receipt.


- [[source-adyen-api-explorer-management-latest-patch-merchants-merchantid-payoutsettings-payoutsettingsid]] — 2026-11-03-captured Management API v3 TEST PATCH for a merchant payout setting's `enabled` flag; `allowed` is verification-derived and both must be true for bank-account payouts, while update success is not payout or bank-receipt proof.


- [[source-adyen-api-explorer-management-latest-post-merchants-merchantid-payoutsettings]] — 2026-11-03-captured Management API v3 TEST request to add a merchant-account payout setting linked to a Legal Entity transfer instrument; Adyen bank verification determines `allowed`, while `enabled` and an optional effective date separately govern payout enablement. Configuration is not payout or bank-receipt proof.


- [[source-adyen-api-explorer-management-latest-get-merchants-merchantid]] — 2026-11-03-captured Management API v3 TEST merchant-account GET, scoped to an Account-read credential with merchant access; status readback is distinct from transaction outcome, and example links use `/v1` rather than the listed `/v3` server.

> [!warning] Contradiction
> This endpoint's captured server is `/v3`, while its example resource links use `/v1`; the `captureDelay` example also uses lower-case `manual` against the table's `Manual`. The sample does not resolve either discrepancy. [[source-adyen-api-explorer-management-latest-get-merchants-merchantid]]


- [[source-adyen-api-explorer-management-latest-post-merchants-merchantid-activate]] — 2026-11-03-captured Management API v3 TEST request for merchant-account activation, requiring Accounts read/write and Adyen-set access; 200/204 request success precedes the asynchronous `merchant.updated` activation result and is not payment or payout proof.


- [[source-adyen-api-explorer-management-latest-get-companies-companyid]] — 2026-11-03 Management API v3 TEST credential-scoped GET of a company account by `companyId`, requiring Account read; returned account status does not establish merchant processing or payouts, and example hrefs use `/v1` despite the declared `/v3` server.


- [[source-adyen-api-explorer-management-latest-get-companies-companyid-merchants]] — 2026-11-03-captured Management API v3 TEST reference for credential-scoped, paginated merchant accounts under a company, including status meanings and conditional Active processing; its v1 response-example links conflict with the v3 server.


- [[source-adyen-api-explorer-document-collector-latest-post-crossborderinvoices]] — captured Document Collector v1 merchant-account PDF upload reference for `paCbInvoice` and `{pspReference}.pdf`; upload success does not establish invoice reconciliation or payment state (2026-09-15 snapshot).


- [[source-adyen-api-explorer-balancecontrol-latest-post-balancetransfers]] — 2026-09-15 Balance Control API v2 merchant-account transfer reference: same company/legal entity, common currency and source funds, sequential same-pair requests, and 200 transfer reference. Its live server path conflicts with the Going live paragraph in [[source-adyen-api-explorer-balancecontrol-latest-overview]]; neither snapshot resolves the base URL.


- [[source-adyen-api-explorer-balancecontrolv1-latest-post-balancetransfer]] — 2026-09-15 Balance Control v1 TEST API reference for same-company/legal-entity merchant-account balance-transfer requests and their returned status, distinct from platform balance-account transfers.


- [[source-adyen-api-explorer-balancecontrolv1-latest-overview]] — 2026-09-15 Balance Control API v1 overview for same-company/same-legal-entity merchant-account transfers, authentication choices, TEST v1 URL, and the balanceTransfer operation; no transfer-outcome schema.


- [[source-adyen-api-explorer-balancecontrol-latest-overview]] — 2026-09-15 Balance Control API v2 overview for company/merchant balance views and balance-transfer endpoint; its live base-path statements conflict.


- [[source-adyen-api-explorer-managementnotification-latest-post-merchant-updated]] — 2026-09-15-captured merchant-account capability and verification update webhook; capability verification is separate from merchant status, and the valid-capability example remains `PreActive`.


- [[source-adyen-api-explorer-management-latest-get-companies]] — 2026-09-15-captured Management API v3 TEST list of company accounts accessible to the calling credential, requiring Account read role; sample links use /v1 and listing does not enable accounts or merchant processing.


- [[source-adyen-api-explorer-management-latest-post-merchants]] — 2026-09-15-captured Management API v3 test-server `POST /merchants` reference for creating a merchant account under a specified company account, with contact-set access, Accounts read/write role and conditional Platforms Manage fields; creation is not live-processing proof.


- [[source-adyen-api-explorer-management-latest-get-merchants]] — 2026-09-15-captured Management API v3 TEST credential-scoped merchant-account list, requiring Account read role with pagination and status fields; v1 example links conflict with v3 server and listing does not prove live activation or payment.


- [[source-adyen-docs-set-up-adyen-payments-application-requirements]] — 2025-modified, 2026-09-15-captured Adyen live-account application checklist for legal-entity/tax or VAT/identity/residency evidence, conditionally reviewed online-site content and ownership documentation; submission is not live approval.


- [[source-adyen-docs-account-balances-next-payout]] — 2023-modified, 2026-09-15-captured Adyen guide to a merchant account's changing Next payout balance, expense-driven negatives, possible refund/payout/deposit effects, and conditional Reserve auto-funding or top-up/transfer routes; balance is not bank receipt.


- [[source-adyen-docs-account-balances]] — 2026-09-15 snapshot of a 2021-modified Adyen balance-definition guide: pending, next payout, reserve and conditional negative refund allowance form available funds, while Adyen-held deposit is separate.


- [[source-adyen-docs-account-manage-payout-account-details]] — 2026-09-15 Adyen merchant-account payout-bank-details guide for reviewed live additions/edits, same-legal-entity copy of approved details, test reconciliation setup, view/edit roles, and removal without approval; configuration does not prove bank receipt.


- [[source-adyen-docs-account-manage-your-balances]] — 2026-09-16 merchant-account balance allocation, top-up and same-company/legal-entity transfer guide, with role-specific requirements and funding-versus-receipt boundary.


- [[source-adyen-docs-account-balances-deposit]] — 2026-09-15 snapshot of Adyen's merchant-account deposit guide: daily exposure/coverage requirement, conditional payout withholding and release, reserve distinction and role-qualified balance view.


- [[source-adyen-docs-account-balances-reserve]] — 2026-09-15 Adyen merchant-account reserve guide for refund shortfalls, payable-to-reserve threshold changes, auto-funding, top-ups and qualified same-company/legal-entity balance transfers; configuration requests are distinct from completed transfers.


- [[source-adyen-docs-account-view-your-balances]] — 2026-09-15 Customer Area and Balance Control API guide to merchant/company balance views by currency, pending/next-payout/reserve/deposit identity, roles, and inconsistent API examples.


- [[source-adyen-docs-account]] — 2026-09-14 snapshot of Adyen's Account landing page, routing Customer Area readers to account setup, payment management and lifecycle, getting paid, balances, and reports; navigation only, not operational or financial outcome evidence.


- [[source-adyen-docs-account-define-account-structure-framework-onboarding]] — 2026-09-15 framework-entity onboarding guide mapping holding/processing legal entities to company/merchant accounts and requiring Adyen approval before go-live.


- [[source-adyen-docs-account-define-account-structure-example]] — 2026-09-15 Dutch tea merchant example of online/POS, US legal-entity, DE/NL regional merchant-account and EU account-group choices; illustrative names and outcomes, not a universal structure or MOR determination.


- [[source-adyen-docs-account-invoice-settings]] — 2026-09-15 snapshot of Adyen Customer Area invoice settings for one merchant account or company-account batch edit, including legal-entity disablement and Support-only charged-account changes; invoice configuration does not establish payment or payout flow.


- [[source-adyen-docs-account-define-account-structure]] — 2026-09-15 snapshot of Adyen's merchant-account selection guide covering legal entities, acquiring region, payout destination, reconciliation, permissions, and POS trade-offs.


- [[source-adyen-docs-account-manage-account-structure]] — 2024-modified Customer Area guide for merchant-account requests and timed closure, account-group administration, and company/merchant view scopes (2026-09-15 snapshot).


- [[source-adyen-docs-account-manage-account-structure-create-an-organization]] — 2026-09-15 Adyen guide to legally related company-account grouping, Support setup, per-company access and roles, and SSO options.


- [[source-adyen-docs-account-account-structure]] — Adyen company/merchant account hierarchy, optional account groups and POS stores, business-dependent structure selection and user-access boundary (2026-09-15 snapshot).
