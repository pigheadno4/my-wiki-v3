---
title: "Braintree 2023 Mastercard Network Fee and Advice-Code Updates"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/risk-and-security/compliance/network-updates/2023/mastercard-f23"
raw_files:
  - "braintree/articles/risk-and-security/compliance/network-updates/2023/mastercard-f23-2026-09-16.md"
tags: [braintree, mastercard, network-updates, fees, merchant-advice-codes, historical-snapshot]
---

## Overview

This collected [[braintree|Braintree]] webpage, titled "Mastercard Networks," summarizes Mastercard fee and Merchant Advice Code changes with stated effective dates from October 2023 through January 2025. Its sections separately qualify the affected markets, card-not-present or recurring-transaction conditions, decline codes, retry behavior, and merchant actions. Treat it as a historical Braintree-hosted summary for [[braintree-payment-platform]], not current Mastercard policy or law, a merchant-specific fee schedule, account applicability evidence, compliance proof, or proof that a fee was assessed.

## Key takeaways

- The page says that from October 8, 2023, all US merchants using preauthorizations would incur a 1.25-basis-point fee, with a $0.01 minimum, on Mastercard card-not-present preauthorization transactions.
- For the US Transaction Processing Excellence program, the prose says that starting November 1, 2023, retrying a transaction more than 35 times in 30 days would trigger a $0.15 fee for each further attempt, rising to $0.30 on January 1, 2024 and $0.50 on January 1, 2025. The adjacent table conflicts with that prose by dating the $0.15 rate to January 1, 2023; this entry does not resolve the discrepancy.
- For recurring card-not-present transactions declined for insufficient funds, the page describes an Authorization Optimizer program in which Mastercard returns a Merchant Advice Code with response code 51 to indicate an optimal retry time. It says merchants receiving MAC 24-30 incur a fee whether or not they use the MAC. The prose dates the US start to October 9, 2023, while the table says October 1, 2023; EU/EEA, UK, non-EEA and Canada timing and fee rows remain in the raw locator.
- The APAC section associates decline codes 79, 82 and 83 with MAC 01 or 03 and a 3-basis-point fee from October 9, 2023 for listed countries. The same paragraph later prints the fee combination as codes 79, 832 and 83, conflicting with its earlier code 82; preserve that captured inconsistency rather than treating `832` as a confirmed code.
- The global section says MAC 40 identifies a consumer non-reloadable prepaid card and MAC 41 a consumer single-use virtual card. It says these codes would be sent on approved and declined transactions with no associated fee, and presents customer notification and retry-strategy use as opportunities rather than requirements or guarantees.

> [!warning] Historical scope and source conflicts
> Dates, rates, regions, codes, and actions here describe this captured Braintree page. Confirm current network rules, merchant-account applicability, and pricing through applicable current Mastercard and Braintree channels. The prose/table date mismatches and the APAC `82`/`832` mismatch are retained as unresolved source conflicts.

## Detail locators

- US card-not-present preauthorization fee, basis-point rate, and minimum: `## What is the Mastercard Preauthorization Fee mandate?`, raw lines 17-21.
- US excessive-authorization retry threshold, staged rates, and prose/table date conflict: `## What is the revised excessive authorization transaction processing excellence program mandate?`, raw lines 24-35.
- Recurring-CNP Authorization Optimizer markets, response-code and MAC condition, regional date/fee table, MAC 24-30 intervals, and fee independent of MAC use: `## What is the Authorization optimizer for CNP transactions mandate?`, raw lines 38-73.
- APAC optimizer decline/MAC combinations, 3-basis-point fee, `82`/`832` conflict, MAC context, and country list: `## What is the Authorization Optimizer for CNP Transactions (APAC) mandate?`, raw lines 76-86.
- Global MAC 40 and 41 meanings, transaction outcomes, no-fee statement, purpose, and optional merchant uses: `## What are the new Mastercard merchant advice codes mandate?`, raw lines 89-103.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- Combined release snapshot: [[source-braintree-articles-risk-and-security-compliance-network-updates-2023-f-2023-all]]

## Raw Sources

- [[raw/braintree/articles/risk-and-security/compliance/network-updates/2023/mastercard-f23-2026-09-16|Braintree Mastercard Networks historical update]] - complete collected snapshot for the dated, region- and transaction-qualified Mastercard fees, optimizer conditions, advice codes, merchant actions, and captured conflicts
