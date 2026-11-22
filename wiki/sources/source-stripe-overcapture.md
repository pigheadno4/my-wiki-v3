---
title: "Stripe — Overcapture"
type: source
date_ingested: 2026-05-11
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/overcapture"
raw_files:
  - "stripe-overcapture-2026.md"
tags: [stripe, overcapture, capture, payment-intents, checkout, ic-plus, sca]
---

## Summary

The November 7, 2026 capture defines overcapture as capture above a PaymentIntent's authorized amount and links three web variants: Stripe-hosted Checkout, full embedded Checkout and advanced Elements. The May 11, 2026 full guide documents the mechanics below for those three routes. Overcapture requires no additional card-network authorization. The pending card statement entry updates with the final captured amount after settlement.

## May 11, 2026 availability

- **Pricing.** The May dedicated guide offers overcapture on IC+ and directs standard-pricing users to Stripe Support to ask for access. The separate November 7 [[source-stripe-elements-advanced-payments|Advanced Elements comparison]] lists Overcapture for both Checkout Sessions and Payment Intents under flexible scenarios marked IC+ only. The Support referral leaves exceptions, plan changes and actual account access unverified.
- **Network and transaction restrictions.** The May guide limits overcapture to eligible online card payments and lists Visa, Mastercard, American Express and Discover. It excludes EEA businesses from the Visa rows and lists Diners Club as limited beta in the US through Discover. Eligibility and limits depend on network, merchant country and category, and where applicable issuer country and card type.
- For a transaction partially authorized below the requested amount, overcapture cannot exceed the approved amount. See [[source-stripe-partial-authorization]] for the May and November 2026 guidance.

## Percent Limits by Network

| Network | Merchant/Country | Limit |
| --- | --- | --- |
| Visa | US restaurants/fast food/caterers | +30% |
| Visa | Global restaurants/fast food, taxicabs, bars, beauty/spas | +20% |
| Visa | Car rentals | Greater of +15% or USD 75 (or local currency equivalent) |
| Visa | Lodging, cruise lines; all other (cardholder-initiated) | +15% |
| Mastercard | US restaurants/fast food (US-issued cards only) | +30% |
| AmEx | Global restaurants, bars, fast food | +30% (debit/prepaid capped at +20%) |
| AmEx | Taxicabs, beauty/spas | +20% |
| AmEx | Lodging, car/truck/RV rental, grocery, retail stores | +15% |
| Discover | Global restaurants, taxicabs, bars, beauty/spas | +20% |
| Discover | Lodging, car rentals | +15% |
| Diners Club (beta) | US via Discover — taxicabs/limousines, restaurants/fast food, drinking places serving alcoholic beverages, beauty/barber shops and health/beauty spas | +20% |
| Diners Club (beta) | US via Discover — lodging, car rentals | +15% |

## May 11, 2026 Strong Customer Authentication (SCA)

When the merchant and cardholder are in a country with SCA requirements, Stripe's May guide generally calls for authenticating and authorizing at least the expected capture amount. If the final amount exceeds the originally authenticated and authorized amount, the guide directs the merchant to cancel and recreate the payment unless an applicable exemption applies. A merchant-initiated transaction with the customer absent is potentially exempt. A reported capture maximum does not supersede SCA or applicable network rules.

## May 11, 2026 request and capture flow

1. **Hosted or full embedded Checkout.** Create the Checkout Session on the server with `mode=payment`, `payment_intent_data.capture_method=manual` and `payment_method_options.card.request_overcapture=if_available`. The May availability prose requires manual capture, but both Session creation examples omit `payment_intent_data.capture_method`. Hosted Checkout uses the Session URL and `success_url`. Full embedded Checkout uses `ui_mode=embedded_page`, the Session `client_secret` to mount Checkout in the browser, and `return_url` when configured. The JavaScript mounting example uses Dahlia Stripe.js.
2. **Advanced Elements using PaymentIntents directly.** Create the PaymentIntent with `capture_method=manual` and request overcapture using `payment_method_options.card.request_overcapture=if_available` before or at confirmation. The direct example uses `confirm: true` and includes manual capture. Overcapture applies to a confirmed, uncaptured payment.
3. **Check the PaymentIntent and its latest Charge server-side.** Inspect `latest_charge.payment_method_details.card.overcapture.status` and `maximum_amount_capturable`. If overcapture is `unavailable`, the maximum is the authorized amount. The May embedded return-page example labels Checkout Session `complete` as payment success. Its overcapture flow can still have an associated PaymentIntent in `requires_capture` with `amount_received=0`. A completed Session or browser return leaves capture unverified.
4. **Capture the PaymentIntent.** Send `amount_to_capture` within the reported cap. If more is needed, incremental authorization is an option where available. The separate May beta-to-GA migration example offers a choice between overcapture and incremental authorization only when both features report `available` on the latest Charge after confirmation. The successful overcapture example moves the Intent from `requires_capture` to `succeeded`, with `amount=1200`, `amount_received=1200` and `amount_capturable=0`. The Charge's `payment_method_details.card.amount_authorized` retains the initial 1000. Settlement and the later statement update are separate stages.

## May 11, 2026 test cards

Stripe's May guide says availability for a given network in testing carries over to live payments for that network. The examples below cover four supporting networks and one Visa card with overcapture unavailable. This network-level statement leaves individual account and transaction eligibility, capture and settlement unverified.

| Number | Payment Method | Notes |
| --- | --- | --- |
| 4242424242424242 | pm_card_visa | Supports overcapture |
| 5555555555554444 | pm_card_mastercard | Supports overcapture |
| 378282246310005 | pm_card_amex | Supports overcapture |
| 6011111111111117 | pm_card_discover | Supports overcapture |
| 4000008400000076 | pm_card_credit_disableEnterpriseCardFeatures | Does NOT support overcapture |

## Related Pages

- [[stripe]]
- [[stripe-checkout]] — Checkout Session request and capture boundaries
- [[source-stripe-flexible-features-migration]] — dated migration example for checking both overcapture and incremental authorization
- [[stripe-overcapture]] — concept page
- [[stripe-multicapture]] — related IC+ capture feature (multiple partial captures vs. single overcapture)
- [[source-stripe-payment-line-items-flexible]] — overcapture with payment line items

## Raw Sources

- [[raw/stripe-overcapture-2026|May 11, 2026 full overcapture guide]] — 751 lines across all three web variants. See network tables and SCA at lines 28–77, hosted Session at 79–224, embedded Session and return page at 297–568, advanced Elements PaymentIntent flow at 637–739, and test methods at 741–751.

## Related raw API references

- [[raw/stripe-payments-overcapture-2026-11-07|Overcapture web variant index]] — November 7, 2026 navigation to Stripe-hosted, full embedded and advanced Elements variants (lines 9–15).
