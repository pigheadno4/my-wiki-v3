---
title: "Authorisation with airline data | Adyen Docs"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/authorisation-request-file/authorisation-with-airline-data"
raw_files:
  - "adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/authorisation-request-file/authorisation-with-airline-data/2026-09-15.md"
tags: [adyen, batch-processing, sftp, authorisation, airline-data]
---

## Overview

This 2026-09-15 [[adyen]] batch-file reference shows how to append airline-data `SL` sub-lines to card, IBAN, or recurring-payment authorisation requests. It gives field-position tables for `Airline`, `AirlineLeg`, and `AirlinePassenger`, plus an optional `MerchantOrderReference` sub-line. It mentions airline data in authorisation and capture contexts, but the transaction-specific parent records and payment outcome are owned by separate guides. [[adyen-batch-processing]]

## Key takeaways

- The `Airline` sub-line uses required `SL`, a parent-line sub-line sequence number, and fixed `Airline` type in fields 1–3. Its customer reference, airline and ticket identifiers, address, and agency fields 4–12 are marked optional. The page refers to the linked airline-data overview for further format and character restrictions; this table alone is not the full validation specification.
- If airline data is included, the file also needs **at least one** `AirlineLeg` and **at least one** `AirlinePassenger` sub-line. The `AirlineLeg` table marks leg number, departure airport, flight number, carrier, fare basis, travel class, destination and travel date required, with stopover and departure tax optional. The `AirlinePassenger` table marks passenger number, `Name`, given and family names required, with birth date (`yyyy-MM-dd`) and traveller type optional. See raw lines 70–135 for exact positions.
- `MerchantOrderReference` is an optional sub-line; its four fields are required when that sub-line is used. Sub-line record numbers are defined as sequential within the parent line; leg and passenger numbers have their own sequential counters. The examples show `PaymentDetails` values but this page does not define the amount value or exponent semantics, so do not infer units or scale from examples.

> [!warning] Example boundaries
> The repeated full-file examples are headed by `Modification` and contain `CaptureWithExternalAuth`, even though this page is titled authorisation with airline data. They also jump from sub-line number 5 to 8 after describing sequential numbering; the first full-file example uses `DEVL` where the common batch-request `FH` reference lists `TEST`/`LIVE`. These are unresolved example-versus-table differences, not alternative validated formats. The examples include card and passenger details for illustration; they do not prove appropriate production handling, accepted files, authorisation, capture, or final outcome.

## Detail locators

- **Scope and eligible parent-request links:** raw lines 14–20.
- **`Airline` fields, requiredness, validation-reference link and isolated/full-file examples:** raw lines 26–68.
- **`AirlineLeg` condition, fields, counters and examples:** raw lines 70–115.
- **`AirlinePassenger` condition, fields, optional birth date/type and examples:** raw lines 117–162.
- **Optional `MerchantOrderReference` sub-line and example:** raw lines 164–186.

## Related

- [[adyen]]
- [[adyen-batch-processing]]
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file]] — common FH/BH/BT/FT format and environment fields
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files]] — SFTP channel and batch account-scope qualifications

## Raw Sources

- [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/authorisation-request-file/authorisation-with-airline-data/2026-09-15|Adyen authorisation with airline data — collected 2026-09-15]]
