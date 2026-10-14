---
title: "Build your iOS Mobile solution — Adyen overview"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/mobile-ios/build"
raw_files:
  - "adyen/docs/point-of-sale/mobile-ios/build/2026-09-15.md"
tags: [adyen, point-of-sale, mobile-pos, ios, mobile-sdk, integration]
---

## Overview

Adyen's iOS Mobile build landing page, captured 2026-09-15, routes merchants building their **own iOS POS app** with the iOS Mobile SDK to **Tap to Pay on iPhone** or **Card reader on iOS** instructions. It belongs to [[adyen-mobile-pos]], a merchant-device in-person path distinct from [[adyen-ios-sdk]] for native online checkout and from apps installed on Adyen Android payment terminals. The page tells users of a ready-made partner Tap to Pay or card-reader solution to skip this build section.

## Key takeaways

- The two iOS payment-interface solutions use the **same iOS Mobile SDK**. They can coexist if the merchant POS app lets the user select the payment interface; the landing page does not say every app implements that selection.
- The page frames integration as merchant development work: a **server-to-server** call establishes a secure SDK-to-Adyen communication session, and the POS app integrates with **Terminal API**. It says `PaymentRequest` must be supported and `ReversalRequest` is preferable. These are overview-level tasks, with detailed behavior delegated to the linked build and Terminal API pages.
- This snapshot says integrating Adyen's native SDK into a cross-platform app is possible but complex and says Adyen does not offer cross-platform wrappers **at the time represented by this page**. That is a dated statement, not current wrapper availability.
- The page links to an **Understand your solution** guide for solution choice, transaction flows and session background, and to separate **Tap to Pay on iPhone** and **Card reader on iOS** build guides. These links are navigation; this overview alone supplies no device/iOS/SDK-version floor, country or payment-method list, Apple entitlement, card-reader model, account approval, live enablement or payment-success proof. Consult the relevant detailed source for those conditions.

## Detail locators

- Raw `# Build your iOS Mobile solution` (lines 15–23): intended self-build audience, partner-solution exclusion, shared SDK and conditional coexistence.
- Raw `## Integration effort` (lines 25–37): backend session, Terminal API `PaymentRequest`/preferred `ReversalRequest`, and dated cross-platform wrapper statement.
- Raw `## Resources` and `## Choose a solution` (lines 39–57): optional Apple resources and links to the two separate iOS build routes; linked content must be read for its own conditions.

## Related

- [[adyen-mobile-pos]] — merchant-device in-person solution hub.
- [[adyen-terminal-api]] — POS message interface named in the integration-effort section.
- [[source-adyen-docs-point-of-sale-mobile-ios-build-tap-to-pay]] — linked Tap to Pay on iPhone build route; consult for its own steps.
- [[source-adyen-docs-point-of-sale-mobile-ios-build-card-reader]] — linked card-reader build route; consult for its own steps.
- [[adyen-ios-sdk]] — separate native online-checkout SDK.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/mobile-ios/build/2026-09-15|iOS Mobile build overview, fetched 2026-09-15]]
