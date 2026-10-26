---
title: "Vipps Flutter Component"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/vipps/flutter-component"
raw_files:
  - "adyen/docs/payment-methods/vipps/flutter-component/2026-09-15.md"
tags: [adyen, vipps, flutter, components, redirect, online-payments]
---

## Overview

This 2026-09-15 guide gives Vipps-specific request and redirect additions for an existing Adyen Flutter Components integration, separated by Sessions and Advanced server-side flows. It contains no standalone Component initialization recipe or observed payment result. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions:** the requirement text calls for existing Flutter Components Sessions flow, Checkout API v68 or later, `action.type: redirect` handling and Vipps added in Customer Area. The `/sessions` table describes optional `shopperStatement` shown in the Vipps app, with the payment `reference` used when it is omitted, and a Vipps minimum `amount.value` of 100 minor units (1.00 NOK). No additional Vipps Component configuration is stated. The request sample uses NOK/NO and a custom-scheme return URL as example values. The **Sessions Flutter Components** prerequisite label incorrectly links to an **Advanced Flutter Drop-in** guide; its other Sessions links point to Components. (raw lines 25–72)
- **Advanced:** the requirement text calls for existing Flutter Components Advanced flow, redirect handling and Customer Area addition, but its Components prerequisite label again links to an **Advanced Flutter Drop-in** guide. The `/payments` table lists optional `paymentMethod.telephoneNumber` for Vipps-hosted page prefill, `shopperStatement` with the same reference fallback, `channel`, and the 100-minor-unit minimum. It says no additional Vipps Component configuration. The sample uses `channel: Flutter` although the table lists Web, iOS and Android as examples; it also uses a web return URL. These sample values do not determine general channel or return handling. The `RedirectShopper` response is an intermediate GET redirect action, not final authorization or settlement. (raw lines 102–172)
- **Test and live boundary:** test instructions require setting up the Vipps test app, adding Vipps in the test Customer Area, creating a payment request and authorizing from an app notification. Live acceptance requires a separate request in the live Customer Area; after addition, the guide calls for low-amount live tests, a server-side `AUTHORISATION` webhook carrying status, and a payment-list check. App authorization and redirect presentation do not by themselves establish final server-side status. (raw lines 74–100, 174–200)

## Detail locators

- Sessions prerequisite misroute, statement fallback, amount minimum and example: raw lines 27–66.
- Advanced prerequisite misroute, optional fields, `channel` example mismatch and redirect response: raw lines 106–172. The `channel` and `amount.value` links in the `/payments` table target `/paymentMethods` reference anchors.
- Test-app setup and distinct live Customer Area request/webhook checks: raw lines 74–100 and 174–200.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-vipps]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/vipps/flutter-component/2026-09-15|Vipps Flutter Component guide, 2026-09-15 snapshot]]
