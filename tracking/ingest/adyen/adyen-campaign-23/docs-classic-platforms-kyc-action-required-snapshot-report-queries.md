# C23 worker retrieval checks — docs-classic-platforms-kyc-action-required-snapshot-report

## Q1: Which sub-merchants appear in this KYC report and how is it produced?

The captured Classic report covers sub-merchants who **processed a payment or received a fund transfer in the last three months and have not completed KYC** (raw line 18). Customer Area configures its CSV schedule daily, weekly or monthly; the page calls the subscription default (lines 18, 22–24). Its columns include account-holder identity, deadline/tier/status and four verification checks (lines 26–43). Forward route: [[index]] → [[adyen-index]] → [[adyen-classic-platforms]] → [[source-adyen-docs-classic-platforms-kyc-action-required-snapshot-report]] → [[raw/adyen/docs/classic-platforms/kyc-action-required-snapshot-report/2026-09-15]].

## Q2: What does this snapshot miss or leave unresolved?

It excludes inactive-for-three-months incomplete-KYC holders by its population rule, and Adyen recommends real-time **notifications** for faster identification (raw lines 18–20). The report's Entity type column says only Business or Individual (line 34), while the related [[source-adyen-docs-classic-platforms-account-holders-and-accounts|Classic creation guide]] lists five types ([[raw/adyen/docs/classic-platforms/account-holders-and-accounts/2026-09-15|related raw lines 25–29]]); the mapping is unspecified. The report is a dated snapshot, not evidence that KYC later passed, payout was enabled or payment succeeded. Forward route: [[index]] → [[adyen-index]] → [[adyen-classic-platforms]] → [[source-adyen-docs-classic-platforms-kyc-action-required-snapshot-report]] → [[raw/adyen/docs/classic-platforms/kyc-action-required-snapshot-report/2026-09-15]].
