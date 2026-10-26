---
title: "Vipps iOS Component | Adyen Docs"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/vipps/ios-component"
raw_files:
  - "adyen/docs/payment-methods/vipps/ios-component/2026-09-15.md"
tags: [adyen, vipps, ios, components, redirect, norway]
---

## Overview

This [[adyen]] guide adds Vipps to an existing iOS Components integration, separately for Sessions and Advanced server-side flows. Both require redirect handling and Customer Area setup. It uses `InstantPaymentComponent` with the `vipps` method. The page is method-specific and does not establish present merchant eligibility, a successful payment, capture or settlement. See [[adyen-online-payments]] and the separate [[source-adyen-docs-payment-methods-vipps|Vipps overview]] for its wallet and regional context.

## Key takeaways

- **Sessions prerequisites and fields:** Requires an existing iOS Components Sessions integration, Checkout API v68 or later, `action.type: redirect` handling and Vipps added in Customer Area. The method-specific `/sessions` table describes `shopperStatement` for the Vipps-app description; if omitted, Adyen says it uses `reference`. It also says Vipps' minimum `amount.value` is **100 minor units, or 1.00 NOK**. The table's Required column is blank, so it does not itself establish that `shopperStatement` is mandatory. Its illustrative request uses Checkout API v71, NOK and `countryCode: NO`; those example values are not a general eligibility proof. See raw lines 25–68.
- **Advanced prerequisites and fields:** Requires an existing iOS Components Advanced integration, redirect handling and Vipps added in Customer Area. The `/payments` table describes optional-looking `paymentMethod.telephoneNumber` to prefill the hosted page, `shopperStatement` with the same `reference` fallback, a relevant `channel`, and the **100 minor unit / 1.00 NOK** minimum. Its Required cells are blank; do not turn the table into a blanket required-fields contract. The illustrative v72 request uses `vipps`, iOS and NOK; its sample response has `resultCode: RedirectShopper` and `action.type: redirect`, an intermediate redirect action rather than final authorization. See raw lines 126–217.
- **Component:** Both flows use `InstantPaymentComponent` after checking for `.other("vipps")`. Sessions sets the session as delegate; Advanced sets the merchant object as delegate, then each calls `initiatePayment()`. Neither section adds Vipps-specific Component configuration or pins an iOS SDK version. See raw lines 70–96 and 138–163.
- **Testing and live gate:** The page sends the merchant to Vipps' developer test app, asks for Vipps on the test merchant account, and describes approving a test-app notification. Separately, live acceptance requires a Vipps request in the live Customer Area; after addition, low-amount live tests are checked by the server's `AUTHORISATION` webhook and live Payment list. Test-app authorization is a shopper action, not proof of payment authorization or live enablement. See raw lines 98–124 and 219–245.

> [!warning] Advanced base-guide link mismatch
> The Advanced prerequisite row says **iOS Components** but links to an Advanced **Drop-in** URL, whereas the redirect and make-payment links specify Components. Use the stated Components scope and verify the intended main-guide route. The Advanced field table also links `channel` and `amount.value` to `/paymentMethods` anchors while introducing `/payments`; use the raw/API reference for field details rather than treating those links as a resolved `/payments` schema. See raw lines 134–135 and 167–176.

## Detail locators

- Sessions request table and illustrative v71 request: raw lines 40–68; Advanced table, illustrative v72 request and redirect response: raw lines 165–217.
- Session and Advanced Component setup: raw lines 70–96 and 138–163.
- Test-app setup includes published fixture credentials in raw lines 100–110 and 221–231; live-request and status-check guidance: raw lines 116–124 and 237–245.

## Related

- [[adyen-ios-sdk]] — separately versioned native Components architecture; this page specifies no SDK release.
- [[source-adyen-docs-payment-methods-vipps]] — method overview and channel navigation.

## Raw Sources

- [[raw/adyen/docs/payment-methods/vipps/ios-component/2026-09-15|Vipps iOS Component, 2026-09-15 snapshot]]
