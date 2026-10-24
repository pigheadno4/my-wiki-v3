---
title: "Adyen PayNow React Native Drop-in guide"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paynow/react-native-drop-in"
raw_files:
  - "adyen/docs/payment-methods/paynow/react-native-drop-in/2026-09-15.md"
tags: [adyen, paynow, react-native, drop-in, qr-code, online-payments]
---

## Overview

This 2026-09-15 Adyen page gives **PayNow-specific additions** to existing React Native Drop-in integrations, separately for Sessions and Advanced server-side flows. It is not a complete base guide, live merchant approval or proof of a completed QR payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions prerequisites and additions:** The page calls for an existing Sessions React Native Drop-in integration, Checkout API **v68 or later**, and PayNow added in Customer Area. It states no extra PayNow `/sessions` parameters or configuration. Its Sessions Integration type link unexpectedly points to an **Advanced-flow** URL, although the payment-session link points to Sessions flow; follow the flow label and inspect the matching base guide. (raw lines 25–47)
- **Advanced prerequisites and additions:** The Advanced section calls for an existing Advanced React Native Drop-in integration, PayNow added in Customer Area and handling of an additional **`action.type: qrCode`** action. It states no extra PayNow configuration or ordinary `/payments` parameters. The action-handling link's anchor says `handle-the-redirect` even though the required action is QR code; treat the link as a navigation pointer, not evidence that QR handling is a redirect. The Advanced section does not separately state the Sessions-row API minimum. (raw lines 59–81)
- **Live and test warning:** Both flow sections say Adyen Support must add PayNow in the **live Customer Area** before live acceptance. They describe penny testing in the live area with a small amount and a **real banking app** scanning a test QR. They recommend against test Customer Area payments because bank transfers there **cannot be reversed** and the bank account is charged. This warning carries real-funds risk; the page gives no authorization, capture, settlement or refund evidence from a QR scan or status-list instruction. (raw lines 49–57, 83–91)
- **Outcome limit:** The page does not describe QR expiry, the scan/result webhook lifecycle, or a completed payment response. Its no-extra-parameter statements are method additions to existing flows, not a waiver of the base integration or a guarantee of final payment outcome. (raw lines 19–23, 37–47, 63–91)

## Detail locators

- Sessions flow requirements, mismatched base link and no-extra statements: raw lines 25–47.
- Advanced QR-code action, redirect-named anchor and no-extra statements: raw lines 59–81.
- Repeated live Support prerequisite and nonreversible real-funds test warning: raw lines 49–57, 83–91.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-paynow]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paynow/react-native-drop-in/2026-09-15|Adyen PayNow React Native Drop-in, 2026-09-15 snapshot]]
