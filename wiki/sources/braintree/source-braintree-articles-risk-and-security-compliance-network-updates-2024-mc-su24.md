---
title: "Braintree 2024 Mastercard Network Updates"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/risk-and-security/compliance/network-updates/2024/mc-su24"
raw_files:
  - "braintree/articles/risk-and-security/compliance/network-updates/2024/mc-su24-2026-09-16.md"
  - "braintree/articles/risk-and-security/compliance/network-updates/2024/s-2024-all-2026-09-16.md"
tags: [braintree, mastercard, card-networks, fees, compliance, authorization]
---

## Overview

This collected [[braintree]] webpage is titled `Mastercard` and records selected Mastercard fee and transaction-processing changes whose body-stated effective dates run from March 2024 through January 2027. It is historical, region- and condition-specific Braintree-hosted retrieval evidence, not current Mastercard policy, law, a merchant-specific price schedule, account eligibility, compliance proof, or proof that a fee or processing rule applied to an individual transaction. The URL slug alone is not used to assign a release-period label absent from the body.

## Key takeaways

- In Asia Pacific, the page says the nominal-authorization Transaction Processing Excellence fee changed to USD 0.10 on September 2, 2024, while revised assessment criteria take effect January 1, 2025 and cover approved authorizations at or below the stated small-amount threshold that are reversed within 48 hours; the fee is limited to card-not-present transactions. The Digital Assurance fee schedule varies by PAN versus dynamic-token submission, 3DS use, and AP subregion.
- The Asia-Pacific Authorization Optimizer item is limited to card-not-present recurring transactions after decline code 51 when Merchant Advice Code 24–30 is provided, with each advice code carrying a stated retry interval. A separate APAC cross-border-assessment item says rates rise from 45 to 125 basis points effective July 1, 2024.
- In Europe, the page records phased authorization-validity fees for cleared final authorizations initiated in the EEA, United Kingdom, and Gibraltar; revised interregional cross-border pricing tied to merchant/issuer regions and non-local card currency; a select-country interregional card-not-present fee increase with intraregional transactions unchanged; region- and transaction-type-specific MDES tokenization-service pricing; and an excessive-authorization threshold tied to the same account number, card acceptor, amount, and 30-day period.
- For the excessive-authorization item, the page recommends that acquirers stop requests after either 10 consecutive declines within 24 hours on the same card and card acceptor ID or 35 declines within 30 days on the same card, card acceptor ID, and amount. Those are page-stated acquirer recommendations attached to the historical EU fee change, not a universal retry rule.
- In the United States, the page records an expanded Network Access and Brand Usage fee for non-domestic authorizations, collection-only, and refund/credit transactions; an Acquirer Brand Volume fee increase alongside two acquirer risk tools; and revised arbitration-case filing fees. The captured arbitration table is visibly fragmented, so exact billing-event/rate pairings should be read cautiously from the raw rather than reconstructed here.

> [!warning] Historical and account-specific authority boundary
> The page is a collected Braintree-hosted snapshot of Mastercard changes, not independent current network authority. Its dates, regions, card-present/card-not-present distinctions, currency and account conditions, decline/advice-code conditions, and merchant-versus-acquirer subjects remain essential; verify current applicability and merchant pricing against current official network and account sources.

> [!warning] Unresolved U.S. Acquirer Brand Volume effective-date conflict
> This Mastercard page gives April 5, 2024 for the U.S. Acquirer Brand Volume fee increase and the associated Merchant Risk Dashboard and Small Business Credit Analytics tools, while [[source-braintree-articles-risk-and-security-compliance-network-updates-2024-s-2024-all]] gives April 15, 2024 for the same change. This snapshot does not resolve the disagreement; neither date is selected here as authoritative or current.

## Detail locators

- Nominal Authorization Transaction Processing Excellence region exclusion, September 2024 price change, January 2025 assessment criteria, amount/reversal conditions, and CNP-only scope: `#### Revised Nominal Authorization Transaction Processing Excellence Program in the Asia/Pacific Region excluding Indonesia`, raw lines 17-31.
- Digital Assurance dates and fee table by PAN/token, 3DS, and AP subregion: `#### Digital Assurance Fee`, raw lines 34-51.
- Authorization Optimizer date, CNP recurring scope, decline code 51, Merchant Advice Code condition, and retry intervals: `#### Authorization Optimizer Pricing for Asia Pacific`, raw lines 54-78.
- EEA/UK/Gibraltar authorization-validity fee phases, elapsed-time bands, and caps: `#### Introduction of Time-Based Authorization Validity Value Fees in the European Economic Area Countries, the United Kingdom, and Gibraltar (Switch)`, raw lines 81-117.
- Europe/Ireland interregional cross-border fee dates, rate, merchant/issuer region and currency conditions, and UK note: `What is the Revising Interregional Acquirer Cross-Border Fee and Acquiring Interregional Transaction Fee in Europe and Ireland, mandate?`, raw lines 121-129.
- European interregional CNP fee increase, unchanged intraregional scope, and country list: `What is the Revising and Introducing Interregional Acquirer Card-Not-Present Fees mandate?`, raw lines 131-137.
- APAC and Europe MDES Token Validation and Lifecycle Services dates, approved-tokenized-transaction condition, rates, and Netherlands explanation: `What is the Introducing Pricing for MDES Tokenization Services mandate?`, raw lines 139-210.
- EU excessive-authorization threshold, fee, initial billing, and acquirer stop recommendations: `What is the Revised Excessive Authorization Attempts in Transaction Processing Excellence Program change?`, raw lines 212-222.
- US NABU date, transaction categories, non-US-issued-card condition, and domestic/non-domestic issuer rates: `What is the Extending Network Access and Brand Usage Fee mandate?`, raw lines 224-239.
- US Acquirer Brand Volume fee, stated all-Mastercard-transaction scope, and named acquirer tools: `What is the Revising Acquirer Brand Volume Fee mandate?`, raw lines 241-245.
- US arbitration fee change and fragmented captured table: `What is the Revision of Arbitration Case Filing Fees mandate?`, raw lines 247-371.
- APAC cross-border assessment date and stated rate change: `What is the Revision of Cross-Border Assessments for Select APAC Countries mandate?`, raw lines 373-377.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]

## Raw Sources

- [[raw/braintree/articles/risk-and-security/compliance/network-updates/2024/mc-su24-2026-09-16|Braintree Mastercard network updates page]] - complete collected historical page with body-stated dates, regions, card and transaction conditions, merchant/acquirer actions, fee tables, and the fragmented arbitration table
- [[raw/braintree/articles/risk-and-security/compliance/network-updates/2024/s-2024-all-2026-09-16|Braintree All Spring 2024 Network Updates]] - complete related collected guide establishing the conflicting April 15, 2024 date for the same U.S. Acquirer Brand Volume fee and two risk tools
