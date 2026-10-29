---
title: "MB WAY API-only integration add-on"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/mb-way/api-only"
raw_files:
  - "adyen/docs/payment-methods/mb-way/api-only/2026-09-15.md"
tags: [adyen, mb-way, api-only, await, app2app]
---

## Overview

This 2026-09-15-captured MB WAY API-only add-on describes an existing **Advanced-flow API-only** integration's MB WAY-specific Web waiting-screen path and optional mobile **App2App** switch. It links to the main integration for base handling. It is not proof of current merchant enablement, successful app switching, or a completed live payment. See [[adyen]], [[adyen-online-payments]], and the [[source-adyen-docs-payment-methods-mb-way|MB WAY overview]] for PT/EUR method scope and the user-level daily cumulative limit.

## Key takeaways

- Prerequisites are an existing API-only integration, additional-action handling for `action.type: await`, and MB WAY added in Customer Area. For `/paymentMethods`, the page specifies **PT**, **EUR**, and `amount.value` in minor units; its response example shows method type `mbway`, not a guarantee that every merchant will receive it (raw lines 23–29, 53–93).
- **Standard Web path:** the method-specific `/payments` table marks `paymentMethod.type: mbway` and `paymentMethod.telephoneNumber` (shopper mobile phone) required, with `shopperStatement` unmarked. The response is `Pending` with an `await` action. Display a waiting screen while the shopper completes the payment in the MB WAY app, then use a webhook for the payment result before presenting the outcome; `Pending` is not final success (raw lines 95–171).
- **Optional mobile App2App path:** only if enabled, sending `channel: iOS` or `Android` and a `returnUrl` is described as linking directly to the MB WAY app without manual phone entry. If `channel` is missing or `Web`, the standard phone-number flow applies. A successful response supplies an `action.url` MB WAY deep link with the return URL appended; use that URL to switch apps, and the shopper returns via `returnUrl` after authorization. The sample action type is annotated “await, or the specific type returned by the API,” so handle the actual returned action rather than assuming one fixed type (raw lines 173–226).
- **Test/live:** the page says any telephone number can be used in test and gives one example. The `shopperStatement` suffixes `-c1`, `-c3`, and `-c5` trigger Authorised, Pending, and Refused test result codes. Live acceptance requires adding MB WAY in live Customer Area. These are test controls and setup, not evidence of a real phone, payment authorization, or production enablement (raw lines 228–247).

> [!warning] Web form and item-data wording
> The Web flow says the shopper enters details in the merchant-built form, and the `/payments` table requires `paymentMethod.telephoneNumber`, yet `## Build your payment form` says no shopper information needs to be collected (raw lines 33–49, 95–103). Treat that sentence as conflicting with the standard Web request; the App2App path is the separate no-manual-phone path. The Web workflow also mentions additional purchased-item information (raw line 37), but its MB WAY-specific parameter table lists no item/order-line field (lines 95–103); do not invent an item schema from that sentence.

> [!warning] Illustrative examples
> Both curl examples omit a continuation between `-X POST` and `-d` (raw lines 70–71, 112–113). The App2App request/response snippets contain inline comments inside `json` fences (lines 184–219) and illustrate a conditional branch rather than a complete validated payload. Do not copy them verbatim as executable JSON or assume the standard Web phone requirement applies to the enabled App2App branch.

## Detail locators

- API-only and await prerequisites, path split: raw lines 15–49.
- PT/EUR method discovery: raw `## Get MB WAY as an available payment method` lines 53–93.
- Standard Web `/payments`, Pending/await and waiting-screen/webhook handling: raw lines 95–171.
- Optional App2App channel, return URL, deep link and return: raw `## Enable App2App switch` lines 173–226.
- Test number, live setup and result-code simulation: raw lines 228–247.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-mb-way]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/mb-way/api-only/2026-09-15|MB WAY API-only guide, captured 2026-09-15]]
