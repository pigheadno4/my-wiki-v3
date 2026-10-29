---
title: "Adyen Scalapay Web Component"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/scalapay/web-component"
raw_files:
  - "adyen/docs/payment-methods/scalapay/web-component/2026-09-15.md"
tags: [adyen, scalapay, web-components, buy-now-pay-later]
---

## Overview

This Adyen guide adds Scalapay to an existing Web Components Sessions or Advanced flow. It configures a `scalapay_3x` redirect Component and the request data for eligible shoppers. The 2026-09-15 capture has 2019 last-modified metadata despite later examples; it is a documentation snapshot, not proof of present merchant enablement, price-plan eligibility or a completed payment. See [[adyen]], [[adyen-online-payments]] and the [[source-adyen-docs-payment-methods-scalapay|Scalapay overview]].

## Key takeaways

- Both flows require an existing Components integration and Scalapay added in Customer Area. The requirement links contain an unresolved encoded `{{getParameter('platform')}}` platform placeholder, so follow the actual Web base-integration route. Activating Scalapay defaults to standard pricing; the page describes Enterprise pricing for sufficient-volume merchants and says to contact an account manager before activation to verify eligibility.
- `/sessions` is the stated default with Components v5.0.0 or later. Both API tables mark shopper `countryCode` (IT, FR, PT or ES) and first/last `shopperName` required; billing address, delivery address and line items are listed without a requirement mark. The `/payments` additional-use-case table also offers optional outbound flight date or lodging check-in date data and says to provide either one in the same transaction, not both. Its example is IT/EUR with `paymentMethod.type: scalapay_3x`, not a universal currency/eligibility claim.
- The v6.0.0-or-later snippet mounts `new Redirect(checkout, { type: 'scalapay_3x' })`; v5.x.x or earlier uses `checkout.create('scalapay_3x')`. The v6 snippet does not show an import for `Redirect`; use the version-specific base Components guide before copying it.
- The related Scalapay overview's captured feature matrix identifies FR, IT, PT and ES with EUR, a redirect flow, and recurring unavailable. Its overview marks refunds and captures as possible but this child page supplies no capture or refund procedure or outcome proof. The child “See also” tokenization link is navigation and does not override the overview's no-recurring mark.
- Testing uses Scalapay test scenarios and status in test Customer Area. Live acceptance requires a separate Scalapay request in live Customer Area. The TEST sample and live-request instruction do not establish current account approval or successful payment execution.

## Detail locators

- Requirements, pricing and unresolved platform template in URLs: raw lines 21–39.
- Sessions and Advanced API field tables, including country/name and flight-versus-lodging condition: raw lines 41–71. The curl `/payments` example uses Checkout API v72 TEST; language library samples each show their own versions at raw lines 73–429.
- Web component v6/v5 mount snippets: raw lines 430–460. Testing and live request: raw lines 462–468.
- The related Scalapay overview's FR/IT/PT/ES, EUR and no-recurring matrix is at `raw/adyen/docs/payment-methods/scalapay/2026-09-15.md` lines 19–23.

## Related

- [[adyen-online-payments]] — provider Web integration context.
- [[source-adyen-docs-payment-methods-scalapay]] — product matrix and feature limits.

## Raw Sources

- [[raw/adyen/docs/payment-methods/scalapay/web-component/2026-09-15|Scalapay Web Component, captured 2026-09-15]]
