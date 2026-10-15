---
title: "Adyen Classic failed captures and refunds"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/classic-integrations/modify-payments/capture/failure-reasons"
raw_files:
  - "adyen/docs/online-payments/classic-integrations/modify-payments/capture/failure-reasons/2026-09-15.md"
tags: [adyen, classic-api, capture, refund, failure-recovery, webhooks]
---

## Overview

This Classic payment-modification page lists five card-scheme rejection scenarios for failed captures and says the scenarios also apply to failed refunds. In this **Classic** guide, a `CAPTURE_FAILED` webhook reports the capture failure but not its reason; the merchant looks up the error and indicated action on the Payment details page in Customer Area. This differs from the separately ingested newer capture-failure guide, which describes structured refusal fields. See [[adyen]], [[adyen-payment-capture]] and [[source-adyen-docs-online-payments-classic-integrations-modify-payments-capture]].

## Key takeaways

- **Technical issue:** Adyen says it will try to fix the issue and re-capture; the merchant need not initiate a retry. If re-capture succeeds, payment status becomes `SentForSettle` and a `CAPTURE` webhook carries `success: true` and `reason: Transaction Recaptured`. Contact Support if it has not re-captured within 10 days. For pass-through payout, settlement and payout are delayed until successful capture.
- **Shopper-cancelled recurring payment:** If a shopper cancels through the bank before capture, the page says neither Adyen nor the merchant can re-capture that transaction; it suggests contacting the shopper. This is not a technical retry case.
- **Incorrect request:** The merchant gives Support the capture-request PSP reference and scheme error; the page says Adyen will fix the issue and re-capture. **Account configuration error:** the merchant gives the same evidence to Support, but re-captures affected payments only **after** Adyen confirms the account configuration is corrected. These are different retry owners and conditions.
- **Capture expired:** A late capture cannot reuse the authorization; funds would require a new authorization. The page directs the merchant to Support if it wants to re-authorize, and to scheme validity/authorization-extension routes for future prevention. It does not claim that extending an already expired authorization recovers it.
- The page says card schemes treat capture and refund failures alike for these scenarios, but its recovery instructions are often explicitly about **re-capture**. Do not infer identical refund retry mechanics, a successful refund, or chargeback reversal. It does not define partial-capture amount/balance limits; use the sibling Classic capture guide for those conditions. Neither a failed-capture webhook nor a recapture attempt establishes final settlement.

## Detail locators

- Lines 19–31: five scenario list, refund applicability, reasonless Classic `CAPTURE_FAILED` webhook and Customer Area diagnosis.
- `## Technical issue` (lines 33–49): Adyen-owned retry, success event, 10-day Support threshold and pass-through payout delay.
- `## Shopper cancelled the payment` (lines 51–59): recurring cancellation and no-recapture boundary.
- `## Incorrect request` and `## Account configuration error` (lines 61–93): scheme error, capture PSP reference, Support actions and distinct re-capture ownership.
- `## Capture expired` (lines 95–109): new authorization requirement and future validity/extension references.

## Related

- [[adyen-payment-capture]] — provider capture concept and reciprocal source route.
- [[source-adyen-docs-online-payments-classic-integrations-modify-payments-capture]] — Classic capture requests, webhooks and partial-capture limits.
- [[source-adyen-docs-online-payments-capture-failure-reasons]] — newer online-payments failure/refusal-field guide; use its own scope.

## Raw Sources

- [[raw/adyen/docs/online-payments/classic-integrations/modify-payments/capture/failure-reasons/2026-09-15|Classic failed captures and refunds, captured 2026-09-15]]
