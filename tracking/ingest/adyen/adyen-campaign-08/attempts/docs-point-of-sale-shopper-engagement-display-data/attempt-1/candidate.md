---
title: "Adyen terminal display-data overview"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/shopper-engagement/display-data"
raw_files:
  - "adyen/docs/point-of-sale/shopper-engagement/display-data/2026-09-15.md"
tags: [adyen, point-of-sale, shopper-engagement, terminal-display, display-request]
---

## Overview

This dated Adyen overview routes merchants to **display requests** that show information on a payment-terminal screen **outside the payment flow**. It names four display purposes: shopper-scannable QR code, virtual receipt preview, image, and regular standby/idle screen. These are display surfaces, distinct from shopper **Input**, physical **Print**, and **Payment** operations; showing content alone does not capture consent, authorize a payment, print a receipt or establish that a sale succeeded. See [[adyen]] and [[adyen-pos-shopper-engagement]].

## Key takeaways

- The QR example is a URL to a loyalty program or app download shown on the terminal for the shopper's phone to scan. The overview does not state that scanning completes enrollment, identifies a shopper or makes a payment.
- A virtual receipt can preview items the shopper is purchasing, optionally with a QR code next to its lines. This is a screen preview, not evidence of a completed transaction or a printed/delivered receipt.
- An image can be an advertisement or POS-app-generated offer. Another display request can return the screen to its normal standby/idle state. The overview does not specify file format, payload encoding, terminal model coverage or display lifetime for these child flows.
- The four linked child guides provide implementation routes. This overview itself gives no Terminal API message fields, response acknowledgment, timeout behavior, session rules, device support, required roles or permission/consent flow. Consult the relevant child guide before asserting those details.

## Detail locators

- Opening paragraph and four-item list: outside-payment display scope and QR/virtual-receipt/image/idle purposes.
- `## What do you want to show?`: navigation to the four child guides for QR, virtual receipt, image and standby screen; the linked pages are not behavioral evidence in this entry.

## Related

- [[adyen-pos-shopper-engagement]] — primary POS terminal interaction hub.
- [[adyen-terminal-api]] — separate payment and Terminal API message context.
- [[source-adyen-docs-point-of-sale-shopper-engagement-display-data-display-qr-code]] — QR display child guide (navigation).
- [[source-adyen-docs-point-of-sale-shopper-engagement-display-data-display-receipt]] — virtual-receipt child guide (navigation).
- [[source-adyen-docs-point-of-sale-shopper-engagement-display-data-display-image]] — image child guide (navigation).
- [[source-adyen-docs-point-of-sale-shopper-engagement-display-data-idle-display]] — idle-screen child guide (navigation).

## Raw Sources

- [[raw/adyen/docs/point-of-sale/shopper-engagement/display-data/2026-09-15|Adyen Display data on the terminal, captured 2026-09-15]]
