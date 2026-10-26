---
title: "iDEAL | Wero Web Drop-in"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/ideal/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/ideal/web-drop-in/2026-09-15.md"
tags: [adyen, ideal, wero, web, drop-in, online-payments, tokenization]
---

## Overview

This 2026-09-15 Adyen guide adds iDEAL | Wero to an existing **Web Drop-in** integration. It provides method-specific additions for Sessions and Advanced flows, rather than a complete base integration. Both flows require redirect handling (`action.type: redirect`) and adding the method in Customer Area. [[adyen-online-payments]]

## Key takeaways

- The **Sessions** branch requires an existing Web Drop-in Sessions integration and Checkout API v68 or later. It adds no method-specific `/sessions` parameters. Importing the individual Web `Redirect` payment method is **optional** for tree shaking/performance, not a prerequisite to Drop-in itself. See raw lines 25–54.
- The **Advanced** branch requires an existing Web Drop-in Advanced integration and redirect handling. Its ordinary `/payments` request adds no method-specific parameters; its individual `Redirect` import is also optional. The Advanced requirements table does not state a Checkout API minimum. Its base-integration hyperlink contains a URL-encoded `{{getParameter('platform')}}` template where a resolved platform would be expected; consult the actual Web Drop-in base guide rather than treating that link as verified. See raw lines 330–358.
- For **recurring** payments, the guide routes iDEAL | Wero through SEPA Direct Debit. Standard SEPA tokenization parameters create the shopper token; `recurring.token.created` carries a `storedPaymentMethodId` for subsequent stored-method requests. The guide restricts these tokenized payments to shopper-absent `UnscheduledCardOnFile` and `Subscription` scenarios. The ordinary-flow no-extra-parameters statements do not remove the tokenization parameters. [[adyen-tokenization]] See raw lines 56–83 and 360–387.
- The recurring `/payments` examples use `paymentMethod.type: sepadirectdebit`, a stored ID and a `Subscription` processing model. They are samples, not a complete guarantee for other recurring modes. The Java samples omit `shopperReference` while the curl and most other language samples include it; follow the linked standard tokenization guidance when building a request rather than copying that example as a full field contract. See raw lines 85–280 and 389–584.
- A `Received` response means the recurring payment request was successfully received, while webhooks track whether payment succeeded. It is not final success or settlement evidence. See raw lines 283–288 and 587–592.
- Adyen calls the iDEAL | Wero TEST environment unreliable and **recommends** live penny tests. When TEST is functioning, its page offers `TESTNL2A` result simulations, with expiration producing `Pending` or `Received`. The live-penny procedure requires a live issuer bank account and checking live Customer Area status; this snapshot does not prove current eligibility or an executed live payment. See raw lines 290–328 and 594–632.

## Detail locators

- Sessions requirements, ordinary request and optional import: raw lines 25–54.
- Sessions SEPA recurring route, stored-method samples and intermediate response: raw lines 56–288.
- Advanced requirements, optional import and ordinary request: raw lines 330–358.
- Advanced SEPA recurring route, stored-method samples and intermediate response: raw lines 360–592.
- TEST reliability caveat, conditional simulations and recommended live-penny procedure: raw lines 290–328 and 594–632.

## Related

- [[adyen-online-payments]] — Web Drop-in integration route.
- [[adyen-tokenization]] — shopper token and stored-method context.
- [[source-adyen-docs-payment-methods-ideal]] — iDEAL | Wero method overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/ideal/web-drop-in/2026-09-15|iDEAL Wero Web Drop-in, captured 2026-09-15]]
