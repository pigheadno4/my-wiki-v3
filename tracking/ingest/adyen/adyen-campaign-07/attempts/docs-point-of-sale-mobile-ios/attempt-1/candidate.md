---
title: "Adyen iOS Mobile solutions overview"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/mobile-ios"
raw_files:
  - "adyen/docs/point-of-sale/mobile-ios/2026-09-15.md"
tags: [adyen, point-of-sale, mobile-pos, ios, tap-to-pay, card-readers]
---

## Overview

Adyen's iOS Mobile solutions overview, captured 2026-09-15, introduces two in-person payment interfaces started from a merchant iOS POS app: Tap to Pay on iPhone uses the iPhone as the payment interface; the paired card-reader path uses the reader as the payment interface. The app and Mobile SDK route is [[adyen-mobile-pos]], distinct from apps installed on Adyen Android payment terminals and the separately versioned [[adyen-ios-sdk]] for native online checkout.

## Key takeaways

- With Tap to Pay on iPhone, the shopper taps a card or digital-wallet device on the merchant iPhone. With a Bluetooth-paired card reader, the shopper uses the reader for tap, insert, swipe or wallet presentation.
- The merchant's iOS POS app must integrate with Terminal API before adding the iOS Mobile SDK. The same iOS Mobile SDK serves both solutions and includes mobile-to-reader pairing functionality for the card-reader path. See [[adyen-terminal-api]] for the Terminal API boundary.
- The two payment-interface paths can be used alongside each other **if the POS app allows selecting the payment interface**. This dated overview does not establish current device, OS, region, merchant entitlement, SDK-version or live-payment eligibility; follow the linked requirements and build guides for those gates.

## Detail locators

- Raw `# iOS Mobile solutions` (lines 19–25): paired-device model and the two shopper interfaces.
- Raw `## Mobile SDK` (lines 27–31): merchant POS app, Terminal API integration and common iOS Mobile SDK, including reader pairing.
- Raw `## Next steps` (lines 33–75): links to system requirements, security, checklists, solution understanding, build, management and error handling. The linked pages must be read for their own conditions; this overview's navigation labels are not proof of those details.

## Related

- [[adyen-mobile-pos]] — common merchant-device Mobile POS route.
- [[adyen-mobile-card-readers]] — card-reader hardware route; model-specific capabilities need their own evidence.
- [[adyen-ios-sdk]] — separately versioned online-checkout SDK.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/mobile-ios/2026-09-15|iOS Mobile solutions, fetched 2026-09-15]]
