---
title: "Adyen PromptPay Web Component guide"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/promptpay/web-component"
raw_files:
  - "adyen/docs/payment-methods/promptpay/web-component/2026-09-15.md"
tags: [adyen, promptpay, web, components, sessions, advanced]
---

## Overview

This Adyen page, last modified 2019-09-06 and captured 2026-09-15, describes adding PromptPay to an existing **Web Components** integration. It gives Sessions and Advanced prerequisites, version-specific Component construction, and test/live setup routes. It does not specify the QR action, shopper completion, expiry or final payment webhook sequence on this page; consult the main integration and method-specific flow evidence for those outcomes. The snapshot does not establish current merchant eligibility or an executed payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Prerequisites:** both Sessions and Advanced require their respective existing Web Components integration. Both tables direct merchants to contact Adyen Support to add PromptPay in Customer Area. These are setup instructions, not evidence that the method is enabled for an account. (raw lines 21–37)
- **API scope:** the page says no additional PromptPay fields are needed and points to `/sessions` or `/payments` for optional cross-method fields. It calls `/sessions` the default with Components v5.0.0 or later and `/payments` the route when an additional use case is implemented. This is source wording, not a guarantee that either flow is available in a particular merchant configuration. (raw lines 47–52)
- **Web Component version split:** for v6, import `AdyenCheckout` and `PromptPay` from `@adyen/adyen-web`; v6.0.0 or later constructs `new PromptPay(checkout).mount('#promptpay-container')`. The v5.x.x-or-earlier example uses `checkout.create('promptpay').mount('#promptpay-container')`. The v6 import link points to a **Drop-in** guide despite this being a Components page; verify the target Web Components guide before implementation. The stray `**` at raw line 76 is source formatting noise. No payment-result semantics are provided by the mount snippets. (raw lines 39–84)
- **Test/live:** the page instructs testing with real payment details and small amounts, checking status in the TEST Customer Area, and contacting Support to add PromptPay in the **live** Customer Area before accepting live payments. It does not establish that a test or live transaction was performed. (raw lines 86–92)

## Detail locators

- Web Components identity, historical modified timestamp and Sessions/Advanced setup: pinned raw lines 5–37.
- v6 import, no-additional-fields guidance and version-specific mounting: pinned raw lines 39–84.
- TEST Customer Area check and LIVE Support gate: pinned raw lines 86–92.
- Web Components integration, webhooks and API Explorer navigation: pinned raw lines 94–98.

## Related

- [[adyen-online-payments]] — main online-payment and Component context
- [[source-adyen-docs-payment-methods-promptpay]] — method overview and QR scope

## Raw Sources

- [[raw/adyen/docs/payment-methods/promptpay/web-component/2026-09-15|PromptPay Web Component guide, 2019-modified and 2026-09-15-captured]]
