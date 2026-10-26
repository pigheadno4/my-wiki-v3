---
title: "Swish React Native Component"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/swish/react-native-component"
raw_files:
  - "adyen/docs/payment-methods/swish/react-native-component/2026-09-15.md"
tags: [adyen, swish, react-native, components, qr, online-payments]
---

## Overview

This 2026-09-15 page is titled “Swish React Component” but its canonical path and integration text address React Native Components. It gives a Swish-specific **Advanced-only** add-on to an existing React Native Components integration: this page explicitly says Components do not support Sessions flow. It does not establish current merchant eligibility or an observed payment result. [[adyen]] [[adyen-online-payments]] [[adyen-react-native-sdk]]

## Key takeaways

- **Flow and prerequisites:** the Sessions section states React Native Components do not support Sessions flow. For Advanced, the page requires an existing React Native Components integration, handling an additional `action.type: qr` action, and adding Swish in Customer Area. This is method-page scope; the general React Native SDK's broader Sessions capability does not override this stated Swish Components limitation. (raw lines 25–41)
- **Advanced request/configuration:** the guide states no Swish-specific configuration or ordinary `/payments` parameters are needed. The test simulator separately uses an error code in `shopperStatement` to model refusal, which is not an ordinary required field. The page gives no SDK version, QR response example, final webhook sequence or complete payment outcome. (raw lines 43–61)
- **Guide-link and outcome limits:** the Advanced **React Native Components** prerequisite label links to a **Drop-in** integration URL. The `qr` action link's anchor is named `handle-the-redirect`; retain the explicit `qr` action label without treating the anchor as evidence of a redirect action type. The page claims a test payment is authorised within 15 seconds, allows simulator refusal scenarios such as `shopperStatement: FF08`, and directs a test payment-list check. Live acceptance requires a separate Swish request in the live Customer Area. These are source instructions and test claims, not a measured result for this snapshot. (raw lines 39–61)

## Detail locators

- React Native Components Sessions unsupported: raw lines 25–29.
- Advanced prerequisites, Drop-in link mismatch and `qr` action/redirect-anchor mismatch: raw lines 31–41.
- No extra ordinary configuration/fields, test simulator and live request: raw lines 43–61.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-react-native-sdk]]
- [[source-adyen-docs-payment-methods-swish]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/swish/react-native-component/2026-09-15|Swish React Native Component guide, 2026-09-15 snapshot]]
