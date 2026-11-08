---
title: "Stripe Subscriptions — Set Up Pix Subscription"
type: source
date_ingested: 2026-11-08
canonical_url: https://docs.stripe.com/billing/subscriptions/pix
original_format: webpage
raw_files:
  - "stripe-subscriptions-pix-2026.md"
tags: [stripe, billing, subscriptions, pix, pix-automatico, brazil, brl, mandate, qr-code, setup-intents]
---

## Summary

The 2026-11-07 capture of this canonical URL is a 15-line navigation index pointing to Stripe-hosted Checkout, Setup Intents API, and Subscriptions API variants. It contains no current variant instructions. The 2026-05-13 full combined capture describes Pix Automático customer-authorized mandates and three distinct subscription flows below. Treat those instructions as dated evidence, not as verified present-day request schemas, eligibility or payment outcomes. Its 20 BRL monthly stock-photo price is an example, not a universal BRL-only rule.

## Pix Automático and Mandate Scope — May 2026 Capture

Pix Automático uses a customer-authorized mandate for recurring charges. The older Checkout and SetupIntent examples include `mandate_options.amount` and `payment_schedule`; the older Subscriptions API prose expressly makes mandate options optional and its example supplies `amount` without `payment_schedule`. Thus these examples do not prove both fields are universally required for all Pix subscription requests. The hosted guide suggests setting an amount above the current price to accommodate a possible future upgrade without returning on-session, but an increase above the mandate amount might fail, and Stripe says it cannot see a customer-set limit. A stricter mandate schedule than a changed subscription interval can also make recurring payments fail.

The old guide models customer identity with `customer_account` for customer-configured Accounts v2 or `customer` for Customers v1. Its May text says Accounts v2 was generally available for Connect and in public preview for other Stripe users, with a preview-version condition. This historical example is not a current eligibility determination. The guide's live example says a Brazilian Pix-enabled bank account is needed to complete or cancel that flow; it does not establish a universal account, country or currency eligibility rule.

## Three Integration Paths — May 2026 Capture

**Stripe-hosted Checkout**: Create a `mode: 'subscription'` Checkout Session with Pix and mandate options, then redirect to its URL. In that variant's prose, banking-app mandate authorization leads to subscription activation and later automatic invoice charges. The captured example uses `amount: 2000` and `payment_schedule: 'monthly'`; do not generalize those values to a required schema.

**Setup Intents API**: Create a Pix SetupIntent for a Customer or customer-configured Account, use `stripe.confirmPixSetup` and its return URL, and verify SetupIntent status on the return page. `succeeded` means setup authorization and a PaymentMethod attached to the Customer; the SetupIntent itself makes no initial payment. Create a subscription with that PaymentMethod as `default_payment_method` afterward. The old guide says the subscription becomes Active after successful payment, not merely when the setup QR is scanned.

**Subscriptions API**: Create an initially `incomplete` Subscription with `payment_behavior: 'default_incomplete'` and `save_default_payment_method: 'on_subscription'`; mandate options are optional in this variant's prose. The response includes the first Invoice's PaymentIntent and confirmation secret. Use `stripe.confirmPixPayment` on the client and verify PaymentIntent status on return. The old guide describes active subscription and saved default payment method after successful payment. QR display or redirect alone is not proof of success.

## Customer Details, QR and Testing — May 2026 Capture

The SetupIntents and Subscriptions API example forms mark name, email and `tax_id` inputs required. Their tables say the Brazilian government requires CPF/CNPJ when buyers complete **cross-border transactions**; the captured guide does not establish a government tax-ID requirement for every Pix subscription or buyer. `000.000.000-00` is a test identifier only. For manual QR display, the SetupIntent and PaymentIntent examples use `handleActions: false` and expose `next_action.pix_display_qr_code` data, image URLs, expiry and hosted instructions. The six email patterns simulate approval, expiry and recurring failure or success in a testing environment; their timings are not production promises.

## Revocation, Changes and Failure — May 2026 Capture

A customer can revoke the mandate in the banking app; the guide says Stripe sends `mandate.updated` and instructs the integration to bring the customer on-session for a replacement mandate. Increasing the subscription above the mandate amount might fail, and a more frequent new billing cycle than the mandate permits causes recurring failures in the old guide. Its scheme restriction allows charging a Pix payment method only once per specified mandate cycle; an add-on requiring immediate payment uses a separate on-session, one-time payment. It describes retry exhaustion and Customer Portal or one-time-payment recovery options. These are dated historical limits; the November index does not confirm their present-day status.

> [!warning] Contradiction
> The former source summary treated `mandate_options.amount` and `payment_schedule` as universally required, CPF/CNPJ as universally government-required, and a QR scan as sufficient to activate the direct API subscription. The May guide itself says Subscriptions API mandate options are optional, limits the stated government tax-ID rule to cross-border transactions, and requires successful payment for direct API activation. The November index has no variant bodies to resolve current requirements.

## Related raw API references

- [[raw/stripe-billing-subscriptions-pix-2026-11-07]] — 2026-11-07 navigation-only index (15 lines); it is not factual provenance for the older flow
- [Stripe-hosted page variant](https://docs.stripe.com/billing/subscriptions/pix.md?api-integration=checkout) — linked by the index; body unread in this comparison
- [Setup Intents API variant](https://docs.stripe.com/billing/subscriptions/pix.md?api-integration=setupintents) — linked by the index; body unread in this comparison
- [Subscriptions API variant](https://docs.stripe.com/billing/subscriptions/pix.md?api-integration=subscription) — linked by the index; body unread in this comparison

## Related pages

- [[stripe-pix]] — concept page
- [[stripe-subscriptions]] — concept page
- [[stripe]] — company page

## Raw Sources

- [[raw/stripe-subscriptions-pix-2026]] — 2026-05-13 combined guide (1059 lines)
