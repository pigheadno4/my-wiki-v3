---
title: "Adyen: Defining your account structure"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/account/define-account-structure"
raw_files:
  - "adyen/docs/account/define-account-structure/2026-09-15.md"
tags: [adyen, account-structure, legal-entity, merchant-account, reconciliation]
---

## Overview

This Adyen account-planning guide (2019-09-05 last-modified metadata; captured 2026-09-15) explains how to choose the number and scope of merchant accounts under an Adyen company account. Fewer merchant accounts simplify operations and reconciliation; more allow finer reporting, access control, and payout separation. Adyen recommends as few as meet business needs and directs merchants to Support for further help. It is guidance for Adyen account configuration, not an identification of the seller or merchant of record for a particular transaction. See [[adyen-account-structure]] and [[adyen]].

## Key takeaways

- The page requires at least one merchant account for each legal entity that processes payments, and says one merchant account cannot be linked to two legal entities. One legal entity may have multiple merchant accounts. The company account receives the monthly invoice by default; separate invoices apply to merchant accounts under a legal entity different from the company account's. [Raw lines 31–39]
- An acquiring connection is configured at merchant-account level, and one merchant account can have only one acquiring region. Adyen describes potential advantages of regional local acquiring, without guaranteeing lower fees, higher authorisation, or faster settlement for a given merchant. [Raw lines 41–45]
- Adyen describes payouts and bank-settlement reconciliation reports at merchant-account level. The merchant account must be associated with the legal entity that owns its ultimate settlement bank account. Multiple bank accounts can be linked for multiple currencies, but only one bank account per settlement currency; to separate same-currency funds by country or region, the page calls for multiple merchant accounts. These are settlement-configuration constraints, not a complete money-flow or contractual-liability model. [Raw lines 47–59]
- Company-level RevenueProtect and Dynamic 3D Secure risk settings can be overridden at merchant-account level. Company-account users have access to all underlying merchant accounts; separate merchant accounts and scoped user or group permissions support access limits. [Raw lines 61–71]
- For in-person processing, the dated page recommends separate ecommerce and POS merchant accounts and says local legal entities and a merchant account per POS region are required. Stores in one region may share a merchant account with `storeID`; separate merchant accounts are needed for store-specific same-currency payouts or invoices, or store-limited user credentials. Verify current applicability through the separately linked POS setup documentation and Adyen. [Raw lines 73–84]

## Detail locators

- Selection trade-offs and Support route: raw lines 19–29. Legal entity, invoicing, and acquiring factors: raw lines 31–45.
- Payout destination, currency, and reconciliation factors: raw lines 47–59. Risk, permissions, and in-person factors: raw lines 61–84.
- The page links an example account-structure guide, account-structure hierarchy, management guide, and framework onboarding at raw lines 86–91. These are navigation, not evidence read for this entry.
- This source does not establish who is merchant of record, the complete legal/contractual model, live eligibility for an account structure, or the outcome of a payment or payout.

## Related

- [[adyen-account-structure]]
- [[adyen]]
- [[source-adyen-docs-account-account-structure]]

## Raw Sources

- [[raw/adyen/docs/account/define-account-structure/2026-09-15|Adyen defining your account structure, 2026-09-15 snapshot]]
