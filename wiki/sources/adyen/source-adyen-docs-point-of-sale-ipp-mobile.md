---
title: "What we support in our Mobile solutions | Adyen Docs"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/ipp-mobile"
raw_files:
  - "adyen/docs/point-of-sale/ipp-mobile/2026-09-15.md"
tags: [adyen, point-of-sale, mobile-pos, tap-to-pay, card-readers, solution-comparison]
---

## Overview

This Adyen Docs comparison maps in-person Mobile POS solutions using a merchant Android or iOS device: Tap to Pay on that device or a mobile device paired with a card reader. In both cases a merchant POS app starts the transaction. The page compares an embedded Android/iOS Mobile SDK with the separate Android Payments app, then provides dated region, payment-method and feature matrices. It concerns merchant-device in-person payments, not Adyen Android-terminal app deployment or the native online Checkout SDK. See [[adyen]], [[adyen-mobile-pos]], and [[adyen-terminal-api]].

## Key takeaways

- In Tap to Pay, the merchant mobile device is the payment interface for contactless cards or wallet devices. The shopper can enter a PIN on the mobile device when required, but cannot insert or swipe a card. With the card-reader solution, the reader accepts tap, insert or swipe and wallets; the page still places PIN entry on the mobile device. The full device/reader hardware requirements live in separate Android and iOS guides.
- The POS app can embed Adyen's Android or iOS Mobile SDK, or communicate with an Adyen Payments app that contains the SDK. Either option still requires the POS app to integrate Terminal API. The embedded SDK can support Tap to Pay and card reader alongside each other if the POS app lets users choose the payment interface. In this snapshot, the Payments app is Android-only and Tap-to-Pay-only; the option table has no iOS Payments app or Payments-app card-reader route. No specific SDK or OS version is established here.
- The region matrix is solution-specific, not a global Mobile POS availability promise. For example, the 2026-09-15 table marks Tap to Pay on iPhone in Canada and Japan while the other three columns are unmarked there; Malaysia marks Tap to Pay on Android, Android card reader and iOS card reader, but not Tap to Pay on iPhone; its EU row excludes Greece for Android Tap to Pay, Android reader and iOS reader while listing named countries for Tap to Pay on iPhone. Consult the complete table for each country and current account/device enablement.
- Payment-method support also differs by interface and region: the snapshot marks Interac Debit and JCB for Tap to Pay on iPhone only; Diners and Discover card-reader entries are US-only; eftpos and UnionPay (CUP) are marked on Tap to Pay but not card readers. The complete matrix, rather than a method name alone, governs the page's advertised combination. These rows do not prove merchant or shopper eligibility or a successful authorization.
- The functionality table marks contactless and PIN across all four solution columns, EMV chip and magstripe only for reader columns, and card acquisition for none. It marks Store and Forward offline payments on the two iOS columns but not Android; surcharge is AU/NZ only for the two Tap-to-Pay columns and unmarked for readers. A table check is dated support information, not a guarantee that an offline payment, surcharge, refund, PIN flow or other feature works for a particular device, SDK release, merchant account, or transaction. Follow the detailed linked guides for operational rules.

## Detail locators

- `What we support in our Mobile solutions` and `Solution options`, pinned raw lines 15–47: mobile-device versus reader payment interface, PIN placement, SDK/Payments-app choices, Terminal API prerequisite and option table.
- `Supported device types`, lines 49–54: navigation to Android and iOS hardware requirement guides; exact models and OS versions are outside this page.
- `Supported countries/regions`, lines 56–73: four-column country/region matrix and exclusions.
- `Supported payment methods`, lines 75–96: per-interface scheme/wallet matrix and US-only reader qualifications.
- `Supported functionality`, lines 98–119: transaction, offline, surcharge, CVM, contactless/chip/magstripe and card-acquisition rows.
- `Next steps`, lines 121–133: separate Android and iOS requirements, integration and maintenance guide routes.

## Related

- [[adyen-mobile-pos]] — main merchant-device Mobile POS solution hub.
- [[adyen-terminal-api]] — message interface required by the POS app in the compared routes.
- [[adyen-mobile-card-readers]] — paired reader-specific evidence.
- [[adyen-android-terminals]] — apps installed on Adyen terminals, a different hardware context.
- [[adyen-ios-sdk]] and [[adyen-android-sdk]] — native online Checkout SDK contexts, not this POS Mobile SDK.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/ipp-mobile/2026-09-15|Adyen Mobile solution support comparison, fetched 2026-09-15]]
