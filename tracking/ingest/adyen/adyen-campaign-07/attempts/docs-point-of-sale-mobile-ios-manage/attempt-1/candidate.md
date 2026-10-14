---
title: "Manage an Adyen iOS Mobile solution"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/mobile-ios/manage"
raw_files:
  - "adyen/docs/point-of-sale/mobile-ios/manage/2026-09-15.md"
tags: [adyen, point-of-sale, mobile-pos, ios, sdk-lifecycle, tap-to-pay, card-readers]
---

## Overview

Adyen's iOS Mobile management guide, captured 2026-09-15, covers tasks for going live and maintaining a merchant-device [[adyen-mobile-pos]] solution: accepting Apple's Tap to Pay terms, keeping the iOS Mobile SDK and device OS supported, updating reader and dock firmware where used, and monitoring version changes. These are ongoing operating conditions for Tap to Pay on iPhone and/or Card reader on iOS, not evidence that a particular merchant, device or transaction is currently eligible or successful.

## Key takeaways

- **Apple terms are Tap to Pay on iPhone only.** The terms must be accepted before Tap to Pay transactions. In test, acceptance occurs on the iPhone. In live Adyen for Platforms integrations, users are prompted on the iPhone at their first live Tap to Pay transaction on that phone. A live merchant that is neither a platform nor marketplace can accept through its merchant account in live Customer Area, covering iPhones transacting under that account; the page sends doubtful acceptance outcomes to Apple Business Connect because Adyen does not know every result. This terms procedure does not apply to Card reader on iOS.
- **SDK support has two different cutoff effects for both paths.** The page says an iOS Mobile SDK version expires six months after release: card-reader PIN transactions are blocked, while Tap to Pay on iPhone and card-reader transactions without PIN remain possible. Twelve months after expiry (18 months after release), removal blocks all transactions and removes that version from GitHub. Update to a supported SDK before removal; the page says earlier MINOR or PATCH versions do not receive bug fixes. Only SDK 2.9.0 or later is visible in Customer Area.
- **Device OS is another gate for both paths.** Below the minimum required iOS version, all Mobile SDK transactions are blocked. The page also gives a Tap to Pay on iPhone one-year OS-update rule and version-specific reminders/errors; the current minimum belongs to its separate software-requirements source, not this guide.
- **Reader hardware needs its own updates.** For Card reader on iOS, check and update reader firmware. A USB dock paired with that path has a separate firmware duty. The SDK supplies alert/update screens; custom UI must implement that functionality if the built-in UI is not used. These duties do not apply to Tap to Pay on iPhone alone.

## Detail locators

- Raw `## Accept Apple Terms of Use for Tap to Pay on iPhone` (lines 21–49): test versus live platform and merchant-account acceptance routes, Customer Area procedure and Apple Business Connect status caveat.
- Raw `## Enable accessibility mode for PIN transactions` and `## Set the transaction screen text` (lines 51–77): Tap to Pay-only accessibility toggle and transaction branding controls; location may make accessibility a regulatory requirement.
- Raw `## Keep the Mobile SDK up to date` (lines 79–121): expiry, removal, semantic-version support policy, Customer Area visibility and release-note lookup.
- Raw `## Keep the device OS up to date` (lines 123–158): minimum OS block and Tap to Pay reminder behavior by iOS release.
- Raw `## Keep the card reader up to date`, `## Keep the dock up to date`, and `## Stay informed about version changes` (lines 160–204): hardware-specific firmware checks, built-in versus custom update UI, system-message subscription.
- Raw `## Change the language` (lines 206–262): supported languages, English fallback, card-reader-only primary/secondary/card language priority, and Support-mediated receipt language.
- Raw `## Use Tap to Share` (lines 264–281): a separate Tap to Pay on iPhone session feature for device connection even without payment; the dated page lists iPhone 12+ and iOS 27+ and points to Apple's integration guide. This is not a payment outcome or a general Mobile SDK eligibility rule.

## Related

- [[adyen-mobile-pos]] — merchant mobile-device solution hub.
- [[source-adyen-docs-point-of-sale-mobile-ios]] — iOS solution overview and payment-interface distinction.
- [[adyen-mobile-card-readers]] — reader hardware boundary.
- [[adyen-ios-sdk]] — separately versioned native online-checkout SDK, outside this POS guide.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/mobile-ios/manage/2026-09-15|Manage your iOS Mobile solution, fetched 2026-09-15]]
