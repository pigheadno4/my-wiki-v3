---
title: "Adyen iOS Mobile POS security guidance"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/mobile-ios/security"
raw_files:
  - "adyen/docs/point-of-sale/mobile-ios/security/2026-09-15.md"
tags: [adyen, point-of-sale, mobile-pos, ios, security, pci-mpoc]
---

## Overview

This dated Adyen guide covers security claims and integration practices for iOS Mobile POS, with a Tap to Pay on iPhone MPoC section and shared iOS Mobile SDK guidance that also discusses the card-reader interface. It identifies an irreversible consequence of removing a device passcode from a device holding store-and-forward offline payments. See [[adyen]], [[adyen-mobile-pos]] and [[adyen-api-access]]. The product approval described here is not certification or safety proof for a merchant's particular POS app, network or deployment.

## Key takeaways

- Adyen says Tap to Pay on iPhone is PCI SSC validated as an MPoC solution for **iOS 18.4 and later**. The page says Apple continues support on some earlier versions as approved by Adyen, with the same yearly deprecation. In this Tap to Pay section, it says a communication session only works within one year of the release of the specific major, minor or patch iOS version; the cited 18.4 and 18.4.1 dates are examples, not current support dates. It recommends targeting the latest major iOS release for a new Mobile solution.
- Adyen says the Mobile SDK does not keep card or wallet payment details locally, sends and receives encrypted payment messages, and uses code obfuscation and OS/device/app/SDK monitoring and attestation. For **Tap to Pay on iPhone**, it attributes transaction encryption and handling to Apple's Secure Element. For the separate **card-reader** interface, it calls the reader a PCI PTS-approved Secure Card Reader that encrypts payment details immediately. These are Adyen's product claims in the snapshot, not a verified property of a specific integration.
- The page's **must** practices are to keep Adyen API keys secret on the server, never call Adyen APIs directly from the mobile POS app, and set a device passcode. It additionally **recommends** secure POS-app/server communication with mutual authentication such as mTLS to prevent tampering with Terminal API requests; app user login; current SDK, OS and security patches; trusted SDK downloads and integrity checks when possible; and the TEST SDK only for internal development/testing. It warns that older SDK versions stop having transaction requests accepted after a short grace period, without giving a fixed duration.
- The iOS SDK uses Keychain in core operation. From **iOS Mobile SDK 3.18.0**, a passcode is required to call any `PaymentService` function. Changing the passcode is allowed; **removing** it blocks transactions on that device and makes store-and-forward offline payments created while the passcode was set unrecoverable. The page suggests `Never` display lock or a simple staff-rememberable passcode if normal passcode use is inconvenient; it does not remove the passcode requirement.

## Detail locators

- `## PCI approval of Tap to Pay on iPhone`: MPoC solution and version-specific iOS release window, including the earlier-version qualification.
- `## Security of the solution`: SDK encryption/no-local-retention and attestation claims; distinct Secure Element and card-reader paths.
- `## Security best practices`: server-held API keys, no direct app-to-Adyen API calls, must versus recommended controls, SDK age and TEST distribution boundaries.
- `### Setting a device passcode`: Keychain dependence, SDK 3.18.0 enforcement, changing versus removing a passcode, and unrecoverable stored offline payments.

## Related

- [[adyen-mobile-pos]] — iOS Mobile solution routes and build/management evidence.
- [[adyen-mobile-card-readers]] — physical reader path.
- [[adyen-api-access]] — API credential handling context.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/mobile-ios/security/2026-09-15|Adyen Security of the iOS Mobile solutions, captured 2026-09-15]]
