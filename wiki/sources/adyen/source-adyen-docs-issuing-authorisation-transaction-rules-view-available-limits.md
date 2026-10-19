---
title: "Adyen Issuing: View available card limits"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/authorisation/transaction-rules/view-available-limits"
raw_files:
  - "adyen/docs/issuing/authorisation/transaction-rules/view-available-limits/2026-09-15.md"
tags: [adyen, issuing, transaction-rules, limits, cards]
---

## Overview

This Adyen Issuing guide (last modified 2025-01-07; captured 2026-09-15) describes viewing available limits on an Adyen-issued card's payment instrument. It distinguishes transaction-rule amount/count limits from capability-level ATM, restricted-country and restricted-industry limits. The GET `/paymentinstruments/{id}/limits` lookup reports the limit, used and remaining amounts or counts, source and active interval at calculation time. It is a read of configured and authorized activity, not proof of card activation, a future authorization decision, capture or settlement. [[adyen]] [[adyen-issuing]]

## Key takeaways

- **Scope and access:** The requirements name an Adyen Issuing integration, Configuration API access and the **Bank Manage TransactionRules role**. The guide says to have created a rule with `totalAmount` or `matchingTransactions` restrictions for the transaction-rule path. The broader opening also discusses limits from capability levels; do not assume every capability limit is covered by the rule setup step. See raw lines 19-30 and 48-57.
- **Return limits are narrower than all configured rules:** the feature supports `totalAmount` and `matchingTransactions` restrictions only, excludes `matchingValues` combined with `matchingTransactions`, returns only limits aggregated at the **payment instrument** level rather than higher levels, and excludes `blockList` because it has no limits. A missing result therefore does not prove there is no higher-level or otherwise unsupported restriction. See raw lines 54-56.
- **Authorization-based counters:** amount uses total authorized card amount and count uses number of authorized card transactions. All authorizations reduce available limit whether captured or not; an expired or canceled authorization releases its amount/count back. Do not equate `spent` or `remaining` with captured or settled funds. See raw lines 59-66.
- **Lookup and hierarchy:** GET `/paymentinstruments/{id}/limits` requires the issued-card/payment-instrument ID. `transactionRuleId` is optional; when omitted, the page says the response returns the limit applying to that card according to transaction-rule hierarchy. The response has `calculatedAt`, optional `amountLimits`/`countLimits` arrays, and entries with `limit`, `spent`, `remaining`, `source` and `interval`. `calculatedAt` marks the snapshot time, not a promise that the remaining value will persist. See raw lines 68-108.
- **Interval/schema caution:** The interval table lists per-transaction, daily, weekly, monthly, lifetime, rolling and sliding types, with duration/start fields conditional on type or unit (raw lines 110-131). It names the field `timezone` and default `UTC`, while the JSON example uses `timeZone` with `CST` (raw lines 131, 168, 190). Treat the sample as illustrative and verify the applicable schema and actual response before parsing field casing or applying a timezone assumption.

## Detail locators

- **Opening and benefits**, raw lines 15-46: rule versus capability sources, amount/count and ATM/geography/industry examples, warning/budget use cases.
- **Requirements**, raw lines 48-57: integration, role, supported restrictions, aggregation level, `blockList` exclusion and transaction-rule setup.
- **Calculating limits**, raw lines 59-66: authorized amount/count, uncaptured deductions and expiry/cancellation release.
- **View available limits**, raw lines 68-108: path and optional query ID, hierarchy fallback, `calculatedAt` and amount/count result fields.
- **Interval fields and illustrative response**, raw lines 110-196: interval types and conditional duration/start fields, sample amount/count limit and `timezone`/`timeZone` discrepancy.

## Related

- [[adyen-issuing]] — Issuing concept and evidence boundary.
- [[source-adyen-docs-issuing-authorisation-transaction-rules]] — rule scope and hierarchy context.
- [[source-adyen-docs-issuing-authorisation-transaction-rules-create-and-manage]] — rule creation and lifecycle context.

## Raw Sources

- [[raw/adyen/docs/issuing/authorisation/transaction-rules/view-available-limits/2026-09-15|Adyen Issuing available-limits guide, captured 2026-09-15]]
