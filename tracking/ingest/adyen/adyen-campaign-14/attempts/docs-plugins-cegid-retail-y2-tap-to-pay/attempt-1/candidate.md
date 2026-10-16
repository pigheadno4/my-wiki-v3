---
title: "Tap to Pay with Cegid Retail Y2 | Adyen Docs"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/cegid-retail-y2/tap-to-pay"
raw_files:
  - "adyen/docs/plugins/cegid-retail-y2/tap-to-pay/2026-09-15.md"
tags: [adyen, cegid-retail-y2, tap-to-pay, ios, android, mobile-pos]
---

## Overview

This 2026-09-15 [[adyen]] Docs guide describes two optional Tap to Pay extensions after a Cegid Retail Y2 CPOS setup: Cegid Retail Mobile POS on iPhone using Adyen's iOS Mobile SDK, and Cegid Retail Live Store on Android using the separate Adyen Payments app. It describes prerequisites and setup, not account approval, device eligibility or a completed contactless payment. [[adyen-cegid-retail-y2]]

## Key takeaways

- **iPhone:** The guide requires InStoreHub on Windows with the CPOS plugin, Retail Mobile POS v5.1.766+, Retail Y2 v18+, and an iPhone meeting linked hardware/iOS requirements. Without InStoreHub, payment receipts cannot be printed; the merchant must check local fiscal rules and ask Cegid about launching without it. Cegid activates the extension, with additional costs, and Adyen must enable Tap to Pay on iPhone for the account. Testing requires a device in Developer Mode. These iPhone-specific requirements should not be replaced by the overview's general Retail Y2 v11.05+ floor.
- **Android:** Retail Live Store hands the flow to the independently downloaded Adyen Payments app, which returns a result to Live Store; this is not the iOS Mobile SDK route. The page lists customer-present payments and optional unreferenced refunds, but sends Live Store version and Android hardware/software eligibility to separate Cegid/Adyen requirements. It distinguishes Test and Live Payments apps and requires a Customer Area API credential/key, client key, **Adyen Payments App role**, encryption key identifier/passphrase/version, **Merchant Account ID** rather than Company Account ID, and **Store ID** rather than store reference if store routing is used. Support must enable Tap to Pay on Android and short responses; unreferenced refunds are optional enablement.
- The Android Payments app performs mandatory PCI-related device checks before showing PIN entry. Developer Options, accessibility services, recording/sharing, camera use during payment and overlay apps have the page's specific restrictions; a passcode/PIN is required. If a check fails, the app cancels the transaction and does not show PIN entry. Do not transfer the iPhone testing Developer Mode instruction to Android live payment settings.
- A CPOS setup and both platform-specific enablement routes are prerequisites. The guide provides a shopper-tap and result-display sequence, but a displayed result is not independent proof of authorization, capture, settlement or bank receipt. The linked device/OS requirements and market terms own eligibility; this page gives no complete regional availability matrix.

## Detail locators

- **CPOS prerequisite and iPhone/Android architecture split:** raw lines 17–28.
- **iPhone versions, InStoreHub/receipts, activation, costs and test mode:** raw lines 30–73.
- **Android separate app, feature list, device/version and Test/Live setup:** raw lines 75–120.
- **Android credential/account/store identity, Support enablement and security gates:** raw lines 122–155.

## Related

- [[adyen]]
- [[adyen-cegid-retail-y2]]
- [[adyen-mobile-pos]] — platform-level mobile POS context, distinct from this Cegid setup

## Raw Sources

- [[raw/adyen/docs/plugins/cegid-retail-y2/tap-to-pay/2026-09-15|Adyen Cegid Tap to Pay guide — collected 2026-09-15]]
