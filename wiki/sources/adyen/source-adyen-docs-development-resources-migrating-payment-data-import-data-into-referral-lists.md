---
title: "Adyen bulk import into referral lists"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/migrating-payment-data/import-data-into-referral-lists"
raw_files:
  - "adyen/docs/development-resources/migrating-payment-data/import-data-into-referral-lists/2026-09-15.md"
tags: [adyen, risk-management, referral-lists, bulk-import, pgp, sensitive-data]
---

## Overview

This dated Adyen guide describes a **bulk CSV import** of card, bank and shopper referral data into lists used for fraud checks. It distinguishes this Support-assisted, PGP-encrypted file route from uploading block/trust-list items through Customer Area CSV. The raw metadata says last modified 2020-05-01 and the snapshot was captured 2026-09-15. See [[adyen]] and [[adyen-risk-management]].

## Key takeaways

- Prepare an RFC 4180 CSV with one referral item per line, a supported record-type prefix, **no header** and **no multiline fields**. Variable fields per line are allowed; the page caps a file at **100,000 lines if file size permits** and asks for UTF-8. Encrypt the file using a **PGP public key supplied by Adyen Support or the Adyen contact**, then send it to Adyen; Support is required for upload. The page does not describe a self-service API endpoint or a response/acceptance report for this route.
- The eight type sections are `card`, `sepa`, `shopperName`, `shopperEmail`, `shopperIp`, `shopperReference`, `shopperAddress` and `shopperPhoneNumber`. Their required-field tables include a `merchantAccountCode`, a type-specific sensitive detail, `description`, and a `flag` with `trust`, `block` or `delete` action values. Address has multiple required parts; use its own table rather than treating all types as a common fixed-width row.
- The input can contain full card numbers, IBANs, names, emails, IP addresses, references, postal addresses and phone numbers. Treat the source's example rows as illustrative data only. PGP encryption is an explicit transport prerequisite, not a statement that a merchant's privacy, PCI or retention obligations are satisfied.
- Each type table describes `merchantAccountCode` as the **merchant account name**, while the example placeholder says `YourMerchantOrCompanyAccount`. The page does not resolve that difference or define effective list visibility, company/merchant inheritance, credential permissions, merchant of record or seller/payee allocation. Use the separately reviewed risk-list guide for general account-scope configuration and confirm the accepted import scope with Adyen before applying sensitive entries.
- An encrypted file sent to Support is a submission, not proof that every item was accepted, that `trust` or `block` caused a risk decision, that `delete` removed an entry, or that a later payment was approved or declined. Risk-list enablement, payment-field matching and risk-profile configuration are separate.

## Detail locators

- Lines 14–20: fraud-check purpose, distinction from Customer Area CSV and encrypted Support upload.
- `## Input file format` (lines 22–38): RFC 4180, row shape, no header/multiline, 100,000-line conditional cap, UTF-8, PGP key source and send step.
- `## Card` and `## SEPA` (lines 40–66): record prefixes, account field, PAN/IBAN and action flags.
- `## Shopper name` through `## Shopper phone number` (lines 68–155): type-specific PII fields, required account/description/flag columns and address subfields.
- `## Example file` (lines 157–169): illustrative sample rows and account placeholder; not proof of ingestion or account scope.

## Related

- [[adyen-risk-management]] — provider risk concept and reciprocal source route.
- [[source-adyen-docs-risk-management-configure-your-risk-profile-risk-lists]] — risk-list enablement, visibility and company/merchant configuration.
- [[source-adyen-docs-risk-management-automate-submitting-referrals]] — separate Referrals API route and request outcomes.

## Raw Sources

- [[raw/adyen/docs/development-resources/migrating-payment-data/import-data-into-referral-lists/2026-09-15|Referral-list bulk import, captured 2026-09-15]]
