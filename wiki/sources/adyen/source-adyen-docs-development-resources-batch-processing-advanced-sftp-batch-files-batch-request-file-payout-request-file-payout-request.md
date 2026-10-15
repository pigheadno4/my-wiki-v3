---
title: "Adyen SFTP batch payout request sub-lines"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/payout-request-file/payout-request"
raw_files:
  - "adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/payout-request-file/payout-request/2026-09-15.md"
tags: [adyen, batch-processing, payout, sftp]
---

## Overview

This Adyen Docs snapshot specifies the `SL` sub-line records for a Payout request inside a batch request file. It defines required payout details, a `Recurring` record, and one destination-data record. It is a request-file schema, not evidence that a file was accepted, a payout authorized, or funds delivered.

## Key takeaways

- The page requires `PayoutDetails` and `Recurring`, plus either `Card`, `BankAccount`, or `IBAN`. The destination sub-line is shown as sub-line 2 in the relevant destination sections. A user role with permission to store payout details is required for the described payout.
- `PayoutDetails` marks amount and currency exponent as separate required numeric fields, followed by a three-character ISO currency code. Its table also marks shopper reference, email, birth date, entity type (`NaturalPerson` or `Company`), and nationality required; shopper statement, IP address and social-security number are optional. The example `1000,2,EUR` must be read as those three field values, without inferring payout execution or a universal unit rule beyond this schema.
- `Recurring` requires type `PAYOUT` and a fixed `Latest` field in the table. The examples write `LATEST` in uppercase; the snapshot does not resolve that capitalization difference.
- The `Card` table marks number, expiry month/year, CVC and cardholder name required. It contains sensitive payment-card data. The card example does not supply a separate CVC value in the listed required position, so use the table for field identity rather than treating the sample row as a validated template.
- `BankAccount` requires account owner, ISO two-letter country, account number, bank location/name and bank code; an invalid country code is said to cause rejection. `IBAN` requires owner, ISO two-letter country and IBAN, with optional BIC. For its owner field, the IBAN table says at least three characters and not numbers alone, otherwise error 203. The `BankAccount` table requires two-letter alphabetic bank-location and bank-name fields and describes an optional two-letter check code, but its sample supplies numeric `20010020`, multiword `Postbank Stockholm`, and `Hameln` in those positions. Do not treat that sample as a validated payout row; use the table and confirm the accepted format with Adyen.

## Detail locators

- Raw heading **Mandatory sub-lines**, lines 16–18: payout-sub-line composition.
- Raw headings **PayoutDetails** and **Recurring**, lines 20–48: required markers, amount/exponent/currency, shopper/entity fields, and fixed values.
- Raw heading **Card**, lines 50–83: permission note, sub-line number, required card fields, and the illustrative row with a field-position discrepancy.
- Raw heading **BankAccount**, lines 85–116: required account fields, ISO country rejection note, and table-versus-sample format mismatch.
- Raw heading **IBAN**, lines 118–146: owner-name validation, required/optional bank fields, and illustrative row.
- Related parent **Payout request file** raw, heading **Payout lines**: the parent `L` record carrying merchant-account and payout metadata for these `SL` records.

## Related

- [[adyen]] — provider context
- [[adyen-batch-processing]] — SFTP batch flow, acknowledgement and result boundaries

## Raw Sources

- [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/payout-request-file/payout-request/2026-09-15|Payout request sub-lines (2026-09-15 snapshot)]]

## Related raw evidence

- [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/payout-request-file/2026-09-15|Payout request file parent (2026-09-15 snapshot)]]
