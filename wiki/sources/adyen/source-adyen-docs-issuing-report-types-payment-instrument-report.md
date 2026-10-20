---
title: "Adyen Issuing Payment Instrument Report"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/report-types/payment-instrument-report"
raw_files:
  - "adyen/docs/issuing/report-types/payment-instrument-report/2026-09-15.md"
tags: [adyen, issuing, reports, payment-instruments, cards]
---

## Overview

This Issuing report guide, last modified 2022-03-01 and captured 2026-09-15, describes the Payment Instrument Report as an inventory of a platform's payment instruments with card details and each instrument's status **at report-generation time**. It can be generated on a schedule or manually for a particular day or consecutive days in Customer Area. This is an inventory snapshot: an active row reports active status at generation time, but does not document the activation event or establish a successful payment or settlement.

## Key takeaways

- Each data row represents one payment instrument. The first two rows identify the report, and the third is the header. The listed schema has 32 columns, but the downloadable sample may omit extra data or columns present under a platform's settings; the sample is not an exhaustive schema contract.
- Core columns include Balance Platform name, payment-instrument ID and platform reference, form factor (virtual/physical), cardholder name, first six and last four PAN digits, sequence number, expiry, status and status reason. Status values shown are `active`, `inactive`, `suspended`, `closed`; listed reasons are `lost`, `stolen`, `damaged`, `suspectedFraud`, `other`.
- The report also links each payment instrument to account-holder and balance-account IDs, references and descriptions, plus issuing country, currency and brand variant. Its final ten columns are reserved for future enhancements. Handle the report as cardholder/card metadata, even though this table shows partial PAN rather than full PAN.
- The `Created date` row describes itself as “The date of the payment,” which is inconsistent with a one-row-per-payment-instrument inventory. Do not reinterpret that field as a verified card-creation or payment date without checking the generated report/schema.

## Detail locators

- Opening and `## Sample`: report purpose, scheduled/manual generation route and platform-specific column variation.
- `## Report structure`: point-in-time row grain, first two rows, third-row header and 32-column table.
- Report-structure table rows 1–16: instrument/card identifiers, partial PAN, status, country, currency and brand.
- Report-structure table rows 17–32: linked account-holder/balance-account metadata and reserved fields; `Created date` wording anomaly is in row 6.

## Related

- [[adyen-issuing]] — main Issuing concept.
- [[adyen]] — provider context.

## Related raw API references

- [[raw/adyen/docs/issuing/generate-download-reports/2026-09-15|Generate and download reports]] — linked scheduling/manual generation procedure; navigation only for this entry.

## Raw Sources

- [[raw/adyen/docs/issuing/report-types/payment-instrument-report/2026-09-15|Payment Instrument Report guide (fetched 2026-09-15)]]
