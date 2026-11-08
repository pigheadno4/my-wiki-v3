---
title: "Stripe Subscriptions — Integrate with Third-Party Payment Processors"
type: source
date_ingested: 2026-11-08
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/subscriptions/third-party-payment-processing"
raw_files:
  - "stripe-subscriptions-third-party-2026.md"
tags: [stripe, billing, subscriptions, third-party, custom-payment-methods, payment-records, off-stripe, orchestration]
---

## Overview

Stripe's combined 2026-05-13 guide documents two ways to use Billing subscriptions and invoices with a third-party processor: an own-processor path with custom PaymentMethods and PaymentRecords, and a separate out-of-band invoice path. The 2026-11-07 canonical capture is only an index linking the two variant routes; it establishes no current setup, eligibility, API version, payment outcome, or change to the May flows. See [[stripe-billing-third-party]], [[stripe-custom-payment-methods]], [[stripe-subscriptions]], and [[stripe]].

## Own processor: custom PaymentMethods and PaymentRecords (May 2026 guide)

This path describes `charge_automatically` subscriptions. The merchant or platform integrates directly with its external processor and is responsible for applicable PSP agreements, law, and supported locations. A Stripe custom PaymentMethod references the external instrument; a PaymentRecord reports off-Stripe attempts and outcomes to Stripe. It is not the third-party processor's settlement receipt.

- Set up the custom payment method type in the Dashboard. The guide has separate customer-configured Account v2 (`customer_account`) and Customer v1 (`customer`) examples.
- Create the subscription with `payment_behavior: default_incomplete`; at this point the May guide says the subscription is `incomplete` with an open invoice. Collect payment through the external processor, then create and attach the custom PaymentMethod and set it as the subscription default.
- For a synchronous outcome, report `guaranteed` or `failed` on a PaymentRecord and attach it to the invoice. For an asynchronous flow, first report an initiated payment, then report its guaranteed or failed attempt when the processor responds. The guide says a payment must be reported within **23 hours** of subscription creation or the subscription becomes `incomplete_expired`.
- For future `charge_automatically` invoices, handle `invoice.payment_attempt_required` after finalization, collect off-session externally, and report the result. With `auto_advance: false`, the guide says this webhook is not sent until normal collection resumes. A reported failure leaves the invoice open; a previously active subscription may become `past_due`.
- On a retry, report another attempt against the **existing** PaymentRecord rather than creating a separate record for each attempt. The guide describes custom schedules or automations and excludes Smart Retries and revenue-recovery emails. For a refund, refund at the third-party processor, then report it to Stripe and use a Credit Note to adjust an issued invoice. The asynchronous path also permits reporting cancellation of an initiated attempt.

> [!warning] Contradiction
> The May guide says attaching a PaymentRecord marks the invoice `paid` and subscription `active` (old line 340), while its asynchronous example attaches an `initiated` record before a later outcome report (old lines 252–317). This capture does not settle the exact invoice/status transition for that case, and no reported Stripe state proves external settlement.

### Own-processor limits and sample version (May 2026 guide)

This variant allows the Payment Element or a custom non-Stripe checkout flow, but says Stripe Checkout and Hosted Invoice Page do not support its off-Stripe payments. It places disputes and refund initiation with the external processor. The customer portal can manage subscriptions using custom payment methods, but the guide says it cannot add a discount when the session's subscription-update `proration_behavior` is `always_invoice`. That token corrects the prior source summary's `always_invoke` typo.

The guide lists supported business and processor locations at old lines 624–790; these are dated lists, not verified current eligibility. It says third-party Billing volume counts toward total Stripe Billing volume under the billing contract. Several May **Node examples** set `apiVersion: '2026-04-22.dahlia'`; this is a sample setting, not a guide-wide minimum or current account requirement. One example at old line 324 has a malformed quoted version ending in a semicolon and should not be copied as runnable guidance.

## Out-of-band invoices (May 2026 guide)

This separate path creates a subscription with `collection_method: send_invoice` and a `days_until_due` chosen to allow external recovery; **30 days** is an example value. It uses a customer-configured Account v2 or Customer v1, keeps only non-sensitive third-party references in metadata, and calls for a custom checkout flow. The May out-of-band variant excludes both Stripe Checkout and Elements, unlike the own-processor variant's Payment Element allowance.

The guide advises disabling finalized-invoice emails only if all emailed subscription invoices use a third-party processor, because that setting also affects other `send_invoice` subscriptions. It also describes disabling customer-portal payment-method management and plan switching for this workflow. After `invoice.finalized`, collect externally. **Only after external payment succeeds**, call `invoices.pay(invoiceId, { paid_out_of_band: true })`; mark paid before the due date to keep the subscription operating normally. The merchant handles external retries, cancellations, refunds, and disputes. The guide says partial payments on out-of-band invoices are unsupported and gives a Credit Note plus new-invoice workaround.

## Related pages

- [[stripe-billing-third-party]] — third-party Billing concept
- [[stripe-custom-payment-methods]] — custom payment method concept
- [[stripe-subscriptions]] — subscription concept
- [[stripe]] — company page

## Related raw API references

- [[raw/stripe-billing-subscriptions-third-party-payment-processing-2026-11-07|2026-11-07 variant index]] — navigation only; links to [own processor](https://docs.stripe.com/billing/subscriptions/third-party-payment-processing.md?process-payments-third-party=own-processor) and [out-of-band invoices](https://docs.stripe.com/billing/subscriptions/third-party-payment-processing.md?process-payments-third-party=out-of-band); variant bodies were not captured here

## Raw Sources

- [[raw/stripe-subscriptions-third-party-2026|May 2026 third-party payment processing guide]] — historical combined own-processor and out-of-band variants (1027 lines)
