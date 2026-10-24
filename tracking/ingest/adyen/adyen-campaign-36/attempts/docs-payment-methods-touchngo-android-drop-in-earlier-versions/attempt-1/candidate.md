---
title: "Adyen Touch'n Go Android Drop-in earlier-versions integration"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/touchngo/android-drop-in/earlier-versions"
raw_files:
  - "adyen/docs/payment-methods/touchngo/android-drop-in/earlier-versions/2026-09-15.md"
tags: [adyen, touchngo, android, drop-in, advanced-flow, malaysia]
---

## Overview

This [[adyen]] earlier-versions Android Drop-in guide describes adding Touch'n Go to an existing integration, passing a payment method through a merchant server, handing a redirect action back to Drop-in, and checking returned details. See [[adyen-online-payments]]. The captured heading is malformed (`Touch v4.x.x integration'n Go Drop-in integration`); its v4.x wording identifies historical scope, not a verified current SDK minimum. This snapshot does not prove merchant enablement or a real payment outcome.

## Key takeaways

- The **Requirements** table specifies an existing **Advanced-flow Android Drop-in** integration and contacting Adyen Support to add Touch'n Go in the **test Customer Area**. The introductory Android Drop-in link and closing See also link instead point to Sessions-flow guides; preserve this source inconsistency rather than treating the links as a Sessions prerequisite or supported Sessions procedure here. The page says Drop-in redirects the shopper to the Touch'n Go app. See raw lines 15–26 and 409–413.
- To show the method, the `/paymentMethods` request supplies `countryCode: MY`, `amount.currency: MYR` and payment `amount.value`; Drop-in uses country/currency to display available methods. These values are method-display inputs, not a guarantee that an account is enabled or that a payment will succeed. See raw lines 28–36.
- On shopper pay, the client passes `paymentComponentData.paymentMethod` to the merchant server, which sends `/payments` with that method and a return URL (maximum **1024 characters**) obtained from `RedirectComponent.getReturnUrl(context)`. The prose spells the field `returnURL`, while examples use `returnUrl`; use the example spelling only as an example, and resolve exact API casing against the linked API reference before implementation. The TEST curl example uses Checkout API v68, `touchngo` and an illustrative app-scheme return URL. See raw lines 38–67.
- The merchant server checks the `/payments` response `action` and passes it to the client for redirection. After shopper return, Drop-in provides `actionComponentData`; the server posts its `details` to `/payments/details`, then uses the returned `resultCode` for shopper display and `pspReference` as transaction identifier. The shown `RedirectShopper` and `Authorised` JSON are examples, not proof of an actual authorization, capture or settlement; the `/payments/details` curl example uses v72, separate from the v68 `/payments` example. See raw lines 350–401.
- The page directs test-status checks to Customer Area and requires contacting Support to add Touch'n Go in the **live Customer Area** before accepting live payments. TEST setup/status checks and a live-add request are not payment execution evidence. See raw lines 403–407.

## Detail locators

- **Earlier-version heading, app redirect, Advanced versus Sessions-link inconsistency:** raw lines 15–26 and 409–413.
- **Method display request:** raw lines 28–36.
- **Client/server request and return URL:** raw lines 38–67.
- **Illustrative library TEST snippets:** raw lines 69–348.
- **Redirect action, returned details, response examples:** raw lines 350–401.
- **TEST/live gates:** raw lines 403–407.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-touchngo]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/touchngo/android-drop-in/earlier-versions/2026-09-15|Touch'n Go Android Drop-in earlier versions — captured 2026-09-15]]
