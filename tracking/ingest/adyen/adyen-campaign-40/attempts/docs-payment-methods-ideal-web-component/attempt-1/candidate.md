---
title: "iDEAL | Wero Web Component"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/ideal/web-component"
raw_files:
  - "adyen/docs/payment-methods/ideal/web-component/2026-09-15.md"
tags: [adyen, ideal, wero, web, components, online-payments, tokenization]
---

## Overview

This 2026-09-15 Adyen guide adds iDEAL | Wero to an existing **Web Components** integration, with separate Sessions and Advanced instructions. It is a method-specific add-on, not a complete base integration. The Web component is `Redirect` with `type: 'ideal'`; the existing integration must handle a `redirect` action and the merchant must add the method in Customer Area. [[adyen-online-payments]]

## Key takeaways

- In the **Sessions** branch, the existing Web Components integration uses Checkout API v68 or later. The ordinary `/sessions` request needs no iDEAL-specific parameters, and the component needs no extra configuration. Import `Redirect` from Adyen Web and initialize it for `ideal`. See raw lines 25–72.
- In the **Advanced** branch, the existing Web Components integration handles the redirect and adds the method in Customer Area; its ordinary `/payments` request needs no iDEAL-specific parameters. It imports and initializes the same Web `Redirect` component. The Advanced requirements table does not state a Checkout API minimum. See raw lines 346–384.
- For **recurring** payments, the guide routes iDEAL | Wero through SEPA Direct Debit. Token creation uses the standard SEPA tokenization parameters; the `recurring.token.created` webhook supplies a `storedPaymentMethodId` for later payments. The guide limits tokenized reuse to shopper-absent `UnscheduledCardOnFile` or `Subscription` scenarios. The no-extra-parameters statements above describe the ordinary method flow, not the recurring tokenization requests. [[adyen-tokenization]] See raw lines 74–101 and 386–413.
- The recurring examples submit a SEPA Direct Debit stored-method `/payments` request. A `Received` response means the request was successfully received; the guide directs merchants to webhooks to track whether payment succeeded. Do not treat `Received` as final authorization or settlement. See raw lines 103–306 and 415–618.
- Adyen describes the iDEAL | Wero TEST environment as unreliable and **recommends** live penny tests. When TEST is running, its page offers `TESTNL2A` simulations, including expiration that can produce `Pending` or `Received`. The live-penny steps use an issuer bank account and live Customer Area status check; this snapshot does not itself establish current access, method enablement or an executed payment. See raw lines 308–344 and 620–656.

## Detail locators

- Sessions prerequisites, request, import, component configuration and initialization: raw lines 25–72.
- Sessions recurring token creation, webhook, shopper-absent reuse and sample requests: raw lines 74–306.
- Advanced prerequisites, component initialization and ordinary request: raw lines 346–384.
- Advanced recurring route and sample requests: raw lines 386–618.
- TEST caveat, conditional simulations and recommended live-penny procedure: raw lines 308–344 and 620–656.

## Related

- [[adyen-online-payments]] — Web Components integration route.
- [[adyen-tokenization]] — token lifecycle and shopper-consented storage context.
- [[source-adyen-docs-payment-methods-ideal]] — iDEAL | Wero method overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/ideal/web-component/2026-09-15|iDEAL | Wero Web Component, captured 2026-09-15]]
