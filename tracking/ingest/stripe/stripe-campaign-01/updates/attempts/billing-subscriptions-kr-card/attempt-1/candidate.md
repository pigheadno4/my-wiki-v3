---
title: "Stripe Subscriptions — Set Up South Korean Card (KR Card) Subscription"
type: source
date_ingested: 2026-11-08
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/subscriptions/kr-card"
raw_files:
  - "stripe-subscriptions-kr-card-2026.md"
tags: [stripe, billing, subscriptions, kr-card, south-korea, krw, setup-intents, mandate]
---

## Overview

Stripe's 2026-05-13 capture explains three `kr_card` subscription integration variants: SetupIntents, direct Subscriptions API with PaymentIntent confirmation, and a Stripe-hosted Checkout page. Its SetupIntents section says prices must be converted to KRW for this method. The 100,000 KRW monthly stock-photo subscription is an example, not a minimum or universal price. See [[stripe]] and [[stripe-korea-payment-methods]].

The 2026-11-07 capture at the same URL contains only a title and links to the three query-parameter variants. It supplies navigation, not evidence that the May flows were removed, deprecated, or still unchanged in their current variant pages. The current contents of those variants need separately pinned captures before making current behavior claims.

## May 2026 integration paths

| Variant | Steps shown in the May capture |
| --- | --- |
| SetupIntents API | Server creates and confirms a SetupIntent to save a `kr_card` payment method. Its `client_secret` goes to Stripe.js for customer redirect to the local processor and mandate authorization. A later server-side subscription creation uses the SetupIntent response's PaymentMethod ID as `default_payment_method`. |
| Subscriptions API | Server creates a subscription using `payment_behavior=default_incomplete` and `payment_settings.save_default_payment_method=on_subscription` in the example, expands `latest_invoice.payments` and `latest_invoice.confirmation_secret`, then confirms a PaymentIntent. The client can receive the confirmation secret; `requires_action` calls for local-processor authentication. |
| Stripe-hosted Checkout | Server creates a `subscription`-mode Checkout Session; the example lists `card` and `kr_card` and redirects the customer to the returned URL. The guide says the customer must authorize future use and describes a successful test transition from `requires_action` to `succeeded`. |

The SetupIntents command includes `usage=off_session`, `mandate_data`, and a later subscription example includes `off_session: true`. The Subscriptions API confirmation command also includes `mandate_data`. These are path-specific examples in the May capture; the captured prose does not establish them as universal requirements across all three paths. The hosted Checkout example does not show those parameters. See May raw lines 34–72, 115–156, and 182–210.

> [!warning] Contradiction
> The May SetupIntents opening says its first API call creates a Subscription and PaymentIntent, but the following heading, command, and explanation show a SetupIntent before subscription creation (May lines 12 and 34–56). Follow the concrete path as dated example evidence; the capture does not resolve the opening sentence.

> [!warning] Contradiction
> Both May direct-confirm sections say in prose to set `payment_method_types` to `kr_card` (lines 79 and 143), while their PaymentIntent confirmation commands use `payment_method_data` fields (lines 81–87 and 145–154). These passages do not establish one universal required confirmation parameter. The November index cannot resolve the discrepancy.

A `requires_action` response means customer authentication remains; it is not proof of payment success. The May text describes an active subscription **after successful payment**. The SetupIntents redirect passage does not itself guarantee a `succeeded` SetupIntent before the later subscription call. No account eligibility, local-processor completion, or recurring-payment outcome was verified from these captures.

## Detail locators

- May raw lines 14–32: product/price setup and KRW statement.
- May raw lines 34–89: SetupIntent, Stripe.js redirect, subscription example, and confirmation discrepancy.
- May raw lines 91–156: direct subscription and PaymentIntent confirmation example.
- May raw lines 158–214: hosted Checkout example and successful test case.

## Related

- [[stripe-korea-payment-methods]] — Korean payment-method concept
- [[stripe-subscriptions]] — broader subscription concept

## Related raw API references

- [[raw/stripe-billing-subscriptions-kr-card-2026-11-07|2026-11-07 variant index: SetupIntents, Subscriptions API, and hosted Checkout]] — navigation only; variant contents were not captured here.

## Raw Sources

- [[raw/stripe-subscriptions-kr-card-2026|KR card subscription variants, captured 2026-05-13]]
