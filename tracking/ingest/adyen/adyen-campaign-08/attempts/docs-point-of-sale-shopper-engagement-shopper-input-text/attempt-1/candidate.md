---
title: "Adyen POS GetText terminal input"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/shopper-engagement/shopper-input/text"
raw_files:
  - "adyen/docs/point-of-sale/shopper-engagement/shopper-input/text/2026-09-15.md"
tags: [adyen, point-of-sale, shopper-engagement, terminal-api, input, text, privacy]
---

## Overview

This dated Adyen Terminal API guide uses a Device/Input **`GetText` `InputRequest`** to ask a shopper or staff member for text on a payment terminal. Its example prompts for an email address. The terminal collects and returns `Input.TextInput`; the merchant POS/system must validate and decide how to use that text. This is a nonfinancial interaction, not identity verification, consent, payment authorization or proof that an email address belongs to the shopper. See [[adyen-pos-shopper-engagement]] and [[adyen-terminal-api]].

## Key takeaways

- The guide requires a Terminal API integration with payment terminals. The request's `MessageHeader` uses `MessageClass=Device`, `MessageCategory=Input`, `MessageType=Request` and terminal `POIID`; its `DisplayOutput` selects CustomerDisplay, text output and predefined `GetText`. `InputData` selects CustomerInput and `InputCommand=TextString`. See raw §§ Requirements and Make a Text input request (lines 21–85).
- `MaxInputTime` sets the time allowed in seconds; `DefaultInputString` is placeholder text describing the expected format; masking is a Boolean option. **Raw field-name tension:** the table spells the key `MaskChararctersFlag`, while the JSON example uses `MaskCharactersFlag`. This source gives no text-length limit or Confirm-flag behavior and does not name eligible terminal models. Verify an implementation against its actual Terminal API schema. See raw field table and example (lines 76–129).
- The prompt remains until the person submits input, the maximum time expires, terminal Cancel is selected, or a POS-app request interrupts it. The guide explicitly says the terminal **does not validate input against a format**. After a successful response, the merchant passes `Input.TextInput` to its own system for validation and further use. Masking or a placeholder is not an email-validity, identity or privacy guarantee; the guide does not specify consent or retention rules. See raw §§ How it works and Make a Text input request (lines 29–36, 166–211).
- Timeout gives `InputResult.Response.Result=Failure`, `ErrorCondition=Cancel` and `AdditionalResponse=message=Screen%20timeout`. A payment request while text input is pending overrides it and returns Failure/`Busy` with a higher-priority message; that branch says nothing about whether the payment later succeeds. Terminal Cancel returns Failure/`Cancel` and an empty `DigitInput` according to the text, despite this being a `TextString` guide. See raw response branches (lines 205–209).
- The JSON email example uses `MaxInputTime=120`, placeholder `name@domain.com` and masking enabled. These are example choices, not universal timeout or masking defaults. See raw JSON example (lines 87–129).

## Detail locators

- Raw §§ Requirements and How it works: Terminal API scope and lifecycle events (lines 21–46).
- Raw § Make a Text input request: header, DisplayOutput and InputData fields, JSON/Java examples, response and merchant validation (lines 48–211).

## Related

- [[adyen]] — provider company page.
- [[adyen-pos-shopper-engagement]] — Input/Display interactions and sibling input guides.
- [[adyen-terminal-api]] — Device/Input message family.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/shopper-engagement/shopper-input/text/2026-09-15|Ask for text input, fetched 2026-09-15]]
