---
title: "Launch a Hybrid Business Model"
type: source
date_ingested: 2026-08-05
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/pricing-packaging/billing-model-guides/hybrid-business-models.md"
raw_files:
  - "metronome/guides/pricing-packaging/billing-model-guides/hybrid-business-models-2026-07-13.md"
tags: [metronome, hybrid-pricing, subscriptions, usage-based-billing, credits, commits, alerts]
---

## Overview

This guide presents a worked hybrid SaaS model that combines recurring per-seat subscription fees with usage products funded by pooled monthly credits. Through the fictional SeatsCo example, it connects products, billable metrics, a rate card, a customer contract, subscription-linked recurring credits, balance alerts, payment-gated top-ups, and customer-facing spend controls.

## Key takeaways

- The illustrative Team plan charges per seat and grants pooled AI credits each month; unused included credits expire at month end, while a separately purchased top-up lasts one year.
- Metronome models the catalog with a subscription product, usage products backed by billable metrics, and a rate card containing both fiat subscription rates and custom-credit usage rates.
- Recurring credits or commits can be linked to a subscription. The guide says quantity increases and decreases automatically affect credit provisioning according to configured proration, while its explicit contract example configures prorated credit for a mid-month seat increase.
- Low-balance webhooks are action signals: the merchant receives the notification and decides whether to gate AI access until credits reset or a top-up is purchased.
- The top-up example adds a prepaid commit whose larger numeric priority makes it draw down after the lower-priority included credits. Its shown payment gate uses Stripe and a PaymentIntent.
- A customer experience can display the pooled balance and use an event `user_id` group key plus a spend alert for per-user controls.

## Hybrid catalog and contract

The worked model uses a Team Plan subscription product and three usage products—AI Assistant, AI Preview, and AI Summary—whose usage is tracked by billable metrics. A centralized rate card holds annual and monthly subscription rates, usage-product rates denominated in AI credits, and a conversion between the custom credit type and the rate card's fiat credit type. The page says the rate card can later be updated as subscription and usage rates evolve, but it does not define propagation or grandfathering behavior here.

The customer contract references that rate card, starts with four annual-plan seats, and creates a monthly recurring credit linked to the subscription through `subscription_config`. The example grants 100 pooled AI credits per seat and gives the recurring credit a one-period duration and priority `1`. Its `apply_seat_increase_config.is_prorated` setting prorates the extra grant when a seat is added mid-month.

Seat quantity changes are submitted through `POST /v2/contracts/edit` with positive or negative `quantity_delta` values. The prose says Metronome automatically handles credit provisioning and proration when subscription quantity changes; however, the shown recurring-credit configuration explicitly names seat increases and does not expose a corresponding seat-decrease field, so the exact removal adjustment should not be inferred from this page alone.

## Balance controls and top-ups

The guide creates `low_remaining_contract_credit_and_commit_balance_reached` at a remaining balance of 10 credits. It describes webhooks for low and depleted balances, after which the merchant can block further AI use until the monthly balance resets or the customer buys more credits. This is merchant-owned enforcement rather than evidence of automatic entitlement mutation by the alert itself.

A purchased top-up is represented in the example as a prepaid commit added through contract edit. Its access schedule grants 1,000 credits for one year, its invoice schedule charges the illustrative amount, and priority `100` places it after the included recurring credit at priority `1`. Although the prose says payment gating can use Stripe or another billing provider, the only payload shown uses `payment_gate_type: "STRIPE"`, `tax_type: "STRIPE"`, and `stripe_config.payment_type: "PAYMENT_INTENT"`; the page does not define configuration or release mechanics for other providers.

## Customer billing experience

`listCustomerBalances` is identified as the way to display the current pooled AI-credit balance inclusive of all seats. For per-user controls, usage events carry `user_id`, the relevant billable metrics define that property as a group key, and a `spend_threshold_reached` alert supplies the matching `group_values`. The resulting webhook can prompt a merchant to cut off that user or notify the user or team administrator; the source does not establish automatic enforcement or notification delivery guarantees.

## Documentation boundaries

SeatsCo, its prices, identifiers, dates, products, and thresholds are illustrative. The page combines several API examples but does not provide complete validation, error, idempotency, concurrency, retry, precision, rounding, or state-transition contracts for those endpoints. It calls the top-up commercial value “credits” while the request adds a prepaid commit, so that user-facing term should not erase the underlying object distinction. No direct contradiction with the existing Metronome subscription, credit, alert, billable-metric, or rate-card concepts was found when these claims remain scoped to this worked hybrid model.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-usage-based-billing]], [[metronome-subscriptions]], [[metronome-credits-and-commits]], [[metronome-products-and-rate-cards]], [[metronome-alerts-and-notifications]], [[metronome-billable-metrics]], [[metronome-currencies-and-custom-pricing-units]]

## Raw Sources

- [[raw/metronome/guides/pricing-packaging/billing-model-guides/hybrid-business-models-2026-07-13|2026-07-13 snapshot — hybrid subscription, pooled credits, automatic seat adjustments, alerts, top-ups, and spend controls]]
