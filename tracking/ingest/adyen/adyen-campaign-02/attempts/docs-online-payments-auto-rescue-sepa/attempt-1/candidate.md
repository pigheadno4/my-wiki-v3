---
title: "Adyen Docs: Auto Rescue for SEPA payments"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/auto-rescue/sepa"
raw_files:
  - "adyen/docs/online-payments/auto-rescue/sepa/2026-09-15.md"
tags: [adyen, online-payments, auto-rescue, sepa, direct-debit]
---

## Overview

This [[adyen]] guide describes Auto Rescue for shopper-not-present SEPA direct debit payments. The page title and description call the transactions "refused," while the operative flow says a SEPA payment first returns `AUTHORISED` and Auto Rescue applies after a chargeback with reason **AM04** (insufficient funds) or **MS03** (no reason specified, used in some regions instead of AM04). This resolves which event the SEPA guide acts on without treating a SEPA `AUTHORISED` response as final collection. The 2026-09-15 snapshot describes configuration, two-attempt limit, webhook outcomes, cancellation, testing, and reporting; it does not establish live enablement or a successful recovery.

## Key takeaways

- Adyen Support or an Account Manager must configure Auto Rescue for SEPA at account or transaction level. The account-level rescue window is 42 days. Transaction-level use then flags the payment request with `autoRescue` and a unique `merchantOrderReference`; `maxDaysToRescue` can be 1–42 days, with 30 days recommended rather than required. See **Step 1: Enable Auto Rescue**.
- SEPA rescue has a maximum of two attempts within the rescue window. The guide ties that limit to the longer delay before a first decline message and potential bank fines for chargebacks. Its example `/payments` request is shopper-not-present (`shopperInteraction: ContAuth`) and uses test endpoints and versioned library examples; these examples are not proof of current SDK behavior or a live payment.
- A later `CHARGEBACK` event with a qualifying reason can start rescue despite the initial `AUTHORISED` response. `AUTORESCUE` webhook outcomes distinguish a successful first attempt with `retryWindowHasElapsed`, a successful second attempt with `maxRetryAttemptsReached`, and failure after chargebacks on both retries with `maxRetryAttemptsReached` and `success: false`. The page says the webhook is received 16 days after a rescue attempt. See **Step 2: Receive Auto Rescue updates**; do not read `maxRetryAttemptsReached` alone as a failure.
- After unsuccessful rescue, Pay by Link is optional and requires Support activation; the page gives a five-day payment-link validity. To stop rescue when the shopper supplies another method or cancels a subscription, the merchant sends a classic Payment API `/cancel` using the original rescue reference and `cancellationType: autoRescue`; the `cancel-received` response is followed by a `CANCEL_AUTORESCUE` webhook that reports whether cancellation succeeded. See **Send a payment link** and **Cancel Auto Rescue**.
- Each retry is a separate transaction with a unique `pspReference`. `merchantOrderReference` connects retries to the original billing cycle in updates and configured reports; if omitted, the reporting column falls back to the original request's `pspReference`. See **Auto Rescue reports**.

## Detail locators

- **Opening explanation, lines 17–29** — SEPA authorization versus chargeback trigger, AM04/MS03 reasons, and two-attempt limit.
- **Step 1: Enable Auto Rescue, lines 47–82** — support configuration, account versus transaction scope, rescue window, unique order reference, and request fields. The examples below it use test URLs and named library versions.
- **Payment response and CHARGEBACK webhook, lines 445–508** — initial `Authorised` result, rescue reference, chargeback reason, and scheduled rescue example.
- **Step 2: Receive Auto Rescue updates, lines 510–644** — event timing, success/failure combinations, reason codes, and example payloads.
- **Send a payment link / Cancel Auto Rescue, lines 646–764** — optional activation, expiration, classic cancellation request, `cancel-received` response, and later cancellation webhook.
- **Test Auto Rescue and go live / Auto Rescue reports, lines 766–851** — test scenario controls, distinct retry references, and report linkage.

## Related

- [[adyen-online-payments]]
- [[adyen-webhooks]]
- [[source-adyen-docs-online-payments-auto-rescue]]

## Raw Sources

- [[raw/adyen/docs/online-payments/auto-rescue/sepa/2026-09-15|Adyen Docs — Auto Rescue for SEPA payments (2026-09-15)]]
