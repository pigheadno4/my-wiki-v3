---
title: "Stripe Subscriptions — Set Up Klarna Subscription"
type: source
date_ingested: 2026-11-08
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/subscriptions/klarna"
raw_files:
  - "stripe-subscriptions-klarna-2026.md"
tags: [stripe, billing, subscriptions, klarna, bnpl, checkout, payment-element, mandate]
---

## Summary

The 2026-05-13 Klarna subscription guide contains two paths: Stripe-hosted Checkout, which it recommends for saving Klarna as a payment method, and an advanced Payment Element integration. The 2026-11-07 capture at the same canonical URL is only an index linking to those two variants. Its loss of inline detail is a navigation change, not evidence of deprecation, altered authorization, mandate or capture behavior, or a successful payment. Current contents of the linked variants were not fetched for this update.

The May guide says Klarna payment options vary by use case and buyer country. Its 23-country tables are sandbox test data from that date, not proof of current country or merchant eligibility.

## Two integration paths in the 2026-05-13 capture

### Path 1: Stripe-hosted Checkout (recommended in the May guide)

The guide starts with a Stripe account, Product and existing Price. Create a server-side Checkout Session with `mode='subscription'` and at least one recurring Price; one-time Prices can be added alongside recurring Prices. Redirect the buyer to the Session URL. The dated sample omits `payment_method_types`; that omission does not establish a universal no-override rule or account-specific Klarna availability. Adding a one-time line item does not make it a recurring mandate or establish manual-capture support.

The guide describes configuring a free trial with `subscription_data` length or end-date settings. To retrieve a created subscription, handle `checkout.session.completed` and record the Session's subscription ID. A returning buyer can also supply the Session ID on a success page and retrieve the Session server-side with `expand=['subscription']`.

**A visit to `success_url` is not payment evidence.** The May guide warns that someone can open that URL without paying, while a buyer who has paid can close the tab before the redirect. Use the webhook or retrieve and verify server-side Session and payment state before granting access; the redirect alone does not prove payment.

> [!warning] Contradiction
> The May guide instructs creating the Checkout Session in `mode='subscription'` (lines 66–83), but its illustrative `checkout.session.completed` payload shows `mode: "setup"` (line 128). Treat the payload as an inconsistent example, not a different subscription-mode instruction.

### Path 2: Payment Element (advanced in the May guide)

Create an incomplete subscription server-side using a Customer and Price with `payment_behavior=default_incomplete`; the example sets `payment_settings.save_default_payment_method='on_subscription'` and expands the first invoice's payment and confirmation-secret fields. On the client, mount the Payment Element using the returned client secret. The dated `stripe.confirmPayment` example passes `elements` and `confirmParams` containing `return_url` and `mandate_data.customer_acceptance`, then redirects to Klarna. This sample does not make its `mandate_data` shape a universal requirement for hosted Checkout.

After return, query the PaymentIntent status. The guide calls payment successful and the subscription active **if** that status is `succeeded`; form submission or redirect alone is not success evidence.

## Klarna characteristics and dated testing

- Klarna payment options vary by use case and buyer country; check the relevant option before integration.
- The May guide's sandbox section gives approved and denied identity/email examples for 23 customer countries. It says Klarna uses cookies for session tracking, so log out between different country tests.
- In those sandbox examples, an arbitrary six-digit authentication code succeeds and `999999` fails. The guide also supplies test repayment values for Direct Debit, bank transfer, credit card and debit card.
- The 23-country data, approval/denial emails and repayment values are test instructions from the May snapshot, not a live coverage guarantee, a successful transaction receipt, or proof of future recurring collection.

Per-country test inputs remain in the full dated raw at lines 164–520 and 683–1038. Neither capture supplies a general Klarna subscription manual-capture contract, actual account eligibility, completed live authorization, successful live charge, settlement, or future recurring payment evidence.

## Related pages

- [[stripe-klarna]] — Klarna concept
- [[stripe-subscriptions]] — subscription concept
- [[stripe]] — company page

## Related raw API references

- [[raw/stripe-billing-subscriptions-klarna-2026-11-07|2026-11-07 Klarna subscription variant index; navigation only]]
- [Stripe-hosted page variant](https://docs.stripe.com/billing/subscriptions/klarna.md?api-integration=checkout) — linked by November index; target not fetched here
- [Advanced integration variant](https://docs.stripe.com/billing/subscriptions/klarna.md?api-integration=elements) — linked by November index; target not fetched here

## Raw Sources

- [[raw/stripe-subscriptions-klarna-2026|Klarna subscription guide, captured 2026-05-13; hosted and advanced paths plus sandbox data]]
