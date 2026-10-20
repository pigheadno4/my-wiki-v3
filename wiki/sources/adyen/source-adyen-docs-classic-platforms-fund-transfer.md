---
title: "Adyen Classic Platforms: Fund transfers between accounts"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/fund-transfer"
raw_files:
  - "adyen/docs/classic-platforms/fund-transfer/2026-09-15.md"
tags: [adyen, classic-platforms, fund-transfers, refunds, webhooks]
---

## Overview

This 2020-modified, 2026-09-15-captured **Classic Adyen for Platforms** guide covers moving funds between Classic platform accounts through the Fund API or Customer Area, then reversing all or part of a prior fund transfer through the API. The source account is **debited** and the destination account **credited**; examples include a bonus or a transfer between account holders' accounts. This is an internal Classic account transfer, distinct from a buyer payment refund or a modern Balance Platform transfer. The page directs new implementations to the newer integration guide. See [[adyen]] and [[adyen-classic-platforms]].

## Key takeaways

- Before transfers or reversals, Adyen Support must enable fund transfers and define platform transfer codes, which identify the reason and are configured against local-regulation requirements. Configure Classic `TRANSFER_FUNDS` and `REFUND_FUNDS_TRANSFER` notification webhooks: both operations are asynchronous and their initial API responses acknowledge receipt, while webhooks carry the result.
- For POST `/transferFunds`, supply `sourceAccountCode`, `destinationAccountCode`, `amount.currency/value`, and a preconfigured `transferCode`; `merchantReference` is optional for linking transactions. The source account holder must be **Active** with payouts allowed; the destination account holder must be **Active** with processing allowed. The Customer Area route requires the **Perform and manage Fund Transfers from the customer area** role and additionally states that the source account must have a positive balance. Its examples use Classic Fund API v6 TEST endpoints.
- The API response's `resultCode: Received` and `pspReference` mean the transfer request was received, not completed. Use `TRANSFER_FUNDS` to learn the outcome; the guide says successful transfers have a `FundTransfer` journal entry in Marketplace Payment Accounting Report. Customer Area also exposes status in Transactions.
- To reverse a prior transfer fully or partly, POST `/refundFundsTransfer` with `originalReference` equal to the original transfer's `pspReference` and the refund `amount.currency/value`; `merchantReference` is optional. The guide explicitly allows this reversal **regardless of account-holder status**, including when an account is no longer Active. Its initial `Received` response is not the result; follow `REFUND_FUNDS_TRANSFER`. Successful reversals have a `FundTransferReversed` journal entry. This describes a transfer reversal, not proof of an external payout or bank receipt.

## Detail locators

- Pinned raw lines 15–36: Classic scope, account-to-account purpose, Support enablement, transfer codes and required asynchronous notifications.
- Pinned raw lines 38–48: transfer API fields and source/destination account-holder conditions; lines 50–81: TEST v6 example, received-response boundary, `pspReference`, webhook and accounting journal.
- Pinned raw lines 83–109: Customer Area permission, source positive-balance condition, initiation and status routes.
- Pinned raw lines 111–121: full/partial reversal, status exception and original-reference/amount fields; lines 123–151: TEST v6 request, asynchronous refund webhook and reversed journal entry.

## Related

- [[adyen-classic-platforms]] — Classic account-holder/account and money-flow context.
- [[source-adyen-docs-classic-platforms-account-structure]] — Classic account ownership and liability.
- [[adyen-platforms]] — newer model with separate resource and transfer APIs.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/fund-transfer/2026-09-15|Classic Platforms fund-transfer guide, captured 2026-09-15]]
