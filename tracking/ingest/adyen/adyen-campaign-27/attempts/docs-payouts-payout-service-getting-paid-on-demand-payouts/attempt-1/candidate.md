---
title: "Adyen Payout Service on-demand bank payouts"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/getting-paid/on-demand-payouts"
raw_files:
  - "adyen/docs/payouts/payout-service/getting-paid/on-demand-payouts/2026-09-15.md"
tags: [adyen, payout-service, balance-platform, on-demand-payouts, transfers]
---

## Overview

This 2020-modified guide, captured 2026-09-15, describes **Payout Service** on-demand payouts outside a regular schedule: funds move from a balance-platform source balance account toward an account holder's linked transfer instrument, such as a verified bank payout account. A platform can create a request in Customer Area or use Transfers API `POST /transfers`. This is a modern balance-platform bank-transfer path, distinct from the legacy Online Payout API and from an internal balance-account transfer. Request creation or HTTP acceptance does not prove source booking or beneficiary-bank receipt. [[adyen]] [[adyen-financial-products]]

## Key takeaways

- The stated integration prerequisite is an Adyen balance platform. For the Customer Area route, the requirements table lists **Configure scheduled payouts** and **Initiate payouts to transfer instruments** roles, although its label says “manage sweep configurations”; do not infer the same human UI roles are an API credential contract. Configure a webhook-receiving server, contact Support to configure a default transfer description, and consider regional bank cutoffs. Calculating available transfer routes before submission is a **recommendation** to reduce delay/failure risk, not listed as a required request field. See raw lines 17-36.
- Customer Area selection names the source balance account, counterparty type `transferInstrument`, destination transfer-instrument ID, currency, amount and priority. The API field table marks `amount`, `balanceAccountId`, `category: bank`, `counterparty.transferInstrumentId` and `priority` required. The destination instrument must be linked to the account holder's legal entity. Priority affects speed **and fees**; optional `reference` stays internal, while `referenceForBeneficiary` is sent to the recipient and transfer webhooks. Description/beneficiary reference limits depend on bank geography, instrument and priority. See raw lines 40-66 and 87-100.
- Customer Area confirmation creates a **payout request**; its Transfers tab is then used to check whether the transfer was booked. The API describes an HTTP 2XX response with a transfer request `id`, not bank credit. The EUR 150 “Instant” Customer Area example and `amount.value: 60000`, EUR, `fast` TEST API v4 example are separate illustrations, not evidence of an instant arrival or a single reconciled transfer. See raw lines 64-85, 106-126 and 424.
- An optional API `review` can request **one** additional approval with `review.numberOfApprovalsRequired: 1`; a team member must approve before Adyen continues processing. HTTP 2XX after requesting review does not show that the review occurred or funds moved. See raw lines 428-436 and 801-807.
- Track the request through Customer Area or `balancePlatform.transfer.created`/`updated` status events and `balancePlatform.transaction.created` for a balance-account deduction; acknowledge webhooks. These are distinct event grains, and a source debit is not beneficiary-bank receipt. See raw lines 809-831.
- The sample 422/`1063_101` block follows one or more prior bank returns. The page distinguishes retryable **temporary** return reasons from **permanent/final** reasons; it expressly says **do not retry** a final status and only retry where the return code recommends retry. Its later “fix” bullets say contact Adyen to update bank details then make a new transfer request; read that step under the prior return-reason restriction, not as blanket retry permission. See raw lines 833-867.

## Detail locators

- Opening and `## Requirements`, raw lines 15-32: product path, UI roles, webhooks, default description, regional cutoff and recommended route check.
- `## 1. Make a transfer request`, raw lines 34-424: Customer Area and Transfers API routes, source/destination identities, required and optional fields, TEST/versioned examples and acceptance.
- `### Trigger additional reviews`, raw lines 428-807: single optional approval, request examples and approval gate.
- `## 2. Track the status of the transfer`, raw lines 809-831: Customer Area and Transfer/Transaction webhook tracking.
- `## Troubleshooting`, raw lines 833-867: prior-return block, temporary versus final reason and conditional retry.

## Related

- [[adyen-financial-products]] — modern product-family context for payouts.
- [[adyen-platforms]] — balance-platform model; this guide is under the Payout Service path.
- [[adyen-payouts]] — legacy Online Payout API concept, distinct from this Transfers API flow.

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/getting-paid/on-demand-payouts/2026-09-15|Adyen Payout Service on-demand payouts guide, captured 2026-09-15]]
