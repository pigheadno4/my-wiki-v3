# docs-account-sales-day-payout-upgrade-to-sdp fixed queries

## Q1 — Purpose, scope, and what not to infer

**Question:** What change does this guide document, and which payout does it concern?

**Answer:** This 2026-09-15 capture explains the merchant's move from Pass-through payout, where funds enter a payable batch when a scheme or method settles, to Sales day payout, where one sales day's transactions are grouped in one payable batch paid after a fixed delay (raw lines 15–23). It also maps how SDR, PAR, Customer Area statuses and webhooks reflect the new model (lines 25–94). This is settlement of merchant sales funds, not a legacy Payout API transfer to a separate recipient. It does not specify the actual delay duration, cutoff, time zone, region, fees or account eligibility, or prove a merchant bank deposit. Canonical route: [[source-adyen-docs-account-sales-day-payout-upgrade-to-sdp]] → [[adyen-sales-day-payout]]; evidence: [[raw/adyen/docs/account/sales-day-payout/upgrade-to-sdp/2026-09-15]] lines 15–29, 42–49.

## Q2 — Central capability, prerequisites, and warnings

**Question:** Which reconciliation adjustments can the upgrade introduce, and how should failures and report/status evidence be read?

**Answer:** The guide lists SDR `CaptureFailed` debit, `RefundFailed` credit, `SettledReversed` debit and `RefundNotCleared` credit adjustments to prior `Settled` or `Refunded` entries; these are not new payments/refunds (raw lines 25–40). The capture/refund tables distinguish failure before versus after value date, 30-day non-clearing, late clearing and definitive failure across SDR, PAR, Customer Area and webhook columns (lines 42–94). A before-value-date reversal can have no SDR entry even while PAR/status changes; the 30-day reversal rows say no webhook. The `REFUND` webhook does not establish external-method acceptance (line 94). Read conflicting refund rows literally: lines 79–91 call a reversal a debit where an SDR cell says credit, show `CaptureFailed` PAR under a refund failure, and describe an already-debited balance after a credit reversal. No eligibility prerequisite or exact payout timing is supplied by this page. Canonical route: [[source-adyen-docs-account-sales-day-payout-upgrade-to-sdp]] → [[adyen-sales-day-payout]]; evidence: [[raw/adyen/docs/account/sales-day-payout/upgrade-to-sdp/2026-09-15]] lines 25–94.
