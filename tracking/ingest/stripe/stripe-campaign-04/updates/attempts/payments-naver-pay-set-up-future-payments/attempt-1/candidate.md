---
title: "Stripe Docs — Set up future payments with Naver Pay"
type: source
date_ingested: 2026-05-08
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/naver-pay/set-up-future-payments"
raw_files:
  - "stripe-naver-pay-set-up-future-payments-2025.md"
tags: [stripe, south-korea, krw, naver-pay, recurring, setup-intents, mandate, accounts-v2, nicepay]
---

## Summary

The 2026-05-08 guide details saving `naver_pay` for future payments through hosted Checkout or the Direct API. The 2026-11-07 capture retains that purpose and indexes Checkout and Direct API. The instructions below are from the full May capture.

## Customer agreement and identity

Get the customer's permission before saving and keep a record of their written opt-in. For off-session charges, the May guide says to specify the permitted transactions, the timing and frequency of charges, how amounts are determined, and the cancellation policy for subscriptions. Submit charges only under the agreed terms.

Attach the method to a customer-configured Accounts v2 Account using `customer_account` or a Customers v1 Customer using `customer`. May describes Accounts v2 as generally available for Connect users and in public preview for other Stripe users. Preview participants need a preview API version. The November index establishes no current access or version requirements.

## Save paths in the May guide

- **Hosted Checkout setup.** Create a Checkout Session server-side with `mode: 'setup'` and the matching customer identity, and redirect to the Session URL. The example lists `card` and `naver_pay`. The customer authorizes their NICEPAY account for future use. A separate [[source-stripe-subscriptions-naver-pay|subscription guide]] covers a Checkout subscription-mode example.
- **Direct API setup without an initial payment.** Create a server-side SetupIntent for the matching customer with `naver_pay` in `payment_method_types`. The guide lists `usage: 'on_session'` and `'off_session'` and illustrates the latter. Pass the SetupIntent client secret to the browser. The May Stripe.js Dahlia example calls `stripe.confirmNaverPaySetup` with that secret, a `return_url`, and online `mandate_data.customer_acceptance` using `infer_from_client: true`. The prose inserts a PaymentIntent client-secret gloss, while the code retrieves and confirms a SetupIntent.
- **Direct API charge and save.** The separate server-side PaymentIntent example uses `naver_pay`, a matching customer identity, `confirm: true`, `setup_future_usage: 'off_session'` and a `return_url`. Include `mandate_data` if creating a mandate. The examples illustrate online IP address and user agent. Both charge-and-save examples use `ngn`, in conflict with the same guide's manual redirect and saved-method examples in `krw` and the separate [[source-stripe-naver-pay-accept-payment|Naver Pay compatibility guide]]. The discrepancy's cause is unverified and these examples establish no NGN support.
- **Optional manual redirect.** The nearby May example creates and confirms a KRW PaymentIntent, with `requires_action` directing the customer to `next_action.redirect_to_url.url`. It omits a customer attachment, `setup_future_usage` and mandate settings. It illustrates a payment redirect. Use webhooks to confirm the payment status. The action and browser return establish neither saved setup nor payment success.

## Reuse, detach and sandbox tests

- Create and confirm a new PaymentIntent using the same saved PaymentMethod ID and matching customer-configured Account or Customer. The May examples use KRW. Set `off_session: true` when the customer is outside this PaymentIntent's checkout flow. The May guide separately requires `capture_method: 'automatic'` for recurring payments and excludes manual capture in that recurring scope.
- Server-side PaymentMethod detachment deactivates reuse and sends `mandate.updated` and `payment_method.detached`.
- In the May Checkout setup sandbox, choosing Naver Pay and **Continue to Naver Pay** opens a Stripe-hosted page with authorization and failure options for setup. The separate example at the end describes a PaymentIntent test, from `requires_action` to `succeeded` on authorization or `requires_payment_method` on failure.

## Detail locators

- May raw lines 29–56 and 155–219 cover consent and customer identity. Lines 88–139 cover Checkout setup and its sandbox controls.
- May raw lines 221–261 and 293–380 cover SetupIntent options and browser confirmation. Lines 382–440 cover the separate PaymentIntent redirect and webhook guidance.
- May raw lines 449–518 cover charge and save, including `ngn` at lines 482 and 511. Lines 520–572 cover saved-method reuse, recurring capture, detachment and the PaymentIntent sandbox example.

## Related Pages

- [[stripe-korea-payment-methods]] — South Korea payment methods concept page
- [[source-stripe-naver-pay-accept-payment]] — Naver Pay acceptance and funding sources
- [[source-stripe-kakao-pay-set-up-future-payments]] — Kakao Pay save and recurring guide
- [[stripe]] — Stripe company page

## Raw Sources

- [[raw/stripe-naver-pay-set-up-future-payments-2025|Naver Pay future payments guide captured 2026-05-08]] — verbatim webpage content

## Related raw API references

- [[raw/stripe-payments-naver-pay-set-up-future-payments-2026-11-07|Naver Pay future payments variant index]] — 2026-11-07 navigation for Checkout and Direct API.
