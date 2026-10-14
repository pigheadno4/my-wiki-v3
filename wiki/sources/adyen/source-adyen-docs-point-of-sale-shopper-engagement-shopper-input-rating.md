---
title: "Ask for a rating | Adyen Docs"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/shopper-engagement/shopper-input/rating"
raw_files:
  - "adyen/docs/point-of-sale/shopper-engagement/shopper-input/rating/2026-09-15.md"
tags: [adyen, point-of-sale, shopper-engagement, terminal-api, input-request, rating]
---

## Overview

This Adyen Docs guide describes a Terminal API **GetRating** `InputRequest` that asks a shopper or staff member for a numerical rating advertised as 0–10, such as an NPS-style question, on an Adyen payment terminal. The response is nonfinancial shopper/staff input; it is not a payment result, consent record, or validated survey score. See [[adyen]], [[adyen-pos-shopper-engagement]], and [[adyen-terminal-api]].

## Key takeaways

- The scope is a Terminal API integration with payment terminals. The request header uses ProtocolVersion `3.0`, `MessageClass=Device`, `MessageCategory=Input`, `MessageType=Request`, a per-terminal `ServiceID` unique over the prior 48 hours, and `SaleID`/`POIID`. `InputRequest.DisplayOutput` targets `CustomerDisplay`, uses `InfoQualify=Display`, `OutputFormat=Text`, `PredefinedContent.ReferenceID=GetRating`, and one or two custom `OutputText.Text` entries; the first is bold and `\n` makes a line break. The terminal adds its own confirmation instruction. This page describes GetRating, not an interchangeable OneKey prompt.
- `InputRequest.InputData` targets `CustomerInput` with `InfoQualify=Input`, `InputCommand=DigitString` and an integer `MaxInputTime` in seconds. Small non-Android portrait terminals show two screens and require **Enter rating** before keypad entry; terminals without a physical keypad show an on-screen keyboard. The page does not give a comprehensive supported-model list.
- A provided rating is returned as `InputResponse.InputResult.Input.DigitInput`, shown as string `"9"` in the example. The page explicitly says terminal input is **not validated against a format** and instructs the merchant to validate and use the value in its own system. Although the guide advertises 0–10, the example's scoring text labels only Poor 0–3, OK 4–6 and Great 7–9; neither that wording nor `DigitString` proves 0–10 enforcement, decimal acceptance, a nonempty response or an NPS calculation. `InputResult.Response.Result=Success` is an input-request result; the example's separate `OutputResult.Response.Result=Success` concerns the displayed prompt.
- The prompt remains until input, configured time limit, terminal **Cancel**, a cancellation request, or another POS request. Timeout returns `InputResult.Response.Result=Failure`, `ErrorCondition=Cancel`, and `AdditionalResponse` `message=Screen%20timeout`. A payment request while input is pending overrides it and returns `Failure`/`Busy` with a higher-priority-request message; that payment's own result is separate. Terminal Cancel gives an empty `DigitInput` and `Failure`/`Cancel`; an empty value is not rating zero or a consent/skip confirmation. Handle these branches separately from valid input.

## Detail locators

- `Ask for a rating` and `Requirements`, pinned raw lines 15–27: shopper/staff 0–10 purpose, NPS example and Terminal API terminal scope.
- `How it works`, lines 29–55: prompt termination events and model/input UI illustrations.
- `Make a Rating input request`, lines 57–94: header, `DisplayOutput` and `InputData` field tables, text formatting and timeout configuration.
- JSON and Java examples, lines 96–174: illustrative GetRating request, including a 0–9 sample label despite the 0–10 page description.
- Response and failure branches, lines 176–221: lack of format validation, `DigitInput`, distinct input/display success, timeout, payment override, terminal Cancel and merchant-side validation.
- `See also`, lines 223–227: cancel-input, other input types and session guides are navigation only.

## Related

- [[adyen-pos-shopper-engagement]] — main terminal interaction concept.
- [[adyen-terminal-api]] — message/result context; rating Input is separate from Payment.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/shopper-engagement/shopper-input/rating/2026-09-15|Adyen GetRating input guide, fetched 2026-09-15]]
