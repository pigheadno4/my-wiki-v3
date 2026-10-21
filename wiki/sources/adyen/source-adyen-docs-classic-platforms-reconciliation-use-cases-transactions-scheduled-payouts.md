---
title: "Track Classic Platforms transactions in scheduled payouts"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/reconciliation-use-cases/transactions-scheduled-payouts"
raw_files:
  - "adyen/docs/classic-platforms/reconciliation-use-cases/transactions-scheduled-payouts/2026-09-15.md"
tags: [adyen, classic-platforms, scheduled-payouts, reporting, reconciliation]
---

## Overview

This Classic Adyen for Platforms guide shows how to find debit and credit transactions included in a scheduled payout using the Marketpay Payout Report. It explicitly directs new implementations to the separate new-integration guide. Its account-holder/account report model belongs to Classic Platforms, not the modern balance-account payout model; see [[adyen]] and [[adyen-classic-platforms]]. A report row or example of an initiated payout is not proof of beneficiary-bank receipt.

## Key takeaways

- This route applies if scheduled payouts are configured. The Marketpay Payout Report's timing is optimized for them and includes payouts initiated within the day with credits and debits in the paid-out amount, grouped by account holder and account. The report reference, not this selected-row example, defines the complete columns and record types.
- The sample shows selected rows and columns for a liable account holder and two other account holders. Read **Account holder**, **Account**, currency, amount and **Record type** together: `Credited`, `Debited`, `Fee` and `Payout` rows illustrate how account-level postings contribute to a negative payout line. PSP and payment-merchant references identify related actions in the example, but some fee or payout entries have blank references.
- The illustrative amounts balance within the three displayed account groups: the liable account shows EUR 60 + 30 − 9.72 − 2 − 78.28 = 0; AccountHolder_1 shows EUR 240 − 240 = 0; AccountHolder_2 shows EUR −48 + 120 − 72 = 0. These selected rows are an example, not a complete or live payout record. Do not treat the report's `Payout` entry as independent evidence that a bank credited the account holder.

## Detail locators

- Classic-only scope, new-integration route, scheduled-payout prerequisite and report timing/grain: raw lines 15–21. Example limitations and displayed account-group rows: lines 23–42. Related account-structure, accounting and balance-report routes: lines 44–48.

## Related

- [[adyen]] — provider context.
- [[adyen-classic-platforms]] — Classic account-holder/account model.
- [[source-adyen-docs-classic-platforms-reports-and-fees-marketpay-payout-report]] — full automatic-payout report definition, columns, rolling balance and record types.
- [[source-adyen-docs-classic-platforms-payouts-scheduled-payout]] — scheduled-payout configuration and status context.
- [[source-adyen-docs-classic-platforms-payouts-payout-notifications]] — separate payout status and return notifications.

## Related raw API references

- The raw page links to Classic account structure, Marketplace Payments accounting and Marketpay Balance reports; their detailed reconciliation rules require their own evidence.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/reconciliation-use-cases/transactions-scheduled-payouts/2026-09-15|Adyen Docs: Track transactions in scheduled payouts (2026-09-15 snapshot)]]
