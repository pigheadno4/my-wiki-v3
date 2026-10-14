---
title: "Ask for amount input | Adyen Docs"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/shopper-engagement/shopper-input/amount"
raw_files:
  - "adyen/docs/point-of-sale/shopper-engagement/shopper-input/amount/2026-09-15.md"
tags: [adyen, point-of-sale, shopper-engagement, terminal-api, input, amount]
---

## Overview

Adyen's GetAmount guide describes a **Terminal API Device/Input interaction** that asks a shopper or staff member to enter an amount on a payment terminal, such as a proposed share of a split bill. The terminal returns the entered `DigitInput` for the merchant system to validate and use. The input request itself does not authorize, capture, split, refund or settle a payment, and the page gives no consent or successful-payment proof. [[adyen]] [[adyen-pos-shopper-engagement]] [[adyen-terminal-api]]

## Key takeaways

- A Terminal API integration with a payment terminal is required. The `GetAmount` request uses `MessageClass: Device`, `MessageCategory: Input`, and an `InputRequest` with `DisplayOutput` for terminal text and `InputData` for `CustomerInput`. Its input command is `DecimalString`, with a configurable `MaxInputTime` in seconds and a format placeholder such as `0.00`. The header table gives a terminal-scoped `ServiceID` uniqueness rule of 1–10 alphanumeric characters within 48 hours; this is not an idempotency or safe-retry guarantee. See **Requirements** and **Make an Amount input request**, pinned raw lines 21–27 and 68–104.
- The terminal shows a currency and two-decimal placeholder; entered digits populate from right to left in the EUR 36.59 example. The default currency is the first currency configured for the store, or for the merchant account when it represents the physical store. The guide does not say the request itself charges that currency or that the displayed number has passed merchant validation. Custom prompt text is limited to about 20 characters on a portrait display. See pinned raw lines 19, 50–66 and 86–104.
- The input screen remains until the shopper/staff submits input, `MaxInputTime` expires, terminal **Cancel** is selected, or the terminal receives a POS cancel-input request or another POS request. On input, `InputResult.Input.DigitInput` carries the amount string; pass it to the merchant system for validation and further use. `InputResult.Response.Result: Success` in the example is an **input** result, not financial authorization. See pinned raw lines 29–36 and 184–234.
- A timeout returns `InputResult.Response` with `Result: Failure`, `ErrorCondition: Cancel` and `AdditionalResponse: message=Screen%20timeout`. User Cancel gives an empty `DigitInput` with Failure/Cancel. A payment request arriving while input waits **overrides** it, yielding input Failure/`ErrorCondition: Busy` and the higher-priority-request message. Do not treat these three outcomes as the same merchant amount choice. See pinned raw lines 228–232.
- The JSON request and response use protocol version 3.0 and illustrate one V400m `POIID`; the Java snippet uses the generated enum `DIGIT_DECIMAL` for the input command. These are examples, not evidence of current model eligibility or a specific account's enabled features. See pinned raw lines 108–226.

## Detail locators

- **Ask for amount input; Requirements; How it works** (pinned raw lines 15–48) — purpose, Terminal API prerequisite, screen termination conditions and device illustrations.
- **Entering an amount; Currency** (pinned raw lines 50–66) — right-to-left two-decimal example and store/merchant-account default currency lookup.
- **Make an Amount input request** (pinned raw lines 68–104) — Device/Input header, `GetAmount` display output, `DecimalString`, `MaxInputTime`, placeholder and prompt length.
- **JSON; Java** (pinned raw lines 108–182) — illustrative request and generated-library field mapping.
- **Input response and outcomes** (pinned raw lines 184–234) — `DigitInput`, success, timeout Cancel, user Cancel, payment-override Busy and merchant validation.
- **See also** (pinned raw lines 236–240) — cancel-input, other input type and multi-request session navigation.

## Related

- [[adyen-pos-shopper-engagement]] — primary terminal-interaction route.
- [[adyen-terminal-api]] — Terminal API message architecture; this input's amount is not a PaymentRequest amount.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/shopper-engagement/shopper-input/amount/2026-09-15|Adyen GetAmount input guide, fetched 2026-09-15]]
