---
title: "Adyen POS single-answer menu input"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/shopper-engagement/shopper-input/menu"
raw_files:
  - "adyen/docs/point-of-sale/shopper-engagement/shopper-input/menu/2026-09-15.md"
tags: [adyen, point-of-sale, shopper-engagement, terminal-api, input, menu]
---

## Overview

This Adyen Terminal API guide, last modified 2025-03-14 and captured 2026-09-15, describes asking a shopper or staff member to choose **one** item from a terminal menu, for example a survey answer. It is a `Device` / `Input` message with a `MenuButtons` display and `GetMenuEntry` command. It collects a nonfinancial selection; its response is not a payment authorization, identity proof or evidence that consent was obtained. [[adyen]] [[adyen-pos-shopper-engagement]] [[adyen-terminal-api]]

## Key takeaways

- The page assumes a Terminal API integration with a payment terminal. The menu can show a header, an optional second header, and up to 15 scrollable option buttons; each option may have one or two text lines. This guide is specifically single-answer. A separate linked guide covers multiple answers. It does not establish a default choice, separate confirmation step, terminal-model eligibility or text-length limit.
- Send a `SaleToPOIRequest` header with `MessageClass=Device`, `MessageCategory=Input`, `MessageType=Request`, and the terminal-scoped `ServiceID`, `SaleID`, `POIID` and protocol version. `InputRequest.DisplayOutput` uses `CustomerDisplay`, `InfoQualify=Display`, text output and `PredefinedContent.ReferenceID=MenuButtons`; its `MenuEntry` array supplies option labels. `InputRequest.InputData` uses `CustomerInput`, `InfoQualify=Input`, `InputCommand=GetMenuEntry` and integer `MaxInputTime` in seconds.
- The menu remains until input arrives, its maximum input time expires, the terminal Cancel key is selected, or the POS app sends a cancel-input or other request. The guide says input is not format-validated. For received input, `InputResult.Input.MenuEntryNumber` is an indicator array: the selected option's position is `1`, others `0`. Pass relevant input to the merchant system for its own validation and use. The illustrated response has five indicator elements despite four submitted options; use the documented selected-position meaning rather than infer a general exact array length from this sample.
- Timeout returns `InputResult.Response.Result=Failure`, `ErrorCondition=Cancel`, and `AdditionalResponse=message=Screen%20timeout`. Pressing Cancel also returns `Failure` / `Cancel`, with an empty `MenuEntryNumber`. A payment request arriving during input overrides it and returns `Failure` / `Busy` plus the higher-priority-request message; it does not mean the menu selection or payment succeeded.
- The sample survey labels, V400m `POIID` and `MaxInputTime=120` are illustrations, not proof of universal terminal support, a universally required 120-second timeout, production configuration, data retention or privacy treatment. The request table specifies `ProtocolVersion=3.0` for this documented flow.

## Detail locators

- Raw `# Ask to select a single answer from a list` through `## How it works` (lines 15–40): shopper/staff purpose, single-answer and 15-option display, integration and end conditions.
- Raw `## Make a single-answer MenuButtons input request` (lines 68–118): header, display/menu and input-command fields, option text and timeout unit.
- Raw JSON and Java examples (lines 119–258): illustrative four-answer survey and `GetMenuEntry` request construction.
- Raw response handling (lines 259–319): no format validation, `MenuEntryNumber` selected-position semantics, timeout, Cancel, higher-priority payment override and merchant-side use.

## Related

- [[adyen-pos-shopper-engagement]] — terminal interaction route.
- [[adyen-terminal-api]] — Device/Input message context.
- [[adyen-payment-terminals]] — physical display hardware; this guide does not qualify models.

## Related raw API references

Navigation named by the guide, not further behavior reviewed for this entry:

- Multiple-answer menu — https://docs.adyen.com/point-of-sale/shopper-engagement/shopper-input/multi-menu
- Cancel input — https://docs.adyen.com/point-of-sale/shopper-engagement/shopper-input/cancel-input
- Create session — https://docs.adyen.com/point-of-sale/shopper-engagement/create-session
- Terminal API Input — https://docs.adyen.com/api-explorer/terminal-api/latest/post/input

## Raw Sources

- [[raw/adyen/docs/point-of-sale/shopper-engagement/shopper-input/menu/2026-09-15|Single-answer MenuButtons input guide, fetched 2026-09-15]]
