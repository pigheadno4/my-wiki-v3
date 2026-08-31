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

The refreshed contract-edit schema exposes feature-gated Stripe `payment_gate_config` when adding a subscription. A subscription-linked recurring commit or credit can choose `BILLING_PERIOD_PAID`, which releases each child balance after payment for that billing period, or `INITIAL_BILLING_PERIOD_PAID_ONLY`, which releases all child balances after the first payment. The page does not define payment-state authority, failure and retry behavior, pending-balance visibility, revocation, concurrency, or Stripe reconciliation. [[source-metronome-api-reference-contracts-edit-a-contract]]

> [!warning] Documentation contradiction
> The provisioning guide names the unassigned-seat field `initial_unassigned_seats_quantity`, while the dedicated create-contract schema from the same 2026-07-13 collection names it `initial_unassigned_seats`. Neither source establishes which spelling is current runtime truth; verify the live schema before implementation.

> [!warning] Terminology mismatch
> The overview and lifecycle guides use `entitlement` in prose, while rate-card examples and existing API context use `entitled`. These sources do not establish that both names are valid schema fields.

## Lifecycle

The dedicated seat-balance read is `POST /v1/contracts/seatBalances/list`. It scopes one customer's contract and can filter seats by `SEAT_BASED` subscription UUIDs or stable seat IDs; a subscription ID not mapped to a seat-based subscription is documented as an error. Missing seat IDs fail by default or are silently omitted when `skip_missing_seat_ids` is true. Results group current and initial combined credit/commit balance by seat and credit type. Optional credit, commit, and nested ledger details are sibling seat expansions whose item schemas omit `credit_type_id`, so the response alone cannot attribute them to a particular balance entry or prove their reconciliation. The page also does not define read-after-seat-change visibility, ordering, snapshot consistency, freshness, or reconciliation with subscription quantity and seat histories. [[source-metronome-api-reference-credits-and-commits-list-seat-balances]]

Seat management after contract creation has two modes. Aggregate subscriptions and shared credit pools use `update_subscription` with either total `quantity` or `quantity_delta`; equal-`starting_at` aggregate updates apply in submission order, and invoice plus recurring-credit effects follow configured proration and `access_amount`. Seat-based credit subscriptions instead add or remove stable `seat_ids` and can add or remove unassigned capacity. Reassignment without changing total quantity removes the old identity and adds one unassigned seat, leaving capacity available for a later assignee. The guide does not extend aggregate same-time ordering to seat updates or define proration calculations, rounding, atomicity, errors, or recovery. [[source-metronome-guides-pricing-packaging-subscription-manage-seats]]

Bearer-authenticated `POST /v1/contracts/getSubscriptionSeatsHistory` reads effective-dated seat-schedule segments for one UUID subscription inside an identified customer contract. `covering_date` selects the segment active at a point and is mutually exclusive with `starting_at` and `ending_before`; range filters can leave either side unbounded. Each returned segment directly carries `starting_at`, nullable `ending_before`, total assigned-plus-unassigned quantity, and assigned seat IDs. Results are ordered by `starting_at` and paged at at most 10 entries through body `cursor` and sibling `next_page`, but direction, ties, cursor stability, snapshot consistency, retention, and exhaustive-history guarantees are undefined. The page does not say whether future scheduled seat segments are included, so the separate quantity-history endpoint's future-exclusion rule must not be generalized. [[source-metronome-api-reference-contracts-get-subscription-seats-history]]

- Metronome's subscription quantity-history endpoint returns historical quantities and prices for customer-facing seat-count history, but excludes future scheduled quantity changes; those future changes must be retrieved through `getContract`.
- A subscription rate-card price change reaches inheriting contracts in the next billing period; a contract overwrite retains its assigned price.
- A sub-cycle trial can use consecutive subscriptions with a time-bounded `$0` override on the first. A full-cycle trial can use one `$0` override that expires before list pricing applies in the next period.
- Add-ons use `add_subscription`. The guide recommends renewal transitions for upgrades and downgrades, with proration only for upgrades and next-period effect for downgrades.
- Most cancellations should end the contract, and a later restart should create a new contract. If cancellation is performed by moving a hybrid subscription's end date, its recurring credit must also be ended separately; the source does not say whether ending the entire contract does this automatically.
- Once the latest service period is finalized, changing a contract end date does not extend an in-advance subscription; future service then requires a new subscription.

The lifecycle page labels one operation as create-contract guidance while linking to edit-contract documentation. Endpoint choice should therefore be verified against the current API.

## Sources

- [[source-metronome-api-reference-contracts-get-subscription-seats-history]] - contract-scoped seat-assignment and total-capacity schedule history, covering-date and range selection, ordered pagination, and future-state and snapshot-completeness unknowns
- [[source-metronome-api-reference-contracts-edit-a-contract]] - feature-gated subscription payment configuration and recurring child-balance release policies

- [[source-metronome-guides-pricing-packaging-subscription-manage-seats]] — aggregate and identity-bearing seat updates, unassigned-seat reassignment, configuration-dependent proration, and seat history and balance routes

- [[source-metronome-api-reference-contracts-get-subscription-quantity-history]] — historical subscription quantities and prices, seat-count presentation, response structure, and the future-change boundary
- [[source-metronome-guides-pricing-packaging-subscription-provision-your-customer]] - contract subscription fields, charging gate, billing-cycle configuration, pooled and individual seat-credit provisioning, and the unassigned-seat field contradiction

- [[source-metronome-guides-pricing-packaging-subscription-subscription-overview]] — subscription object model, quantity, collection direction, and credit scope
- [[source-metronome-guides-pricing-packaging-subscription-define-subscription-pricing]] — per-offering products, quantity-one rates, seat key, and multi-rate recommendation
- [[source-metronome-guides-pricing-packaging-subscription-manage-subscription-lifecycle]] — price propagation, trials, transitions, proration, and cancellation boundaries

- [[source-metronome-api-reference-credits-and-commits-list-seat-balances]] - seat-based subscription and seat filtering, missing-seat semantics, balance identity, sibling detail expansions without credit-type attribution, and visibility unknowns

## Related

- [[metronome-products-and-rate-cards]]
- [[metronome-customers-and-contracts]]
- [[metronome-credits-and-commits]]
- [[metronome-usage-based-billing]]
