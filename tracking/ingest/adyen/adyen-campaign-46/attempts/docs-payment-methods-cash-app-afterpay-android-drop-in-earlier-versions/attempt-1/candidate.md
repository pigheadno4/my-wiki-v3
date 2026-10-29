---
title: "Adyen Cash App Afterpay Android Drop-in v4.x.x"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cash-app-afterpay/android-drop-in/earlier-versions"
raw_files:
  - "adyen/docs/payment-methods/cash-app-afterpay/android-drop-in/earlier-versions/2026-09-15.md"
tags: [adyen, cash-app-afterpay, android, drop-in, earlier-versions, redirect]
---

## Overview

This captured guide adds Cash App Afterpay to an **Android Drop-in v4.x.x Advanced flow** integration. Drop-in shows the US method and redirects the shopper; the merchant server makes `/payments`, checks `/payments/details` after app return, and uses webhooks if the outcome is pending or the shopper does not return. It is a historical version-specific recipe, not proof of current eligibility or a successful live payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- Prerequisites are an existing **Advanced flow Android Drop-in** integration and Cash App Afterpay added in Customer Area. `/paymentMethods` uses US/USD to show the method. Drop-in yields `paymentComponentData.paymentMethod`; pass it to the server along with shopper full name, email, billing/delivery addresses and `lineItems`. Telephone is optional. The payment example uses `paymentMethod.type=afterpaytouch_US` and an Android app return scheme. The introduction's Android Drop-in link and final See also link point to Sessions-flow URLs, while the Requirements row expressly says Advanced flow; select the Advanced guide for this v4.x.x path.
- The `/payments` response's redirect `action` goes back to the client. On app return, Drop-in provides `actionComponentData.details`; the server sends it in `/payments/details` and presents that response's `resultCode`. `Pending` or `Received` means the final result is unknown, potentially for minutes or hours; wait for an AUTHORISATION webhook. If the shopper does not return, use the webhook outcome: `success=false` fails the transaction and `success=true` completes it. A redirect action or return alone is not final payment evidence.
- Capture may be automatic or manual depending on merchant account configuration. Shipment-based delay needs delayed automatic or manual capture; partial capture requires manual capture. Capture must occur within **13 days** after authorization; otherwise the payment is cancelled and the first installment charged at authorization is refunded. Test authorizations expire in **one day**, requiring manual test capture within one day. Manual capture specifies `amount.value`, with optional `lineItems`.
- After ordinary partial capture, the unclaimed amount is automatically cancelled. For accounts enabled for multiple partial captures, the balance is **not** automatically cancelled after the first capture; setup requires Support and each capture creates a separate invoice. Uncaptured payments may be cancelled; captured payments require refund to return funds. Full/partial refund specifies `amount.value` with optional `lineItems`.
- The discount instruction uses a negative line amount. Its example is arithmetically coherent if the USD 1 discount applies to each of the two Item #2 units: 400 + 2×300 − 2×100 = 800 minor units. The snippet has an ellipsis and a missing comma before the discount object, so it is not executable JSON. Test checkout uses a US Afterpay sandbox shopper account and test card; live acceptance needs a Cash App Afterpay request in live Customer Area. The related overview distinguishes this US/USD product from regional Afterpay/Clearpay naming.

## Detail locators

- Raw `# Cash App Afterpay Drop-in v4.x.x integration`, lines 15–41: version, redirect, Advanced prerequisite and US/USD. Raw `## Make a payment`, lines 43–63 and example lines 65–125: client/server handoff and request fields.
- Raw lines 520–591: redirect action, `/payments/details`, Pending/Received and AUTHORISATION webhook outcome. Raw `## Capture the payment`, lines 593–612: capture mode, deadlines and partial-capture exception.
- Raw `## Refunds and cancellations`, lines 614–623: cancel/refund conditions. Raw `## Discounts`, lines 625–659: per-unit arithmetic and non-executable snippet. Raw `## Test and go live`, lines 661–679: sandbox and live setup.

## Related

- [[source-adyen-docs-payment-methods-cash-app-afterpay]] — US/USD regional product overview
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/cash-app-afterpay/android-drop-in/earlier-versions/2026-09-15|Cash App Afterpay Android Drop-in v4.x.x guide, captured 2026-09-15]]
