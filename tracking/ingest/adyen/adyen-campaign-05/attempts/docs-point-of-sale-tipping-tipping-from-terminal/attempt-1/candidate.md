---
title: "Adyen Docs: Tipping from the terminal"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/tipping/tipping-from-terminal"
raw_files:
  - "adyen/docs/point-of-sale/tipping/tipping-from-terminal/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, tipping, gratuity]
---

## Overview

Adyen's 2026-09-15 terminal-tipping guide describes shopper entry of a tip on an Adyen-provided terminal in an integrated Terminal API payment. The terminal can ask for a tip amount, including predefined and custom choices, or ask the shopper for a total amount above the original purchase amount; the same Terminal API `AskGratuity` tender option triggers either flow. This is an authorization-time POS payment flow, not a separate post-authorization capture or payout instruction. [[adyen]] · [[adyen-terminal-api]]

## Key takeaways

- The guide requires a Terminal API integration with Adyen-provided payment terminals and standard webhooks; display notifications for staff are optional. It states support across terminal models except unattended terminals, subject to this dated page rather than present-day device or merchant eligibility.
- **Tip-amount mode:** The default prompt occurs before card entry and needs no Adyen-side enablement. A prompt after card entry needs Adyen Support enablement; optional single tap prevents an additional contactless tap after tip selection. A prompt with no configured presets lets the shopper enter a tip or decline to tip. Configured options can mix percentages, fixed amounts, and a custom amount.
- **Total-amount mode:** The terminal presents the original purchase amount and asks the shopper for a total at least equal to it; the difference is the tip. The guide calls this customary in Nordic countries/regions, not exclusive to them. Adyen Support must enable this mode.
- Customer Area or Management API can configure gratuities at company, merchant, store, or terminal level. The Management API PATCH uses a currency-qualified `gratuities` object; up to four predefined options, or three plus custom entry, are described. This page does not define configuration inheritance or override precedence. A separate linked guide covers per-payment POS overrides and was not read here.
- To initiate either mode, `PaymentRequest.PaymentTransaction.AmountsReq.RequestedAmount` is the **original purchase amount**, while `SaleData.SaleToAcquirerData` carries `AskGratuity` as Base64 JSON or form-style key/value. After the shopper responds, the terminal sends original purchase plus tip to Adyen. The `PaymentResponse` reports `TipAmount` when a tip was added and `AuthorizedAmount` as the total authorized amount; `AdditionalResponse` reports corresponding amounts in minor units. The example is an illustration, not a settlement or capture guarantee.
- An optional, Support-enabled high-tip warning can ask the shopper to confirm when the tip reaches a configured percentage of the **original purchase amount**. It applies to both tip-amount and total-amount modes and is described for standalone and integrated terminals. Staff can receive optional display-notification webhooks; a settlement report can be configured to include a gratuity column, without the page establishing payout timing or allocation.

## Detail locators

- **Scope, modes, and requirements:** raw lines 17–36. The regional custom is about total-entry presentation; terminal-model and webhook statements are snapshot requirements.
- **Before/after card and direct tip entry:** “Ask for a tip amount” and its timing sections, lines 38–71. Support enables after-card mode; single tap is optional.
- **Presets and configuration:** Customer Area lines 79–109; Management API lines 111–132. The API example begins at line 134 and uses a test `/v3/terminals/{terminalId}/terminalSettings` endpoint; the page also links API Explorer “latest” and shows SDK examples with their own versions. Confirm current API schema and account-level setting behavior before implementing. Percentages use the transaction amount; API fixed tip examples use minor units.
- **Total entry:** “Ask for a total amount,” lines 401–410. Total must be at least the original purchase; Support enablement is a condition.
- **Payment amount and response:** “Make a payment,” lines 416–509. Raw has the required message-header fields and `SaleToAcquirerData` formats at lines 420–452, then the original-plus-tip platform request and response fields at lines 489–509. `AdditionalResponse` format follows the request encoding. The EUR 142.50/10% example at lines 454–546 is illustrative.
- **Staff, reporting, and warning:** lines 548–571. Display notifications are webhooks; settlement-report gratuity column is a reporting option; Support enables the threshold warning.

## Related

- [[adyen-terminal-api]] — Terminal API request and response context
- [[adyen-payment-capture]] — separate online capture concept; this guide describes tip inclusion in the POS authorization amount

## Related raw API references

Linked tender-option, payment, per-payment override, standard/display-webhook, settlement-report, currency-code, and Management API Explorer pages are navigation only; they were not read for this entry.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/tipping/tipping-from-terminal/2026-09-15|Adyen Tipping from the terminal, fetched 2026-09-15]]
