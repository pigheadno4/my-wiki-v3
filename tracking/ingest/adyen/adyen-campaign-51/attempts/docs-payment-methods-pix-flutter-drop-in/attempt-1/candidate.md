---
title: "Adyen Pix Flutter Drop-in"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/pix/flutter-drop-in"
raw_files:
  - "adyen/docs/payment-methods/pix/flutter-drop-in/2026-09-15.md"
tags: [adyen, pix, flutter, drop-in, brazil, qr-code]
---

## Overview

This 2026-09-15-captured Adyen guide adds Pix to an existing Flutter Drop-in integration, separately for Sessions and Advanced server flows. It covers method setup, request additions, QR action handling, refund timing, and test/live steps. The guide's TEST BR/BRL examples and Customer Area simulation do not prove current merchant enablement or a real paid transaction. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Sessions:** the page requires an existing Flutter Drop-in Sessions integration, Checkout API v68 or later, and contacting Support to add Pix in Customer Area. The Sessions prerequisite links to an **Advanced-flow** base guide despite naming Sessions; follow the Sessions-labeled payment-session link for that flow and verify the base guide. The `/sessions` table marks `amount` required; `shopperName`, CPF/CNPJ `socialSecurityNumber`, `shopperStatement`, and line-item fields are unmarked. It gives `shopperStatement` a 140-character maximum. The TEST v71 example uses BR/BRL and `pix`, with a now-past 2021 `sessionValidity` sample. See raw lines 25–96 and 509–530.
- **Advanced:** the page requires an existing Flutter Drop-in Advanced integration, `qrCode` additional-action handling, and Pix added in Customer Area. Its `/payments` table marks `paymentMethod` (from front-end `state.data.paymentMethod`) and `amount` required. It advises sending `shopperName` and CPF/CNPJ `socialSecurityNumber` for shopper recognition, but leaves them unmarked. For a supplied `shopperStatement`, this flow says **under 60 characters**, unlike the Sessions table's 140-character maximum; preserve the flow-specific wording. Optional `sessionValidity` defaults to one hour on Checkout API v71 or earlier and 24 hours on v72 or later. TEST v72 examples use BR/BRL and a now-past 2025 validity timestamp. See raw lines 532–608.
- Neither flow requires extra Pix configuration in this page. The Advanced example response shows `resultCode: Pending` with `action.type: qrCode` and QR data. Pix is asynchronous, so this QR action and a pending offer are **not paid confirmation**. The page does not give a Flutter SDK version or a complete final-status webhook recipe. See raw lines 509–511, 546–548, and 1055–1075.
- The guide says refunds are available within **90 days after payment** through Customer Area or API. In TEST, promoting a pending offer to sale simulates a Pix payment and supports reconciliation testing; paid or promoted test offers appear in the Payment list. Before live acceptance, submit a Pix request in the **live Customer Area**. This simulation is not a real shopper payment or live authorization. See raw lines 513–530 and 1077–1094.

> [!warning] Flow and example qualifications
> The Sessions prerequisite points to an Advanced-flow URL (raw line 33). Sessions and Advanced state different `shopperStatement` limits (lines 48 and 562); do not merge them into one universal limit. Example `sessionValidity` dates in 2021 and 2025 are past the 2026 capture (lines 71 and 597), and `Pending` plus `qrCode` is not final payment (lines 1055–1075).

## Detail locators

- Sessions prerequisites, setup, field table and TEST v71 request: raw lines 25–96; SDK-language examples continue through line 505.
- No additional Pix configuration, refund window, TEST offer promotion and live request: raw lines 509–530; repeated at 1077–1094.
- Advanced prerequisites, action type, field table and TEST v72 request: raw lines 532–608; SDK-language examples continue through line 1053.
- Advanced pending QR response: raw lines 1055–1075.

## Related

- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/pix/flutter-drop-in/2026-09-15|Fully read Pix Flutter Drop-in raw]]
