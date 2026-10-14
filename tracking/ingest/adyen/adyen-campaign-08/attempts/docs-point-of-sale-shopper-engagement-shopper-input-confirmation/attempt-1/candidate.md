---
title: "Ask for confirmation | Adyen Docs"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/shopper-engagement/shopper-input/confirmation"
raw_files:
  - "adyen/docs/point-of-sale/shopper-engagement/shopper-input/confirmation/2026-09-15.md"
tags: [adyen, point-of-sale, shopper-engagement, terminal-api, input, confirmation]
---

## Overview

Adyen's GetConfirmation guide describes a **Terminal API Device/Input** request that displays a merchant-supplied prompt and asks a shopper to confirm or decline it on a payment terminal. Its Terms-and-Conditions example returns a `ConfirmedFlag` representing the selected button or key. The terminal interaction itself does not authorize a payment, establish legal consent validity, or prove that the full terms were shown or retained. [[adyen]] [[adyen-pos-shopper-engagement]] [[adyen-terminal-api]]

## Key takeaways

- A Terminal API payment-terminal integration is required. The request header uses `MessageClass: Device`, `MessageCategory: Input`, and protocol version 3.0. `InputRequest.DisplayOutput` targets `CustomerDisplay` with `GetConfirmation`; `InputRequest.InputData` targets `CustomerInput` with `InputCommand: GetConfirmation` and a configurable `MaxInputTime` in seconds. The header's `ServiceID` is terminal-scoped, 1–10 alphanumeric characters and unique within 48 hours; this is not a general safe-retry guarantee. See **Requirements** and **Make a Confirmation input request**, pinned raw lines 21–27 and 48–86.
- `OutputContent.OutputText` is an ordered array of **four** text fields: title, additional text, left Cancel-button label, and right Confirm-button label. On a portrait display, the title is limited to about 20 characters; the additional text can be long and can use `\n` for a line break. In the example the labels are **Decline** and **Agree**. Do not swap button meaning based on label order. See pinned raw lines 66–77 and 90–138.
- On input, `Input.ConfirmedFlag: true` means the shopper selected the **right** button (Agree in the example) or keypad Confirm; `false` means the **left** button (Decline) or keypad Cancel. The guide says this input is not validated against a format and instructs the merchant to pass relevant `InputResult.Input` data to its own system for validation/further use. A response `Result: Success` is an input-operation result, not proof of payment approval or a sufficient legal record of consent. See pinned raw lines 182–225.
- The screen remains until input, configured timeout, terminal Cancel, or a cancel-input/other POS request. **Timeout** yields input `Result: Failure`, `ErrorCondition: Cancel`, and `message=Screen%20timeout`. A **payment request** while input is pending overrides it and yields input Failure/`ErrorCondition: Busy` plus a higher-priority-request message. A shopper's left-button/keypad Cancel maps to `ConfirmedFlag: false` in the guide, and should not be conflated with the timeout Failure/Cancel result. See pinned raw lines 29–36 and 188–225.
- The JSON and Java blocks are examples, including one V400m `POIID`, a 30-second `MaxInputTime`, and a sample Terms-and-Conditions prompt. They do not establish current device or account eligibility or prove that a particular shopper viewed a complete legal text. See pinned raw lines 90–180.

## Detail locators

- **Ask for confirmation; Requirements; How it works** (pinned raw lines 15–46) — purpose, Terminal API prerequisite, display persistence/termination and form-factor illustrations.
- **Make a Confirmation input request** (pinned raw lines 48–86) — Device/Input header, four ordered display texts, button mapping, GetConfirmation input command and timeout.
- **JSON; Java** (pinned raw lines 90–180) — illustrative request fields and one terminal model.
- **Input result and terminal outcomes** (pinned raw lines 182–225) — no format validation, `ConfirmedFlag` true/false meanings, example success, timeout Cancel, payment override Busy, merchant validation.
- **See also** (pinned raw lines 227–231) — cancel-input, other input and session navigation.

## Related

- [[adyen-pos-shopper-engagement]] — primary shopper-terminal interaction route.
- [[adyen-terminal-api]] — Terminal API message context; confirmation input is separate from PaymentRequest.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/shopper-engagement/shopper-input/confirmation/2026-09-15|Adyen GetConfirmation input guide, fetched 2026-09-15]]
