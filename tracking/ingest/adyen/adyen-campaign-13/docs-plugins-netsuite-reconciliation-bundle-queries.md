# Fixed queries — docs-plugins-netsuite-reconciliation-bundle

## Q1 — Purpose, scope, and what must not be inferred

**Answer:** This captured Adyen guide describes the NetSuite bank-deposit reconciliation bundle. It imports Adyen Settlement Detail Reports, matches entries by PSP reference and record type to NetSuite transactions, and creates NetSuite Bank Deposit records. It is scoped to configured merchant account, subsidiary, currency, mapped transaction fields, and NetSuite accounts. The NetSuite record or SDR processing state is not independent proof of bank-credit arrival, complete reconciliation, or correct accounting. The snapshot does not verify live bundle sharing or installed configuration.

**Raw locators:** lines 15–19 (identity and workflow); 23–61 (setup and account/credential scope); 63–96 (profile granularity and deposit creation); 98–114 (matching); 116–151 (process/status/manual upload).

**Canonical route:** [[adyen-index]] → [[adyen-netsuite]] → [[source-adyen-docs-plugins-netsuite-reconciliation-bundle]] → [[raw/adyen/docs/plugins/netsuite/reconciliation-bundle/2026-09-15]].

## Q2 — Central capability, prerequisites, and warnings

**Answer:** Add an Adyen payout account/currency and subscribe to the SDR; install bundle ID 226682, which must be shared with the NetSuite account. Configure test/live domain and an Adyen Reporting API credential/basic-auth password. Create SDR Profiles for merchant account and each subsidiary/currency, with valid deposit and relevant fee/adjustment accounts. Map SDR Type fields and PSP field IDs for SETTLED, REFUNDED, CHARGEBACK and REVERSED, leaving saved-search defaults. Automatic Deposit creation is optional; otherwise SDR approval precedes Bank Deposit creation. Scheduled polling can be manually staged through poll/receive, match, and create actions; errors route to troubleshooting. Manual CSV upload is described, but this source does not state safe retry/dedup behavior, so do not blindly reprocess pending or errored reports.

**Raw locators:** lines 23–40 (prerequisites, bundle/sharing); 42–61 (Reporting credential and profiles); 63–96 (scope, account settings and auto/approval option); 98–114 (mapping); 116–151 (scheduled/manual/status/upload routes).

**Canonical route:** [[adyen-index]] → [[adyen-netsuite]] → [[source-adyen-docs-plugins-netsuite-reconciliation-bundle]]; complete fields and steps at [[raw/adyen/docs/plugins/netsuite/reconciliation-bundle/2026-09-15]].
