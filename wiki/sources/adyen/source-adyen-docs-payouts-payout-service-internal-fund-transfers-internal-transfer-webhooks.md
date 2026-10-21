---
title: "Adyen Payout Service: Internal transfer webhooks"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/internal-fund-transfers/internal-transfer-webhooks"
raw_files:
  - "adyen/docs/payouts/payout-service/internal-fund-transfers/internal-transfer-webhooks/2026-09-15.md"
tags: [adyen, payouts, payout-service, platforms, internal-transfers, webhooks]
---

## Overview

This 2026-09-15 **Payout Service-path** guide describes Transfer webhooks for moving funds internally between balance accounts in a platform. The source account produces an outgoing leg and the target account an incoming leg, with received, authorised and booked states. It also shows a return as a modification of the original transfer. Its subject is balance-account movement, not the legacy Online Payouts Payout API or an external bank payout. See [[adyen]] and [[adyen-platform-internal-transfers]].

## Key takeaways

- **Two legs and prerequisites:** The platform server must receive/accept webhooks and subscribe to **Transfer webhooks** in the TEST Customer Area. `balancePlatform.transfer.created` announces initiation; `balancePlatform.transfer.updated` reports status changes. For each event, source/outgoing and target/incoming balance accounts get separate webhook sets. Identify these as `category: internal`, `type: internalTransfer`, with direction relative to the account (raw lines 19–50).
- **Stage evidence:** Scheduled or on-demand transfer initiation yields `received` on both legs; authorised updates indicate reservation on both sides, with negative source and positive target reserved amounts; booked updates report a source debit and target credit, including counterparty balance-account IDs and transaction IDs in the samples. A received or authorised webhook is not booked movement. The TEST request is `POST /btl/v4/transfers` with source `balanceAccountId`, target `counterparty.balanceAccountId`, `category: internal`, EUR amount and references; language SDK versions and optional idempotency examples are in raw (raw lines 52–367, 371–881).
- **Return is a nested modification:** The page links a separate return operation and illustrates a return request with amount and reference. Its return `transfer.updated` messages carry the original transfer's data plus an `events[].modification` with `type: return`, direction, reference and received/authorised/booked status. At booked return, it describes one update for each account; the account that had received the original funds becomes outgoing, and the original sender receives incoming funds. In the return examples, top-level transfer `status: booked` persists through earlier nested return stages, so read the modification status rather than treating the parent status as a new return outcome (raw lines 883–1455).
- **TEST sample discrepancies:** The request payload uses EUR minor-unit value `10000`, while the illustrated transfer webhooks use `1000`. The returned-transfer examples also change incoming-leg IDs versus the preceding transfer samples, and some sample JSON has missing commas. They do not form one reconcilable live ledger; use event/account/transaction identifiers from the actual operation. This guide shows no external bank transfer or beneficiary receipt (raw lines 58–76, 382–509, 685–881, 905–1455).

## Detail locators

- Transfer-webhook subscription, account leg direction and stage taxonomy: pinned raw lines 19–50.
- TEST Transfers API v4 and language SDK request examples: pinned raw lines 52–367.
- Source/target received updates: pinned raw lines 371–509.
- Source/target authorised reservations: pinned raw lines 511–677.
- Source/target booked debit/credit and transaction IDs: pinned raw lines 679–881.
- Return request and nested modification received/authorised/booked events: pinned raw lines 883–1455.

## Related

- [[adyen-platform-internal-transfers]] — main internal balance-account transfer concept.
- [[adyen-platforms]] — parent platform/account model.
- [[source-adyen-docs-platforms-internal-fund-transfers-internal-transfer-webhooks]] — parallel Platforms-path guide with a deprecated Payment-webhooks link absent here.
- [[source-adyen-docs-marketplaces-internal-fund-transfers-internal-transfer-webhooks]] — parallel Marketplace-path guide.
- [[adyen-webhooks]] — general asynchronous event handling.

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/internal-fund-transfers/internal-transfer-webhooks/2026-09-15|Payout Service internal transfer webhooks, captured 2026-09-15]]
