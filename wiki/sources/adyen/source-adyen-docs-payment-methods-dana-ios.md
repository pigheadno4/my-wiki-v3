---
title: "DANA for iOS integration chooser"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/dana/ios"
raw_files:
  - "adyen/docs/payment-methods/dana/ios/2026-09-15.md"
tags: [adyen, dana, ios, navigation]
---

## Overview

This 2026-09-15 Adyen page is an **iOS integration chooser** for DANA. It links Drop-in and Components child guides and four base iOS integration guides. It states that the main integration comes before adding DANA, but does not itself document method configuration, eligibility or a transaction result. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- The **Drop-in** child link is described as an all-in-one UI solution for adding DANA to an iOS app. The **Components** child link names `InstantPaymentComponent` for DANA payments. These are page labels and routes; implementation behavior is supplied by the linked child guide. (raw lines 19–27)
- The See also section says to create the main integration before adding DANA and links iOS Drop-in and iOS Components main guides for **Sessions** and **Advanced** flows. Those base-guide links do not by themselves prove which flows each DANA child supports or state child-specific SDK/API versions. (raw lines 29–36)
- This chooser provides no DANA merchant-eligibility or ID/IDR rule, request/configuration fields, redirect or return handling, token/recurring steps, TEST/LIVE gate, webhook state or observed authorization/capture/settlement. Follow the relevant child and method guides for those claims. (raw lines 15–36)

## Detail locators

- Drop-in and Components child-guide links: raw lines 19–27.
- Main-integration sequencing and four Sessions/Advanced base links: raw lines 29–36.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-dana]]
- [[source-adyen-docs-payment-methods-dana-ios-drop-in]]
- [[source-adyen-docs-payment-methods-dana-ios-component]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/dana/ios/2026-09-15|Adyen DANA for iOS, 2026-09-15 snapshot]]
