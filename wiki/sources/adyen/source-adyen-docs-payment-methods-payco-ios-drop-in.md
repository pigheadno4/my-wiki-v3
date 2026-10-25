---
title: "Adyen PayCo iOS Drop-in guide"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/payco/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/payco/ios-drop-in/2026-09-15.md"
tags: [adyen, payco, ios, drop-in, redirect]
---

## Overview

This 2026-09-15 Adyen page gives PayCo-specific additions for existing iOS Drop-in integrations using either Sessions or Advanced server-side flow. It covers prerequisites, method-specific request/configuration omissions, and testing assistance; it does not document a completed payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Sessions requires an existing iOS Drop-in Sessions integration using Checkout API v68 or later and PayCo added in the Customer Area. The page says no additional parameters are needed in the base `/sessions` request and no additional PayCo configuration is needed. Unlike its Advanced requirements row, this Sessions section does not explicitly list redirect handling.
- Advanced requires an existing iOS Drop-in Advanced integration, redirect handling for `action.type: redirect`, and PayCo added in the Customer Area. The page says no additional PayCo configuration or base `/payments` parameters are needed. It does not state a Checkout API minimum for Advanced.
- Under both “Test and go live” headings, the page says there are no specific PayCo test credentials and directs readers to Adyen Support for testing assistance. It gives no test transaction, live activation confirmation, or final payment-result procedure.

## Detail locators

- Sessions prerequisites: pinned raw lines 25–34; no additional `/sessions` parameters/configuration: lines 36–46; testing guidance: lines 48–54.
- Advanced prerequisites: lines 56–66; no additional configuration or `/payments` parameters: lines 68–78; repeated testing guidance: lines 80–86.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-payco]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/payco/ios-drop-in/2026-09-15|PayCo iOS Drop-in, 2026-09-15]]
