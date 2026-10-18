---
title: "Adyen Business Accounts third-party transfer webhooks"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/third-party-transfer-webhooks"
raw_files:
  - "adyen/docs/business-accounts/third-party-transfer-webhooks/2026-09-15.md"
tags: [adyen, business-accounts, bank-transfers, direct-debit, webhooks]
---

## Overview

This 2026-09-15 Adyen Business Accounts guide illustrates Transfer webhooks for a user's business account and its associated balance account when a third-party bank account sends funds, initiates a direct debit request, or receives an outgoing bank transfer. `balancePlatform.transfer.created` reports a request; `balancePlatform.transfer.updated` reports later changes. The document's test payloads illustrate states and fields, not a specific live transfer or beneficiary-bank receipt. See [[adyen]], [[adyen-business-accounts]] and [[source-adyen-docs-platforms-payout-webhooks]].

## Key takeaways

- The stated preparation is a payout service integration, a server able to receive and accept webhooks, and subscriptions to both Transfer and Transaction webhooks. The latter is a separate webhook family; this page's examples are Transfer webhooks.
- Identify these bank events by `category: bank`, `type: bankTransfer` or `bankDirectDebit`, and `direction` relative to the balance account. An incoming direct debit request is an incoming request that debits the user's associated balance account; incoming funds credit it. Outgoing bank transfers debit it.
- The illustrated accounting progression is received → authorised (reserved) → booked. Outgoing `booked` means the user's balance account was debited, not that the beneficiary bank credited the recipient; external rejection can subsequently produce `failed` or `returned`. Insufficient balance instead produces `refused` with `notEnoughBalance` and requires a new transfer request after funding.
- Keep transfer `status`, nested accounting `events`, and `tracking` separate. An internal-review example retains top-level `status: booked` while `tracking.status` is `pending` or `failed` (`refusedForRegulatoryReasons`). The instant-priority credited example likewise retains top-level `booked` and uses `tracking.status: credited`. A tracing event carries network identifiers, not proof that funds reached the beneficiary bank.
- `estimatedArrivalTime` is an estimate that can differ from actual arrival. The snapshot describes it for local payouts with regular, fast, or wire priority, excluding instant and cross-border payouts. Return reasons can be temporary or permanent; a permanent blocked transfer instrument causes subsequent requests to fail with 422. The reason-code table also recommends retrying for some blocked/closed-account codes, so do not treat its generic retry wording as overriding the permanent-block warning.

## Detail locators

- Requirements and classification: raw lines 30–50.
- Incoming funds and direct debit request examples: “Receiving funds” (lines 54–379) and “Receiving direct debit requests” (lines 380–746). The direct debit samples contain trailing commas, so treat them as illustrative payloads rather than valid JSON fixtures.
- Outgoing request, state and failure examples: “Sending funds” (lines 747–2700), especially refused (1430), booked (1534), pending/internal review (1657–1967), failed (1970), ETA (2115), tracing (2262), credited (2425), and returned (2558).
- Return blocking, network reasons and reason-code table: lines 2699–2898. The page's prose for incoming booked `counterparty` says the user's business account, while its example shows the third-party sender's bank account (lines 261–315); verify payload identity against the actual event rather than assuming that prose label describes the example.

## Related

- [[adyen-business-accounts]] — product and resource context.
- [[source-adyen-docs-platforms-payout-webhooks]] — related platform payout Transfer webhook states.

## Raw Sources

- [[raw/adyen/docs/business-accounts/third-party-transfer-webhooks/2026-09-15|Adyen Docs: Third-party transfer webhooks (2026-09-15 snapshot)]]
