---
title: "Adyen Marketplaces internal transfer webhooks"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/internal-fund-transfers/internal-transfer-webhooks"
raw_files:
  - "adyen/docs/marketplaces/internal-fund-transfers/internal-transfer-webhooks/2026-09-15.md"
tags: [adyen, marketplaces, platforms, internal-transfers, transfer-webhooks]
---

## Overview

This 2026-09-15-captured [[adyen]] Marketplace guide explains Transfer webhooks for moving funds between balance accounts in [[adyen-platform-internal-transfers]]. An internal transfer has an outgoing source-account view and incoming target-account view. The guide shows received, authorised and booked stages, then return modifications of the original transfer. Its TEST payloads illustrate event interpretation, not a specific live transfer or bank payout.

## Key takeaways

- Subscribe to **Transfer webhooks** in test Customer Area and accept them on your server. The page lists `balancePlatform.transfer.created` for a future transfer and `balancePlatform.transfer.updated` for status changes; it separately labels the Payment-webhook route deprecated. Identify this flow by `category=internal`, `type=internalTransfer`, and outgoing source versus incoming target `direction`. Each event has separate source and target webhook views. See raw lines 19–54.
- For an on-demand or scheduled internal transfer, the initiated `created` view has `status=received` and negative source versus positive target `balances.received`. The authorised `updated` view reserves the amount with negative source versus positive target `balances.reserved`. The booked `updated` view records the balance-account movement, with negative source versus positive target `balances.balance` in the examples. These are stages of internal balance-account movement, not beneficiary-bank receipt. See raw lines 371–885.
- Returning funds is described as a modification of the original transfer. Initiation and authorisation appear as `balancePlatform.transfer.updated` events with nested `modification.type=return`, `direction=outgoing` from the original recipient and `status=received` or `authorised`; booked return gives two account views, outgoing from the original recipient and incoming to the original sender. The original transfer's top-level `status` can still read `booked` while the nested return modification advances, so inspect the modification rather than treating that top-level field as the return result. See raw lines 887–1459.
- Example values are illustrative. The TEST transfer request uses EUR 10000 while webhook samples use EUR 1000, and examples vary transfer/event identifiers. Do not reconcile them as one exact transaction trace. The return example's zero balances are its example state, not a universal balance rule. See raw lines 56–74, 375–430, 909–1029 and 1174–1459.

## Detail locators

- Current Transfer webhook types, two account views, subscription and deprecated Payment-webhook pointer: raw lines 19–36.
- Internal identifiers and three lifecycle stages: raw lines 38–54.
- TEST transfer request and SDK examples: raw lines 56–369.
- Received, authorised and booked source/target payloads: raw lines 371–885.
- Return request and received/authorised modifications: raw lines 887–1170.
- Booked return's two account views: raw lines 1174–1459.

## Related

- [[adyen]] — provider profile.
- [[adyen-platform-internal-transfers]] — canonical internal balance-account transfer concept.
- [[adyen-platforms]] — modern balance-platform context.
- [[source-adyen-docs-platforms-internal-fund-transfers-internal-transfer-webhooks]] — separate Platforms URL with related guide; preserve both source routes.

## Raw Sources

- [[raw/adyen/docs/marketplaces/internal-fund-transfers/internal-transfer-webhooks/2026-09-15|Marketplace internal-transfer webhooks — pinned 2026-09-15 raw snapshot]]
