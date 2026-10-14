---
title: "Adyen Terminal API numeric shopper input"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/shopper-engagement/shopper-input/digit"
raw_files:
  - "adyen/docs/point-of-sale/shopper-engagement/shopper-input/digit/2026-09-15.md"
tags: [adyen, point-of-sale, shopper-engagement, terminal-api, numeric-input]
---

## Overview

Adyen's digit-input guide describes a Terminal API **Device/Input** request that asks a shopper or staff member to enter a numerical string on a payment terminal. Its example collects a ZIP code; the resulting `DigitInput` is not automatically format-validated and must be handled by the merchant system. This input operation is separate from the linked amount-input path and is not evidence of a payment, identity verification, secure PIN collection or valid consent. The 2026-09-15 snapshot does not establish current terminal-model eligibility. [[adyen]] [[adyen-pos-shopper-engagement]] [[adyen-terminal-api]]

## Key takeaways

- The request is for a Terminal API payment-terminal integration. `SaleToPOIRequest.MessageHeader` uses `MessageClass=Device`, `MessageCategory=Input` and `MessageType=Request`; its `ServiceID` is 1–10 alphanumeric characters and unique for the terminal `POIID` over the previous 48 hours. The source gives no model-specific support table. See `## Requirements` and `## Make a Digit input request`.
- `InputRequest.DisplayOutput` targets `CustomerDisplay` with `InfoQualify=Display`, text output and `PredefinedContent.ReferenceID=GetDigit`. Its single custom text line is about 20 characters on a portrait display, and the terminal adds a confirmation instruction. `InputRequest.InputData` targets `CustomerInput` with `InfoQualify=Input` and `InputCommand=DigitString`; `MaxInputTime` is a seconds timeout and `DefaultInputString` is placeholder text for expected format, not proof of a prefilled/validated value. The sample's 30 seconds and ZIP placeholder are examples, not defaults. See `## Make a Digit input request`.
- The guide offers a mask-user-input flag with true/false values. Its parameter table spells the field `MaskChararctersFlag` while the JSON request sample spells `MaskCharactersFlag`, and the Java sample omits it; verify the actual API field before implementation. Masking is a display option, not a claim that the input is a certified PIN flow or protected in transit/storage. The guide gives no digit-length or ZIP/phone format validation rule. See `## Make a Digit input request`.
- A successful `InputResult.Input.DigitInput` contains the entered numerals as a string. The guide explicitly says input is **not validated against a format**, then instructs the POS system to validate and use the returned value. The illustrative ZIP response is not a proof that a shopper entered a valid postal code. See response step 2 and step 3 under `## Make a Digit input request`.
- The prompt remains until input arrives, the configured maximum time expires, the terminal Cancel key is selected, or the terminal receives a cancel-input/other POS-app request. Timeout returns input `Failure/Cancel` with `message=Screen%20timeout`; shopper Cancel returns `Failure/Cancel` with an empty `DigitInput`. A payment request while input is pending overrides it and returns input `Failure/Busy` with a higher-priority-request message. These are input-response outcomes, not payment results. See `## How it works` and the response notes under `## Make a Digit input request`.

## Detail locators

- `## Requirements` and `## How it works`: Terminal API scope and events ending the pending prompt.
- `## Make a Digit input request`: MessageHeader, GetDigit display and DigitString input fields, portrait text guidance, mask-field spelling conflict, request examples and timeout configuration.
- Response notes under `## Make a Digit input request`: `DigitInput` value, lack of format validation, timeout/Cancel/Busy responses and merchant-side validation handoff.

## Related

- [[adyen-pos-shopper-engagement]] — terminal shopper interaction routes.
- [[adyen-terminal-api]] — request and response envelope.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/shopper-engagement/shopper-input/digit/2026-09-15|Adyen numeric input guide, fetched 2026-09-15]]
