---
title: "Adyen Payout Service transfer details and confirmation letters"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/view-transfers-details"
raw_files:
  - "adyen/docs/payouts/payout-service/view-transfers-details/2026-09-15.md"
tags: [adyen, payout-service, transfers-api, transfer-status, confirmation-letter]
---

## Overview

This Payout Service-path guide (last modified 2019-12-06; captured 2026-09-15) describes viewing balance-account transfer records through Customer Area or the Transfers API, and downloading a **bank-transfer** confirmation letter. It explicitly lists an **Adyen for Platforms integration** as a prerequisite even though the URL is under Payout Service; do not infer independent Payout Service eligibility from the path. The examples show bank and internal balance-account transfers. A booked balance-account debit or sent-instruction letter does not, by itself, prove the beneficiary bank received funds. See [[adyen]] and [[adyen-payouts]].

## Key takeaways

- **Access and evidence:** The guide describes initiation, authorisation and booking before balance-account money movement, and recommends webhooks for ongoing tracking and reconciliation. API retrieval needs **TransferService Webservice Retrieve**. Customer Area transfer viewing needs **Balance platform base**; downloading a confirmation letter needs a separate **Download transfer confirmation letter** role, and unmasked PII needs **View bank transfers PII**. Without the PII role, letter PII is masked.
- **List and individual lookup:** Customer Area **Balances > Transfers** shows one balance platform at a time with date/status/reference filters. `GET /transfers` describes `createdSince` and `createdUntil`, an interval under six months, optional balance-account/account-holder filters and page limit; the response provides `data` and pagination `_links`. The prose also says to supply at least one unique identifier, but the shown cURL list example has dates and limit only. `GET /transfers/{id}` or Customer Area search retrieves a specific transfer by ID; its response includes amount, direction, event history, reference and current status. The bank examples show outgoing bank-account counterparties and booked accounting plus estimated-arrival tracking; the list also shows an internal balance-account counterparty. These static examples are not live transfer evidence.
- **List-example conflicts:** The parameter text says `createdSince` and `createdUntil` must be **less than six months apart**, but the accompanying prose describes **May 12, 2025 to May 13, 2026**. The actual cURL uses **May 12–13, 2026**, a one-day window, and omits the unique identifier demanded by nearby prose. Do not copy the narrative range or infer that the API accepts an identifier-free request from this inconsistent example; verify current API behavior separately.
- **Confirmation letter limit:** For a booked **bank transfer**, Customer Area can download a PDF that identifies transfer and beneficiary details and confirms **Adyen sent the instruction to carry out the transfer**. It may include ACH/FPS trace identifiers if available. The documented filters are Status **Booked** and Type **Bank transfer**. The letter is evidence of an instruction and documented transfer state, not final receipt by the beneficiary bank.

## Detail locators

- Transfer stages, webhook recommendation, integration and role prerequisites: pinned raw lines 15-45.
- List filters, six-month window, identifier statement, conflicting prose/cURL dates and paginated response: pinned raw lines 47-89 and 253-258.
- Example outgoing bank and internal balance-account records, including booked and estimated-arrival fields: pinned raw lines 262-457.
- Specific-transfer lookup, response fields and example bank-transfer history: pinned raw lines 459-746.
- Bank confirmation letter, required roles, PII masking and booked-bank filters: pinned raw lines 748-789.

## Related

- [[adyen-payouts]] — main Payout Service concept and reciprocal source route.
- [[adyen-platform-internal-transfers]] — related internal balance-account transfer model shown in the list example.

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/view-transfers-details/2026-09-15|Payout Service transfer-details guide, captured 2026-09-15]]
