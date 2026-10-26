---
title: "Adyen Vipps iOS Drop-in integration guide"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/vipps/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/vipps/ios-drop-in/2026-09-15.md"
tags: [adyen, vipps, ios, drop-in, redirect]
---

## Overview

This 2026-09-15 Adyen guide adds Vipps to an existing iOS Drop-in integration, separately for Sessions and Advanced server-side flows. It covers method-specific request fields, test-app and live setup, and the Advanced redirect response. The main iOS Drop-in guides own the rest of the integration. This snapshot and its examples do not establish current merchant enablement, a completed payment, capture or settlement. See [[adyen]], [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-vipps]].

## Key takeaways

- Sessions requires an existing iOS Drop-in Sessions integration using Checkout API v68 or later and Vipps added in Customer Area. Its `/sessions` table describes `shopperStatement` as the description shown in the Vipps app, falling back to `reference` if omitted, and specifies a minimum `amount.value` of 100 minor units (1.00 NOK). The table's Required cells are blank, so it does not establish `shopperStatement` as mandatory. The TEST `/v71/sessions` example uses NOK, `countryCode: NO`, and an app-scheme return URL; those example values are not merchant-eligibility proof. No Vipps-specific Drop-in configuration is needed.
- Advanced requires an existing iOS Drop-in Advanced integration, `action.type: redirect` handling and Vipps added in Customer Area. Its `/payments` table describes `paymentMethod.telephoneNumber` for hosted-page prefill, `shopperStatement` with the same `reference` fallback, a relevant `channel`, and the same 100-minor-unit/1.00-NOK minimum. Required cells are blank; do not infer every listed parameter is mandatory. The TEST `/v72/payments` example uses `paymentMethod.type: vipps`, `channel: iOS` and an HTTPS `returnUrl`. Its `RedirectShopper`/`action.type: redirect` response is an intermediate redirect, not payment authorization. No Vipps-specific Drop-in configuration is needed.
- The Advanced table's `channel` and `amount.value` links point to `/paymentMethods` anchors despite appearing under `/payments`. Verify endpoint-specific field details in the linked API reference; those links do not resolve an Advanced request schema. The Sessions and Advanced sample return URLs also differ, so the snippets should not be copied as a universal iOS return-URL rule.
- For TEST, the page points to a Vipps developer test app, then asks the merchant to add Vipps to the test merchant account, create a payment request and authorize the notification in the app. Before LIVE acceptance, submit a separate Vipps request in the live Customer Area; after addition, make low-amount live test payments and check the server's `AUTHORISATION` webhook and live Payment list. Approving a test-app notification is a shopper step; payment status must be checked separately, and neither step proves capture or settlement.

## Detail locators

- Scope and Sessions prerequisites, `/sessions` fields and TEST example: pinned raw lines 15–66. No-extra-configuration statement: lines 68–72.
- Sessions test-app steps and live-request gate: pinned raw lines 74–102; published test credentials remain in the raw at lines 84–86.
- Advanced prerequisites, configuration and `/payments` field table: pinned raw lines 104–133; note the `/paymentMethods` links at lines 132–133.
- Advanced TEST request, redirect response, test-app and live-request steps: pinned raw lines 135–204; test credentials remain in the raw at lines 186–188.

## Related

- [[adyen-online-payments]] — main concept for server-side flow and payment-state context
- [[source-adyen-docs-payment-methods-vipps]] — method overview and separate regional context

## Raw Sources

- [[raw/adyen/docs/payment-methods/vipps/ios-drop-in/2026-09-15|Vipps iOS Drop-in guide, 2026-09-15]]
