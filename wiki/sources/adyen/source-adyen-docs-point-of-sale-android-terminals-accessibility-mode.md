---
title: "Adyen Android terminal accessibility mode overview"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/android-terminals/accessibility-mode"
raw_files:
  - "adyen/docs/point-of-sale/android-terminals/accessibility-mode/2026-09-15.md"
tags: [adyen, point-of-sale, android-terminals, accessibility, audio-guidance]
---

## Overview

Adyen's dated Android-terminal accessibility overview describes audio guidance for shoppers with visual impairments and routes to two activation paths: a merchant POS app payment request or actions on the payment terminal. It is a navigation page for terminal audio guidance, not an accessibility certification, legal-compliance conclusion, device-eligibility guarantee, or proof of a successful payment. [[adyen]] [[adyen-android-terminals]]

## Key takeaways

- Adyen says accessibility mode must first be enabled for the merchant's terminals. During an accessible payment, the terminal reads screen instructions and UI elements touched as the shopper moves a finger over the display. The overview notes that legal accessibility obligations may depend on location but gives no jurisdiction-specific rule. See the introductory paragraphs and `## Methods to turn on accessibility mode` in the pinned raw.
- The POS-app route sends a payment request with a Base64-encoded `Operation` object. The terminal-side route lists headphones, an on-screen button, or holding the physical keypad's **5** key if present. The overview gives no model/software eligibility matrix, PIN-screen behavior or payment-feature exclusions; use its detailed routes for those conditions. See `## Methods to turn on accessibility mode` and `## Next steps`.
- After a successful or canceled accessible payment, the terminal returns to regular mode automatically. This describes the mode lifecycle, not an assurance that any given transaction succeeds. See `## Methods to turn on accessibility mode`.

## Related

- [[adyen-android-terminals]] — terminal feature and model routes.
- [[source-adyen-docs-point-of-sale-android-terminals-accessibility-mode-accessibility-from-terminal]] — detailed terminal-side setup, model/software and activation limits from a separately captured guide.

## Related raw API references

- [[raw/adyen/docs/point-of-sale/android-terminals/accessibility-mode/accessibility-from-pos/2026-09-15|POS-app accessibility activation detail — navigation only; not read for this source]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/android-terminals/accessibility-mode/2026-09-15|Adyen accessibility mode on Android terminals overview, fetched 2026-09-15]]
