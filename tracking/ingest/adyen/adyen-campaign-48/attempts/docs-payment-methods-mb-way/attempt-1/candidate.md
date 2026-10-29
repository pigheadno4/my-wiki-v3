---
title: "Adyen MB WAY payment method overview"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/mb-way"
raw_files:
  - "adyen/docs/payment-methods/mb-way/2026-09-15.md"
tags: [adyen, mb-way, portugal, eur, wallet]
---

## Overview

This 2026-09-15-captured Adyen Docs overview describes MB WAY as a Portugal payment method and Multibanco solution. It contrasts Web phone-number/app confirmation with mobile app-to-app authorization, gives a PT/EUR capability matrix and daily cumulative user limit, and routes to platform guides. It states that an Adyen integration does not require a separate Multibanco contract. This snapshot is not evidence of current merchant enablement or a completed transaction. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- On **Web**, the shopper enters a mobile phone number, selects pay, and receives a notification in the MB WAY app to confirm the transaction. In a merchant **mobile app (App2App)**, the shopper selects MB WAY and is redirected to the MB WAY app to authorize; the overview says no phone-number entry is required for that path. These are distinct shopper journeys, not interchangeable request recipes. See raw lines 23–30.
- The matrix classifies MB WAY as a **direct wallet** for **PT/EUR**. It marks recurring, separate captures, partial captures, multiple partial captures, and chargebacks unavailable; refunds, partial refunds, and multiple partial refunds are marked available. These overview indicators do not supply endpoint instructions or prove merchant-specific capabilities. See raw lines 32–34.
- The page states a **default daily cumulative limit of EUR 1,000** for MB WAY users, adjustable by the user in the MB WAY app up to **EUR 5,000**. This is a user/day cumulative limit, not a per-payment cap or guaranteed acceptance threshold. See raw line 36.
- The page routes to Web, iOS, Android, React Native, Flutter, API-only, Pay by Link, and in-person guides. The API-only route describes building one's own UI for website or mobile app. See raw lines 38–86.

## Detail locators

- Shopper journeys and Multibanco contract statement: raw lines 23–30.
- PT/EUR capability matrix: raw lines 32–34.
- User daily cumulative limit: raw line 36.
- Platform/API/Pay by Link/in-person routes: raw lines 38–86.
- General online payments, 3DS, capture, and payment-method links: raw lines 88–93; these links do not add MB WAY-specific 3DS or capture assertions.

## Related

- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/mb-way/2026-09-15|Fully read MB WAY overview raw]]
