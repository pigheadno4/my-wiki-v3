---
title: "RefundWithData request | Adyen Docs"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/refundwithdata-request-file/refundwithdata-request"
raw_files:
  - "adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/refundwithdata-request-file/refundwithdata-request/2026-09-15.md"
tags: [adyen, batch-processing, refund-with-data, sftp, request-schema]
---

## Overview

This 2026-09-15 snapshot of a 2021-modified Adyen page is the sub-line field reference for a titled **RefundWithData** SFTP batch request. It describes a `PaymentDetails` sub-line plus either `Card` or `IBAN`, with optional `Address` sub-lines. It defines request layout only: no upload acknowledgment, per-record refund result, final financial outcome, account eligibility, or retry rule follows from this page. See [[adyen]], [[adyen-batch-processing]], and the broader [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files]] for SFTP/PGP and result-file routes.

## Key takeaways

- The title and Card/IBAN introductions identify a refund-with-data request, while the opening mandatory-sub-lines sentence calls it a **bank transfer authorisation request** and the Card/IBAN ordering sentences say **authorization request**. Treat that object/action wording as an unresolved source conflict; do not recast this schema as proof of an authorization or a completed refund.
- `PaymentDetails` is mandatory with one of `Card` or `IBAN`. Its table separates **Field Required** from **Value Required**: fields such as currency exponent, birth date, entity type, and nationality must occupy a position but may have an empty value, while amount and ISO currency code require values. The table calls amount numeric and provides a separate exponent field; it does not explicitly define an amount-to-minor-unit conversion. Shopper reference/email are optional in this table but its descriptions say they are required for recurring payments and recurring-contract creation. See raw `### PaymentDetails` for all positions and conditions.
- The Card table marks PAN, expiry month/year, CVC, and cardholder name required; the IBAN table marks account-owner name, two-letter country, and IBAN required while BIC is optional. The IBAN table says an invalid owner-name format yields error 203 and an invalid country code rejects the transaction/request. These are request-field/validation statements, not evidence of a refund outcome. The Card fields contain sensitive card data; use the linked SFTP guide's PGP requirements and do not treat a raw sample as a safe live input.
- The raw examples conflict with the positional tables. The shortened `PaymentDetails` examples called valid place birth date/entity type/nationality immediately after currency despite the table assigning them fields 12/14/15. The Card sample lacks a separate CVC position although the Card table marks CVC required. The examples are therefore not reliable complete positional templates without resolving the discrepancy.
- `Address` is optional; if both billing and delivery addresses are supplied, the page uses separate `Address` sub-lines. Its table lists the address type and individual address fields, including a two-letter ISO country code whose invalid value is said to reject the request. See raw `## Optional sub-lines` / `### Address`.

## Detail locators

- `## Mandatory sub-lines` and `### PaymentDetails`: mandatory sub-line combination, field-versus-value requiredness, amount/exponent/currency positions, and recurring-field qualifications.
- `#### Example PaymentDetails sub-lines`: examples that do not preserve the table's full field positions.
- `### Card`: marked required card fields, sample file, and the missing separate CVC position in that sample.
- `### IBAN`: required bank-owner/country/IBAN fields, optional BIC, validation errors, and sample file.
- `## Optional sub-lines` / `### Address`: optional billing and delivery rows and address-field rules.

## Related

- [[adyen]]
- [[adyen-batch-processing]]
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files]] — SFTP transport, PGP protection, and result/acknowledgment routing.

## Raw Sources

- [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/refundwithdata-request-file/refundwithdata-request/2026-09-15|RefundWithData request sub-line schema, 2026-09-15]]
