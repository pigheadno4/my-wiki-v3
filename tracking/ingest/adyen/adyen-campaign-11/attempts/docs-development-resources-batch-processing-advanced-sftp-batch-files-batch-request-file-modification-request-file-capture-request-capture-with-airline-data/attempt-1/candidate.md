---
title: "Adyen SFTP capture request with airline data"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/modification-request-file/capture-request/capture-with-airline-data"
raw_files:
  - "adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/modification-request-file/capture-request/capture-with-airline-data/2026-09-15.md"
tags: [adyen, batch-processing, sftp, capture, airline-data]
---

## Overview

This [[adyen]] SFTP batch request guide explains how to append airline data sub-lines to a payment capture request. The title and sample are capture-specific: the sample file header is `Modification`, its parent line is `Capture`, and it includes `Capture`, `Airline`, `AirlineLeg`, and `AirlinePassenger` sub-lines. The descriptions also say airline sub-lines can accompany authorisation requests. These are request-file structures under [[adyen-batch-processing]], not a new authorisation, a capture result, or proof of funds movement; see [[adyen-payment-capture]] for lifecycle context.

## Key takeaways

- Airline data is optional for a capture request. When included, the page requires at least one `AirlineLeg` and at least one `AirlinePassenger` sub-line. The `Airline` record has `SL`, a sequential sub-line number and fixed type at fields 1–3; its customer, airline, ticket and agency data fields 4–12 are marked optional in the table. Format and character limits are delegated to the linked airline-data overview, which this source does not reproduce.
- `AirlineLeg` field 4 is a leg identifier counting from 1, followed by departure airport, flight number, carrier, fare basis, travel class, optional stopover, destination, travel date and optional departure tax. `AirlinePassenger` field 4 is a passenger identifier counting from 1, field 5 is fixed `Name`, fields 6–7 are given/family name, and birth date and traveller type are optional. Their `SL` counters also increment within the parent line; the separate leg/passenger counters have their own identity.
- The example uses `FH,...,Modification` with `L,...,Capture` and `SL,1,Capture,9145754231690158,100,2,EUR`, followed by airline, leg and passenger records. It illustrates amount and currency exponent as separate fields, but this page does not define the `Capture` sub-line's numeric reference or all capture field requiredness. Do not treat the airline ticket number, file sequence, line number, or `SL` counter as an authorisation or capture PSP reference; use the dedicated capture-request field guide for that mapping.
- The examples also include `ShopperInteraction` and `AuthorisationData` sub-lines without defining them here. Their presence in an example is not evidence that they are mandatory for every airline-data capture. The page has no ACK, result-file, webhook or payment outcome data.

## Detail locators

- **Capture purpose and authorisation/capture cross-route wording:** raw lines 14–28, under `# Capture with airline data`, `## Airline data sub-lines`, and `### Airline`.
- **`Airline` field positions/optional details and capture-file example:** raw lines 30–65.
- **At-least-one-leg condition, leg fields/counters and examples:** raw lines 67–111, under `### AirlineLeg`.
- **At-least-one-passenger condition, passenger fields/counters and examples:** raw lines 113–153, under `### AirlinePassenger`.

## Related

- [[adyen]]
- [[adyen-batch-processing]]
- [[adyen-payment-capture]]

## Related raw API references

- [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/modification-request-file/capture-request/2026-09-15|Capture request field guide — navigation only; raw not read for this entry]]

## Raw Sources

- [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/modification-request-file/capture-request/capture-with-airline-data/2026-09-15|Adyen SFTP airline-data capture request guide — collected 2026-09-15]]
