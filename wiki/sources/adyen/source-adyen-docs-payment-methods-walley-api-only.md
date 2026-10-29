---
title: "Walley API-only integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/walley/api-only"
raw_files:
  - "adyen/docs/payment-methods/walley/api-only/2026-09-15.md"
tags: [adyen, walley, api-only, redirect, buy-now-pay-later]
---

## Overview

This Walley API-only guide, last modified 2023-03-03 and captured 2026-09-15, describes building a custom payment form and using the Web API-only `/payments` redirect path. It covers B2C/B2B discovery, required shopper and line-item data, `/payments/details` and webhook outcomes, capture/refund modifications, and testing. This dated source does not prove current merchant enablement, a successful live payment, or actual settlement. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The page requires an existing Web API-only integration of at least **v66** and Support assistance to add Walley in test Customer Area. Its main integration URL contains an unusual `API%20Only%2F%3Ftarget%3D_blank` fragment; use the verified base guide route rather than treating that malformed-looking link as a version rule (raw lines 21–26).
- For `/paymentMethods` discovery, the listed country/currency pairs are **DK/DKK, FI/EUR, NO/NOK, SE/SEK**. Denmark or DKK is **B2C only**. API type `walley` is B2C and `walley_b2b` is B2B; for B2B, company.name is required and registrationNumber optional. Collect telephoneNumber and shopperEmail (raw lines 28–50). **Example conflict:** the `/payments` snippets use `countryCode: NO` with `currency: EUR`, and a +46 phone, while the discovery table specifies NO/NOK and the request says a working mobile number including country code. Do not infer NO/EUR acceptance from the example (raw lines 41–48, 60–69, 71–110).
- The `/payments` table marks telephoneNumber, shopperEmail, and lineItems id, description (maximum 50 characters), amountExcludingTax, taxAmount, taxPercentage, and quantity required; company.name is required **only for walley_b2b**, while registrationNumber is B2B-relevant but unmarked. A missing or incorrect working mobile number fails Walley validation, according to the page (raw lines 54–69).
- `/payments` returns a redirect action; redirect to `action.url`, then submit the URL-decoded `redirectResult` to `/payments/details` after website return. The mobile browser advice is scoped to app/mobile integrations (raw lines 351–405). `Pending`/`Received` is not final: await AUTHORISATION webhook; if the shopper does not return, use webhook outcome. `Authorised` is described as sent to the bank for processing and usually leading to funds, with manual capture still required when configured (raw lines 408–427).
- Capture after goods are sent; authorization expires if uncaptured within **90 days**. Automatic capture defaults to immediate, but Walley's asynchronous `202` success update can make it produce a `403` forbidden response. The page suggests an automatic delay of at least **one day**, or manual capture; with automatic capture enabled, override via `captureDelayHours`, while without it, wait at least **10 seconds** after `/payments` before manual capture (raw lines 429–455).
- For partial capture, include amount and lineItems for only captured items; B2B lineItems values must match authorization, and an amount-only B2B capture is for full capture. The lineItems sum must match the capture amount or Adyen adds a dummy line item. **Manually cancel remaining amount** after partial capture (raw lines 452–538). The sample partial-capture request has a malformed URL (`https: //`) and its response swaps the example payment/capture PSP references relative to the request; treat these as non-copy-ready examples. The sample `status: received` is an acknowledgement, not proof of final capture (raw lines 477–536).
- Cancel before capture; refund after capture. Full refund does not need lineItems; partial refund should specify amount and only refunded items, with lineItems sum matching amount or Adyen inserts a dummy line item. The page says refund `pspReference` is for the refund transaction, not the original payment (raw lines 540–618).
- Test guidance maps Walley `CivRegNo` to Adyen `socialSecurityNumber` and gives a B2B company example; it does not document a live enablement step on this page (raw lines 620–634).

## Detail locators

- API-only scope and test setup: raw `## Requirements` lines 21–26.
- B2C/B2B, country/currency, required request data and samples: raw `## Build your payment form for Walley` lines 28–52 and `## Make a payment` lines 54–365.
- Redirect and asynchronous result handling: raw `## Handle the redirect` lines 367–406 and `## Show the payment result` lines 408–427.
- Capture latency, partial capture and remaining-amount cancellation: raw `## Capture the payment` lines 429–538.
- Refunds/cancellations and test: raw lines 540–640.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-walley]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/walley/api-only/2026-09-15|Walley API-only guide, captured 2026-09-15]]
