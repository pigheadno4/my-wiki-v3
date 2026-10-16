---
title: "Adyen NetSuite reconciliation bundle troubleshooting"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/netsuite/reconciliation-bundle/troubleshooting"
raw_files:
  - "adyen/docs/plugins/netsuite/reconciliation-bundle/troubleshooting/2026-09-15.md"
tags: [adyen, netsuite, reconciliation, settlement-report, troubleshooting]
---

## Overview

This [[adyen]] troubleshooting guide distinguishes a NetSuite Settlement Detail Report (SDR) transaction-matching exception from a later Bank Deposit creation error in the NetSuite reconciliation bundle. It routes the reader through setup checks, SDR status and script logs, targeted rematching or deposit-record checks, then customization/release-note/support checks. A created NetSuite Bank Deposit record or resolved SDR error is accounting-workflow evidence, not proof that the receiving bank credited funds. See [[adyen-netsuite]] for the bundle context.

## Key takeaways

- Start by checking the reconciliation-bundle setup. If an SDR transaction cannot match a NetSuite transaction, SDR **Status** becomes **Exceptions Need Resolving** and the affected line's **Match Status** is **Match Not Found**. Resolve unmatched lines before creating deposits. [Raw: Step 1 and Step 2 > Exceptions Need Resolving, lines 21–36]
- For a match failure, inspect the corresponding `Adyen - Find SDR Detail Matches` script execution log and its search filters. If the search omits the needed payment event type or status, revise the saved search through the Settlement Type Map, save it, update the map, then choose **Rematch Transactions** on the SDR. This is a targeted remedy for that match condition, not a general instruction to rerun all reconciliation. [Raw: Exceptions Need Resolving, lines 38–62]
- **Error Creating Deposit** belongs to the deposit stage after matching. The guide lists an already-deposited matched transaction (with **Transaction not in balance**), a matched transaction outside **Undeposited Funds** (inspect transaction ID and Account Information), or a duplicate matched transaction in a Bank Deposit record, such as a multi-method cash sale (also **Transaction not in balance**). The duplicate case calls for checking that each matched transaction appears only once. [Raw: Error Creating Deposit, lines 64–81]
- Manual troubleshooting scripts are described only when Adyen SDRs are already created, through **Adyen - Bank Deposit Rec - Control Panel**. The page then points to a clean install to isolate customizations, release notes for known fixes, and Support with merchant account, test/live environment, reproduction, errors, logs and NetSuite settings if unresolved. [Raw: Error Creating Deposit, lines 83–84; later Steps 2–4, lines 86–105]
- The page does not define subsidiary/currency SDR profiles, credential roles, initial report retrieval, or settlement-type-map creation; follow the linked bundle setup source for those. Its 2023-last-modified, 2026-09-15 snapshot cannot establish current account configuration, successful rematch/deposit creation, or bank receipt.

## Detail locators

- Bundle setup route and SDR error-stage list: `Step 1: Check your bundle setup` and `Step 2: Check common error statuses`, lines 21–30.
- Match-not-found status, log/search-filter investigation, Settlement Type Map update and rematch: `Exceptions Need Resolving`, lines 32–62.
- Already-deposited, Undeposited Funds, duplicate Bank Deposit and conditional manual scripts: `Error Creating Deposit`, lines 64–84.
- Customization isolation, release notes and Support escalation details: later `Step 2` through `Step 4`, lines 86–105.

## Related

- [[adyen]] — provider page.
- [[adyen-netsuite]] — NetSuite bundle concept.
- [[source-adyen-docs-plugins-netsuite-reconciliation-bundle]] — SDR profile and Settlement Type Map setup route.

## Raw Sources

- [[raw/adyen/docs/plugins/netsuite/reconciliation-bundle/troubleshooting/2026-09-15|Adyen NetSuite reconciliation bundle troubleshooting (2026-09-15)]]
