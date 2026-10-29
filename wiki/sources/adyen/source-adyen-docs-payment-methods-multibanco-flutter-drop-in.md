---
title: "Adyen Multibanco Flutter Drop-in"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/multibanco/flutter-drop-in"
raw_files:
  - "adyen/docs/payment-methods/multibanco/flutter-drop-in/2026-09-15.md"
tags: [adyen, multibanco, flutter, drop-in, sessions, advanced-flow]
---

## Overview

This 2026-09-15-captured Adyen guide adds Multibanco to an existing Flutter Drop-in integration. It covers Sessions and Advanced flow prerequisites, no additional Multibanco request or configuration parameters, Advanced voucher-action handling, and test offer promotion. A Multibanco voucher is issued at checkout for later shopper payment; a pending offer is not a paid sale. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-multibanco]].

## Key takeaways

- **Sessions:** start with an existing Flutter Drop-in Sessions flow, **Checkout API v68 or later**, and Multibanco added in Customer Area. The guide says no additional **Multibanco** parameters are needed for `/sessions` and no extra method configuration is needed. Base integration requirements still apply. The Sessions integration-type link is labeled Sessions but its URL selects `advanced-flow`; the session-creation link selects Sessions. See raw lines 25–47.
- **Advanced:** start with an existing Flutter Drop-in Advanced flow, handle `action.type: voucher`, and add Multibanco in Customer Area. No additional Multibanco configuration or `/payments` parameters are specified, beyond the base flow. The action-handling link's fragment says `handle-the-redirect` even though the required action here is `voucher`; use the actual voucher action contract. The v68 minimum is stated only in the Sessions requirements table. See raw lines 66–88.
- To test, request Multibanco in the **test** Customer Area. The page describes promoting a pending test payment from **Payments > Offers** by PSP reference using **Promote offer to sale**, then checking **Payments > Payment list**; it recommends this for reconciliation testing. Manual test promotion simulates payment and is distinct from a shopper redeeming a real voucher. See raw lines 49–62 and 90–103.
- Live acceptance separately requires submitting a Multibanco request in the **live** Customer Area. This page does not prove current merchant enablement or a successful live transaction. See raw lines 64 and 105.

## Detail locators

- Sessions prerequisites and no additional method parameters/configuration: raw lines 25–47.
- Advanced prerequisites, voucher action and no additional method parameters/configuration: raw lines 66–88.
- Test offer promotion and reconciliation: raw lines 49–62 and 90–103.
- Separate live Customer Area request: raw lines 64 and 105.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-multibanco]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/multibanco/flutter-drop-in/2026-09-15|Fully read Multibanco Flutter Drop-in raw]]
