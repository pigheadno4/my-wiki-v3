---
title: "Adyen Korean Card Payments via redirect overview"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cards/korean-cards"
raw_files:
  - "adyen/docs/payment-methods/cards/korean-cards/2026-09-15.md"
tags: [adyen, cards, korean-cards, redirect, online-payments]
---

## Overview

This [[adyen]] overview, last modified and captured **2026-09-15**, introduces Korean Card Payments via **Korea Cyber Payment (KCP)** as a hosted-page redirect from a merchant website or app. The page says KCP accepts cards issued in South Korea, including single- and co-branded cards (raw lines 15–23). Its table lists **credit/debit cards**, **KR**, and **KRW** (raw lines 25–27). This is a method overview under [[adyen-online-payments]], not proof of a particular merchant's current enablement or a completed card payment.

## Key takeaways

- The shopper proceeds from the merchant website or app to a **KCP-hosted payment page** (raw line 23). The page gives no return/result/webhook or card-data procedure; those need a selected integration guide and transaction evidence.
- The captured capability table marks **recurring, separate capture, partial capture, multiple partial captures and chargebacks unavailable**, while marking **refunds, partial refunds and multiple partial refunds available** (raw lines 25–27). These are page-level historical marks for the KR/KRW redirect method, not a guarantee that a merchant, transaction or region is enabled or that a refund succeeded.
- The page offers **Web** pre-built UI for a website and **API only** custom UI for website, iOS or Android app as child routes (raw lines 29–41). These links are navigation, not complete setup steps or authorization-outcome proof. The separately ingested Web Drop-in/Component and API-only sources hold their own flow-specific prerequisites and examples.

## Detail locators

- KCP identity and hosted redirect: raw lines 15–23.
- KR/KRW capability table and feature marks: raw lines 25–27.
- Web and API-only integration route descriptions: raw lines 29–41.
- General online-payments, 3DS, capture and payment-method links: raw lines 43–48.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-cards-korean-cards-web-drop-in]]
- [[source-adyen-docs-payment-methods-cards-korean-cards-web-component]]
- [[source-adyen-docs-payment-methods-cards-korean-cards-api-only]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/cards/korean-cards/2026-09-15|Full pinned Korean Cards redirect overview]]
