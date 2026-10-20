---
title: "Adyen Classic Platforms: Common reconciliation processes"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/reconciliation-use-cases"
raw_files:
  - "adyen/docs/classic-platforms/reconciliation-use-cases/2026-09-15.md"
tags: [adyen, classic-platforms, reconciliation, reports]
---

## Overview

This 2021-modified page captured 2026-09-15 is a **Classic Adyen for Platforms** navigation hub for report-based reconciliation. It points to separate guides for accounts receivable, a transactional ledger, scheduled payouts, and fees. It directs new implementations to a different integration guide and contains no worked report rows or completed reconciliation result. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- Before building a reconciliation process, the page tells readers to understand the payment lifecycle, Classic platform account structure and funds flow; select relevant report types; configure, download and combine reports; and understand fee types. These are stated preparation steps, not proof that files have been generated or joined.
- The four linked processes are: reconcile the net amount settled to platform accounts, track transactions by account holder and account, track transactions in scheduled payouts, and reconcile fees described as debited from the liable account. Each item is a link and one-line purpose; its detailed method lives in the linked guide, not in this page.
- This hub alone does not establish a matching key, amount calculation, bank receipt, successful payout, or verified fee debit for a particular platform. Follow the corresponding detailed guide and underlying reports for those claims.

## Detail locators

- Classic-only/new-integration boundary and hub purpose: raw lines 19–21. Preparation list: raw lines 23–30.
- Accounts receivable and ledger routes: raw lines 32–38. Scheduled-payout and liable-account-fee routes: lines 40–46.

## Related

- [[adyen]] — provider.
- [[adyen-classic-platforms]] — Classic platform and account-holder model.
- [[source-adyen-docs-classic-platforms-prepare-reports]] — report preparation and combination navigation.
- [[adyen-platforms]] — separate modern Platforms model.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/reconciliation-use-cases/2026-09-15|Common reconciliation processes — 2026-09-15 snapshot]]
