---
title: "Adyen Marketplaces: Payout transfer webhooks"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/payout-webhooks"
raw_files:
  - "adyen/docs/marketplaces/payout-webhooks/2026-09-15.md"
tags: [adyen, marketplaces, platforms, payouts, transfer-webhooks]
---

## Overview

This 2023-modified, 2026-09-15-captured [[adyen]] Marketplaces guide describes Transfer webhook events for an outgoing bank payout from a user's balance account toward a counterparty bank account. It covers the transfer request, balance-account reservation/debit, bank tracking, failure, credit confirmation and return. It is webhook guidance and test illustration, not proof that a particular transfer reached a beneficiary bank. [[adyen-platforms]]

## Key takeaways

- The page lists a **payout service integration**, a server that receives and accepts webhooks, and Customer Area subscriptions to **Transfer and Transaction webhooks**. Identify payout Transfer webhooks by `category=bank`, `direction=outgoing`, `type=bankTransfer`. `balancePlatform.transfer.created` announces an initiated outgoing request; `balancePlatform.transfer.updated` reports later status changes. Created payload fields include amount, reference, beneficiary reference, user's source balance account, holder and counterparty transfer instrument. See [[raw/adyen/docs/marketplaces/payout-webhooks/2026-09-15|raw lines 19–69]].
- `authorised` means the amount is **reserved** on the user's balance account. If funds are insufficient, the guide says the transfer is `refused` with `reason=notEnoughBalance`; it does not complete, and a **new transfer request** is needed after adding funds. `booked` means funds have been **deducted** from the source balance account and carries an accounting `events.transactionId`. Booked is explicitly **not final**: an instant payout may fail after bank rejection, and a regular/wire payout may be returned. See [[raw/adyen/docs/marketplaces/payout-webhooks/2026-09-15|raw lines 138–232, 325–334]].
- After booking, an internal review can appear as `trackingData.status=pending` with `type=internalReview` even while top-level transfer status remains `booked` in the example. Failed review carries `reason=refusedForRegulatoryReasons` in the tracking event; the guide directs users to Support. For a passed review, it describes instant-priority tracking `credited` confirmation or an `estimatedArrivalTime` for other priorities; the estimate can deviate from actual arrival and is described as available for local, not instant or cross-border payouts. See [[raw/adyen/docs/marketplaces/payout-webhooks/2026-09-15|raw lines 434–706, 830–836, 1111–1226]].
- `tracing` events carry network-specific IDs for investigating delayed or missing funds (UK GBP FPS `fpid`, US USD ACH `traceNumber`). An external-bank rejection after unsuccessful automatic retries can produce transfer `failed`; a later bank return yields `returned`. Return payloads can include `networkReason` with code, description and namespace. Tracing and estimated arrival are investigation aids, not bank-receipt confirmation. See [[raw/adyen/docs/marketplaces/payout-webhooks/2026-09-15|raw lines 706–830, 950–974, 1227–1372]].
- Some return reasons are temporary, while permanent account issues can cause Adyen to block later requests to that bank account with HTTP **422**. The source's reason table offers code-specific remedial actions, including retry suggestions for some account-detail codes, but it does **not** map each listed code to temporary/permanent status or override the stated blocked-instrument rule. Check the actual reason and account state before any new request. See [[raw/adyen/docs/marketplaces/payout-webhooks/2026-09-15|raw lines 1349–1355, 1532–1547]].

## Identity and example boundary

The worked sections use a **EUR 100.00** third-party-bank payout as illustration. Distinguish transfer `data.id`, individual `events[].id`, accounting `events.transactionId`, merchant `reference`, beneficiary `referenceForBeneficiary`, and network tracing IDs. The failed-review sample changes the amount to EUR 10.00 and shows `categoryData.type=bank` versus the common `bankTransfer`, so the examples are not a single guaranteed event trace. A top-level `reason=approved` in a sample does not negate a later tracking failure or returned status. See [[raw/adyen/docs/marketplaces/payout-webhooks/2026-09-15|raw lines 58, 579–706, 1227–1530]].

## Detail locators

- Event prerequisites and payout identification; request creation and source/counterparty fields: [[raw/adyen/docs/marketplaces/payout-webhooks/2026-09-15|raw lines 15–138]].
- Reservation, refusal, booking, internal review and bank-failure states: [[raw/adyen/docs/marketplaces/payout-webhooks/2026-09-15|raw lines 138–830]].
- ETA limits, UK/US tracing, instant confirmation, bank return and 422 block: [[raw/adyen/docs/marketplaces/payout-webhooks/2026-09-15|raw lines 830–1547]].

## Related

- [[adyen-platforms]] — modern Platforms and Marketplace balance-account/payout route.
- [[source-adyen-docs-platforms-payout-webhooks]] — related Platforms-path guide; keep paths and examples distinct.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/marketplaces/payout-webhooks/2026-09-15|Marketplace payout transfer webhooks (captured 2026-09-15)]]
