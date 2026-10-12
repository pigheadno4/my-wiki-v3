---
title: "Adyen Docs: ACH Direct Debit chargebacks"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/chargeback-guidelines/ach-chargebacks"
raw_files:
  - "adyen/docs/risk-management/chargeback-guidelines/ach-chargebacks/2026-09-15.md"
tags: [adyen, ach-direct-debit, ach-returns, chargebacks, risk-management]
---

## Overview

This 2026-09-15 [[adyen|Adyen]] guide covers ACH Direct Debit *returns*, which it also calls chargebacks, after an ACH payment has been authorized, captured, and settled. It explains return notices and webhooks, a three-day refund delay, and reason-code-specific retry decisions. Adyen says an ACH return cannot be defended; a permitted retry is a separate action and must not be inferred from an initial `Authorised` payment result. The guide belongs under [[adyen-risk-management|Adyen risk management]].

## Key takeaways

- The guide says ACH has no real-time authorization guarantee: an authorized debit can later reverse for insufficient funds, usually three to five days after payment. It gives consumer dispute windows of up to two years and business windows of up to one year after settlement for authorization-related returns. These are claims in the dated documentation snapshot, not a live determination of an individual return's deadline.
- Adyen delays refunds for three days after settlement. If a refund is requested but a customer initiates a return within that period, Adyen cancels the refund request automatically and sends a `CHARGEBACK` webhook. In the return flow, the optional request-for-permission and information-supplied stages do not yet deduct funds; at the Chargeback stage Adyen debits the merchant account.
- A bank-account Notice of Change can precede a return. If subscribed to the Direct Debit Notice of Change Notification webhook, the merchant receives an `ach.notificationOfChange` event. Adyen says it updates saved details as much as possible, including an existing recurring-payment `shopperReference` in many cases, but the merchant should inspect the event for missing details and ask the customer to update its own records when needed.
- Return reason codes appear in `NOTIFICATION_OF_CHARGEBACK` and `CHARGEBACK` webhooks and Customer Area. The guide's table covers common codes, not all cases: R01 and R09 allow at most two retries within 30 days of original authorization; R11 permits a retry within 60 days of original settlement while directing merchants to suspend recurring transactions and resolve the authorization issue; codes such as R02 (closed account) and R07 (revoked authorization) prohibit retry. Check the code and required remediation before acting. Adyen warns that repeated retries of transactions that cannot succeed can lead to Nacha fines and a block on new ACH Direct Debit transactions.
- In Adyen's test environment, an ACH payment with `ownerName` set to `chargeback:[REASON_CODE]` triggers the selected return scenario after capture and settlement. The test path skips the optional stages and Notification of Chargeback, going directly to Chargeback; the guide tells readers to wait for the `CHARGEBACK` webhook and verify the code in Customer Area.

## Detail locators

- **Scope, return timing, and prevention** — opening text and `## Causes of ACH chargebacks` through `## Reduce the chargeback risk`, raw lines 15-35; external account validation is recommended for a first transaction.
- **Refund effect and return stages** — `## Refunding disputed payments` through `## Chargeback`, raw lines 37-99; includes the refund-cancellation webhook, optional Notice of Change, optional bank-document stages, notification, and account debit.
- **Reason-code decisions and penalty** — `## Decide if you can retry the payment`, raw lines 101-130; read the full table for code-specific retry limits and customer or bank follow-up.
- **Test-only return scenario** — `## Test a chargeback scenario`, raw lines 132-557; versioned language examples, `ownerName` fixture, test-stage shortcut, and the webhook/Customer Area check.

## Related

- Company: [[adyen]]
- Main concept: [[adyen-risk-management]]

## Raw Sources

- [[raw/adyen/docs/risk-management/chargeback-guidelines/ach-chargebacks/2026-09-15|Adyen Docs — ACH Direct Debit chargebacks (2026-09-15)]]
