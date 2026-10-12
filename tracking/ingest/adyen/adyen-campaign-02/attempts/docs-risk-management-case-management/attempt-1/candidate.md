---
title: "Adyen Case Management"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/case-management"
raw_files:
  - "adyen/docs/risk-management/case-management/2026-09-15.md"
tags: [adyen, risk-management, case-management, manual-review, capture, webhooks]
---

## Overview

This [[adyen]] guide describes premium risk case management for manually reviewing eligible online-payment transactions after authorization and before capture. Merchant-defined custom risk rules with a **Review** action send a transaction to the Customer Area queue, where a reviewer can accept or reject it. The guide covers prerequisites, `fraudResultType=AMBER`, configurable payment modifications and notifications, expiry, and case review tools. See [[adyen-risk-management]] for provider context.

## Key takeaways

- Case management requires an online-payments integration, enabled risk and premium features, plus an authorized Customer Area reviewer role. Zero-value authorizations cannot enter case management. A transaction blocked by another risk rule is refused instead of being sent for review.
- With risk-result data enabled, an in-review payment carries `additionalData.fraudResultType=AMBER` in the payment response and `AUTHORISATION` webhook. For PayPal, the guide says `AMBER` arrives only in that webhook. In this context, `AMBER` means authorized but not automatically captured, so merchant order and fulfillment logic must account for the pending review.
- If case-management capture delay is enabled, the guide gives up to seven calendar days to reject and says an untouched case expires and is automatically accepted, with funds captured according to capture settings. The same page separately lets the company configure **Expire** as Capture, Cancel, or None, and says manual-capture users must capture an accepted payment themselves. Read the expiry statement together with those settings; do not infer universal automatic capture or a settled payment.
- Company-level case behavior settings choose payment modifications on Accept, Reject, and Expire: capture, cancel/refund as appropriate for the payment method, or no modification. Notifications are separately selectable; configured `MANUAL_REVIEW_ACCEPT` and `MANUAL_REVIEW_REJECT` webhooks support asynchronous order-state updates. Capturing, canceling, or refunding an open payment outside case management closes its case.
- Reviewers can assign and decide cases in the queue. Shopper DNA spans merchant accounts in the company, but shopper attributes are masked by default and unmasked data requires the **Merchant View PII** role. A cancellation caused by rejecting a case is a permanent payment decision; changing the closed case's Fraud/Genuine manual status does not reverse it.

## Detail locators

- **Purpose, eligibility, roles, and exclusions:** raw lines 15–40.
- **Review signal, PayPal exception, and merchant follow-up:** raw lines 42–65.
- **Trigger, blocked-risk exclusion, conditional seven-day expiry, and capture behavior:** raw lines 76–134.
- **Notification settings and example webhook:** raw lines 136–179.
- **Queue, shopper DNA access, decisions, and irreversible rejected cancellation:** raw lines 181–281.

## Related

- [[adyen]]
- [[adyen-risk-management]]
- [[adyen-webhooks]]

## Raw Sources

- [[raw/adyen/docs/risk-management/case-management/2026-09-15|Adyen Case management — collected 2026-09-15]]
