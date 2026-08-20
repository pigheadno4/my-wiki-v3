---
title: "Metronome Subscriptions"
type: concept
category: technology
tags: [metronome, subscriptions, rate-cards, contracts]
---

## Definition

Metronome models a subscription as a recurring-fee product priced on a rate card and activated through a customer contract. The subscription guides divide responsibility among the product and rate, contract-level quantity and credits, and later lifecycle operations.

The provisioning guide distinguishes three configurations. A standard subscription charges a recurring fee and treats usage as either included or separately paid in arrears. A seat-based credit pool grants shared usage balance with contract-level overages, while individual-seat credits grant seat-scoped balance with contract-level overages.

## Pricing and provisioning

- Create one subscription product per offering. A rate-card rate represents the list price for quantity `1`; the contract later supplies quantity, proration, collection direction, and associated credits.
- One subscription product can have separate rates for different billing frequencies. When a rate card contains multiple subscription rates, the pricing guide recommends defaulting those rates to `false` and enabling the applicable rate or rates during contract provisioning; it does not define exclusivity or multi-rate resolution.
- In a seat-based credit model, applicable usage products need a `seat_id` presentation group key so usage can be associated with the relevant product and seat.
- Subscription credits can be pooled for the subscription or scoped per seat. Their grant schedule, drawdown, and transition mechanics require dedicated credit sources.

Contract provisioning uses a `subscriptions` config for each subscription. The config selects the rate by `billing_frequency` and `product_id`, sets advance or arrears collection, supplies initial quantity, and defines proration and invoice timing for mid-period changes. Metronome charges the subscription only when that config exists and its associated rate is enabled; an override must identify both billing frequency and product because one product can map to several rates. For advance subscriptions, `billing_cycle_config.anchor_date` may decouple the subscription cycle from the contract usage-invoice anchor.

A shared seat-credit pool links the subscription to a recurring credit by a temporary subscription identifier. Each period grants shared balance equal to `access_amount` per seat, and newly added seats release additional shared balance according to proration. For individual-seat credits, the streaming metric must define the seat group key before creation, applicable usage products use it as a presentation group key, every event carries a stable unique seat identifier, and the subscription uses `quantity_management_mode: SEAT_BASED` with seat configuration. The guide documents default support for up to 1,000 individual-credit seats and directs larger cases to Metronome.

> [!warning] Documentation contradiction
> The provisioning guide names the unassigned-seat field `initial_unassigned_seats_quantity`, while the dedicated create-contract schema from the same 2026-07-13 collection names it `initial_unassigned_seats`. Neither source establishes which spelling is current runtime truth; verify the live schema before implementation.

> [!warning] Terminology mismatch
> The overview and lifecycle guides use `entitlement` in prose, while rate-card examples and existing API context use `entitled`. These sources do not establish that both names are valid schema fields.

## Lifecycle

- A subscription rate-card price change reaches inheriting contracts in the next billing period; a contract overwrite retains its assigned price.
- A sub-cycle trial can use consecutive subscriptions with a time-bounded `$0` override on the first. A full-cycle trial can use one `$0` override that expires before list pricing applies in the next period.
- Add-ons use `add_subscription`. The guide recommends renewal transitions for upgrades and downgrades, with proration only for upgrades and next-period effect for downgrades.
- Most cancellations should end the contract, and a later restart should create a new contract. If cancellation is performed by moving a hybrid subscription's end date, its recurring credit must also be ended separately; the source does not say whether ending the entire contract does this automatically.
- Once the latest service period is finalized, changing a contract end date does not extend an in-advance subscription; future service then requires a new subscription.

The lifecycle page labels one operation as create-contract guidance while linking to edit-contract documentation. Endpoint choice should therefore be verified against the current API.

## Sources

- [[source-metronome-guides-pricing-packaging-subscription-provision-your-customer]] - contract subscription fields, charging gate, billing-cycle configuration, pooled and individual seat-credit provisioning, and the unassigned-seat field contradiction

- [[source-metronome-guides-pricing-packaging-subscription-subscription-overview]] — subscription object model, quantity, collection direction, and credit scope
- [[source-metronome-guides-pricing-packaging-subscription-define-subscription-pricing]] — per-offering products, quantity-one rates, seat key, and multi-rate recommendation
- [[source-metronome-guides-pricing-packaging-subscription-manage-subscription-lifecycle]] — price propagation, trials, transitions, proration, and cancellation boundaries

## Related

- [[metronome-products-and-rate-cards]]
- [[metronome-customers-and-contracts]]
- [[metronome-credits-and-commits]]
- [[metronome-usage-based-billing]]
