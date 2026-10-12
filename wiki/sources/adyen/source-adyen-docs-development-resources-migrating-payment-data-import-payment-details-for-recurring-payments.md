---
title: "Adyen Import Payment Details for Recurring Payments"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/migrating-payment-data/import-payment-details-for-recurring-payments"
raw_files:
  - "adyen/docs/development-resources/migrating-payment-data/import-payment-details-for-recurring-payments/2026-09-15.md"
tags: [adyen, tokenization, recurring-payments, migration]
---

## Overview

This Adyen migration guide describes importing recurring payment details from another payment service provider. The merchant supplies a CSV of recurring contracts, encrypts it with a PGP public key from Adyen Support or an Adyen contact, and sends it to Adyen; Adyen performs the import and sends an output file with per-detail results. It is a provider-assisted file migration, not an API call or proof that any specific contract was imported or can be charged.

## Key takeaways

- Input is RFC 4180 CSV in UTF-8, one recurring contract per data line. Field names and values are case-sensitive; multi-line fields are disallowed; the stated limits are 1,000,000 lines and 1 GB. `ShopperReference` is shopper-unique, at least three characters, case-sensitive, and should not contain name, email or other PII. Fields vary by payment method, so the common table and method-specific sections must be read together.
- Card imports require card number and expiry data. For Visa and Mastercard Subscription or UnscheduledCardOnFile series, the guide marks initial-transaction `networkTxReference` as required and warns that missing scheme identifiers may cause soft declines and non-compliance assessment fees. Mastercard `transactionLinkId` is imported only if `networkTxReference` is also provided. For other schemes the guide recommends the initial-transaction reference and describes temporary static-value handling; that should not be generalized to Visa or Mastercard.
- Separate input sections cover card, address, SEPA, ACH, PayPal and Klarna details, plus an optional auxiliary CSV to remap old shopper references to new references. For example, Klarna recurring support varies by payment method and country/region. The `RecurringContract` input describes ONECLICK, RECURRING and PAYOUT uses; an example CSV row is not evidence of a currently eligible payment method or payout route.
- The output reports migration status, identifiers and method/card metadata. `Success` means a line imported; `Skipped` can reflect missing essential data, and `statusMessage` reports why a card could not be imported. Adyen warns that it will add output fields, so parsers must tolerate new headers. Optional output status fields require contacting Support. An encrypted output file requires providing Adyen with the merchant's public key.

## Detail locators

- `## Input file format` and `## Input file fields`: CSV format, encryption, shared fields, and `RecurringContract` semantics.
- `### Card fields`: card expiry alternatives, scheme transaction identifiers and Mastercard linkage. `### Address fields` through `### Recurring Klarna payment fields`: conditional method-specific input; `### Shopper reference re-mapping (optional auxiliary file)` describes the second file.
- `## Output file`: `Success`/`Skipped`, returned references, optional status columns, evolving headers and sample output.

## Related

- [[adyen]]
- [[adyen-tokenization]]

## Raw Sources

- [[raw/adyen/docs/development-resources/migrating-payment-data/import-payment-details-for-recurring-payments/2026-09-15|Adyen recurring payment detail import guide (2026-09-15 snapshot)]]
