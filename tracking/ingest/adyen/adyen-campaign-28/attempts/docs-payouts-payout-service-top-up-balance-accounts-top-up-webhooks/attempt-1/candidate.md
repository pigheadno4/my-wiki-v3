---
title: "Payout Service recurring top-up webhooks"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/top-up-balance-accounts/top-up-webhooks"
raw_files:
  - "adyen/docs/payouts/payout-service/top-up-balance-accounts/top-up-webhooks/2026-09-15.md"
tags: [adyen, payouts, payout-service, recurring-top-ups, webhooks, direct-debit]
---

## Overview

This Payout Service page, last modified 2020-09-11 and captured 2026-09-15, distinguishes **recurring-top-up configuration changes**, **triggered direct-debit transfer states**, and **balance-account credit**. It says Top-up API management is asynchronous: a successful API response does not itself prove the schedule was created, updated or deleted. These webhook examples are historical evidence paths, not proof of a real direct debit, balance credit or external-bank receipt. See [[adyen]] and [[adyen-payouts]] (raw lines 5–23).

## Key takeaways

- For an **enterprise payouts** integration with a server that receives/accepts webhooks, the page recommends Configuration webhooks for successful recurring schedule `created`, `updated` and `deleted`; Transfer webhooks for a direct debit's status changes; and Transaction webhooks for resulting fund movement. A configuration event proves a schedule change, not a debit or credited funds (raw lines 25–49).
- The guide identifies top-up transfer events by `category: bank` and `type: bankDirectDebit`. `balancePlatform.transfer.created` indicates initiation, while `balancePlatform.transfer.updated` tracks states including received, authorised and booked in its examples. Transfer status should be read at its own stage; initiation or authorization is not a balance-account credit (raw lines 164–434).
- The narrative calls the created event an **outgoing** direct-debit request from a balance account, and its initiated/authorised examples use `direction: outgoing`; its booked example for the same illustrated transfer changes to `direction: incoming`. This is an unresolved sample direction inconsistency, so do not derive a universal top-up money direction from those fields alone (raw lines 168, 216, 291, 380).
- A transfer can fail after initial request acceptance. The page gives `rejected` and `returned` `balancePlatform.transfer.updated` examples; their event arrays include a prior `booked` accounting event before the later negative outcome. Thus the illustrated booked state cannot be treated as irreversible top-up finality. The rejected sample's narrative says failure before finalization; the returned narrative describes funds reaching a destination bank and coming back. Those examples do not by themselves establish a particular bank's receipt or a refund/reversal in a real account (raw lines 435–702).
- `balancePlatform.transaction.created` is the page's **balance-account credit** evidence: it says transaction webhooks are sent only when transfer funds are credited, unlike a transfer webhook for each status change. Its sample has `status: booked` and balance-account/transfer IDs. This is a different evidence grain from configuration or transfer-state messages and remains subject to the page's later failure/return examples (raw lines 706–751).

## Detail locators

- Asynchronous Top-up API and three webhook families: raw lines 19–32.
- Configuration created/updated/deleted events and samples: raw lines 35–161.
- Direct-debit transfer types, received/authorised/booked samples and direction discrepancy: raw lines 164–434.
- Rejected/returned transfer examples with prior booked accounting entries: raw lines 435–702.
- Credited-funds transaction event and sample: raw lines 706–751.

## Related

- [[source-adyen-docs-payouts-payout-service-top-up-balance-accounts-manage-recurring-top-ups]]
- [[source-adyen-docs-payouts-payout-service-top-up-balance-accounts-create-recurring-top-ups]]
- [[adyen-platforms]]

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/top-up-balance-accounts/top-up-webhooks/2026-09-15|Pinned top-up webhook guide]]
