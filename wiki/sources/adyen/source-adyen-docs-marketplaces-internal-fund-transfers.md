---
title: "Adyen Marketplace internal fund transfers"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/internal-fund-transfers"
raw_files:
  - "adyen/docs/marketplaces/internal-fund-transfers/2026-09-15.md"
tags: [adyen, marketplaces, platforms, internal-transfers, balance-accounts]
---

## Overview

This 2020-modified Marketplace orientation page, captured 2026-09-15, defines an **internal funds transfer** as movement between balance accounts within the marketplace. It contrasts an **external payout**, which moves funds from a balance account to a user's external transfer instrument, described here as a verified bank account. Internal movement may be between the marketplace liable account and a user account, two accounts of the same user, or accounts of different users. [[adyen]] [[adyen-platform-internal-transfers]]

## Key takeaways

- The page routes to **scheduled** internal transfers, triggered by timing and amount, and **on-demand** transfers initiated when needed (raw lines 21–26, 38–46).
- Examples include liable-account bonuses to users, debiting a user's balance account for an additional marketplace fee, and moving funds between a user's own accounts. These are possible use cases, not proof that a specific fee, transfer or split was executed (raw lines 28–36).
- Separate next steps route to returning an internal transfer to the sender without creating a new transfer and to related transfer webhooks. Follow those guides for request conditions, status and return evidence; this orientation page does not define role, currency, timing, failure or booked-status rules (raw lines 38–54).
- Internal transfer initiation, booking, a return and external bank payout are distinct events. Nothing on this overview establishes completion of a particular movement or a bank receipt (raw lines 19–26, 38–54).

## Detail locators

- Definition, liable/user/same-user/different-user balance-account paths and external-payout distinction: raw lines 17–26.
- Use cases and process navigation to scheduled, on-demand, return and webhook guides: raw lines 28–54.

## Related

- [[adyen]] — provider.
- [[adyen-platform-internal-transfers]] — balance-account transfer concept.
- [[source-adyen-docs-marketplaces-internal-fund-transfers-scheduled-fund-transfers]] — scheduled transfers.
- [[source-adyen-docs-marketplaces-internal-fund-transfers-on-demand-fund-transfers]] — on-demand transfers.
- [[source-adyen-docs-marketplaces-internal-fund-transfers-return-transfers]] — return flow.
- [[source-adyen-docs-marketplaces-internal-fund-transfers-internal-transfer-webhooks]] — event evidence.
- [[source-adyen-docs-platforms-internal-fund-transfers]] — separate Platforms-path overview.

## Raw Sources

- [[raw/adyen/docs/marketplaces/internal-fund-transfers/2026-09-15|Marketplace internal fund transfers — 2026-09-15 snapshot]]
