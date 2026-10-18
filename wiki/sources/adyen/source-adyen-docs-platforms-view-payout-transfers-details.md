---
title: "Adyen Platforms: view payout transfer details"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/view-payout-transfers-details"
raw_files:
  - "adyen/docs/platforms/view-payout-transfers-details/2026-09-15.md"
tags: [adyen, platforms, payouts, transfers, customer-area, reporting]
---

## Overview

This 2026-09-15 Adyen for Platforms guide shows how to inspect transfer records through Customer Area or the Transfers API, with webhooks recommended for recurring payout monitoring. It covers listing/searching transfers, retrieving one transfer, and downloading a bank transfer confirmation letter. A transfer record can represent a bank payout or another balance-platform transfer; the page's list example includes a bank transfer and an internal transfer. These viewing routes do not by themselves prove that a beneficiary bank credited the recipient. See [[adyen]], [[adyen-platforms]] and [[source-adyen-docs-platforms-payout-webhooks]].

## Key takeaways

- **Access and scope:** The page requires an Adyen for Platforms integration. Transfers API retrieval requires the **TransferService Webservice Retrieve role**. Customer Area viewing requires **Balance platform base role**; downloading a letter needs **Download transfer confirmation letter**, and unmasked PII in that letter also needs **View bank transfers PII**. Without the latter role, PII is masked. A role listed here is not evidence that a particular operator has it.
- **List transfers:** In Customer Area, use **Balances > Transfers** and a **Balance platform** filter; the UI shows one balance platform at a time. Date, status and reference filters support investigation, including a bank-transfer/failed view for rejected payouts. Transfers API `GET /transfers` offers date and account/balance filters, pagination via `_links`, and the guide says to provide at least one unique identifier. Its table says `createdSince` and `createdUntil` must be less than six months apart. The surrounding example prose spans May 2025 to May 2026, while the curl sample spans May 12–13, 2026 and shows no account identifier; do not treat that example as resolving the stated date-window and identifier requirements. Consult the API schema for an executable request.
- **Inspect one transfer:** Search Customer Area by transfer ID or description and select an ID, or call `GET /transfers/{id}`. The guide highlights amount/currency, direction, event history, internal reference and current `status` (for example `received`, `authorised`, `booked`). The list response includes both a bank-transfer record and an internal-transfer record, while the detailed `GET /transfers/{id}` example has `category=internal` and `type=internalTransfer`; it does not establish bank-payout status or a canonical join across examples. Balance-account booking is a different event from beneficiary-bank receipt.
- **Confirmation letter boundary:** For a booked bank transfer, a permitted Customer Area user can download a PDF listing available transfer and beneficiary details, potentially including ACH/FPS tracing identifiers. The letter confirms that Adyen sent the instruction to carry out the transfer. It is evidence of the instruction, not a bank acknowledgement or proof that funds arrived. The page's role and mask conditions apply to sharing it.
- **Version and environment:** The curl examples target test Balance Platform Transfers API v4. SDK examples are versioned (Java 33.0.0, PHP 24.0.0, .NET 27.0.0, Node 23.3.0, Go 16.3.0, Python 13.3.0 and Ruby 10.1.1). Some generated sample calls contain placeholder strings or malformed syntax; use the linked current Transfers API reference for implementation, not these examples as proven working code.

## Detail locators

- Webhook preference, payout-transfer sequence and viewing routes: raw lines 19–34. Required API and Customer Area roles: lines 35–45. Customer Area listing/filtering: lines 47–69.
- `GET /transfers` query table, six-month and identifier statements, conflicting examples, SDK samples and list response with bank plus internal transfer: lines 70–473. Customer Area search and `GET /transfers/{id}`: lines 475–650. Detailed response sample's internal-transfer identity and statuses: lines 652–736.
- Confirmation letter meaning, contents, role/masking gates and download steps: lines 738–779.

## Related

- [[adyen]] — provider context.
- [[adyen-platforms]] — balance-platform and user context.
- [[source-adyen-docs-platforms-payout-webhooks]] — payout Transfer webhook state, bank-tracking and failure/return context.
- [[source-adyen-docs-online-payments-online-payouts-payout-webhook]] — separate legacy Payout API webhook path; its event model is not this Transfers API route.

## Related raw API references

- The raw page links to the Transfers API list/get operations, webhook setup, payout configuration, and tracing webhooks. Check those sources independently for current request schemas and bank-status interpretation.

## Raw Sources

- [[raw/adyen/docs/platforms/view-payout-transfers-details/2026-09-15|Adyen Docs: View payout transfer details (2026-09-15 snapshot)]]
