---
title: "Adyen Trustly Android Component guide"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/trustly/android-component"
raw_files:
  - "adyen/docs/payment-methods/trustly/android-component/2026-09-15.md"
tags: [adyen, trustly, android, components, sessions, advanced, online-banking]
---

## Overview

This 2026-09-15 Adyen guide adds Trustly to an existing **Android Components** integration. It identifies v5.0.0, released October 2023, as its guide scope and points earlier versions to a separate page. It gives Sessions and Advanced prerequisites, no Trustly-specific request/configuration additions, and TEST/LIVE setup. The page delegates payment action, return and outcome handling to the main integration guides; it does not itself show a successful transaction or received funds. The related Trustly overview warns that even successful `AUTHORISATION` may precede an unfunded bank transfer and chargeback. See [[adyen]], [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-trustly]].

## Key takeaways

- **Version and base setup:** the page says it is for Android Components v5.0.0 and links a guide for earlier versions. Both Sessions and Advanced tables require their corresponding existing Android Components integration at **minimum version 5.0.0**, plus Trustly added in Customer Area. The v4.x.x/earlier route is separate authority; do not apply this page's v5 requirements to it. (raw lines 19–39)
- **No method-specific additions:** Trustly requires no additional `/sessions` fields in Sessions or `/payments` fields in Advanced, and no additional Trustly Component configuration in either flow. The following generic links still direct Sessions to checkout-session creation and Advanced to launching/showing the Component. “No additional” is limited to Trustly-specific changes, not a waiver of ordinary base integration requirements. (raw lines 41–67)
- **Outcome boundary:** this page gives no concrete redirect action, return/`/payments/details` request, result-code table or final webhook sequence. The related Trustly overview says a successful `AUTHORISATION` confirms bank-transfer initiation, **not receipt of funds**, and documents a later chargeback path if funds fail to arrive. Do not equate a base-flow authorization or Component completion with settlement. (this page raw lines 41–81; related overview raw lines 38–53)
- **Environment:** the source points to a Trustly TEST environment, a `YYMMDD-XXXX` Login ID/Personal number test format, TEST Customer Area status checks, and a separate Trustly request in the **live** Customer Area before live acceptance. It does not establish that a specific test succeeded or live enablement was granted. (raw lines 69–75)

## Detail locators

- Android Components v5/earlier-version boundary and Sessions/Advanced prerequisites: pinned raw lines 19–39.
- No Trustly-specific fields/config and main-guide continuation: pinned raw lines 41–67.
- TEST values/check and LIVE request: pinned raw lines 69–75.
- Related overview's authorization-versus-funds and chargeback warning: [[source-adyen-docs-payment-methods-trustly]], raw lines 38–53.

## Related

- [[adyen-online-payments]] — main provider payment/outcome context
- [[source-adyen-docs-payment-methods-trustly]] — bank-transfer and chargeback qualification
- [[source-adyen-docs-payment-methods-trustly-android-component-earlier-versions]] — earlier-version Android Component navigation

## Raw Sources

- [[raw/adyen/docs/payment-methods/trustly/android-component/2026-09-15|Trustly Android Component guide, 2026-09-15]]
