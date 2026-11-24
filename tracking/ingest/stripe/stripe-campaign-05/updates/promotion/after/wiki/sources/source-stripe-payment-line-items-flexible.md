---
title: "Stripe — Payment Line Items for Flexible Payments"
type: source
date_ingested: 2026-05-11
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/payment-line-items/flexible-payment-scenarios"
raw_files:
  - "stripe-payments-payment-line-items-flexible-payment-scenarios-2026-11-07.md"
  - "stripe-payment-line-items-flexible-2026.md"
tags: [stripe, payment-line-items, multicapture, overcapture, incremental-authorization, partial-authorization, surcharge, flexible-payments]
---

## Summary

Stripe’s May 11 and November 7, 2026 guides describe how merchants supply `amount_details` on PaymentIntents for multicapture, overcapture, incremental authorization, partial authorization, and surcharge. The four flexible authorization or capture paths use `capture_method: manual` with an `if_available` request for the relevant feature. Availability depends on payment-method support. Expand `amount_details.line_items` to return line items in the API response.

## Multicapture Rules

- Klarna and PayPal are excluded from multicapture.
- Treat `amount_details` and `amount_details[line_items]` independently. At the first capture, add either if absent at creation. Include or explicitly unset either that was present at creation.
- The guides’ general rule says to keep including fields sent in previous captures and prohibits adding them later if preceding captures omitted them.
- Stripe sums `discount_amount`, `tax.total_tax_amount`, and `shipping.amount` and aggregates line items across captures. The shipping postal codes can be omitted and must stay consistent when supplied.
- A partial nonfinal capture can remain `requires_capture`. An explicit `final_capture: true`, or omitting it where it defaults to true, can complete the PaymentIntent.
- Both guides illustrate closing a partially captured Intent with `amount_to_capture: 0` and `final_capture: true`. This specific final request omits `amount_details` and `line_items`, and its `succeeded` example response retains the first capture’s line items. Read that example alongside the general continuity rule above.

## Overcapture Rules

Request overcapture using `request_overcapture: 'if_available'` in the card example. When capturing more than the current authorization, set `amount_to_capture` up to `maximum_amount_capturable` and pass updated `amount_details` consistent with the actual capture amount.

## Incremental Authorization Rules

Request incremental authorization using `request_incremental_authorization: 'if_available'` in the card example. Use `increment_authorization` to raise the authorization up to the payment method’s limit and send `amount_details` matching the new total authorized amount. The example remains `requires_capture` with no amount received after the increment.

## Partial Authorization Rules

Request partial authorization using `request_partial_authorization: 'if_available'` in the card example. When the issuer authorizes a smaller amount and the supplied details no longer reconcile, `amount_details.error.code` is `amount_details_amount_mismatch`.

- **Update at capture.** Send `amount_details` matching the partially authorized amount. A matching update clears the error and allows Stripe to send card line-item data to the networks. Actual L2/L3 savings depend on qualification.
- **Capture without the update.** The example succeeds at capture with the error still present. Stripe withholds the mismatched card line-item data, so the transaction cannot qualify for L2/L3 interchange savings.

## Surcharge Rules

- Include the surcharge in the PaymentIntent `amount` and specify its amount in `amount_details[surcharge][amount]`. A separate surcharge line item double counts it and produces an HTTP 400 in the guides’ incorrect example.
- For tax with a surcharge, the November 7 guide explicitly directs tax to top-level `amount_details[tax][total_tax_amount]` rather than line-level tax. The May 11 correct example already used that field. May’s public-preview SDK comment applies to its incorrect Node example. November uses curl and links to the card surcharge guide.

## Detail locators

- November lines 15–22, 107–113, and 182–217 cover manual multicapture, first-capture data and continuity. Lines 277–333 show the zero-amount finalization. The example shows `succeeded` and a retained `amount_capturable` value. The response fragment supplies no general post-finalization balance rule.
- November lines 338–441, 531–717, and 724–919 cover the other authorization and capture paths. The example at lines 823–861 shows a nested line-item URL with a different ID than the PaymentIntent, so use the Intent itself for object identity.
- November lines 925–946 and 1024–1071 contain the correct and incorrect surcharge examples. May lines 1153–1178 and 1280–1359 retain the earlier examples.

## Related Pages

- [[stripe|Stripe]]
- [[stripe-payment-line-items]] — payment line items concept
- [[source-stripe-payment-line-items]] — main feature guide
- [[stripe-surcharge]] — surcharge concept

## Raw Sources

- [[raw/stripe-payments-payment-line-items-flexible-payment-scenarios-2026-11-07|November 7, 2026 flexible payment scenarios guide]] — full capture (1,071 lines).
- [[raw/stripe-payment-line-items-flexible-2026|May 11, 2026 flexible payment scenarios guide]] — full capture (1,359 lines).
