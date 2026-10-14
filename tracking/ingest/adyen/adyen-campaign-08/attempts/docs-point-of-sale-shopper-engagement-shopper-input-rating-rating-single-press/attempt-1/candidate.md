---
title: "Adyen one-key POS rating input"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/shopper-engagement/shopper-input/rating/rating-single-press"
raw_files:
  - "adyen/docs/point-of-sale/shopper-engagement/shopper-input/rating/rating-single-press/2026-09-15.md"
tags: [adyen, point-of-sale, shopper-engagement, terminal-api, rating, input]
---

## Overview

Adyen's single-key rating guide, captured 2026-09-15, describes `GetOneKeyRating` as an alternative to the default `GetRating` Terminal API input request. A shopper's single key press answers and sends the response immediately, with no separate confirmation step described. This [[adyen-pos-shopper-engagement]] interaction gathers a rating, not a payment result, consent record, validated survey response, or proof of a particular customer identity.

## Key takeaways

- **Device and request scope.** The dated guide requires a Terminal API integration and lists M400, P400 Plus, V400m, M450, P630, AMS1, S1F2, S1F2L, S1E2L and SFO1 as supported terminals. The `SaleToPOIRequest.MessageHeader` is protocol 3.0, `MessageClass: Device`, `MessageCategory: Input`, `MessageType: Request`, with SaleID, POIID and a ServiceID unique for the terminal within the prior 48 hours. The list does not establish current model, merchant or regional availability; uniqueness is not an idempotent-retry guarantee.
- **Display and input fields have distinct roles.** `InputRequest.DisplayOutput` targets `CustomerDisplay`, uses Text output and `PredefinedContent.ReferenceID: GetOneKeyRating`, with up to four merchant text fields: question, scale label, skip label and optional footer. The first text is bold; `\n` starts a new line. `InputRequest.InputData` targets `CustomerInput`, uses `InputCommand: DigitString` and an integer `MaxInputTime` in seconds. The page gives no separate maximum DigitInput length or fixed rating-scale validation rule.
- **Read the response by outcome.** The guide says input is not validated against a format and directs the merchant system to validate and use `InputResult.Input.DigitInput`. Its example is a shopper-entered `9` with `InputResult.Response.Result: Success`. A timeout returns `Failure`/`Cancel` with `message=Screen%20timeout`; shopper Cancel or Skip yields an empty `DigitInput` and `Failure`/`Cancel`. If a payment request arrives while input is pending, it overrides the input request, which fails with `Busy` and a higher-priority-request message. The payment request's own financial result is separate.
- **The prompt can end in other ways.** The guide says input, expiry of `MaxInputTime`, terminal Cancel, a dedicated cancel-input request, or any other POS app request ends the displayed input request. Do not treat a missing rating as a zero score or silently retry a pending interaction.

## Detail locators

- Raw opening and `## Requirements` (lines 15–30): one-key alternative and dated model list.
- Raw `## How it works` (lines 32–47): display duration and terminal/POS cancellation or override triggers.
- Raw `## Make a Rating input request` field tables (lines 49–87): Device/Input header, display text positions, `GetOneKeyRating`, `DigitString`, `MaxInputTime` and 48-hour ServiceID uniqueness.
- Raw JSON and Java examples (lines 89–181): sample question, scale, Skip, 30-second timeout and request construction; sample values are illustrative.
- Raw response handling (lines 183–228): no format validation, `DigitInput`, success example, timeout, payment override, Cancel/Skip and merchant-side validation.
- Raw `## See also` (lines 230–235): separate default rating, cancel-input, input-type and session guides; navigation only.

## Related

- [[adyen-pos-shopper-engagement]] — POS customer-interaction hub.
- [[adyen-terminal-api]] — Terminal API and financial-message boundary.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/shopper-engagement/shopper-input/rating/rating-single-press/2026-09-15|Ask for a rating—single key press, fetched 2026-09-15]]
