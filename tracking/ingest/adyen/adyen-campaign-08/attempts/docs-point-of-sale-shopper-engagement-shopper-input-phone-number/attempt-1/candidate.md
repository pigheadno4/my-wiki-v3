---
title: "Adyen POS phone-number input"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/shopper-engagement/shopper-input/phone-number"
raw_files:
  - "adyen/docs/point-of-sale/shopper-engagement/shopper-input/phone-number/2026-09-15.md"
tags: [adyen, point-of-sale, shopper-engagement, terminal-api, phone-number, input]
---

## Overview

This Adyen Terminal API guide, last modified 2025-03-14 and captured 2026-09-15, describes collecting a shopper's phone number on a payment terminal with a nonfinancial `Device` / `Input` request. The terminal pre-fills a country code based on terminal location but allows a change; its response returns entered `DigitInput` for the merchant system to validate and use. Collection and a `Success` input result do not establish phone ownership, identity, contact consent or payment authorization. [[adyen]] [[adyen-pos-shopper-engagement]] [[adyen-terminal-api]]

## Key takeaways

- The stated requirement is a Terminal API integration with payment terminals. Send a `SaleToPOIRequest` with `MessageClass=Device`, `MessageCategory=Input`, `MessageType=Request`, protocol version 3.0 and terminal-scoped request identifiers. `DisplayOutput` uses `CustomerDisplay`, text output and `PredefinedContent.ReferenceID=GetPhoneNumber`; its one `OutputText.Text` is the merchant's prompt. The terminal adds its own instruction for confirming input, but this guide does not define an independent verified-confirmation flag.
- `InputData` uses `CustomerInput`, `InputCommand=DigitString`, and integer `MaxInputTime` measured in seconds. `DefaultInputString` is described as placeholder text showing the expected format; it is not the location-based country-code rule. `MaskCharactersFlag` is shown in the JSON example to mask entered digits. The parameter table misspells it `MaskChararctersFlag`; do not use that spelling as a proven API field. The page states no text-length or universal phone-format constraint.
- The guide explicitly says input is **not validated against a format**. A received `InputResult.Input.DigitInput` contains the entered numerals/phone number; pass it to the merchant system for validation and further use. Do not treat the placeholder, terminal country code, masking, or example `Result=Success` as verification that the number is reachable or belongs to the shopper.
- The input screen remains until input arrives, `MaxInputTime` expires, the terminal Cancel key is selected, or the POS app sends a cancel-input or other request. Timeout returns `Failure` / `Cancel` with `message=Screen%20timeout`; terminal Cancel returns `Failure` / `Cancel` with empty `DigitInput`. A payment request while input waits overrides it and returns `Failure` / `Busy` with a higher-priority-request message. These are input-request outcomes, not evidence of payment completion.
- The V400m ID, example `MaxInputTime=40`, placeholder digits and `MaskCharactersFlag=true` are illustrative request values. The dated guide gives no current terminal-model matrix, data-retention rule, consent mechanism or production privacy policy.

## Detail locators

- Raw `# Ask for phone number input` through `## How it works` (lines 15–36): purpose, location-derived changeable country code, integration and screen-end conditions.
- Raw `## Make a PhoneNumber input request` (lines 48–99): Device/Input header, display prompt, `GetPhoneNumber`, `DigitString`, timeout, placeholder and masking table typo.
- Raw JSON and Java examples (lines 100–164): illustrative terminal, prompt, 40-second timeout, placeholder and masking setting; Java omits the JSON masking flag.
- Raw response and result handling (lines 165–211): lack of format validation, returned `DigitInput`, timeout, Cancel, Busy override and merchant-side validation route.

## Related

- [[adyen-pos-shopper-engagement]] — terminal shopper interaction route.
- [[adyen-terminal-api]] — Device/Input message context.
- [[adyen-payment-terminals]] — physical terminal context; no model eligibility follows from the example.

## Related raw API references

Navigation named by the guide, not further behavior reviewed for this entry:

- Cancel input — https://docs.adyen.com/point-of-sale/shopper-engagement/shopper-input/cancel-input
- Select another input type — https://docs.adyen.com/point-of-sale/shopper-engagement/shopper-input/select-input-request
- Terminal API Input — https://docs.adyen.com/api-explorer/terminal-api/latest/post/input

## Raw Sources

- [[raw/adyen/docs/point-of-sale/shopper-engagement/shopper-input/phone-number/2026-09-15|Phone-number input guide, fetched 2026-09-15]]
