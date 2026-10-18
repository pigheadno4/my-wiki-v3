---
title: "Adyen Platforms payout transfer webhooks"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/payout-webhooks"
raw_files:
  - "adyen/docs/platforms/payout-webhooks/2026-09-15.md"
tags: [adyen, platforms, payouts, transfer-webhooks, bank-transfers]
---

## Overview

This 2026-09-15 Adyen for Platforms guide describes Transfer webhook events for an outgoing bank payout from a user's balance account to a bank account. It covers the transfer's request, balance-account, bank-tracking, failure and return states. This is the balance-platform transfer route, separate from the legacy Online payouts/Payout API webhook path. It is webhook guidance, not evidence that a particular payout was accepted by a beneficiary bank or received by its customer. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- **Subscribe and identify the payout:** The page lists a payout service integration and a server that receives/accepts webhooks, subscribed in Customer Area to both Transfer and Transaction webhooks. For payout-related Transfer webhooks, it identifies `category=bank`, `direction=outgoing`, and `type=bankTransfer`. `balancePlatform.transfer.created` reports creation of an outgoing request; `balancePlatform.transfer.updated` reports later changes. The created event contains amount, reference, beneficiary reference, source user balance account, linked account holder and counterparty transfer instrument. Do not equate a created request with a bank payout.
- **Separate balance and bank states:** `authorised` means the amount has been reserved on the user's balance account. Insufficient balance instead yields `refused` with `reason=notEnoughBalance`; the page says that request does not complete and calls for adding funds and sending a new transfer request. `booked` means the amount was deducted from the user's balance account and includes an accounting `events.transactionId`. The page explicitly says booked is not final: an instant transfer may later fail after bank rejection, while a regular or wire transfer may be returned. Do not interpret reserved or booked balance-account funds as beneficiary-bank receipt.
- **Review and bank progress:** After booking, a transfer may enter `trackingData.status=pending` with `type=internalReview`; failure of that review has `reason=refusedForRegulatoryReasons` and tracking `status=failed`, for which the guide says to contact Support. Passing review can lead to instant-payout `tracking.status=credited` confirmation or, for other priorities, a tracking `estimatedArrivalTime`. The estimate may differ from actual arrival and the snapshot says it is available for local payouts, not instant or cross-border payouts. A later `tracing` event carries network-specific identifiers, such as UK FPS `fpid` or US ACH `traceNumber`, useful for bank investigations. A tracing identifier or arrival estimate is not itself a receipt.
- **Failure and return consequences:** An external-bank rejection after unsuccessful automatic retries can produce transfer `status=failed`; a counterparty-bank return produces `status=returned`, both with a `reason` and `transactionId` in the guide's webhook description. Return `networkReason` can carry a network code, description and namespace, mapped to Adyen's reason. Some return reasons are temporary; permanent issues can block the transfer instrument so new requests to that bank account fail with HTTP 422. The raw reason table suggests different remediation by code. A retry is a new transfer decision after diagnosing reason and bank details, not a continuation of a completed payout.
- **Identity and example limits:** Distinguish top-level transfer `data.id`, `events[].id`, accounting `events.transactionId`, merchant `reference`, `referenceForBeneficiary`, and tracing identifiers; they serve different purposes. The many test JSON examples reuse placeholder IDs across sections, and the failed-review sample changes the amount and `categoryData.type` compared with the common EUR 100 example. Treat each sample as illustration rather than a canonical event join, universal sequence or account-specific proof. No bank statement, actual user receipt, legal ownership or current route eligibility follows from this snapshot.

## Detail locators

- Purpose, created/updated webhook types, prerequisites and `bank/outgoing/bankTransfer` identifiers: raw lines 15–60. Created event fields and test sample: lines 62–138. Authorised reservation and insufficient-balance refusal/new request: lines 140–232.
- Booked deduction, accounting transaction ID and explicit nonfinal warning: lines 327–434. Internal-review pending/passed/failed and priority-specific tracking: lines 436–706. External failure after retries: lines 708–830.
- Estimated arrival, availability limits and sample: lines 832–950. Tracing networks/identifiers and sample: lines 952–1111. Instant credited confirmation: lines 1113–1227. Bank return, permanent block, network reason and code-specific remediation: lines 1229–1550. Related payout routes: lines 1551–1555.

## Related

- [[adyen]] — provider context.
- [[adyen-platforms]] — platform balance-account, user and transfer context.
- [[source-adyen-docs-online-payments-online-payouts-payout-webhook]] — separate legacy Payout API webhook route; its event semantics must not be imported into this balance-platform transfer flow.

## Related raw API references

- The raw page links to the Transfer webhook API event definitions, transfer request schema, Customer Area webhook setup, scheduled/on-demand payouts and transfer routes. Consult them independently for current endpoint and route details.

## Raw Sources

- [[raw/adyen/docs/platforms/payout-webhooks/2026-09-15|Adyen Docs: Payout transfer webhooks (2026-09-15 snapshot)]]
