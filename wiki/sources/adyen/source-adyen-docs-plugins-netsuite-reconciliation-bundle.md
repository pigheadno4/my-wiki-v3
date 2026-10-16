---
title: "Adyen NetSuite reconciliation bundle"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/netsuite/reconciliation-bundle"
raw_files:
  - "adyen/docs/plugins/netsuite/reconciliation-bundle/2026-09-15.md"
tags: [adyen, netsuite, settlement-detail-report, reconciliation, bank-deposits]
---

## Overview

Adyen's NetSuite reconciliation bundle is a NetSuite bank-deposit reconciliation workflow. It pulls Adyen Settlement Detail Reports (SDRs), matches entries to NetSuite transactions using PSP reference and record type, and creates NetSuite Bank Deposit records in configured accounts. A created NetSuite record is a reconciliation artifact, not independent evidence that a bank received funds. This 2026-09-15 captured page has older 2023 last-modified metadata and does not establish a particular account's installed bundle or processing result. [[adyen]] [[adyen-netsuite]]

## Key takeaways

- Setup begins with an Adyen payout account and currency and a subscription to the Settlement Detail Report. The page then installs the **ADYEN - Bank Deposit Reconciliation** SuiteBundle (ID 226682), configures NetSuite Adyen Integration Settings with `ca-test` or `ca-live` and an Adyen **Reporting** API credential/basic-auth password, and creates SDR Profiles. If the bundle search or Install button is missing, the page says it has not been shared with the NetSuite account and directs the user to Adyen support with the account number.
- An SDR Profile selects the Adyen merchant account, NetSuite subsidiary, deposit account, and settlement currency. The page requires separate profiles for each subsidiary/currency and, when the SDR has multiple settlement currencies to match, one profile for each. A profile marked inactive is not used by the bundle. Fee, adjustment, chargeback, error-notification and warning settings are field-specific; `Invoice correction account` and `Consolidate Invoice Corrections` are explicitly marked **Not used**.
- A Settlement Type Map pairs SDR CSV column/Type values with NetSuite script IDs and saved searches. The listed `SETTLED`, `REFUNDED`, `CHARGEBACK`, and `REVERSED` types can be matched to corresponding NetSuite transactions using a PSP field ID; the page says to leave saved-search defaults. Matching depends on the mapped references and account/currency scope, and a match is not a bank-credit confirmation.
- **Automatically Create Deposits** controls whether Bank Deposit transactions are created on SDR generation or SDR records require approval first. The background process runs on a schedule; the Control Panel offers separate manual actions to poll/receive SDRs, find detail matches, and create Bank Deposits. The status page has `Pending Approval` → `Creating Deposits` and an error route. These states describe NetSuite processing, not completed external settlement.
- The guide also permits manually uploading an SDR CSV, for example in advanced testing. It does not state deduplication or safe-replay behavior for repeated polling, manual import, approval, or deposit creation, so this snapshot alone cannot justify reprocessing a pending or errored report. Consult the linked troubleshooting route for a concrete error before corrective action.

## Detail locators

- Opening and `## Setup and installation`, lines 19–61: SDR/PSP matching, payout-account and SDR-subscription prerequisites, bundle ID/sharing, Reporting credential, environment domain, and profile creation.
- `## Adyen SDR profile fields`, lines 63–96: merchant account, subsidiary/currency granularity, eligible deposit and fee accounts, inactive/unused fields, automatic-versus-approved deposit creation, notification, and Pacific-time date option.
- `### Create a new mapping`, lines 98–114: SDR CSV fields, four Type values, PSP field ID and saved-search defaults.
- `## Polling for new Settlement Detail Reports` and `## Check status`, lines 116–141: scheduled process, manual control-panel stages, approval and error states.
- `## Manually upload a Settlement Detail Report`, lines 143–151: manual CSV upload route and sample-report navigation.

## Related

- [[adyen-netsuite]] — provider NetSuite integration concept, pending promotion with this campaign.
- [[source-adyen-docs-reporting-settlement-reconciliation-transaction-level-settlement-details-report]] — Adyen SDR entry and field reference; its report statements do not prove bank receipt.

## Raw Sources

- [[raw/adyen/docs/plugins/netsuite/reconciliation-bundle/2026-09-15|Adyen NetSuite reconciliation bundle guide, fetched 2026-09-15]]
