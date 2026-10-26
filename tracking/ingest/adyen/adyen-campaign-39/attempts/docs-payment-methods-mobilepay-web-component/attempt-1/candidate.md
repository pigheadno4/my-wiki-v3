---
title: "Adyen MobilePay Web Component"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/mobilepay/web-component"
raw_files:
  - "adyen/docs/payment-methods/mobilepay/web-component/2026-09-15.md"
tags: [adyen, mobilepay, web, components, redirect, payouts]
---

## Overview

This 2026-09-15 Adyen guide adds MobilePay to an existing Web Components integration. It gives separate Sessions and Advanced server-side flow additions, then a conditional route for generating a token during a MobilePay payment for a future MobilePay-wallet payout. It is a dated documentation snapshot, not evidence of current merchant enablement or a completed payment or payout. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions:** Start with an existing Sessions Web Components integration, Checkout API v68 or later, redirect handling (`action.type: redirect`), and MobilePay added in Customer Area. The page says no MobilePay-specific `/sessions` parameters or configuration are needed. Import `Redirect` from Adyen Web and initialize the MobilePay `Redirect` Component. These statements do not replace base-flow requirements. (raw lines 19–71)
- **Advanced:** Start with an existing Advanced Web Components integration, redirect handling and MobilePay added in Customer Area. Import and initialize `Redirect`. No extra `/payments` parameters are stated for a normal payment, but the payout-token case is an explicit exception. The Advanced requirements table states no Checkout API minimum; the v68+ statement belongs to Sessions. (raw lines 109–147)
- **Future wallet payouts:** This feature is marked experimental and token creation is supported only with `/payments`. The prescribed payment request adds `telephoneNumber`, `shopperReference`, and `enablePayout: true`, after the recurring lifecycle webhook is configured. Save the webhook's `storedPaymentMethodId` against that shopper reference; a later `/transfers` request supplies the token in `counterparty.card.cardIdentification`. The webhook is token evidence, not a payout result. (raw lines 333–365, 379–400)
- **Testing and outcome:** The page says ordinary MobilePay payments cannot be tested in the test environment: request MobilePay in the live Customer Area, make low-amount live payments, check the server's `AUTHORISATION` webhook, and inspect the payment list. A separate section describes a Vipps MobilePay test-app procedure for experimental payout-token testing. Read this as a source-level scope distinction, not proof that a normal TEST MobilePay payment works or that a payout completed. No live operation was performed for this ingestion. (raw lines 74–107, 367–400)
- **Example caution:** The Component snippets show `type:mobilepay` without quotes; the Advanced curl example spells `enablePayOut` while the step-by-step prose spells `enablePayout`, and its currency, payment-method type and return URL are blank. Other language snippets omit the payout-token fields. These examples are not a complete executable request or a reliable schema authority; verify the relevant exact-version integration before use. (raw lines 66–71, 135–140, 147–168, 172–330, 333–345)

## Detail locators

- Sessions prerequisites, request, import, configuration and initialization: raw lines 25–71.
- Advanced prerequisites, import, initialization and normal-payment exception: raw lines 109–147.
- Advanced request snippets by language: raw lines 149–330.
- Payout-token request, webhook and later transfer: raw lines 333–365.
- Payment and payout-token testing sections: raw lines 74–107 and 367–400.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[adyen-card-payouts]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/mobilepay/web-component/2026-09-15|Adyen MobilePay Web Component guide, 2026-09-15 snapshot]]
