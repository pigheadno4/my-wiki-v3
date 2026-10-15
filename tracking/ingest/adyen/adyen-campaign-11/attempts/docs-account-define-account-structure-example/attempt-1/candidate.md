---
title: "Adyen example account structures"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/account/define-account-structure/example"
raw_files:
  - "adyen/docs/account/define-account-structure/example/2026-09-15.md"
tags: [adyen, account-structure, merchant-account, legal-entity, example]
---

## Overview

This dated Adyen Docs example (2019-09-05 last-modified metadata; captured 2026-09-15) follows a hypothetical Dutch tea merchant as it adds POS, US, and region-specific merchant accounts. It illustrates account, invoice, payout, report, and access choices under the assumed business setup. It does not establish a required structure for every merchant, a merchant-of-record identity, contractual liability, live eligibility, or a complete flow of funds. For general rules use [[adyen-account-structure]] and [[source-adyen-docs-account-define-account-structure]].

## Key takeaways

- Starting scenario: a Netherlands legal entity sells tea online to the EU and runs an Amsterdam store. The example starts with company account `TeaShop` and online account `TeaShop_ECOM`, adds `TeaShop_POS` for the store, and describes separate merchant-account reports and payouts with company-level invoicing. These are the example's online/POS assumptions. [Raw lines 23–39]
- US expansion: the hypothetical merchant creates a US legal entity to use local acquiring, then adds `TeaShop_US_ECOM`. The example says its US-linked account has separate reports, payouts, and invoice from the Netherlands company-level invoice. The text describes expected local-acquiring benefits but does not guarantee fee or authorization improvement. [Raw lines 41–50]
- Regional separation: the scenario adds `TeaShop_DE_ECOM` and `TeaShop_NL_ECOM` to separate funds, reports, and user permissions. Both new accounts remain linked to the **Netherlands** legal entity; their invoice stays with the company-level Netherlands invoice. The older `TeaShop_ECOM` is retained for other EU business outside Germany and the Netherlands. An account name or sales geography alone therefore does not identify its legal entity or merchant of record. [Raw lines 52–62]
- The optional `Account group EU` groups four EU merchant accounts, including POS, for shared user access and cross-account payment search in the illustration. The example does not say grouping merges merchant-account payouts or invoices. [Raw lines 64–72]

## Detail locators

- Assumed merchant and smallest setup: raw lines 23–39. New US legal entity and account: raw lines 41–50. Germany/Netherlands account split and invoicing: raw lines 52–62. Account-group access: raw lines 64–72.
- The original `TeaShop_ECOM` account changes described business coverage after the region-specific accounts are added; the page provides no migration procedure or transaction-level reassignment rule. Treat the diagram and named accounts as an illustration rather than a validated implementation template.
- General guidance and management guides are linked at raw lines 19–21 and 74–78; they are navigation from this example, not additional claims from their unread content.

## Related

- [[adyen-account-structure]]
- [[adyen]]
- [[source-adyen-docs-account-define-account-structure]]

## Raw Sources

- [[raw/adyen/docs/account/define-account-structure/example/2026-09-15|Adyen example account structures, 2026-09-15 snapshot]]
