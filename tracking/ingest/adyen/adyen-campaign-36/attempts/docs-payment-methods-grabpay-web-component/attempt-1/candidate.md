---
title: "Adyen GrabPay Web Component"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/grabpay/web-component"
raw_files:
  - "adyen/docs/payment-methods/grabpay/web-component/2026-09-15.md"
tags: [adyen, grabpay, web, components, wallet, paylater]
---

## Overview

This captured Adyen guide adds GrabPay to an existing Web Components integration in Sessions or Advanced flow. It separates GrabPay Wallet from PayLater request data and provides country-specific Component choices. It is a historical documentation snapshot (page metadata last modified 2019-11-13), not proof of current method availability, merchant eligibility or a completed payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- An existing Sessions or Advanced Web Components integration and GrabPay enablement in Customer Area are prerequisites. For GrabPay **PayLater**, whether postpaid or installment, send `deliveryAddress` and `lineItems` in the applicable `/sessions` or `/payments` request. The page recommends the same data for GrabPay **Wallet** to ease a later PayLater addition; it does not call those fields mandatory for Wallet.
- The guide labels `/sessions` the default with Web Components v5.0.0 or later and presents `/payments` for an additional use case or integrations before v5.0.0. These are endpoint routes in the page, not a claim that v5+ cannot use Advanced flow.
- Choose the Component according to shopper location and currency: `grabpay_MY` for Malaysia/MYR, `grabpay_PH` for Philippines/PHP, or `grabpay_SG` for Singapore/SGD. The request samples show the Singapore case, including `paymentMethod.type: grabpay_SG` for `/payments`; they do not prove a merchant's eligibility for every listed country.
- For Web v6.0.0 or later, the Singapore example mounts `new Redirect(checkout, { type: 'grabpay_SG' })`; for v5.x.x or earlier, it uses `checkout.create('grabpay_SG')`. Both examples assume an `AdyenCheckout` instance and a target DOM element. The source includes a stray `**` after the v6 code block and the Sessions Node examples reference `Config` and `EnvironmentEnum` without imports; treat snippets as illustrative rather than copy-ready.
- Testing requires Support-provided test wallet credentials and logging in to the Grab simulator with a registered phone number and received one-time password. Check test-payment status in the Adyen test Customer Area. Live acceptance requires a separate GrabPay request in the live Customer Area. Setup, simulator login, Component mount and API submission are not payment-outcome evidence.

## Detail locators

- Sessions/Advanced integration and Customer Area prerequisites: pinned raw lines 21–42.
- PayLater-only additional-data distinction and endpoint selection: pinned raw lines 44–57 and 510–517.
- `/sessions` examples (test v69, Singapore): pinned raw lines 59–508; `/payments` examples (curl test v72, Singapore `grabpay_SG`): lines 519–809. The examples mix server API-library versions and amounts; use the endpoint contract for a specific implementation.
- Country/currency Component mapping and Web v6 versus v5 mounting: pinned raw lines 811–849.
- Test and live prerequisites: pinned raw lines 851–860.

## Related

- [[adyen-online-payments]] — Web Components and Sessions/Advanced architecture
- [[source-adyen-docs-payment-methods-grabpay]] — method overview, if ingested separately

## Raw Sources

- [[raw/adyen/docs/payment-methods/grabpay/web-component/2026-09-15|GrabPay Web Component guide, 2026-09-15]]
