---
title: "Stripe — Overcapture"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-overcapture-2026.md"
tags: [stripe, overcapture, capture, payment-intents, checkout, ic-plus, sca]
---

## Summary

IC+ feature allowing capture above the authorized amount without creating a new card network authorization. The initial pending authorization updates with the final captured amount after settlement — customers see no immediate statement change. Covered across three integration paths: Stripe-hosted Checkout, Embedded Checkout, and direct PaymentIntents (Elements).

## Availability

- **IC+ pricing only**
- Visa (excl. EEA), Mastercard, AmEx, Discover; online card payments only
- `capture_method: 'manual'` required

## Percent Limits by Network

| Network | Merchant/Country | Limit |
| --- | --- | --- |
| Visa | US restaurants/fast food/caterers | +30% |
| Visa | Global restaurants/fast food, taxicabs, bars, beauty/spas | +20% |
| Visa | Car rentals | Greater of +15% or $75 USD |
| Visa | Lodging, cruise lines; all other (cardholder-initiated) | +15% |
| Mastercard | US restaurants/fast food (US-issued cards only) | +30% |
| AmEx | Global restaurants, bars, fast food | +30% (debit/prepaid capped at +20%) |
| AmEx | Taxicabs, beauty/spas | +20% |
| AmEx | Lodging, car/truck/RV rental, grocery, retail stores | +15% |
| Discover | Global restaurants, taxicabs, bars, beauty/spas | +20% |
| Discover | Lodging, car rentals | +15% |
| Diners Club (beta) | US via Discover — restaurants, taxicabs, beauty/spas | +20% |
| Diners Club (beta) | US via Discover — lodging, car rentals | +15% |

## SCA Countries

Under SCA, merchants must authenticate for the highest estimated amount upfront. If the final amount exceeds the authenticated amount, the original payment must be canceled and re-created. Exceptions: MIT (merchant-initiated transactions where customer isn't present) may qualify for exemption.

## API Flow

**Enable**: `payment_method_options.card.request_overcapture: 'if_available'` on create/confirm.

**Check availability**: `charge.payment_method_details.card.overcapture.status` → `available` or `unavailable`; `overcapture.maximum_amount_capturable` shows the cap.

**Capture**: `amount_to_capture` up to `maximum_amount_capturable`. PI `amount` updates to reflect captured amount. Original authorized amount preserved in `charge.payment_method_details.card.amount_authorized`.

**If max insufficient**: use incremental authorization instead.

## Test Cards

| Number | Payment Method | Notes |
| --- | --- | --- |
| 4242424242424242 | pm_card_visa | Supports overcapture |
| 5555555555554444 | pm_card_mastercard | Supports overcapture |
| 378282246310005 | pm_card_amex | Supports overcapture |
| 6011111111111117 | pm_card_discover | Supports overcapture |
| 4000008400000076 | pm_card_credit_disableEnterpriseCardFeatures | Does NOT support overcapture |

## Related Pages

- [[stripe-overcapture]] — concept page
- [[stripe-multicapture]] — related IC+ capture feature (multiple partial captures vs. single overcapture)
- [[source-stripe-payment-line-items-flexible]] — overcapture with payment line items

## Raw Sources

- [[stripe-overcapture-2026]] — verbatim overcapture guide, all 3 UI variants (751 lines)
