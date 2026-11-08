---
title: "Stripe Subscriptions — Set Up Naver Pay Subscription"
type: source
date_ingested: 2026-11-08
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/subscriptions/naver-pay"
raw_files:
  - "stripe-subscriptions-naver-pay-2026.md"
tags: [stripe, billing, subscriptions, naver-pay, south-korea, krw, setup-intents, mandate]
---

## Summary

The 2026-05-13 capture is a full Naver Pay subscription guide with SetupIntents-labeled, Subscriptions API, and Stripe-hosted Checkout variants. It uses an illustrative 100,000 KRW monthly price and expressly says to convert prices to KRW for this payment method (old lines 10–34, 93–216). Its examples place parameters on different requests and do not establish one universal field list.

The 2026-11-07 capture at the same canonical URL is **a variant index only** (new lines 5–15). It supplies three navigation links, without a currency rule, current request schema, state transition, eligibility, or deprecation statement. Omission of the old detailed guide from this capture is not evidence that those paths or rules were withdrawn.

## May 2026 guide: SetupIntents-labeled variant

The concrete steps show a server-side SetupIntent-create example with `payment_method_data[type]=naver_pay`, `payment_method_types[]=naver_pay`, `usage=off_session`, and online `mandate_data.customer_acceptance` fields (old lines 36–52). The guide says the SetupIntent `client_secret` is passed to Stripe.js client-side to redirect the buyer to Naver Pay for mandate authorization (old line 54). A subsequent subscription-create example uses the SetupIntent response's PaymentMethod ID as `default_payment_method` and includes `off_session: true` **on that subscription request** (old lines 56–75). The guide's prose does not separately state that the shown `off_session` field is universally required. It also does not specify a `SetupIntent succeeded` check in this section. Do not infer a transition or universal implementation contract from the sample.

The section is internally inconsistent: its introduction says a first call creates a Subscription and PaymentIntent (old line 14), while its concrete steps create a SetupIntent first and then a subscription (old lines 36–75). Its PaymentIntent-confirm paragraph says to set `payment_method_types=naver_pay`, but the shown command uses unusual `payment_method_data[]` fields (old lines 79–89). The conflicting prose and sample have not been reconciled or executed.

The guide describes `requires_action` as a customer-completion step and says the subscription becomes Active and saves the default method **after successful payment** (old lines 77, 91). It does not prove any actual mandate or payment.

## May 2026 guide: Subscriptions API variant

The direct path describes creating an `incomplete` subscription with `payment_behavior=default_incomplete`, `payment_settings.save_default_payment_method=on_subscription`, and expansions for first-invoice payment and confirmation-secret data (old lines 117–141). Its PaymentIntent-confirm example has `payment_method_data[type]=naver_pay`, a return URL, and online `mandate_data` (old lines 143–156). The surrounding prose instead tells the reader to set `payment_method_types`; that prose/example mismatch remains unresolved and does not establish a runnable request contract.

A `requires_action` response calls for customer authentication with Naver Pay. The guide says the subscription becomes Active and saves the default payment method **after a successful payment** (old line 158). Authentication initiation alone does not prove payment success, and an Active label is not independent evidence of settlement or future recurring charge success.

## May 2026 guide: Stripe-hosted Checkout variant

The guide uses a Checkout Session in `subscription` mode with a recurring price and example `payment_method_types` containing `card` and `naver_pay` (old lines 160–211). It says the customer authorizes future use of Naver Pay through Checkout (old lines 184–186). The test paragraph describes a successful sandbox authentication case changing the PaymentIntent from `requires_action` to `succeeded` (old lines 214–216). It is a test path, not evidence of a live payment or bank receipt.

The Checkout sample does not show the SetupIntent-path `usage=off_session` or subscription-create `off_session=true`, or the direct confirm-path `mandate_data`. Their absence from that sample proves neither a prohibition nor a default.

## Scope and unresolved verification

The May capture's KRW instruction is dated evidence, and the November index does not independently confirm current currency scope or merchant eligibility. Neither capture demonstrates a completed mandate, live first charge, settlement, or successful future off-session payment.

The three November variant targets were not read for this source update. Their current client/server sequence, parameter requirements, payment states, and eligibility need path-specific evidence. Comparisons to [[source-stripe-subscriptions-kakao-pay]] and [[source-stripe-subscriptions-kr-card]] are limited here to the **three-path organization** observed for Naver Pay; identical parameter and eligibility rules are not established by this capture.

## Related pages

- [[stripe-korea-payment-methods]] — Korea payment-method concept
- [[stripe-subscriptions]] — subscription context
- [[stripe]] — company page

## Related raw API references

The 2026-11-07 [[raw/stripe-billing-subscriptions-naver-pay-2026-11-07|Naver Pay variant index]] points to these **unread** variant URLs for separate collection. It is navigation only and is not included in factual `raw_files` provenance:

- [SetupIntents API variant](https://docs.stripe.com/billing/subscriptions/naver-pay.md?api-integration=setupintents)
- [Subscriptions API variant](https://docs.stripe.com/billing/subscriptions/naver-pay.md?api-integration=subscription)
- [Stripe-hosted page variant](https://docs.stripe.com/billing/subscriptions/naver-pay.md?api-integration=checkout)

## Raw Sources

- [[raw/stripe-subscriptions-naver-pay-2026|2026-05-13 full Naver Pay subscription guide]]
