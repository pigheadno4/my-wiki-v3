---
title: "Adyen Klarna Android integration chooser"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/klarna/android"
raw_files:
  - "adyen/docs/payment-methods/klarna/android/2026-09-15.md"
tags: [adyen, klarna, android, drop-in, components]
---

## Overview

This [[adyen]] page is an Android integration chooser for Klarna. It links to an all-in-one Drop-in guide, a Redirect Component guide, and general Android Sessions flow guides for both UI options. It does not give method request fields, SDK versions, payment result handling or capture rules; use the linked child guide and [[adyen-online-payments]] for those topics.

## Key takeaways

- **Android routes:** Drop-in points to `/payment-methods/klarna/android-drop-in`; Components points to `/payment-methods/klarna/android-component` and calls it a Redirect Component (raw lines 19–27).
- **Base integration context:** The final line links general Android Sessions Drop-in and Components guides (raw line 29). Those are navigation links, not evidence that both child pages use only Sessions flow or that a merchant can already process Klarna payments.
- **Scope boundary:** The chooser has no product-country matrix, request schema, returned action, final outcome, capture or recurring instructions. Follow the relevant Klarna overview and child implementation guide.

## Detail locators

- Page identity and Android UI choices: pinned raw lines 15–27.
- General Android Sessions guide links: pinned raw line 29.

## Related

- [[adyen-online-payments]] — provider online checkout and concept route.
- [[source-adyen-docs-payment-methods-klarna]] — product-level Klarna qualifications.
- [[source-adyen-docs-payment-methods-klarna-android-drop-in]] — Drop-in child guide.

## Related raw API references

- [[raw/adyen/docs/payment-methods/klarna/android-component/2026-09-15|Klarna Android Redirect Component child guide]] — navigation only; child content was not used as behavioral evidence.

## Raw Sources

- [[raw/adyen/docs/payment-methods/klarna/android/2026-09-15|Klarna Android chooser, captured 2026-09-15]]
