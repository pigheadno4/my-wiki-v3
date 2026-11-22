---
title: "Stripe — Orchestration: Cross-Processor Retries"
type: source
date_ingested: 2026-05-11
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/orchestration/retries"
raw_files:
  - "stripe-payments-orchestration-retries-2026-11-07.md"
  - "stripe-orchestration-retries-2026.md"
tags: [stripe, orchestration, retries, multi-processor, 3d-secure, adaptive-acceptance, radar, private-preview]
---

## Summary

The May 11 and November 7, 2026 guides describe private-preview rules that can retry eligible failed payments on a processor different from the one that made the original attempt. November adds an email request path and a registration example for `orchestration_preview`. A request asks for preview access. Rule activation is a separate step.

## Set up the retry rule

Open **Payments → Orchestration → Rules** in the Dashboard. In the rule builder add an **Action** with **Main processor** for the original attempt and **Retry processor** for the cross-processor attempt after an eligible failure. Duplicate an existing rule and edit the resulting draft. The Rules guide specifies that drafts only affect payments after activation, sandbox rules do not affect live payments, and each environment can have one active set. [[source-stripe-orchestration-rules]]

## Cross-processor retry behavior

These cases are described in both captures.

| Scenario | Documented behavior |
| --- | --- |
| 3DS was attempted on the first attempt on the main processor | If authentication fails, or succeeds but that payment attempt still fails, Orchestration skips cross-processor retry and sends `payment_intent.payment_failed`. |
| The configured retry processor lacks a required payment feature, such as Connect `on_behalf_of` | Orchestration skips that incompatible retry processor after the original attempt fails. |
| Stripe is the main processor and blocks the payment, for example through Radar | Orchestration treats the block as a decline and retries on the configured alternate, subject to retry eligibility. |
| Adaptive Acceptance enabled with Stripe as main processor | Stripe may make an additional Stripe-side attempt before the cross-processor retry. |
| Adaptive Acceptance enabled with Stripe as retry processor | Stripe may make a cross-processor retry followed by a separate Adaptive Acceptance attempt on Stripe. |

Adaptive Acceptance attempts are conditional. These branches describe retry decisions, separate from the final payment and settlement outcomes.

## Unsupported-feature validation and error protection

The feature-support guides document HTTP 400 with code `orchestration_unsupported` when the request uses an unsupported feature. The message identifies the first unsupported feature. This request validation is distinct from the `payment_intent.payment_failed` webhook in the first-attempt 3DS branch.

With opt-in error protection, Stripe can route a payment requiring an unsupported feature to Stripe instead of the otherwise selected processor. When the original processor was Stripe and the payment enters cross-processor failover, the guides say Stripe ignores error protection to avoid a duplicate Stripe attempt. The November routing guide separately checks the configured alternate for compatibility. An otherwise eligible retry can use a compatible alternate. An alternate that lacks a required feature is skipped. [[source-stripe-orchestration-feature-support]] · [[source-stripe-orchestration-route-payments]]

## Related Pages

- [[stripe-orchestration]] — Orchestration and retry decision scope
- [[source-stripe-orchestration-rules]] — Rule actions, draft and activation workflow
- [[source-stripe-orchestration-feature-support]] — Compatibility, validation errors and optional error protection
- [[source-stripe-orchestration-route-payments]] — Routing and fallback guide
- [[stripe]] — Stripe company page

## Raw Sources

- [[raw/stripe-payments-orchestration-retries-2026-11-07]] — 2026-11-07 full webpage capture (54 lines)
- [[raw/stripe-orchestration-retries-2026]] — 2026-05-11 full webpage capture (40 lines)
