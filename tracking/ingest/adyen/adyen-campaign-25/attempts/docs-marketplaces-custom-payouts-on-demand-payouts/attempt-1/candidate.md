---
title: "Adyen Marketplace on-demand payouts"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/custom-payouts/on-demand-payouts"
raw_files:
  - "adyen/docs/marketplaces/custom-payouts/on-demand-payouts/2026-09-15.md"
tags: [adyen, marketplaces, platforms, custom-payouts, bank-transfers]
---

## Overview

This 2020-modified Marketplace-path guide, captured 2026-09-15, describes triggering an off-schedule bank payout from a user's balance account to that user's verified transfer instrument through Customer Area or Transfers API `POST /transfers`. It is a modern [[adyen-platforms]] flow from [[adyen]], not a third-party bank transfer: that separate route uses Adyen business accounts and additional verification (raw lines 15–27, 46–48). Regional/method cutoff times affect expected bank arrival; this guide does not promise an arrival time.

## Key takeaways

- Prerequisites are an Adyen for Platforms integration; the Transfers API `TransferService Webservice Initiate role` for API calls or Customer Area `Initiate payouts to transfer instruments` role for that route; accepted transfer webhooks; an allowed `sendToTransferInstrument` capability; and Support enablement of transfers for the source balance account plus a default transfer description (raw lines 29–44). From LEM API v3, capability verification is per transfer instrument, independent of the legal entity's other instruments. Calculate available transfer routes before a request as recommended, because country, currency and counterparty constrain priority availability.
- The bank-category request identifies the debited source `balanceAccountId`, amount/currency, destination `counterparty.transferInstrumentId` linked to the account holder's legal entity, and transfer `priority`, which affects speed and fees (raw lines 99–112). Internal `reference`, recipient-facing `description` and `referenceForBeneficiary` serve distinct purposes; Customer Area gives beneficiary-reference maxima of 35 characters for IBAN and 15 otherwise, while description limits depend on country and priority (lines 70–74, 110–112). The Customer Area EUR 150 Instant and API EUR 600 Fast examples are illustrative and test scoped (lines 82–97, 114–141).
- HTTP 2XX with a transfer ID confirms the transfer request, not debit or bank credit (raw line 436). A list of `priorities` lets Adyen try the next available route if the earlier priority has no route; this is route selection within that request, not a retry policy for a returned or failed payout (lines 440–446, 474–538). Its sample response remains `status: received`, `reason: pending`.
- Optional `review.numberOfApprovalsRequired` currently permits `1`, and a team member must approve before Adyen continues processing (raw lines 542–550, 916–921). A future `executionDate.date` must be within 30 days in ISO YYYY-MM-DD; optional timezone uses a tz identifier with `Europe/Amsterdam` stated as default. The guide separately describes a 00:00–03:00 processing window based by default on the Balance Platform timezone (lines 925–944). A future-dated request remains `received/pending` until funds and any approval are checked; Adyen attempts processing once, and an error such as insufficient funds ends `failed` with a webhook. Before that date, a separate `/transfers/cancel` request can cancel it (lines 929–978).
- Use transfer-created/updated and transaction-created webhooks, with Customer Area, to track status and balance-account debit; `sequenceNumber` counts transfer updates and the event array retains earlier events (raw lines 980–1003). A prior bank return can block later payouts with `1063_101`; inspect return reason, do not retry final return codes, and retry only where recommended. The page's corrective route updates the user's bank details through Hosted Onboarding or LEM transfer instrument API before a new on-demand payout attempt (lines 1011–1039).

## Detail locators

- Roles, capability, Support setup, cutoff and route preparation: raw lines 19–44. Customer Area/request field definitions and versioned test SDK examples: lines 46–436.
- Priority fallback and pending response: raw lines 440–538; one-person review and versioned test examples: lines 542–921.
- Future execution, one-attempt failure, cancellation, status webhooks and returned-bank-account block: raw lines 925–1039.

## Evidence boundary

The source balance account belongs to the user's platform balance structure and the counterparty is that user's transfer instrument; it does not authorize sending to arbitrary third parties. A request ID, `received/pending` response, booked debit or illustrative instant priority does not prove the beneficiary bank received funds. The page lists a scheduled-payout `balanceAccountSweepExecution` webhook among payout updates (raw line 992); treat that route as scheduled-payout context rather than proof of this on-demand transfer. The described date/timezone defaults and role availability are dated snapshot guidance, not live configuration evidence. Keep this Transfers API flow separate from [[adyen-payouts|legacy Online Payout API]] and Classic Platforms payouts.

## Related

- [[adyen-platforms]] — current marketplace/platform integration.
- [[adyen-platform-internal-transfers]] — different balance-to-balance movement.
- [[adyen-payouts]] — separate legacy Online Payout API concept.

## Raw Sources

- [[raw/adyen/docs/marketplaces/custom-payouts/on-demand-payouts/2026-09-15|Pinned Marketplace on-demand payout guide, captured 2026-09-15]]
