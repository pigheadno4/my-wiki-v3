---
title: "Adyen Terminal API multiple-answer menu input"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/shopper-engagement/shopper-input/multi-menu"
raw_files:
  - "adyen/docs/point-of-sale/shopper-engagement/shopper-input/multi-menu/2026-09-15.md"
tags: [adyen, point-of-sale, shopper-engagement, terminal-api, input, multiple-choice]
---

## Overview

Adyen's multi-menu guide describes a Terminal API **Device/Input** request that shows a shopper a `MenuButtons` question on a payment terminal and lets them select more than one answer. It is a terminal input interaction, separate from the linked single-answer menu, confirmation, signature and payment operations. The page's survey/subscription example does not establish financial authorization, valid marketing consent or a completed shopper decision. The 2026-09-15 snapshot is not proof of current terminal-model availability or live behavior. [[adyen]] [[adyen-pos-shopper-engagement]] [[adyen-terminal-api]]

## Key takeaways

- The guide requires a Terminal API payment-terminal integration. It describes a header question and up to **15 scrollable option buttons**, each with one text line. For a one-answer question it routes to the separate single-answer guide. It does not give a supported-model list or a legal consent rule. See the introduction and `## Requirements`.
- For multi-select, the POS system sends `SaleToPOIRequest.MessageHeader` with `MessageClass=Device`, `MessageCategory=Input` and `MessageType=Request`. The `ServiceID` is 1–10 alphanumeric characters and unique within the prior 48 hours for that terminal `POIID`. `InputRequest.DisplayOutput` targets `CustomerDisplay` with `InfoQualify=Display`, text output, `PredefinedContent.ReferenceID=MenuButtons`, one header text field and up to 15 `MenuEntry` texts. See `## Make a multiple-answers MenuButtons input request`.
- `InputRequest.InputData` targets `CustomerInput` with `InfoQualify=Input` and `InputCommand=GetMenuEntry`. **`MinLength` or `MaxLength` must be included to enable multiple answers**; they bound the selected-answer count. `MaxInputTime` sets a timeout in seconds. The example sets 60 seconds, minimum 0 and maximum 3 for its three displayed options; those are example values, not documented defaults. See `## Make a multiple-answers MenuButtons input request`.
- On input, `InputResult.Input.MenuEntryNumber` is a positional array: selected options have `1` and unselected options have `0` (first and third selected is `[1,0,1]`). The POS system passes relevant `InputResult.Input` data to its own system for validation and further use. The response example also includes an `outputTextWarning` in `AdditionalResponse`; it should be read as that example's response, not as a default warning. See step 2 and step 3 of `## Make a multiple-answers MenuButtons input request`.
- Below-minimum or above-maximum selections produce `InputResult.Response.Result=Failure`, `ErrorCondition=NotAllowed`, and an explanatory `AdditionalResponse`. A timeout produces an `EventNotification` with `EventDetails=message=Did+not+receive+a+response+from+the+POI.`. A payment request received while input is pending overrides it and yields input `Failure/Busy` with a higher-priority-request message; shopper Cancel yields input `Failure/Cancel`. The initial request can also end on a separate cancel-input request or another POS-app request; the guide states the specific Busy response for the payment-request case. See `## How it works` and the response notes under `## Make a multiple-answers MenuButtons input request`.

## Detail locators

- Introduction and `## Requirements`: multi-select purpose, 15-button/one-line display limit and Terminal API scope.
- `## How it works`: events ending a pending input request.
- `## Make a multiple-answers MenuButtons input request`: exact MessageHeader, DisplayOutput/MenuEntry and InputData fields, `MinLength`/`MaxLength` activation and request examples.
- Response notes under `## Make a multiple-answers MenuButtons input request`: `MenuEntryNumber` positional flags, `NotAllowed`, timeout notification, payment override `Busy`, shopper `Cancel`, and validation handoff.

## Related

- [[adyen-pos-shopper-engagement]] — terminal shopper interaction routes.
- [[adyen-terminal-api]] — request and response envelope.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/shopper-engagement/shopper-input/multi-menu/2026-09-15|Adyen multiple-answer menu guide, fetched 2026-09-15]]
