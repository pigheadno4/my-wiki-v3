---
title: "Adyen Business Accounts: Send funds to third parties"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/send-funds"
raw_files:
  - "adyen/docs/business-accounts/send-funds/2026-09-15.md"
tags: [adyen, business-accounts, bank-transfers, third-party-payments]
---

## Overview

This 2022-modified guide, captured 2026-09-15, describes sending business-related funds from a user's Adyen business account to a third-party bank account, such as a supplier's account. It expressly distinguishes the recipient account from a transfer instrument connected to the user's legal entity: the third party owns that account. The user's business account is debited, the business account number is shown on the recipient's statement, and Adyen describes outgoing bank-transfer webhooks to the platform server. These are documented flow descriptions, not proof of a particular transfer's booking or beneficiary receipt.

## Key takeaways

- Transfer priority depends on currency, account region and destination. The captured guide describes Regular, Instant, Fast, Wire, Cross-border and Internal options. Higher priority may incur higher fees; cross-border transfers may face intermediary-bank delays and charges that reduce the beneficiary's received amount. Its introductory priority sentence incorrectly says funds arrive to the user's account, although the surrounding page describes outgoing transfers to third parties (raw lines 19–43).
- The USD/EUR/GBP account-region matrices, cut-off/settlement/amount table, and destination-bank format/description tables are historical reference data, not current availability or receipt guarantees. Cut-off prose says transfers initiated after a cut-off are processed the next day within the specified settlement delay, but the examples and table disagree in places: the SEPA wire example uses 16:30 CET while the table lists 16:55 CET, and the US example alternates next-day framing with same-day receipt. Do not select a cut-off from those conflicting passages as authoritative for a live transfer.
- The request needs `accountIdentification.type`, chosen from destination bank location and transfer currency, with type-specific bank details. The guide says cross-border transfers must be sent as wire transfers and include the bank-account owner's address, while its priority list/table separately label `Cross-border`/`crossBorder`; consult the current transfer API and Adyen for the applicable request priority rather than collapsing these labels. The detailed table distinguishes required IBAN versus optional IBAN and `numberAndBic` cases.
- The page says collection from third-party bank accounts by direct debit was being worked on, so its statement is not evidence that this receiving flow was available in the captured snapshot. The page ends with navigation to webhook and transaction-query guides; their contents are not evidence here.

## Detail locators

- Opening — outbound third-party ownership, debit, recipient-statement number, webhook reference, and planned direct debit (raw lines 15–23).
- `Supported currencies, locations, and priorities` — priority descriptions and cross-border intermediary-bank warning (raw lines 25–43); USD/EUR/GBP source-account matrices (lines 45–76).
- `Transfer cut-off times` — general timing explanation, contradictory SEPA/US examples, and country/currency/priority cut-off, delay and amount table (raw lines 78–145).
- `Bank account identification types and supported priorities` — request selector and cross-border address/wire wording (raw lines 147–162).
- `Supported countries, currencies, and priorities` — destination currency, priority, description-character and account-format tables, including cross-border identification variants (raw lines 164–205).
- `Next steps` — navigation to outgoing-transfer webhooks and bank-transaction queries (raw lines 207–219).

## Related

- Company: [[adyen]]
- Main concept: [[adyen-business-accounts]]
- Platform context: [[adyen-platforms]]

## Raw Sources

- [[raw/adyen/docs/business-accounts/send-funds/2026-09-15|2026-09-15 Business Accounts send-funds guide]]
