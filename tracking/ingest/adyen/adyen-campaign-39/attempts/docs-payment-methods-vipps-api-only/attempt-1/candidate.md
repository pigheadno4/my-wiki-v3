---
title: "Vipps API-only integration | Adyen Docs"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/vipps/api-only"
raw_files:
  - "adyen/docs/payment-methods/vipps/api-only/2026-09-15.md"
tags: [adyen, vipps, api-only, web, redirect, norway]
---

## Overview

This [[adyen]] page adds Vipps to an existing **Web Advanced API-only** checkout. The merchant builds the payment-method UI, requests method availability for NO/NOK, submits a `vipps` payment, and handles a redirect action through the base integration. The guide is a 2026-09-15 snapshot, not evidence of current merchant eligibility or a successful payment. See [[adyen-online-payments]] and the separate [[source-adyen-docs-payment-methods-vipps|Vipps overview]] for method context.

## Key takeaways

- **Prerequisites and method discovery:** Requires an existing Web API-only Advanced integration, redirect handling for `action.type: redirect`, and Vipps added in Customer Area. For `/paymentMethods` discovery, the page specifies `countryCode: NO`, `amount.currency: NOK`, and `amount.value` in minor units. The v72 example response lists `type: vipps`; an example response does not establish availability for a particular merchant. See raw lines 23–29 and 44–84.
- **Merchant form and payment request:** The dedicated form section says no shopper information needs to be collected. The `/payments` table describes `paymentMethod.telephoneNumber` to prefill the Vipps-hosted page, `shopperStatement` for the app description with `reference` fallback, a relevant `channel`, and the Vipps **100 minor unit / 1.00 NOK** minimum. The table leaves Required cells blank; do not infer that each listed field is mandatory. The Web v72 request example uses `paymentMethod.type: vipps` and `channel: Web`. See raw lines 38–42 and 86–120.
- **Redirect and result boundary:** The example `/payments` response is `RedirectShopper` with `action.type: redirect`; the page points to the base integration's redirect handling. This is an intermediate shopper handoff, not a final authorization. The page directs the merchant to the `AUTHORISATION` webhook and Payment list for live payment status, while its test-app checklist describes shopper authorization in the app. See raw lines 27–36, 122–136 and 138–164.
- **Test and live setup:** The page points to Vipps' test app, asks the merchant to add Vipps in the test Customer Area, create a test payment and approve the app notification. Live acceptance requires a separate request in the live Customer Area; after addition, it recommends low-amount live payments checked by webhook and Payment list. Test-app credentials are in the pinned raw. None of this shows that a live request was approved or a payment executed. See raw lines 138–164.

> [!warning] Inconsistent high-level steps and example syntax
> The “How it works” list says the shopper enters details in the merchant-built form and says to include additional item information (raw lines 33–36). The dedicated form section says no shopper data needs collection, while the dedicated `/payments` table and example name no item-information field (raw lines 38–40 and 86–120). Do not manufacture a required shopper/item field from the high-level list; check the base guide or Adyen if the distinction affects implementation. The `/paymentMethods` curl example also prints `-X POST` without a continuation marker before `-d`, so it is not a copy-ready shell command (raw lines 56–62). The `channel` and `amount.value` links in the `/payments` table target `/paymentMethods` anchors (raw lines 94–95).

## Detail locators

- API-only Web prerequisites and high-level flow: raw lines 23–36.
- Method discovery parameters, v72 request/response examples and curl syntax: raw lines 44–84.
- Payment fields, v72 request and redirect response: raw lines 86–136.
- Test-app fixture and live-request/status process: raw lines 138–164. Detailed return processing remains in the linked base API-only guide, not this method-specific page.

## Related

- [[source-adyen-docs-payment-methods-vipps]] — method overview and channel routes.
- [[adyen-webhooks]] — broader webhook outcome context.

## Raw Sources

- [[raw/adyen/docs/payment-methods/vipps/api-only/2026-09-15|Vipps API-only, 2026-09-15 snapshot]]
