---
title: "Stripe: France Titres-Restaurant (Meal Vouchers)"
type: source
date_ingested: 2026-05-05
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers"
raw_files:
  - "stripe-payments-meal-vouchers-fr-meal-vouchers-2026-11-07.md"
  - "stripe-fr-meal-vouchers-2025.md"
tags: [stripe, meal-vouchers, france, titres-restaurant, benefits, siret, split-tender]
---

## Summary

Stripe's May 5 and November 7, 2026 overviews describe France titres-restaurant as a private preview for nonrecurring card payments in EUR. It covers French customers, approved French Stripe accounts, Elements and partial Connect support. The November capture adds an email waitlist and a documentation-generated registration request. The [preview waitlist](https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers.md#fr_meal_voucher_preview) requests access, with onboarding subject to Stripe follow-up. For partial Connect support, both captures direct platforms to fr-meal-voucher-beta@stripe.com.

## Issuers and Readiness

- **Issuers.** Bimpli (formerly Apetiz), Pluxee (formerly Sodexo) and Up Déjeuner are covered by the voucher-specific integration. Stripe routes eligible Swile vouchers through Mastercard without extra integration work. Swile determines eligibility and generally excludes businesses that accept vouchers through food-service platforms.
- **Eligibility.** Obtain approval from the Commission Nationale des Titres-Restaurant (CNTR) for each accepting branch and a commercial acceptance agreement with at least one supported issuer. Restaurants, grocers, canteens and other businesses serving prepared food are the generally eligible business types.
- **Branch provisioning.** Provide the approved branch's SIRET to Stripe before acceptance. Both dated overviews estimate 1–3 business days to bind it to the merchant identifier. The November Dashboard guide describes 1–2 business days for validation and treats the name and SIRET as immutable after creation in that UI. The separate Payment Locations API guide describes 1–2 business days in its pending onboarding path. Certain acknowledged API updates, such as SIRET or address changes, return the capability to pending and pause voucher acceptance until reactivation. See [[source-stripe-fr-meal-vouchers-setup-restaurant]].

## Settlement, Capture and Disputes

The voucher issuer pays the acceptor directly. Set up settlement bank details with the contracted issuer and direct settlement questions to that issuer. Stripe deducts its processing fee from the Stripe balance and records it as a negative `BalanceTransaction`. Issuer fees are separate. The issuer determines the statement descriptor from the SIRET on the PaymentIntent or SetupIntent. Stripe sends no statement descriptor to the network for this voucher route.

Bimpli, Pluxee and Up Déjeuner have no dispute-resolution system for these vouchers. A captured voucher payment supports neither full nor partial refunds. Where fulfillment is uncertain, use separate authorization and capture so the voucher authorization can be released while it remains uncaptured.

## Payment, Setup and PaymentMethod Identification

Both overview captures document opt-in on each PaymentIntent using the literal `payment_details.benefit.fr_meal_voucher.siret` for the physical branch. PaymentIntent creation fails if that supplied SIRET was not provisioned. The overviews also say Stripe does not retry failed voucher payments as ordinary card payments or vice versa.

The separate November purchase and Connect guides require Stripe version `2026-05-27.preview` or later. The purchase guide requires an active `fr_meal_vouchers_conecs_payments` location capability. In that flow, pass the Payment Location ID in `payment_details[location]` and set `payment_details[benefit][fr_meal_voucher][enabled]` to `if_payment_method_is_eligible`. Stripe resolves the location's stored SIRET at confirmation. A change after Intent creation can affect the SIRET used for that confirmation. Previously confirmed payments retain their original SIRET. Connect has separate direct and platform charge instructions and requests the location capability on behalf of the merchant of record. See [[source-stripe-fr-meal-vouchers-accept-payment]] and [[source-stripe-fr-meal-vouchers-connect]].

The November save guide uses the same preview version floor and active-location prerequisite for SetupIntent. It uses `setup_details[location]` and `setup_details[benefit][fr_meal_voucher][enabled]` for setup. Later reuse is on-session and uses PaymentIntent's `payment_details` with the Customer and saved PaymentMethod IDs. The dated sources leave compatibility between the literal SIRET and location-based forms open. Conditional opt-in expresses method eligibility at payment time. An Intent or an eligible-card example leaves authorization, capture and issuer settlement to be established separately. See [[source-stripe-fr-meal-vouchers-save-payment]].

Both overviews illustrate a scalar `PaymentMethod.card.benefits.programs` containing `fr_meal_voucher`, with the issuer in `PaymentMethod.card.benefits.issuer`. The November Connect guide illustrates an array at that PaymentMethod path and a scalar under the separate `ConfirmationToken.payment_method_preview.card.benefits.programs` path. These examples establish the shapes shown in their respective captures. They leave a universal response shape and actual transaction eligibility unresolved. See [[source-stripe-fr-meal-vouchers-connect]].

## Balance and Split Tender

Both overviews document a €25 daily cap and a balance refresh at midnight French local time. The optional balance lookup applies to a saved voucher PaymentMethod. The separate May and November balance guides show `POST /v1/payment_methods/:id/check_balance`. Its `as_of` timestamp describes a snapshot. It reserves no funds, and a concurrent purchase can still cause a later authorization to decline.

Stripe does not orchestrate split tender natively. Use separate payments for eligible food and for ancillary fees or an amount exceeding the voucher balance. The November balance guide's prose recommends processing the secondary payment first or using manual voucher capture after the secondary payment succeeds. Its diagram places the voucher PaymentIntent first and calls for reversion if the secondary payment fails. In the voucher leg, release is available only while authorization remains uncaptured. See [[source-stripe-fr-meal-vouchers-check-balance]].

## Related Pages

- [[stripe-fr-meal-vouchers]] — product concept and dated integration routes
- [[source-stripe-fr-meal-vouchers-accept-payment]] — PaymentIntent acceptance and confirmation
- [[source-stripe-fr-meal-vouchers-connect]] — direct and platform charges, fee routing and object-specific benefit examples
- [[source-stripe-fr-meal-vouchers-check-balance]] — saved-card balance and split tender
- [[source-stripe-fr-meal-vouchers-save-payment]] — setup, on-session reuse and temporary authorization
- [[source-stripe-fr-meal-vouchers-setup-restaurant]] — Dashboard and API onboarding
- [[stripe]] — company page

## Raw Sources

- [[raw/stripe-payments-meal-vouchers-fr-meal-vouchers-2026-11-07|November 7, 2026 product overview]] — full capture with the preview waitlist
- [[raw/stripe-fr-meal-vouchers-2025|May 5, 2026 product overview]] — full historical capture; Markdown emphasis on “split tender” was normalized
