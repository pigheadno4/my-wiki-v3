---
title: "Adyen Zip Web Component integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/zip/web-component"
raw_files:
  - "adyen/docs/payment-methods/zip/web-component/2026-09-15.md"
tags: [adyen, zip, web, components, redirect, recurring]
---

## Overview

This captured Adyen guide explains adding Zip to an existing Web Components integration, with separate Sessions and Advanced server-flow tabs, a redirect Component, and a recurring-token route. The guide's page metadata says last modified 2019-09-06; its examples and version references are retained as captured evidence, not proof of current account eligibility or live payment success. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- Build the matching Sessions or Advanced Web Components flow and add Zip in Customer Area. The `/sessions` tab is described as the default with Components v5.0.0 or later; `/payments` is presented for an additional use case. The API reference tables list shopper name, email, date of birth, telephone, billing/delivery addresses and `lineItems`, but leave their **Required** column blank; do not infer that every listed field is required from these tables. Optional `lineItems.imageURL` appears on Zip's product page, limited to 500 characters. The `/payments` tab also describes `paymentMethod.clickAndCollect=true` when the shopper picks up an order.
- The request examples use `paymentMethod.type=zip`, `AU`/`AUD` and a `returnUrl`. These are example values; the separate Zip overview lists AU and US with AUD and USD without explicitly pairing all countries and currencies. In the Advanced path, the `/payments` response's `action` provides redirect information, with a `RedirectShopper` example. Redirecting or returning is not itself payment finality.
- For Web Components v6.0.0 or later, the page shows `new Redirect(checkout, { type: 'zip' }).mount(...)`; for v5.x.x or earlier, `checkout.create('zip').mount(...)`. The mounted Component is the client display step, separate from the server API request.
- The page states Zip supports recurring transactions. To create a token, send `storePaymentMethod=true` and a unique `shopperReference` in a `/payments` request; **after settlement**, a `recurring.token.created` lifecycle webhook carries `storedPaymentMethodId`. The server must receive that webhook. Future token payments use that ID, the same shopper reference, `shopperInteraction=ContAuth`, and `recurringProcessingModel=Subscription` or `UnscheduledCardOnFile`. A redirect response or an initial authorization alone does not establish token creation.
- The `/payments` curl example includes literal `{hint:...}` markup in the JSON at line 724; it should not be treated as a ready-to-send request. Other SDK snippets are examples, not verified executions. Test guidance points to Zip test accounts and Customer Area payment status; live use requires a Zip request in the live Customer Area.

## Detail locators

- Raw `# Zip Component`, lines 15–45: identity, flow prerequisites, and Sessions version/default.
- Raw `## API reference`, lines 43–55 and 692–705: endpoint-specific field lists, blank requiredness cells, image URL limit and click-and-collect condition. Raw `/sessions` curl lines 61–112 and `/payments` curl lines 709–765: AU/AUD example request details and literal hint markup.
- Raw lines 1386–1399 and `## Component configuration` lines 1402–1432: redirect action and v6 versus v5 Component construction.
- Raw `## Recurring payments`, lines 1434–1467: token creation, after-settlement webhook, future-payment fields and models. Raw `## Test and go live`, lines 1667–1673: test and live boundaries.

## Related

- [[source-adyen-docs-payment-methods-zip]] — method overview and regional capability context
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/zip/web-component/2026-09-15|Zip Web Component guide, captured 2026-09-15]]
