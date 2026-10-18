# Scheduled internal fund transfers — retrieval probes

## Q1 — Purpose and boundary

**Query:** What does this Adyen for Platforms page schedule, and does creating the schedule prove that money reached a user's bank account?

**Expected answer:** It configures sweeps that evaluate internal transfers between balance accounts within the platform. The guide's POST response and balanceAccountSweep.created webhook concern schedule creation. Resulting transfer requests are followed separately via outgoing/incoming transfer webhooks through received, authorised, booked or failed states. Neither an active schedule nor the Events-tab Success label alone proves booked movement or external bank receipt. The page has reused payout/bank-recipient wording and a later transfer-instrument description example; do not change the main internal balance-account scope from those passages.

**Raw locators:** lines 15-23 (identity); 415-448 (schedule creation and webhook); 819-825 (transfer request, booking, two entries); 869-877 (Events-table Success means transfer created); 490-817 (mixed payout/transfer-instrument text). **Canonical discovery route:** [[adyen-index]] → [[adyen-platform-internal-transfers]] → [[source-adyen-docs-platforms-internal-fund-transfers-scheduled-fund-transfers]] → [[raw/adyen/docs/platforms/internal-fund-transfers/scheduled-fund-transfers/2026-09-15]].

## Q2 — Capability, setup and warnings

**Query:** Can a platform schedule a weekly internal sweep between different account holders, what conditions and time zone matter, and how should a failed run be checked?

**Expected answer:** The captured guide requires a Platforms integration, Transfers API credential with TransferService Webservice Initiate role, Customer Area Initiate internal transfers and Balance platform base roles, configured transfer webhooks and Support enablement for the source balance account. For different account holders, the sender needs sendToBalanceAccount and receiver needs receiveFromBalanceAccount capability. The API cron expression is evaluated in the balance account's time zone; the currency must match a balance currency. The API flow defaults to the full available balance unless optional triggerAmount, targetAmount or sweepAmount changes it. Failure troubleshooting starts with the source available balance; if sufficient funds still fail, contact Support. These documented conditions do not prove any specific account is eligible or that a particular run booked. No unsupported cutoff, business-day, partial-transfer, return or automatic-retry guarantee should be inferred.

**Raw locators:** lines 25-42 (requirements); 112-128 (API fields and time zone); 415-460 (active schedule and amount controls); 819-840 (resulting status and failure). **Canonical discovery route:** [[adyen-index]] → [[adyen-platform-internal-transfers]] → [[source-adyen-docs-platforms-internal-fund-transfers-scheduled-fund-transfers]] → [[raw/adyen/docs/platforms/internal-fund-transfers/scheduled-fund-transfers/2026-09-15]]; consult the dedicated internal-transfer webhook guide for event detail.
