---
title: "Adyen account structure"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/account/account-structure"
raw_files:
  - "adyen/docs/account/account-structure/2026-09-15.md"
tags: [adyen, account-structure, company-account, merchant-account, account-groups]
---

## Overview

This Adyen account-structure guide describes the hierarchy of one company account, one or more merchant accounts, optional account groups for multiple merchant accounts, and optional stores under merchant accounts for point-of-sale locations. It explains which level holds users and invoices, processes payments and receives payouts/reconciliation reports, or groups user access. The raw page was last modified 2023-10-19 and captured 2026-09-15. See [[adyen]] and [[adyen-account-structure]].

## Key takeaways

- A business has a single **company account** and one or more **merchant accounts** underneath. The company account represents the core business to Adyen, holds merchant accounts and users, and receives the monthly invoice by default. For POS, one or more stores may sit under each merchant account to represent physical locations; the linked in-person guide owns store setup details.
- **Merchant accounts** are the sub-accounts in which payments are processed. The guide locates payout receipt and reconciliation reports there, along with configuration of payment methods, processing currencies, and overrides of company-level risk rules. A single merchant account is enough for many customers; multiple accounts can be useful or required depending on the business. Its Europe/US tea-shop example illustrates a possible split, not a mandatory geography rule.
- When there are multiple merchant accounts, **account groups** provide an optional user-access layer. Subject to user roles, users may search payments and view/download reports across the group's merchant accounts. The page says one merchant account may belong to only one account group. It gives country/region and brand grouping as examples, not required designs.
- This account hierarchy is not a determination of legal entity, merchant of record, contractual liability, beneficiary ownership, platform organization structure, or end-to-end funds flow. In particular, the page's merchant-account payout location does not establish who legally sells to the shopper or owns proceeds. The linked structure-selection and management pages are needed for their respective procedures.

## Detail locators

- Lines 15–21: top-level hierarchy, optional groups, and POS stores.
- `## Company account`, lines 23–25: company representation, users, default invoice.
- `## Merchant accounts`, lines 27–35: processing, payouts, reports, configuration, business-dependent count, illustrative regional split.
- `## Account groups`, lines 37–50: optional access grouping, role-qualified abilities, one-group membership cap, illustrative grouping.
- `## Next steps`, lines 52–60: navigation to choosing and managing the structure.

## Related

- [[adyen-account-structure]] — proposed provider concept and reciprocal source route.
- [[source-adyen-docs-point-of-sale-design-your-integration-determine-account-structure]] — separately scoped in-person account and store guide.
- [[adyen-pos-store-management]] — separate POS store-management concept.
- [[adyen-api-access]] — API credential account scope and roles, not the business hierarchy.

## Raw Sources

- [[raw/adyen/docs/account/account-structure/2026-09-15|Account structure guide, captured 2026-09-15]]
