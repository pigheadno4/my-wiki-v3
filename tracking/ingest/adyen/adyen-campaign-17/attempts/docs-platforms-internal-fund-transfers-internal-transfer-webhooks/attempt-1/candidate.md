---
title: "Webhooks for Adyen for Platforms internal fund transfers | Adyen Docs"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/internal-fund-transfers/internal-transfer-webhooks"
raw_files:
  - "adyen/docs/platforms/internal-fund-transfers/internal-transfer-webhooks/2026-09-15.md"
tags: [adyen, platforms, internal-transfers, transfer-webhooks, balance-accounts]
---

## Overview

This Adyen for Platforms guide describes Transfer webhooks for internal movement between two balance accounts in a platform. A subscribed server receives `balancePlatform.transfer.created` at initiation and `balancePlatform.transfer.updated` as the transfer is authorised and booked, with an outgoing source-account view and incoming target-account view for each stage. It also illustrates return modifications. The snapshot was fetched 2026-09-15 and its metadata says last modified that day; test-environment examples are not evidence of an actual transfer, user-bank payout, or beneficiary-bank receipt. [[adyen]] [[adyen-platforms]] [[adyen-platform-internal-transfers]]

## Key takeaways

- **Scope and prerequisites:** Internal-transfer webhooks use `category: internal` and `type: internalTransfer`; `direction` is outgoing for the source balance account and incoming for the target. The server must receive and accept webhooks, and the platform must subscribe to Transfer webhooks in the test Customer Area in the documented setup. A separate legacy payment-webhook route is explicitly labeled deprecated. The example initiates a Transfers API v4 test request between two balance-account IDs; its SDK snippets have distinct library versions and do not establish current roles, live eligibility or success.
- **Three transfer stages:** On initiation, `balancePlatform.transfer.created` has `status: received` and the sample `balances.received` movement is negative on the outgoing leg and positive on the incoming leg. `balancePlatform.transfer.updated` with `status: authorised` means the amount is reserved, with negative `balances.reserved` on the source and positive on the target. A later `updated` with `status: booked` describes the internal push from source to target; the sample `balances.balance` is negative on source and positive on target, with booked accounting events and leg-specific `transactionId` values. Received and authorised are not booked movement.
- **Identifiers and correlation:** Each side's example has its own top-level `data.id` and event IDs, and the booked outgoing and incoming legs carry different transaction IDs. `balanceAccountId`, `direction` and `counterparty.balanceAccountId` identify the account and the opposite account in each view; `reference` and `referenceForBeneficiary` carry the illustrative request references. Do not assume a single transfer ID or transaction ID is shared across the two legs, and do not derive a universal reconciliation join from sample values.
- **Return is a modification:** The return-request example is followed by `balancePlatform.transfer.updated` events whose nested `events[].modification` has `type: return`, its own `received`, `authorised` and `booked` stages, direction and return reference. The top-level transfer can remain `status: booked` for the original movement while the return modification is only received or authorised. The guide says booked return webhooks arrive for both involved balance accounts; this is an internal reversal to the original source balance account, not an external bank refund or payout. The page does not describe failure, rejection, cancellation or retry handling for these flows.
- **Example cautions:** The example request uses `amount.value: 10000`, while its transfer webhooks show `amount.value: 1000`; treat those amounts as inconsistent illustrations, not a tested request/response pair. Some displayed JSON lacks commas, the outgoing booked example spells `valuDate` differently from the incoming `valueDate`, and a return `modification.id` differs from the surrounding `data.id` in one booked payload. Use the current webhook schema and observed account IDs/events for implementation; this snapshot does not define a safe cross-leg ID invariant from those examples.

## Detail locators

- Webhook types, two account views, subscription and category/type/direction selectors: pinned raw lines 19–54.
- Test Transfers API request and versioned SDK examples: pinned raw lines 56–369; request amount versus later webhook amount conflict at lines 68–70 and 398–400.
- Received outgoing/incoming events, signs and separate `data.id` values: pinned raw lines 375–511.
- Authorised reservations, source/target signs and cumulative accounting events: pinned raw lines 515–679.
- Booked account movements, counterparties, transaction IDs and malformed/typo sample fields: pinned raw lines 683–885.
- Return request and modification received/authorised stages with unchanged top-level booked status: pinned raw lines 887–1170.
- Booked return on both accounts and sample ID inconsistency: pinned raw lines 1174–1459.

## Related

- [[adyen-platform-internal-transfers]] — canonical internal-versus-external transfer concept.
- [[adyen-platforms]] — platform account context.
- [[source-adyen-docs-platforms-internal-fund-transfers]] — overview of internal transfer relationships and process routes.

## Raw Sources

- [[raw/adyen/docs/platforms/internal-fund-transfers/internal-transfer-webhooks/2026-09-15|Internal-transfer webhooks — 2026-09-15 snapshot]]
