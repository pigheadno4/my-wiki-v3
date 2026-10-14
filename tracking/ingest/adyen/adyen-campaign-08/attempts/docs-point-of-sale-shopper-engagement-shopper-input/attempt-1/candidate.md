---
title: "Adyen POS shopper input overview"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/shopper-engagement/shopper-input"
raw_files:
  - "adyen/docs/point-of-sale/shopper-engagement/shopper-input/2026-09-15.md"
tags: [adyen, point-of-sale, shopper-engagement, terminal-api, input]
---

## Overview

Adyen's shopper-input overview catalogs ways a Terminal API-integrated payment terminal can collect input from a shopper or staff member in addition to processing payments. The page says this interaction is between the merchant POS app and terminal, without the Adyen backend, and that the merchant must process collected input with its own business logic. This is a navigation page; it does not prove a payment, legally valid agreement/signature, identity verification, supported terminal model or current provider eligibility. [[adyen]] [[adyen-pos-shopper-engagement]] [[adyen-terminal-api]]

## Key takeaways

- The stated integration type is Terminal API with payment terminals. The overview gives examples such as collecting an email address or running a survey; it does not specify a `Device` versus `Service` message class, API fields, response schema, validation, timeout or cancellation outcomes. Read the selected child guide for those rules. See the introduction and `## Requirements`.
- It distinguishes **confirmation** (show information and ask the user to agree) from **signature** (show information and ask for a signature). It distinguishes a multiple-choice menu allowing **one** answer from a menu allowing **more than one**. These labels are guide routes, not proof that a response has legal consent or signature validity. See `## Input types`.
- **Digit** is described as whole-number input, with ZIP code or staff table number as examples. **Amount** displays currency and accepts a number with two decimals. **Phone number** pre-fills a country code from the terminal's location but lets the user change it. **Rating** lets the user choose 0–10, and **Text** is suggested for an email address. The overview does not define format checks, accepted ranges beyond the stated rating, masking, payment effects or safe storage. See `## Input types`.
- Each input type combines predefined display elements with merchant-supplied text. The user responds through the terminal keypad or on-screen keyboard/buttons. The page does not map UI variants to specific models. See `## Input types`.
- The overview links to **Cancel collecting input** for an in-progress request and **Create a session** to show a waiting screen while the merchant backend processes input. Those links provide navigation, not cancellation response codes, session lifetime or proof of processing completion. See `## Other related options`.

## Detail locators

- Introduction and `## Requirements`: POS-app/terminal communication boundary, merchant business logic and Terminal API integration type.
- `## Input types`: nine child-guide routes and their short UI/purpose descriptions: confirmation, signature, one/multiple answer menus, digit, amount, phone number, rating and text.
- `## Select an input request`: direct links to the nine input guides.
- `## Other related options`: cancel-in-progress and waiting-screen/session navigation.

## Related

- [[adyen-pos-shopper-engagement]] — shopper interaction hub.
- [[adyen-terminal-api]] — Terminal API request/response model; operation-specific rules require the selected child guide.
- [[source-adyen-docs-point-of-sale-shopper-engagement-shopper-input-confirmation]] — confirmation child guide.
- [[source-adyen-docs-point-of-sale-shopper-engagement-shopper-input-menu]] and [[source-adyen-docs-point-of-sale-shopper-engagement-shopper-input-multi-menu]] — one- and multiple-answer menu guides.
- [[source-adyen-docs-point-of-sale-shopper-engagement-shopper-input-digit]], [[source-adyen-docs-point-of-sale-shopper-engagement-shopper-input-amount]], [[source-adyen-docs-point-of-sale-shopper-engagement-shopper-input-phone-number]], and [[source-adyen-docs-point-of-sale-shopper-engagement-shopper-input-rating]] — field-specific guides.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/shopper-engagement/shopper-input/2026-09-15|Adyen shopper-input overview, fetched 2026-09-15]]
