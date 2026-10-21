---
title: "Adyen Payout Service internal balance-account transfers"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/internal-fund-transfers"
raw_files:
  - "adyen/docs/payouts/payout-service/internal-fund-transfers/2026-09-15.md"
tags: [adyen, payout-service, internal-transfers, balance-accounts]
---

## Overview

This Payout Service-path overview (last modified 2020-09-11; captured 2026-09-15) routes movement of funds **between balance accounts within a balance platform**. It describes setting an Adyen balance account as the settlement account as a simple funding route and sweeps to help keep a specified balance account above an amount. It is an orientation and navigation page, not a record of an executed transfer or external bank payout. See [[adyen]] and [[adyen-platform-internal-transfers]].

## Key takeaways

- **Two initiation routes:** A scheduled internal transfer is configured to trigger based on timing and amount; an on-demand transfer moves funds between balance accounts when needed. This overview does not state detailed capability, role, timing, currency, amount, failure, or booked-status rules; use the linked process guides for those.
- **Follow-up routes:** The page points to internal-transfer webhooks and a transfer-details view. The linked guides, rather than this overview, establish event sequences, return behavior and whether a particular transfer reached a booked state. A configured sweep or request is not itself evidence of completed movement.
- **Product boundary:** The destination here is another balance account. That is distinct from Payout Service getting-paid guides for transfers to external bank accounts, and from the legacy Online Payout API.

## Detail locators

- Settlement-account funding context, sweeps and balance-account-to-balance-account purpose: pinned raw lines 15-19.
- Scheduled and on-demand initiation routes: pinned raw lines 21-26.
- Webhook and transfer-details navigation: pinned raw lines 28-44.

## Related

- [[adyen-platform-internal-transfers]] — main internal balance-account transfer concept and reciprocal source route.
- [[source-adyen-docs-payouts-payout-service-internal-fund-transfers-scheduled-fund-transfers]] — scheduled sweep process.
- [[source-adyen-docs-payouts-payout-service-internal-fund-transfers-on-demand-fund-transfers]] — on-demand process.
- [[source-adyen-docs-payouts-payout-service-internal-fund-transfers-internal-transfer-webhooks]] — event detail.

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/internal-fund-transfers/2026-09-15|Payout Service internal fund-transfer overview, captured 2026-09-15]]
