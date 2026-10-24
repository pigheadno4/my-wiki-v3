---
title: "Adyen DANA iOS Drop-in guide"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/dana/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/dana/ios-drop-in/2026-09-15.md"
tags: [adyen, dana, ios, drop-in, recurring]
---

## Overview

This [[adyen]] page gives **DANA-specific additions** to an existing **iOS Drop-in** integration, divided into **Sessions** and **Advanced** server-side flows. It describes an ordinary base request and a distinct merchant-server recurring-token path. The source is a 2026 website snapshot and examples use IDR/TEST; it does not establish current merchant enablement, DANA authorization, initial settlement, token creation or later payment success. [[adyen-online-payments]]

## Key takeaways

- **Sessions base path:** The Sessions section requires an existing iOS Drop-in Sessions integration, **Checkout API v68 or later**, and adding DANA in Customer Area. It says no additional DANA parameters for the ordinary /sessions request and no extra DANA configuration. This section does not spell out redirect handling in its requirements table; that requirement appears explicitly in the Advanced section. See raw lines 25–46.
- **Advanced base path:** The Advanced section requires an existing iOS Drop-in Advanced integration, `action.type: redirect` handling and DANA added in Customer Area. It says no additional DANA configuration or parameters for the ordinary /payments call. Its requirements table does not state an API minimum; a v68 URL in recurring examples is not the same as an Advanced-flow minimum. See raw lines 298–320 and 361–380.
- **Recurring route:** Both sections state DANA supports recurring. To create a shopper token they require a separate **/payments** request with `storePaymentMethod: true` and shopper reference. **When the initial payment has settled**, a `recurring.token.created` webhook supplies the `storedPaymentMethodId`; the merchant server is directed to receive recurring-token lifecycle events. Future /payments requests use the token and matching shopper reference with `ContAuth` and `Subscription` for fixed intervals or `UnscheduledCardOnFile` for non-fixed contracts. The base no-extra-parameters text must not be applied to these token requests, and the page does not detail shopper-consent mechanics. See raw lines 48–85 and 322–359.
- **Examples and environment:** Multi-language token-payment snippets use illustrative DANA type, IDR, TEST endpoints and placeholder credentials/IDs. Both Test and go live sections state that testing **successful live** DANA payments needs a real mobile number registered with DANA, also point to TEST Customer Area payment status, and require a separate request in **live** Customer Area before accepting live payments. These statements retain distinct environment scopes; status lookup/request submission do not prove final transaction outcome. See raw lines 87–296 and 361–570.

## Detail locators

- Sessions requirements and base/recurring paths: raw lines 25–85.
- Sessions examples and test/live text: raw lines 87–296.
- Advanced requirements and base/recurring paths: raw lines 298–359.
- Advanced examples and repeated test/live text: raw lines 361–570.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/dana/ios-drop-in/2026-09-15|Adyen DANA iOS Drop-in snapshot]]
