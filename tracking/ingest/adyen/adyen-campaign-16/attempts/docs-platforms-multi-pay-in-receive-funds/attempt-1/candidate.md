---
title: "Adyen Platforms multi pay-in: receive partner funds"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/multi-pay-in/receive-funds"
raw_files:
  - "adyen/docs/platforms/multi-pay-in/receive-funds/2026-09-15.md"
tags: [adyen, platforms, multi-pay-in, bank-transfer, webhooks]
---

## Overview

This 2026-09-15 Adyen for Platforms guide describes receipt of a third-party acquirer or PSP pay-in partner's payout into a multi pay-in account linked to a balance platform. Adyen says it creates and legally holds that account solely for users' benefit; funds arrive there before the platform allocates them to users' Adyen balance accounts. The page covers account setup and incoming-bank-transfer webhooks, not the later allocation request or a particular user balance booking. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- **Funding actors and gate:** Configure the multi pay-in account as the pay-in partner's payout account. Adyen allowlists the partner's bank account and says it automatically rejects transfers from other bank accounts. The third-party acquirer/PSP sends the bank transfer; the multi pay-in account is Adyen-held for users' benefit and is distinct from individual user balance accounts. The webhook examples identify a liable account holder and the multi pay-in balance account; do not read that account-holder field as proof of user allocation or legal ownership of the multi pay-in bank account.
- **Currency and reference scope:** The guide's account-format table gives EUR Netherlands/eurozone and GBP UK IBAN examples and a USD US account/routing-number example, depending on region and processing currency. Transfer examples show the partner's reference and referenceForBeneficiary; these are partner-supplied reference fields, not a guaranteed match to a later user payment or split. See the raw examples for exact fields and values.
- **Incoming evidence:** The page identifies incoming partner bank transfers in transfer webhooks with category bank, direction incoming and type bankTransfer. It describes balancePlatform.transfer.created at received, transfer.updated at authorised and booked, and balancePlatform.transaction.created when funds are credited to the multi pay-in account. The booked transfer gives a transactionId and the transaction event relates back to the transfer. These events distinguish receipt, reservation/authorisation and credit to the multi pay-in account; a received or authorised event alone is not booked credit, and even booked credit here is not user allocation, user payout or shopper payment proof. Subscribe to the desired webhooks in Customer Area.
- **Sample limits:** The USD 100 sample payloads are marked test. In the authorised transfer.updated example, the accounting event has status authorised but the outer transfer status remains received; do not treat that snippet as a reliable top-level status transition. The booked payload also carries different transactionId values at nested-event and outer-transfer positions, so do not infer a universal ID join from the sample. This page does not specify settlement timing or a retry/failure workflow beyond rejection of transfers from non-allowlisted bank accounts. Use actual event status and later allocation evidence for a particular operation.

## Detail locators

- Multi pay-in purpose, Adyen legal holding, partner payout configuration, allowlist and regional account formats: pinned raw lines 15-35.
- Webhook types, bank/incoming/bankTransfer identifiers and test USD 100 example: pinned raw lines 37-59.
- Received and authorised transfer examples, including contradictory outer status: pinned raw lines 63-202, especially 186-200.
- Booked transfer, nested/outer transaction IDs and credited transaction event: pinned raw lines 206-342, especially 281-300 and 306-340.
- Separate top-up, allocation and refund next-step routes: pinned raw lines 344-360.

## Related

- [[adyen-platforms]] — main Platforms concept and reciprocal source route.
- [[source-adyen-docs-platforms-multi-pay-in-payments]] — separate third-party payment allocation route.
- [[source-adyen-docs-platforms-multi-pay-in-top-up-multi-pay-in]] — separate internal liable-account top-up route.
- [[source-adyen-docs-platforms-multi-pay-in-refunds]] — separate partner-payment refund route.

## Raw Sources

- [[raw/adyen/docs/platforms/multi-pay-in/receive-funds/2026-09-15|Adyen Receive funds, captured 2026-09-15]]
