---
title: "Adyen Marketplace multi pay-in: receive partner funds"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/multi-pay-in/receive-funds"
raw_files:
  - "adyen/docs/marketplaces/multi-pay-in/receive-funds/2026-09-15.md"
tags: [adyen, marketplaces, platforms, multi-pay-in, bank-transfers]
---

## Overview

This 2026-09-15 Marketplace guide describes receiving a third-party acquirer or PSP **pay-in partner's payout** as an incoming bank transfer into a multi pay-in account linked to the platform. The guide says Adyen creates and legally holds that account solely for the users' benefit; it holds their funds **before** the platform allocates them to user balance accounts. A received partner transfer or credit to this staging account is not proof of a particular payment's allocation, a user balance-account credit, payout, or shopper refund. [[adyen]] [[adyen-multi-pay-in]]

## Key takeaways

- Set the multi pay-in account as the pay-in partner's payout account. Adyen allowlists the partner's bank account and automatically rejects bank transfers from other accounts. The snapshot gives region/currency-dependent account-number formats: EUR Netherlands/eurozone and GBP UK IBANs, and US USD account number plus routing number; these are examples, not current availability promises (raw lines 17–35).
- Subscribe in Customer Area to desired `balancePlatform.transfer.created`, `balancePlatform.transfer.updated`, and `balancePlatform.transaction.created` webhooks. Incoming partner funds are identified as `category: bank`, `direction: incoming` relative to the multi pay-in account, and `type: bankTransfer` (raw lines 37–59).
- The USD 100 TEST examples present `received` on transfer creation, `authorised` in an update, then `booked` with `transactionId`; a booked Transaction webhook identifies the credited multi pay-in account and related transfer. These examples concern a **partner bank payout into the Adyen-held staging account**, not an internal transfer from that account to users. Distinguish notification of incoming funds from booked account credit and later allocation (raw lines 59–123, 127–202, 206–342).
- **Example inconsistencies:** the “Transfer authorized” prose promises a transfer.updated `status: authorised` and its nested accounting event has that status, but the example's top-level `data.status` remains `received` (raw lines 127–129, 176–200). In the booked TEST Transfer example, nested `events[].transactionId` is `1WT1N05XXY7P9XGB`, while top-level `data.transactionId` is `EVJN42272224222B5JB8BRC84N686ZUSD`; the subsequent Transaction webhook's `data.id` matches the latter (raw lines 282, 296, 315). The page does not resolve the IDs' semantics, so do not infer a universal join-key rule from this sample.
- The final next-step links route to separate allocation and refund guides. The snapshot labels a “Top up multi pay-in account” link with the refunds URL, so that link text is not a reliable top-up route (raw lines 344–360).

## Detail locators

- Pay-in partner, Adyen-held account, allowlisting and dated account-number formats: raw lines 17–35. Webhook subscription and incoming-bank identifiers: lines 37–59.
- USD 100 TEST received, authorized, booked and transaction payloads, including status inconsistency: lines 59–342. Next-step navigation: lines 344–360.

## Related

- [[adyen]] — provider.
- [[adyen-multi-pay-in]] — multi pay-in concept and allocation boundary.
- [[source-adyen-docs-platforms-multi-pay-in-receive-funds]] — separate Platforms-path receipt guide.
- [[source-adyen-docs-marketplaces-multi-pay-in-payments]] — Marketplace allocation of third-party payments.
- [[source-adyen-docs-marketplaces-multi-pay-in-refunds]] — Marketplace refund route.
- [[adyen-platforms]] — modern platform context.

## Raw Sources

- [[raw/adyen/docs/marketplaces/multi-pay-in/receive-funds/2026-09-15|Marketplace multi pay-in receive funds — 2026-09-15 snapshot]]
