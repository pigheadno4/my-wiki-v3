---
title: "Adyen Revolut Pay overview"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/revolutpay"
raw_files:
  - "adyen/docs/payment-methods/revolutpay/2026-09-15.md"
tags: [adyen, revolut-pay, wallet, pilot, closed-beta, authentication]
---

## Overview

This 2026-09-15 Adyen overview presents Revolut Pay as a Revolut-account digital wallet and explicitly labels it a **pilot-phase, closed-beta** offering with an eligibility-based access request. It describes mobile and desktop shopper sign-in/checkout paths, a capability table, and an API-only child route. The captured page does not prove present availability, merchant eligibility, beta approval or a completed payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Access gate:** the page says Revolut Pay is in a pilot phase and still a closed beta. It invites a request for access and says Adyen will discuss next steps **if eligible**. The historical invitation is not evidence that any account is enabled or that the pilot terms remain current. (raw lines 23, 36–38)
- **Shopper paths:** the page describes payment directly from a Revolut account with an authentication flow. On mobile it says the shopper is redirected to the Revolut app, with browser sign-in/checkout if the app is absent. On desktop/laptop it says a new tab offers QR, email, SMS or passkey sign-in, followed by app or browser payment channels. The table separately labels the payment flow **Direct**; that label does not erase the described app/new-tab handoff or specify Checkout API action handling. Neither sign-in nor app redirection proves authorization or settlement. (raw lines 25–34)
- **Capability snapshot:** the table labels wallet, **International** countries and **Multiple** currencies without enumerating supported jurisdictions or currencies. It marks recurring unavailable, refunds/partial refunds and separate/partial captures available, multiple partial refunds and multiple partial captures unavailable, and chargebacks available. The two multiple-partial x marks say “See note,” but no explanatory note appears on this captured page; use a more specific authority before acting on limits. These marks do not prove merchant-specific eligibility or actual transaction behavior. (raw lines 32–38)
- **Implementation route:** this overview links an **API-only** child guide for building a website/iOS/Android UI. It gives no request fields, API/SDK version, return URL, webhook outcome, capture procedure or refund execution here. (raw lines 40–53)

## Detail locators

- Pilot/closed-beta identity and eligibility request: pinned raw lines 15–25 and 36–38.
- Mobile and desktop shopper paths and Direct-flow table label: pinned raw lines 25–34.
- Country/currency labels and feature marks, including unresolved “See note”: pinned raw lines 32–34.
- API-only platform route and general navigation: pinned raw lines 40–53.

## Related

- [[adyen-online-payments]] — main provider payment-method context
- [[adyen]] — provider

## Raw Sources

- [[raw/adyen/docs/payment-methods/revolutpay/2026-09-15|Revolut Pay overview, 2026-09-15]]
