---
title: "Adyen Swish Android Drop-in integration guide"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/swish/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/swish/android-drop-in/2026-09-15.md"
tags: [adyen, swish, android, drop-in, qr]
---

## Overview

This 2026-09-15 Adyen guide adds Swish to an existing Android Drop-in integration in either Sessions or Advanced server-side flow. It covers Customer Area setup, an optional submit-button setting, Advanced `qr` action handling and TEST simulator instructions. This method add-on relies on the main Android Drop-in guides for the full payment flow. The snapshot does not establish current merchant eligibility, a completed live payment, capture or settlement. See [[adyen]], [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-swish]].

## Key takeaways

- Sessions requires an existing Android Drop-in Sessions integration using Checkout API v68 or later, with Swish added in Customer Area. The page says no Swish-specific `/sessions` parameters are needed. It describes `setSubmitButtonVisible` to control whether the submit button appears; its Required cell is blank, so the setting is optional-looking rather than a prerequisite. The Kotlin configuration block contains `...`, nested braces and an unbound `value`, so it is illustrative rather than a validated copy-ready snippet.
- Advanced requires an existing Android Drop-in Advanced integration, handling the additional `action.type: qr` action, and Swish added in Customer Area. Its action-handling hyperlink points to a `handle-the-redirect` anchor although the row explicitly says `qr`; preserve the stated `qr` type rather than treating the link label as a redirect response. It says no extra Swish `/payments` parameters are needed and offers the same optional submit-button setting with the same illustrative Kotlin block. This section states no Checkout API minimum.
- **Cross-guide action naming:** This Android Drop-in Advanced guide states `action.type: qr` (raw line 81). The separate Web API-only guide [[source-adyen-docs-payment-methods-swish-api-only]] also states `qr` in its requirement but shows `qrCode` in its response example (that source's pinned raw lines 28 and 152). These are distinct integration scopes; the example does not establish that the action values are interchangeable or that this guide's redirect-named link anchor changes its stated `qr` action.
- In TEST, the page says a Swish payment is authorised within 15 seconds and says refusal scenarios can be simulated by placing a Merchant Swish Simulator error code in `shopperStatement` (for example `FF08`). It directs merchants to inspect test-payment status in the test Customer Area. The 15-second statement is TEST guidance, not a guarantee for a live or refused payment, and a request or simulated result is not capture or settlement proof. For LIVE acceptance, the page requires a separate Swish request in the live Customer Area.

## Detail locators

- Scope and Sessions prerequisites, no-extra-parameter statement: pinned raw lines 15–40. Optional configuration table and illustrative Kotlin snippet: lines 42–62.
- Sessions TEST simulator, Customer Area status and separate LIVE request: pinned raw lines 64–72.
- Advanced prerequisites and `qr` action versus redirect-anchor link: pinned raw lines 74–82. Optional configuration, no-extra-parameter statement and TEST/LIVE steps: lines 84–118.

## Related

- [[adyen-online-payments]] — main concept and integration-state context
- [[source-adyen-docs-payment-methods-swish]] — method overview and separate region/feature scope
- [[source-adyen-docs-payment-methods-swish-api-only]] — separate Web API-only action requirement and response-example conflict

## Raw Sources

- [[raw/adyen/docs/payment-methods/swish/android-drop-in/2026-09-15|Swish Android Drop-in guide, 2026-09-15]]
