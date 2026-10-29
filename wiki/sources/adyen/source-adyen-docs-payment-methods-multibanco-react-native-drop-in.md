---
title: "Multibanco React Native Drop-in"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/multibanco/react-native-drop-in"
raw_files:
  - "adyen/docs/payment-methods/multibanco/react-native-drop-in/2026-09-15.md"
tags: [adyen, multibanco, react-native, drop-in, payments]
---

## Overview

This 2026-09-15 Adyen guide describes Multibanco-specific additions to an existing React Native Drop-in integration for Sessions or Advanced server-side flow. It relies on the main integration for common request and action handling. See [[adyen]], [[adyen-online-payments]], and the [[source-adyen-docs-payment-methods-multibanco|Multibanco overview]] for voucher-payment context.

## Key takeaways

- **Sessions flow:** requires an existing React Native Drop-in Sessions integration, Checkout API v68 or later, and Multibanco added in Customer Area. It says no **additional Multibanco-specific** parameters are needed when creating `/sessions` and no additional method configuration is needed; this does not remove base integration requirements. See raw lines 25–47.
- **Advanced flow:** requires an existing React Native Drop-in Advanced integration, handling an additional `action.type: voucher`, and Customer Area setup. It likewise states no additional method configuration or method-specific `/payments` parameters. Its requirements table does not state the Sessions v68 minimum. See raw lines 66–88.
- Before testing, submit a Multibanco request in the **test Customer Area**. The test guide simulates payment by promoting a pending offer to a sale under **Payments → Offers**; paid and promoted offers appear under **Payment list** for reconciliation checks. This is manual test simulation, not proof of shopper voucher redemption or live settlement. Submit a separate request in the **live Customer Area** before live acceptance. See raw lines 49–64 and 90–105.

> [!warning] Base-guide links
> The Sessions requirement says **Sessions flow React Native Drop-in** but its URL points to `advanced-flow` (raw line 33). The `/sessions` step at line 41 points to `sessions-flow` and is the appropriate route for that step. The Advanced voucher-action requirement links to an anchor named `#handle-the-redirect` (line 75); that anchor label is not evidence that the voucher action itself is a redirect. Follow the flow and action type stated in the guide.

## Detail locators

- Sessions requirements and method-specific omissions: raw lines 25–47.
- Advanced voucher action and method-specific omissions: raw lines 66–88.
- Test offer promotion, reconciliation and live setup: raw lines 49–64 and 90–105.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-multibanco]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/multibanco/react-native-drop-in/2026-09-15|Multibanco React Native Drop-in, captured 2026-09-15]]
