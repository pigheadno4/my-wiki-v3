---
title: "Adyen Marketplace webhook structures and types"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/webhook-types"
raw_files:
  - "adyen/docs/marketplaces/webhook-types/2026-09-15.md"
tags: [adyen, marketplaces, platforms, webhooks, transfers, balances]
---

## Overview

This 2026-09-15-captured [[adyen]] Marketplace catalog maps webhook families, common envelope fields, event `type` and object-specific meanings in [[adyen-webhooks]]. It is an asynchronous event routing reference, not proof that a subscription is active, a message was delivered, funds booked, or a payout reached a bank. The Marketplace's account holders, balance accounts, users, liable account and bank counterparties remain distinct evidence objects.

## Key takeaways

- The page says webhooks may follow resource creation/update, request initiation or balance-account fund movement. The usual body has `data`, `environment` (`test`/`live`) and `type`; `data` varies by event and some types have `data.status`. Its account-holder-created JSON is a TEST example, not an actual delivered event. The opening subscription list names Configuration, Payment method, Transfer, Negative balance warning and Report; a later **Balance webhooks** section is also present. Treat the list and section as a coverage inconsistency rather than assuming Balance is unavailable. See raw lines 19–77 and 164–170.
- Configuration events include account-holder, balance-account, platform-/account-scoped managed payout schedule, managed payout **execution**, custom sweep, payment-instrument and optionally enabled risk-signal changes. Managed execution `succeeded` means a payout was **initiated** and yields a resulting `transferId`; `skipped` means conditions were unmet, while `failed` gives a reason and may recur until its cause is resolved. A custom sweep created/updated/deleted event concerns schedule configuration, not execution or bank receipt. Some managed-payout event link labels visibly contain a space after `balancePlatform.`; consult the linked schema for exact identifiers. See raw lines 79–132.
- Payment-method webhooks distinguish processed creation requests from add-request removal scheduling and actual removal; the scheduled-for-removal row says an add request will be removed in **30 days** unless missing KYC information is provided. These concern the payment-method request lifecycle, not a completed shopper payment. See raw lines 133–141.
- Transfer `balancePlatform.transfer.created` reports a request to credit/debit a balance account; `.updated` reports changed request status. The classification table distinguishes payment/capture, refund and chargeback (`category=platformPayment` with separate types), bank payout (`category=bank,type=bankTransfer,counterparty.transferInstrumentId`), internal transfer (`category=internal,type=internalTransfer,counterparty.balanceAccountId`), and third-party bank transfer (`category=bank,type=bankTransfer,counterparty.bankAccount`). These event labels must not be treated as interchangeable or as final settlement/bank receipt. See raw lines 143–162.
- Balance `balancePlatform.balanceAccount.balance.updated` reports a balance change. The negative-balance warning is for a marketplace balance account negative **more than 20 days** with a **scheduled** automatic transfer from the marketplace liable account; it does not establish that the transfer happened. Report `balancePlatform.report.created` means generated and ready to download, not that its rows were reconciled. The page explicitly deprecates Payment webhooks in favor of Transfer webhooks; legacy status examples should not be used as the current event path. See raw lines 164–199.

## Detail locators

- Trigger categories, opening subscription list, envelope and TEST example: raw lines 19–77.
- Configuration resource, managed/custom payout and risk event tables: raw lines 79–132.
- Payment-method request/removal events: raw lines 133–141.
- Transfer event types and category/type/counterparty classifications: raw lines 143–162.
- Balance, negative warning, report readiness and deprecated Payment webhook families: raw lines 164–199.
- Payout and internal-transfer scenario routes: raw lines 201–211.

## Related

- [[adyen]] — provider profile.
- [[adyen-webhooks]] — canonical asynchronous webhook concept.
- [[adyen-platforms]] — modern Marketplace balance-platform context.
- [[source-adyen-docs-platforms-webhook-types]] — separate Platforms URL and related catalog.
- [[source-adyen-docs-marketplaces-payout-webhooks]] — payout-specific transfer and bank status.
- [[source-adyen-docs-marketplaces-internal-fund-transfers-internal-transfer-webhooks]] — internal account-to-account event detail.

## Related raw API references

- The page links type-specific API Explorer webhook schemas; consult them for exact identifiers and payload fields, especially rendered managed-payout labels containing spaces.

## Raw Sources

- [[raw/adyen/docs/marketplaces/webhook-types/2026-09-15|Marketplace webhook structures and types — pinned 2026-09-15 raw snapshot]]
