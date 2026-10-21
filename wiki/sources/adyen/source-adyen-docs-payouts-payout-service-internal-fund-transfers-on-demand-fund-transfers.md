---
title: "Adyen Payout Service on-demand internal funds transfers"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/internal-fund-transfers/on-demand-fund-transfers"
raw_files:
  - "adyen/docs/payouts/payout-service/internal-fund-transfers/on-demand-fund-transfers/2026-09-15.md"
tags: [adyen, payout-service, platforms, internal-transfers, balance-accounts]
---

## Overview

This [[adyen]] Payout Service-path guide, last modified 2020-09-11 and captured 2026-09-15, explains on-demand movement between balance accounts through Customer Area or Transfers API POST `/transfers`. It belongs under [[adyen-platform-internal-transfers]]. The source balance account is debited and the counterparty balance account credited; this is internal movement, not a bank payout. The page's description mentions an internal direct debit, but its detailed request and EUR examples show a push from source to destination; do not derive a pull-request recipe from the push example alone.

## Key takeaways

- The stated prerequisites are an Adyen for Platforms integration, **TransferService Webservice Initiate** for the Transfers API credential, **Initiate internal transfers** and **Balance platform base role** for Customer Area, a server that receives/accepts Transfer webhooks, and Support enablement of transfers for the **source** balance account. When the balance accounts belong to different account holders, the source holder needs `sendToBalanceAccount` and the recipient holder needs `receiveFromBalanceAccount`; the page states this capability check conditionally, not for every same-holder transfer. See raw lines 21–38.
- In Customer Area, select the source balance account to debit, counterparty type `balanceAccount`, destination balance-account ID to credit, currency and amount, then confirm the request. Optional internal reference, description and beneficiary reference have distinct purposes and character/length constraints. Creation is not booked movement; check the Transfers view for booking. See raw lines 40–88.
- The API route uses POST `/transfers` with `amount`, source `balanceAccountId`, destination `counterparty.balanceAccountId` and `category: internal`; `description`, `reference` and `referenceForBeneficiary` are optional in this guide. The TEST curl and SDK examples push EUR 100.00 from a liable account to a user's account, with versioned Java/PHP/.NET/Node/Go/Python/Ruby samples; these are examples, not live execution evidence. See raw lines 90–417.
- The response includes transfer `id`, `status` and `reason`; its example is `received` / `pending`. A `refused` reason may be `notEnoughBalance`. Wait for Transfer webhooks to confirm booking rather than treating the POST response as proof. The guide describes separate outgoing-source and incoming-recipient webhook series progressing `received` → `authorised` → `booked`, with failure notifications. Customer Area likewise shows two entries, one debit and one credit. See raw lines 419–471.

## Evidence boundary

The introductory description says “send funds or initiate an internal direct debit” (raw lines 15–19), yet the operational fields and concrete examples in this page describe a source-initiated push (raw lines 54–58, 92–104). This page does not document a separate pull instruction, nor does it establish approval, booking, payout or bank receipt for a particular transfer. Use the linked webhook guide for event detail; do not infer an external bank payout from this internal balance-account route.

## Detail locators

- Requirements and conditional cross-holder capabilities: raw lines 21–38.
- Customer Area source/destination action and booking check: raw lines 40–88.
- API fields and versioned TEST examples: raw lines 90–417.
- Response status versus two-sided webhook booking: raw lines 419–471.

## Related

- [[adyen-platform-internal-transfers]]
- [[adyen-payouts]]
- [[source-adyen-docs-payouts-payout-service-internal-fund-transfers-internal-transfer-webhooks]]

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/internal-fund-transfers/on-demand-fund-transfers/2026-09-15|Payout Service on-demand internal funds transfer guide, 2026-09-15 capture]]
