---
title: "Adyen Auto Rescue for Card Payments"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/auto-rescue/cards"
raw_files:
  - "adyen/docs/online-payments/auto-rescue/cards/2026-09-15.md"
tags: [adyen, auto-rescue, cards, recurring-payments, retries, webhooks]
---

## Overview

This Adyen guide covers Auto Rescue for refused shopper-not-present card payments. It explains account-level and per-transaction enablement, retry updates and final outcomes, optional payment-link recovery, cancellation, test scenarios, and reconciliation. Its card flow is separate from the overview's SEPA direct debit terminology issue.

## Key takeaways

- Adyen or its Support Team must enable the feature. Account-level enablement applies to eligible payments with `shopperInteraction: ContAuth` and a positive value, using a one-calendar-month rescue window. Per-transaction enablement requires Adyen configuration, an `autoRescue` flag, and a unique `merchantOrderReference` tied to the relevant billing cycle or subscription; `maxDaysToRescue` can specify 1–48 days. The guide recommends 30 days, while its example uses 40; neither number is a guaranteed retry duration.
- A refused payment response distinguishes `retry.rescueScheduled: true` from `false` and provides a `retry.rescueReference`. A scheduled rescue is a plan to attempt a later payment, not an authorization or successful collection. Ineligible failures such as fraud or account closure may not be rescued.
- Individual retry attempts are reported by `AUTHORISATION` webhooks; `success` and `retry.rescueScheduled` distinguish a successful retry, a failed retry with another attempt scheduled, and a failed retry without another scheduled attempt. An `AUTORESCUE` webhook reports the process end and whether rescue succeeded; in that event, `eventDate` is documented as the date the process started. If the merchant uses manual capture, each rescued payment still needs capture to transfer funds to its account.
- If a shopper supplies new payment details or cancels a subscription during rescue, the guide directs the merchant to cancel the rescue using the Payment API `/cancel` with the rescue reference as `originalReference` and `cancellationType: autoRescue`. The immediate `[cancel-received]` response is receipt of the request; the later `CANCEL_AUTORESCUE` webhook reports whether cancellation succeeded.
- After an unsuccessful process, a separately activated Pay by Link option can include a five-day payment link in the end webhook. The guide also supplies test-only `autoRescueScenario` values. Every retry attempt is a separate transaction with its own `pspReference`; `merchantOrderReference` connects attempts for reporting.

## Detail locators

- `## Step 1: Enable Auto Rescue` (raw lines 35–75): Adyen configuration, account/transaction eligibility, unique order reference, flags, and rescue-window range. Version-qualified Checkout request examples occupy raw lines 77–461.
- Payment response after the request (raw lines 464–497): refused result, scheduled versus unscheduled rescue, and rescue reference.
- `## Step 2: Receive Auto Rescue updates` (raw lines 499–654): retry `AUTHORISATION` webhooks, manual-capture warning, final `AUTORESCUE` outcome, and reason codes.
- `## Send a payment link` (raw lines 656–701): separately enabled post-failure link, expiry, and subsequent payment notification.
- `## Cancel Auto Rescue` (raw lines 703–777): cancellation conditions, Payment API request, distinct cancellation PSP reference, and eventual cancellation webhook.
- `## Test Auto Rescue and go live` and `## Auto Rescue reports` (raw lines 779–857): test scenarios, reporting configuration, distinct retry transactions, and order-reference correlation.

## Related

- Company: [[adyen]]
- Concept: [[adyen-card-auto-rescue]]
- Related concept: [[recurring-payments]]
- Overview source: [[source-adyen-docs-online-payments-auto-rescue]]

## Raw Sources

- [[raw/adyen/docs/online-payments/auto-rescue/cards/2026-09-15|2026-09-15 Adyen Auto Rescue card guide]]
