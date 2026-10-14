---
title: "Adyen Docs: Use a standalone terminal"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/standalone/standalone-use"
raw_files:
  - "adyen/docs/point-of-sale/standalone/standalone-use/2026-09-15.md"
tags: [adyen, point-of-sale, standalone-terminals, payments, refunds]
---

## Overview

Adyen's 2026-09-15 standalone-use guide explains transactions initiated directly on a terminal after standalone setup: card/NFC and QR payments, Manual Key Entry (MKE), MOTO, purchase cashback, tipping, in-progress cancellation, referenced or unreferenced refunds, stored-value actions, Totals, and receipt reprints. This is a terminal-operated flow, separate from POS-app Terminal API requests. The instructions and pictured outcomes are historical guidance, not proof of current feature enablement or a completed payment or refund. [[adyen]] · [[adyen-standalone-terminals]]

## Key takeaways

- For an ordinary card or NFC payment, the operator selects `Payment`, enters the amount, then hands the terminal to the shopper. Old-menu non-Android terminals have a different Start/Confirm entry. QR wallet payments display a code for the shopper's app. MKE manually enters card data when chip/stripe reading fails; MOTO is a separate card-not-present flow that must be enabled. MKE, MOTO, and purchase cashback use the Transactions passcode and New transaction menu, with old-menu variations in raw.
- Support enablement is stated for tipping, referenced refunds, gift/stored-value cards, and MOTO; gift/stored-value cards are limited to non-Android standalone terminals in this snapshot. Tipping, when enabled, prompts on each initiated payment. The guide supports cashback with a purchase, but says cashout without a purchase is unsupported on standalone payment terminals. A separate gift-card action can cash out the full stored value only; this does not generalize to card-account cashout.
- Before a payment finishes processing, the operator may **try** to cancel it. A `Cancelled` display marks a successful attempt; if cancellation fails and the payment was approved, the guide routes to a refund. A cancel press alone is not a proven reversal.
- Referenced refunds select an original transaction from History and use a Transactions passcode; Adyen describes lower error/fraud risk and QR-method support versus unreferenced refunds. Unreferenced refunds start a new Refund or MOTO refund, use the Transactions passcode and, if requested, a six-digit Refunds passcode. The card-present Refund requires shopper card presentation; MOTO refund manually enters card number, expiry and CVC. The guide's statements about refund receipt, processing, and shopper-account timing are conditional on success, not evidence for a particular refund.
- Totals show terminal-processed sales, refunds, tips, and cancellations since the last reset. Reset starts a new reporting period; the prior period stops showing in the current report, though the last known report can still be viewed and printed. History also supports reprinting a shopper or merchant receipt.

## Detail locators

- **Scope and gates:** raw heading “Requirements” (29–41) identifies standalone hardware, non-Android stored-value limit, and Support-enabled features; “Make a payment” (43–57) has setup, amount entry, shopper handoff and older non-Android menu route.
- **Payment variants:** “QR code payments” (59–73), “Manual Key Entry payment” (75–96), “MOTO payment” (98–119), “Cashback” (121–146), and “Tipping” (148–155). These are terminal actions with different card-present/card-not-present inputs and passcodes; the raw holds the exact screens and legacy keypad sequence.
- **Cancel and refunds:** “Cancel an in-progress payment” (157–166) versus “Refund a payment” (168–181), “Make a referenced refund” (183–197), and “Make an unreferenced refund” (199–226). The latter includes the conditional Refunds passcode and three-wrong-attempt wait.
- **Stored value:** “Use gift cards and other stored value cards” (228–258) lists redeem, activate, load, balance inquiry, and full-only gift-card cashout. Balance inquiry cannot be cancelled under this guide.
- **Local reporting:** “View, print, and reset totals” (260–283) and “Reprint transaction receipt” (285–299). These local terminal records do not establish settlement or merchant reconciliation.

## Related

- [[adyen-standalone-terminals]] — standalone solution and terminal-operated flow
- [[adyen-terminal-api]] — separate integrated POS message flow
- [[adyen-payment-terminals]] — hardware/model scope

## Related raw API references

The linked standalone setup, MOTO enablement, menu-access, terminal-selection, and troubleshooting guides were not read for this entry; use them as navigation only.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/standalone/standalone-use/2026-09-15|Adyen standalone terminal use, fetched 2026-09-15]]
