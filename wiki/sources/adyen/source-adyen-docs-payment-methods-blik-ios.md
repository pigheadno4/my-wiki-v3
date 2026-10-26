---
title: "Adyen BLIK for iOS integration chooser"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/blik/ios"
raw_files:
  - "adyen/docs/payment-methods/blik/ios/2026-09-15.md"
tags: [adyen, blik, ios, drop-in, components]
---

## Overview

This 2026-09-15 Adyen page is an **iOS integration chooser** for BLIK. It routes to iOS Drop-in and Components child guides and to the corresponding Sessions main integration guides. It does not define BLIK code entry, One Click consent, SDK version, request fields, waiting-screen/webhook outcome or live certification; the child guides provide those details. This route does not prove current merchant eligibility or a completed payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Drop-in is described as Adyen's all-in-one UI solution for adding BLIK to an iOS app. Its child guide owns the actual implementation and payment lifecycle. (raw lines 19–25)
- Components is described as the **Redirect Component** route for iOS. The child guide owns its method-specific setup and outcome behavior; this chooser does not identify a particular Component class. (raw lines 27–31)
- The final line links iOS Drop-in and Components **Sessions-flow** main guides. Those links are navigation, not a claim that only Sessions exists or that either route is enabled for an account. The source image alt text calls the icons “web,” but the headings, links and prose consistently say iOS; that icon labeling does not change platform scope. (raw lines 21–33)

## Detail locators

- iOS identity and Drop-in/Components child routes: pinned raw lines 15–31.
- iOS Sessions base-guide navigation and icon alt-text mismatch: pinned raw lines 21–33.

## Related

- [[adyen-online-payments]] — main provider integration context
- [[source-adyen-docs-payment-methods-blik-ios-drop-in]] — iOS Drop-in implementation
- [[source-adyen-docs-payment-methods-blik-ios-component]] — iOS Components implementation
- [[source-adyen-docs-payment-methods-blik]] — BLIK method overview

## Raw Sources

- [[raw/adyen/docs/payment-methods/blik/ios/2026-09-15|BLIK iOS chooser, 2026-09-15]]
