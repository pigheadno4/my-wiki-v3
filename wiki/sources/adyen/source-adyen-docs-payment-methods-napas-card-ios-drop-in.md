---
title: "Adyen Napas card iOS Drop-in add-on"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/napas-card/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/napas-card/ios-drop-in/2026-09-15.md"
tags: [adyen, napas, vietnam, ios, drop-in, cards]
---

## Overview

This 2026-09-15 Adyen page describes adding **Napas card to an existing iOS Drop-in integration**. It gives method-specific field/configuration statements, test fixture locations and a separate live request. It does not specify the full redirect/return or final payment-outcome procedure. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Prerequisite and method fields:** The guide requires an existing iOS Drop-in integration and Napas card added in the **test Customer Area** before beginning. It says no extra Napas card API fields are required and routes generic optional fields to the applicable endpoint reference. It calls `/sessions` the default for **Drop-in v5.0.0 or later**, with `/payments` for an additional use case. v5.0.0 is a **Drop-in version**, not an asserted Checkout API minimum. (raw lines 21–33)
- **Drop-in configuration:** Both the v5.0.0-or-later and v4.x.x tabs say there is no required Napas-specific Drop-in integration. This method-specific statement does not remove the base iOS Drop-in setup, test Customer Area step or result handling supplied elsewhere. (raw lines 35–43)
- **TEST and live boundary:** The page lists test-only card/OTP fixtures for success, blocked card, insufficient funds and amount-over-limit scenarios; the sensitive example values remain at raw lines 47–54. It directs checking test payment status in Customer Area. Live acceptance separately requires submitting a Napas card request in the **live Customer Area**. A named “Successful” fixture or status-list link is not evidence of an executed authorization, capture or settlement. (raw lines 45–58)
- **Navigation mismatch:** Under “See also,” the link is labeled **iOS Components integration guide** and points to a Components Sessions URL even though this page's title and prerequisite are **iOS Drop-in**. Treat that as related navigation, not a replacement for the requested Drop-in base guide. This page does not independently document which shopper gateway handles card/PIN/OTP entry or how callbacks determine the final result. (raw lines 15–26, 60–64)

## Detail locators

- iOS Drop-in and test Customer Area prerequisite: raw lines 15–26.
- No extra fields, `/sessions` default and Drop-in v5.0.0 qualifier: raw lines 28–33.
- v5/v4 no-specific-configuration statements: raw lines 35–43.
- TEST scenarios and live request: raw lines 45–58.
- See-also Components versus Drop-in mismatch: raw lines 60–64.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-napas-card]]
- [[source-adyen-docs-payment-methods-napas-card-ios-component]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/napas-card/ios-drop-in/2026-09-15|Adyen Napas card iOS Drop-in, 2026-09-15 snapshot]]
