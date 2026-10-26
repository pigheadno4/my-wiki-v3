---
title: "Adyen Swish React Native Drop-in"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/swish/react-native-drop-in"
raw_files:
  - "adyen/docs/payment-methods/swish/react-native-drop-in/2026-09-15.md"
tags: [adyen, swish, react-native, drop-in, qr, online-payments]
---

## Overview

This 2026-09-15 Adyen page gives Swish-specific additions to an existing React Native Drop-in integration, separately for Sessions and Advanced server-side flows. It describes prerequisites and TEST/LIVE setup, without a full QR presentation, shopper return, webhook outcome or settlement procedure. The snapshot does not establish current merchant enablement or a completed payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions:** The page calls for an existing Sessions React Native Drop-in integration, Checkout API v68 or later, and Swish added in Customer Area. It says no Swish-specific extra `/sessions` or configuration parameters. Its Sessions Integration type link points to an Advanced-flow URL even though the session-creation link points to Sessions flow; follow the flow label and the correct base guide. (raw lines 25–47)
- **Advanced:** The page calls for an existing Advanced React Native Drop-in integration, additional `action.type: qr` handling, and Swish added in Customer Area. It says no Swish-specific extra configuration or `/payments` parameters. The action-handling link ends in `#handle-the-redirect`, which does not itself turn the stated QR action into a redirect. The Advanced section does not separately state the Sessions-only v68+ minimum. (raw lines 57–79)
- **TEST and LIVE:** In both sections, the page says a Swish TEST payment is authorised within 15 seconds and gives Merchant Swish Simulator refusal scenarios through a `shopperStatement` error code. It directs checking TEST payment status in Customer Area. Live acceptance requires a separate Swish request in the live Customer Area. Those instructions are documentation, not proof that this ingestion ran a TEST or LIVE transaction. (raw lines 49–55, 81–87)
- **Scope limit:** The no-extra-parameter statements concern Swish-specific additions to an existing integration, not base Drop-in request requirements. This page does not spell out QR rendering, app switch, expiry, shopper confirmation, final webhook or capture/refund behavior; use the linked main integration and other Swish guides for those distinct questions. (raw lines 19–23, 39–47, 66–87)

## Detail locators

- Sessions prerequisites, mismatched link and no-extra statements: raw lines 25–47.
- Advanced `qr` action, redirect-named anchor and no-extra statements: raw lines 57–79.
- Repeated TEST simulator and live request instructions: raw lines 49–55 and 81–87.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-react-native-sdk]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/swish/react-native-drop-in/2026-09-15|Adyen Swish React Native Drop-in guide, 2026-09-15 snapshot]]
