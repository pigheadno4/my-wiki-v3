---
title: "PayPo Flutter Drop-in integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paypo/flutter-drop-in"
raw_files:
  - "adyen/docs/payment-methods/paypo/flutter-drop-in/2026-09-15.md"
tags: [adyen, paypo, flutter, drop-in, redirect, buy-now-pay-later]
---

## Overview

This 2026-09-15-captured Adyen guide adds PayPo to an **existing Flutter Drop-in** integration. It gives separate Sessions and Advanced server-side flow additions, request data, redirect/action handling, full capture and funding conditions, and test/live setup. It is method-specific add-on guidance, not a complete Flutter integration or proof of current merchant enablement or payment execution. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- For the **Sessions** flow, the page requires an existing Flutter Drop-in integration, Checkout API **v68 or later**, and Support assistance to add PayPo in Customer Area. Its “Sessions flow” integration-type link points to an **Advanced-flow URL**; follow the Sessions-specific create-session link for that step and verify the base guide rather than treating the mismatched link as flow authority (raw lines 25–41).
- The Sessions `/sessions` addition marks shopperName (firstName and lastName) and shopperEmail required. Billing and delivery addresses appear without a required mark. The PL/PLN and app-scheme returnUrl in the v71 sample are example values, not a universal claim about all allowed routes (raw lines 43–75).
- For the **Advanced** flow, the page requires an existing Advanced Flutter Drop-in that handles the additional `redirect` action and PayPo added in Customer Area. The `/payments` addition marks `paymentMethod.type: paypo`, shopperName and shopperEmail required; billing and delivery addresses are not marked required. Its v72 sample uses PLN and an HTTPS returnUrl; the two sample returnUrl forms should not be read as a single Flutter redirect recipe (raw lines 443–502, 845–859).
- Neither flow needs PayPo-specific Drop-in configuration parameters (raw lines 423–427, 455–459). The Advanced `/payments` response includes a redirect action, so the existing integration must handle that action (raw lines 449–453, 845–859).
- Before authorization, the offer/payment link is available for **up to 72 hours**. On shopper acceptance, the status becomes **Authorised** and the shopper has **30 days** to pay under PayPo terms; the page contrasts this with terms that start at capture for some other methods. After authorization, the merchant must capture, and **only full-amount capture** is possible. Automatic capture immediately after authorization can be configured when adding PayPo in live Customer Area (raw lines 391–405, 861–875).
- The page says the merchant need not wait for the shopper to pay PayPo: after **capture** the merchant is funded the full amount. The capture request uses the original payment PSP reference. This is a source-stated funding condition, not a guarantee of current settlement timing for a merchant (raw lines 401–420, 871–890).
- Test instructions give the required sample name/email values and PayPo verification code **123456**; live acceptance requires a PayPo request in live Customer Area (raw lines 429–441, 893–905).

## Detail locators

- Add-on scope, Sessions requirements, and request fields: raw lines 15–48; Sessions v71 curl and SDK examples at lines 50–389.
- Sessions capture, configuration and test/live sections: raw lines 391–441.
- Advanced requirements, request fields and examples: raw lines 443–859; redirect action response at 845–859.
- Advanced capture, configuration and test/live sections: raw lines 455–459 and 861–905.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-paypo]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paypo/flutter-drop-in/2026-09-15|PayPo Flutter Drop-in guide, captured 2026-09-15]]
