---
title: "View Marketplace transfer details"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/view-transfers-details"
raw_files:
  - "adyen/docs/marketplaces/view-transfers-details/2026-09-15.md"
tags: [adyen, marketplaces, transfers, balance-accounts]
---

## Overview

This pinned Marketplace guide covers viewing **payment-related, internal and bank transfer records** through Customer Area or the Transfers API. A transfer's initiation and authorization precede capture for payment-related events or booking for other events. For recurring tracking and reconciliation, the guide recommends webhooks; list/detail reads inspect recorded state. See [[adyen]] and [[adyen-platforms]] (raw lines 15–33).

## Key takeaways

- An Adyen for Platforms integration is required. The API credential needs **TransferService Webservice Retrieve role**; Customer Area viewing needs **Balance platform base role** (raw lines 35–43).
- Customer Area **Balances → Transfers** lists one balance platform at a time and offers date/status/reference filtering, including PSP payment reference for payment-related transfers. A transfer ID opens its details; search can use ID or description (raw lines 45–69, 476–493).
- GET `/transfers` lists records with `createdSince` and `createdUntil` and optional account/holder and pagination filters; the response has `data` and pagination `_links`. The prose requires a date interval **less than six months** and at least one unique identifier. **Source example conflict:** its prose example spans May 2025 to May 2026, while curl uses May 2026 to May 2026 and supplies no account/holder identifier. Do not treat those examples as a validated request contract (raw lines 71–100, 264–270).
- GET `/transfers/{id}` reads one transfer's amount, direction, event history, reference and current status, such as `received`, `authorised`, or `booked` (raw lines 495–509, 643–651).
- The TEST list response mixes a **bankTransfer** and an **internalTransfer**. The bank example is `booked` yet carries `reason: counterpartyAccountNotFound` and only an estimated arrival tracking event; neither `booked` nor that estimate proves beneficiary-bank receipt. Inspect the relevant event and bank-return evidence separately (raw lines 273–390). The specific-transfer example shows an internal transfer's booked accounting event with a transaction ID, not a payout (raw lines 653–737).

## Detail locators

- Status sequence, roles, Customer Area filters: raw lines 19–69.
- List-query bounds, source example conflicts, response and pagination: raw lines 71–474.
- Single-transfer lookup and recorded-state fields: raw lines 476–651.
- Booked internal-transfer example: raw lines 653–737.

## Related

- [[adyen]]
- [[adyen-platforms]]
- [[adyen-platform-internal-transfers]]
- [[adyen-reporting]]

## Raw Sources

- [[raw/adyen/docs/marketplaces/view-transfers-details/2026-09-15|Pinned transfer-details guide]]
