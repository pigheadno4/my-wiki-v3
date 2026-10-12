---
title: "CAPTURE_FAILED and REFUND_FAILED reasons | Adyen Docs"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/capture/failure-reasons"
raw_files:
  - "adyen/docs/online-payments/capture/failure-reasons/2026-09-15.md"
tags: [adyen, online-payments, capture, refund, failure-recovery, webhooks]
---

## Overview

This Adyen documentation page explains card-scheme rejection scenarios reported by `CAPTURE_FAILED` and `REFUND_FAILED` webhooks and the corresponding merchant, shopper, or Adyen recovery path. It covers online captures and refunds, including installment-based transactions.

## Key takeaways

- Adyen says card schemes treat captures and refunds the same for these failures. Online failure webhooks can include structured refusal fields in `additionalData`; when those fields are absent, use the top-level `reason`. Automations should key on `refusalReasonCode`, while allowing for codes that Adyen has not yet listed.
- Refusal details are operational evidence and must not be exposed to shoppers. `refusalReasonRaw` varies by payment method and region; for captures and refunds, its availability does not depend on the Customer Area Raw acquirer result setting.
- Recovery depends on the failure class. For a technical issue, Adyen attempts to fix and re-capture automatically; contact Support if that has not happened within 10 days. Pass-through payout merchants receive funds only after successful capture, so this failure delays settlement.
- A shopper-cancelled recurring payment cannot be re-captured by either the merchant or Adyen. For an incorrect request, Adyen directs the merchant to Support and says it will fix and re-capture the payment. For an account configuration error, re-capture becomes appropriate only after Adyen confirms the configuration has been corrected.
- An expired capture cannot reuse the authorization. Re-authorization in live Customer Area is limited to supported payment methods and requires the `Merchant re-authorise payments` role; otherwise, the merchant must create another payment request or send a payment link. If the scheme says a capture cannot be re-captured, the merchant must diagnose and fix the scheme-reported cause; for a refund failure, the merchant can instead agree another refund method with the shopper.

## Detail locators

- `Refusal reason fields` — automation key, fallback field, field definitions, evolving-code warning, Raw acquirer result distinction, and shopper-disclosure warning.
- `Technical issue` > `What you need to do` — Adyen re-capture behavior, success webhook values, 10-day Support threshold, and pass-through payout settlement delay.
- `Shopper cancelled the payment` > `What you need to do` — recurring-payment context and non-recapture outcome.
- `Incorrect request` and `Account configuration error` — diagnostic messages, Support inputs, who fixes the issue, and when re-capture is allowed.
- `Capture expired` > `What you need to do` — new-authorization requirement, limited re-authorization eligibility and role, fallback payment paths, and prevention references.
- `Capture cannot be re-captured` > `What you need to do` — merchant-owned correction, Support escalation details, and alternate refund method.

## Related

- Company: [[adyen]]
- Concept: [[adyen-payment-capture]]

## Raw Sources

- [[raw/adyen/docs/online-payments/capture/failure-reasons/2026-09-15|2026-09-15 snapshot — Adyen capture and refund failure reasons]]
