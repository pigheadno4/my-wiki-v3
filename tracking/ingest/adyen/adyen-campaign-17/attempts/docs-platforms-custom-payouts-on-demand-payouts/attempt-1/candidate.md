---
title: "Adyen for Platforms on-demand payouts"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/custom-payouts/on-demand-payouts"
raw_files:
  - "adyen/docs/platforms/custom-payouts/on-demand-payouts/2026-09-15.md"
tags: [adyen, platforms, custom-payouts, transfers-api, bank-transfers]
---

## Overview

This Adyen for Platforms guide explains an off-schedule payout from a user's source balance account to that user's verified bank-account transfer instrument, initiated in Customer Area or with Transfers API `POST /transfers`. It concerns a bank-category payout to the user's own instrument. The opening separately routes third-party bank transfers through Adyen business accounts and additional verification. A created, accepted, authorized or booked transfer in this guide is not proof that the beneficiary bank credited the account. [[adyen]] [[adyen-platforms]]

## Key takeaways

- **Prerequisites and identities:** the guide requires Adyen for Platforms, a Transfers API credential with `TransferService Webservice Initiate role` for API use, the Customer Area `Initiate payouts to transfer instruments` role for that route, accepted Transfer webhooks, and the user's allowed `sendToTransferInstrument` capability. From LEM API v3 the capability is verified per transfer instrument. Support must enable transfers for the source balance account and configure the platform's default transfer description. The target instrument must be linked to the account holder's legal entity.
- **Request shape and route:** choose a source `balanceAccountId`, amount with currency, `category: bank`, target `counterparty.transferInstrumentId`, and transfer priority. The priority affects speed and fees; supported routes and regional cutoff times affect expected arrival. The page recommends calculating available routes first. Internal `reference`, bank-facing `description`, and `referenceForBeneficiary` serve distinct purposes. Character limits and statement visibility vary by counterparty location, currency and priority; inspect the raw tables before constructing a description.
- **Stages and evidence:** Adyen checks capability and its reviews, with optional platform-team review, then authorizes and books the transfer. Booking deducts the user's balance account and sends funds to the transfer instrument. HTTP 2XX with a transfer ID confirms request creation, while the sample fallback response still has `status: received` and `reason: pending`. Transfer-created/updated and transaction-created webhooks, plus Customer Area, carry later status and debit evidence. Neither those stages nor the illustrative samples prove beneficiary-bank receipt.
- **Priority fallback and approval:** a `priorities` list lets Adyen try the first route and automatically try the next available priority if unavailable; this is fallback within the request, not a general instruction to resubmit. An optional `review.numberOfApprovalsRequired` currently permits only `1`; a team member must approve before processing. Failed required reviews fail the payout.
- **Future date and failure:** `executionDate.date` must be within 30 days and ISO `YYYY-MM-DD`; the optional timezone uses a tz identifier, with `Europe/Amsterdam` stated as its default. The page says a future-dated payout stays `received/pending` until execution, when funds and any team approval are checked. Adyen attempts processing once; insufficient funds or another error leaves it `failed` and produces a webhook. Cancellation is routed to a separate guide before execution. The described 00:00–03:00 processing window depends on the Balance Platform timezone by default.
- **Returned-bank-account warning:** a previous bank return can block later transfers with error `1063_101`. Some return reasons are temporary while others are final; read the webhook return reason and do not retry a final one. The guide proposes updating bank details and then using the on-demand process again for this block. That guidance is conditional, not a blanket retry for a pending or failed payout.
- **Snapshot/sample limits:** the curl/SDK samples target the test environment and cite different library versions; the Customer Area EUR 150 Instant example differs from the EUR 600 Fast API samples. The Customer Area text gives beneficiary-reference maxima of 35 characters for IBAN or 15 otherwise, whereas later currency/priority tables list an 80-character accepted maximum for many routes and separate statement visibility; consult the applicable current route/schema before use. No sample establishes live eligibility or bank receipt.

## Detail locators

- Raw lines 15–44: on-demand scope, third-party business-account distinction, cutoff, roles, capability, Support setup and route recommendation.
- Raw lines 46–71: request, capability, review, authorization, booking and webhook stages.
- Raw lines 73–139: Customer Area and API fields, source/target identities, references and visible limit conflict; lines 141–463 hold versioned test examples and HTTP response boundary.
- Raw lines 467–565: priority-list fallback and illustrative `received/pending` response.
- Raw lines 569–948: optional one-person additional review and versioned test examples.
- Raw lines 952–1005: future execution date, timezone, one processing attempt, failure and cancellation route.
- Raw lines 1007–1066: transfer/transaction status events and returned-bank-account block/retry qualifications.
- Raw lines 1068–1245: country, currency and priority-specific description/reference character acceptance and statement visibility, including zero-visibility cases.

## Related

- [[source-adyen-docs-platforms-manage-transfer-instruments]] — user's bank-account instrument and verification context.
- [[source-adyen-docs-platforms-verification-overview-capabilities]] — capability status context.
- [[adyen-payouts]] — legacy Online Payout API concept; this page uses Transfers API.

## Raw Sources

- [[raw/adyen/docs/platforms/custom-payouts/on-demand-payouts/2026-09-15|On-demand payouts snapshot, fetched 2026-09-15]]
