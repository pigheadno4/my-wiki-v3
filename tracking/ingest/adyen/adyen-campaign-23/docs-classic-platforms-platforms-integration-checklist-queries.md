# C23 worker queries — Classic Platforms integration checklist

Route: [[index]] → [[adyen-index]] → [[adyen-classic-platforms]] → [[source-adyen-docs-classic-platforms-platforms-integration-checklist]] → [[raw/adyen/docs/classic-platforms/platforms-integration-checklist/2026-09-15]].

## Q1. What is this checklist for, and what must be set up before following it?

It is the **Classic** Adyen for Platforms integration and go-live checklist; new implementers are directed to the separate new integration guide (raw line 19). It assumes a test integration and choices for information collection, HOP versus custom onboarding, and payout method (raw lines 23–37). A test account plus platform and payments API credentials are required to verify the integration (raw lines 50–63). The test sequence covers account-holder onboarding/verification, split payments, payouts, notification webhooks and reconciliation (raw lines 39–48).

## Q2. Which verification, payout and live boundaries matter?

A sub-merchant/account holder must complete verification before payouts (raw line 75). A HOP return or custom data submission requires notification-based status follow-up (raw lines 97–106, 116–124). The payout step calls a `/payoutAccountHolder` 200 response successful (raw lines 143–150), while the next step says Classic Platforms API requests are asynchronous and notifications supply final results (raw lines 154–165); a 200 does not independently prove bank receipt. The live checklist requires a contract/live account, settings and credential changes, then lifecycle testing; test setup alone does not establish live eligibility or real payment/payout success (raw lines 183–242).
