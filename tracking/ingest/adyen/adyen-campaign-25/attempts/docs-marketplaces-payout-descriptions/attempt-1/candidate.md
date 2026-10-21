---
title: "Adyen Marketplace payout descriptions"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/payout-descriptions"
raw_files:
  - "adyen/docs/marketplaces/payout-descriptions/2026-09-15.md"
tags: [adyen, marketplaces, platforms, payouts, transfer-descriptions]
---

## Overview

This 2026-09-15 Marketplace-path [[adyen]] guide describes how payout descriptors are submitted, passed through clearing, and potentially shown on users' beneficiary-bank statements in the modern [[adyen-platforms]] model. `description` and `referenceForBeneficiary` can be sent through Transfers API or Customer Area, but network rules and the receiving bank determine what is displayed (raw lines 15–27). A submitted descriptor is not evidence of a booked payout or bank receipt.

## Key takeaways

- A descriptor may include an originator name, remittance text and bank/clearing identifiers. Depending on region, the originator is Adyen's or the marketplace's legal entity. Where the marketplace's name is used, it can provide a Doing Business As name through hosted onboarding or Legal Entity Management API, then must contact Adyen to set that name as originator (raw lines 29–35). This name does not settle legal seller or fund ownership for an individual transfer.
- Managed and custom scheduled payouts can use static text or dynamic placeholders in `description` or `referenceForBeneficiary`; an Adyen contact can configure them at balance-platform level. The placeholder table covers balance account/account holder IDs, references and descriptions. `$transferReference` represents a 15-character generated reference for managed payouts or a 30-character one for custom schedules; `$shortTransferReference` is only for custom scheduled payouts and is 15 characters (raw lines 37–60). For custom schedules, balance-account descriptor settings override balance-platform settings; an unconfigured descriptor uses the stated default (line 69).
- The page recommends `$shortTransferReference` for reconciliation through Customer Area, confirmation letters, the Balance Platform Payout Report and bank statements (raw lines 62–67). Its broad “provided by all banks” wording is qualified by the page's own route table showing zero statement visibility for some accepted fields; appearance or location on a particular statement cannot be guaranteed from that recommendation (lines 131–138, 149–158, 246–255).
- On-demand Transfers API payouts and Cashout requests require static strings in each request; scheduled placeholders are unsupported. The guide names `/transfers` and `/cashouts` and recommends a unique internal reference in the description for reconciliation (raw lines 71–76). These are separate payout products, with their own request and outcome requirements.
- Allowed characters, submitted maximum and statement-visible length vary by counterparty region, currency and priority. They are distinct columns in the tables: for example, PLN regular descriptions and beneficiary references are accepted yet show zero visible characters; SEPA EUR instant beneficiary reference and SGD wire fields also show zero. Australia AUD fast lists 280 statement characters while Adyen accepts only 140 for description and 80 for beneficiary reference (raw lines 78–255). Check the exact route instead of treating the table's largest visible number as a submission limit.

## Detail locators

- Descriptor journey and originator/remittance components: raw lines 15–35.
- Scheduled payout placeholders, transfer-reference lengths, reconciliation paths, precedence and default: raw lines 37–69.
- On-demand/Cashout static-string rule: raw lines 71–76.
- Country/currency/priority acceptance and visibility tables: Europe lines 78–187, North America lines 189–211, Asia Pacific lines 213–255.

## Evidence boundary

The beneficiary bank decides what appears on its customer's statement; Adyen's accepted request text may be shortened, omitted or displayed elsewhere (raw lines 23–27, 78–255). The “all banks” statement for the short reference conflicts with zero-visibility table rows, so bank-specific display must be checked against actual statement evidence. This page does not verify a live marketplace's descriptor setup, payout execution, bank credit or legal payee. Keep scheduled, on-demand and Cashout configuration distinct from Classic Platforms payouts.

## Related

- [[adyen-platforms]] — current marketplace/platform context.
- [[source-adyen-docs-marketplaces-custom-payouts-on-demand-payouts]] — on-demand payout request and status route.
- [[source-adyen-docs-marketplaces-managed-payouts]] — managed payout context.

## Raw Sources

- [[raw/adyen/docs/marketplaces/payout-descriptions/2026-09-15|Pinned Marketplace payout-description guide, captured 2026-09-15]]
