---
title: "Import data from another payment provider | Adyen Docs"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/migrating-payment-data"
raw_files:
  - "adyen/docs/development-resources/migrating-payment-data/2026-09-15.md"
tags: [adyen, payment-data-migration, tokenization, recurring-payments, pgp]
---

## Overview

This 2026-09-15 capture of an Adyen page last modified in 2019 outlines a **provider-assisted import** of payment data from a prior PSP to Adyen. It frames old payment activity as useful for analysis and then gives a staged card-detail and recurring-charge migration. It does not describe exporting data out of Adyen, transferring merchant-of-record status, or activating any specific payment method. See [[adyen]] and [[adyen-tokenization]].

## Key takeaways

- Before import, the merchant must support tokenization and recurring charging across the two PSPs during transition, choose an internal `shopperReference` for Adyen, check how the old PSP can map it, and arrange the old PSP's file-transfer method. The reference links the shopper to stored details; it is not itself a payment credential or proof of shopper consent.
- If the old PSP can export Adyen's required format, the page directs the merchant to Adyen Support for a custom PGP key. Otherwise, it says the old provider should encrypt its format with Adyen's PGP key so Adyen can manipulate it after receipt. This describes an encrypted file-transfer path coordinated with the old PSP and Adyen, not an API endpoint or evidence that a merchant met all PCI/data-protection obligations.
- Adyen recommends three stages: route new tokenizations/sign-ups to Adyen while old-customer recurring charges remain at the old PSP; export old card details for Adyen import; then switch old-customer charging to Adyen. If new tokenizations cannot move immediately, the guide says to request any tokens the old PSP created during the transition. Import files for recurring details and referral data are separate. The recurring-import and referral-list guides give their respective CSV fields. Per-detail import results are covered by the recurring-import guide; the referral-list guide does not describe an acceptance report.
- The page says Adyen does not charge for migrating payment data and that migration usually takes at least 10 days because of technical/compliance complexity. These are dated provider statements, not a current price or delivery SLA. The closing “ready to process payments” statement follows completion of the described migration; this snapshot alone does not prove any import succeeded, contract is chargeable, account is enabled, or payment authorized.

## Detail locators

- Historic-payment analysis purpose and dated price/timing statements: lines 15–21.
- Two-PSP processes, shopper-reference selection/mapping, old-PSP transfer and PGP/Support branches: `Requirements`, lines 23–39.
- Three-stage new-versus-old customer/token and charge cutover: `Import card details`, lines 41–53.
- Separate recurring/referral import CSV files: lines 49–51.

## Related

- [[adyen-tokenization]] — stored-payment and recurring scope.
- [[source-adyen-docs-development-resources-migrating-payment-data-import-payment-details-for-recurring-payments]] — independently retained detailed encrypted CSV and result-file guide.
- [[source-adyen-docs-development-resources-migrating-payment-data-import-data-into-referral-lists]] — independently retained referral-list CSV guide; no acceptance report is described.

## Raw Sources

- [[raw/adyen/docs/development-resources/migrating-payment-data/2026-09-15|Import data from another payment provider (2026-09-15)]]
