---
title: "Adyen PayMe payment method overview"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/payme"
raw_files:
  - "adyen/docs/payment-methods/payme/2026-09-15.md"
tags: [adyen, payme, wallets, hong-kong, online-payments]
---

## Overview

This 2026-09-15 Adyen overview describes **PayMe** as a Hong Kong wallet method whose shoppers can top up their balance from a bank account. It identifies the shopper payment handoff, a Hong Kong local-entity prerequisite, a capability matrix and Web, iOS, Android and API-only integration guide routes. It is a documentation snapshot, not evidence of current merchant eligibility or a completed payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Shopper handoff:** On desktop or laptop, shoppers scan a QR code to pay in the PayMe app; on mobile, they are redirected to that app. These are shopper actions, not a stated authorization or settlement result. (raw lines 19–21)
- **Acceptance prerequisite and scope:** The page says a merchant must have a local entity in Hong Kong to accept PayMe. Its matrix lists wallets, an additional-action flow, HK and HKD. It does not describe onboarding, account approval or the details of that additional action. (raw lines 23–27)
- **Matrix capabilities:** The table marks refunds, partial refunds and multiple partial refunds as supported. It marks recurring, separate captures, partial captures, multiple partial captures and chargebacks as unsupported. These are overview matrix flags; use the linked lifecycle guides for execution rules and status handling. (raw lines 25–27)
- **Integration routes:** The page links pre-built Web, iOS and Android UI guides and an API-only route for a merchant-built UI. It gives no SDK/API minimum version, request schema, result handling or live enablement procedure. (raw lines 29–53)

## Detail locators

- Wallet identity, QR/app handoff and local-entity requirement: raw lines 15–23.
- Country/currency/payment-flow and capability matrix: raw lines 25–27.
- Web, iOS, Android and API-only guide routes: raw lines 29–53.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/payme/2026-09-15|Adyen PayMe overview, 2026-09-15 snapshot]]
