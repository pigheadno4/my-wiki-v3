---
title: "Adyen DuitNow Web Component"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/duitnow/web-component"
raw_files:
  - "adyen/docs/payment-methods/duitnow/web-component/2026-09-15.md"
tags: [adyen, duitnow, web, components, online-payments]
---

## Overview

This 2026-09-15 capture of a page marked last modified in 2019 describes adding DuitNow to an existing Web Components integration. It gives Sessions and Advanced prerequisites, v6 versus older Component construction, and test/live setup. It does not describe the QR or additional-action lifecycle, webhook outcome, current merchant eligibility, or an executed payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Flow and setup:** The page requires an existing Web Components integration in the chosen Sessions or Advanced server-side flow and says to contact Adyen Support to add DuitNow in Customer Area. It does not state a Checkout API minimum. The API reference says no additional DuitNow-specific request fields; it calls `/sessions` the default for Components v5.0.0 or later and points to `/payments` for an additional use case. Those are Web Components/flow qualifications, not a Checkout API version requirement or a waiver of base-flow fields. (raw lines 21–52)
- **Versioned Component creation:** For Web Components v6, import `DuitNow` with `AdyenCheckout` and construct `new DuitNow(checkout).mount(...)`; for v5.x.x or earlier, use `checkout.create('duitnow').mount(...)`. The v6 import instruction's link contains `integration=Drop-in` despite this page's Components scope; treat the link as a navigation mismatch, not a Drop-in instruction. The page has a stray standalone `**` after the v6 snippet. (raw lines 39–45, 54–84)
- **Testing and live:** The page says to test with real payment details and small amounts, inspect status in test Customer Area, and contact Support to add DuitNow in the live Customer Area before accepting live payments. This is setup/status guidance, not evidence of completed authorization, capture or settlement. No real payment was performed for this ingestion. (raw lines 86–92)
- **Scope limit:** The page provides no method-specific QR rendering, app switch, expiry, shopper confirmation or final result procedure. Its See also webhook link is navigation rather than evidence of a particular event sequence. The 2019 last-modified metadata coexists with later Web Components v6 prose in the captured snapshot; it does not establish when each section changed. (raw lines 1–13, 39–98)

## Detail locators

- Sessions/Advanced prerequisites and Support setup: raw lines 21–37.
- v6 import and no-extra-field API reference: raw lines 39–52.
- v6 versus v5 or earlier Component construction: raw lines 54–84.
- Test/live instructions and navigation: raw lines 86–98.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/duitnow/web-component/2026-09-15|Adyen DuitNow Web Component guide, 2026-09-15 snapshot]]
