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
