# PayPal TypeScript Server SDK 2.5.0 ingest

Work item: `github-2d232d73cb3e8d105629`. User approved delta and a one-time focused-reading exception on 2026-09-21. Preserve older versions and immutable evidence. No commit/push authorization.

## Checklist

- [x] Read cumulative source/changelog, ten changed retained files and affected prior models; inspect meaningful source/build/support diff changes.
- [x] Verify inventories mechanically: 397 prior files (924075 bytes), 400 current files (927259 bytes); every size/hash passes. Packet, comparison, snapshot and release-note hashes pass.
- [x] Separate generated documentation: 373 model documents changed, 368 have changes confined to example sections. Read non-example additions for billing-cycle, subscription, and three new model documents. Example migration is JSON to typed TypeScript; not proof every example is correct.
- [x] Concept update first.
- [x] Cumulative source/changelog update.
- [x] Company and concept citations; preserve source count.
- [x] Comparison/contradiction check: documented local-schema constraint gap; no cross-company comparison needed.
- [x] Index and logs.
- [x] Validation and completion: five wiki pages passed; collection validation passed (117 snapshots, 102 release records, 59 comparisons, 116 work items); diff whitespace check passed. CLI marked the item ingested. No commit or push.

## Grounding

All model paths below are under `raw/github/paypal/paypal-typescript-server-sdk/snapshots/2026-09-20-790be9b/files/src/models/`.

- `subscription.ts`: `status?: SubscriptionStatus;` and `statusChangeNote?: string;`.
- `cycleFrequency.ts`: "The interval count at which the terms will be reset, this is ignored if the unit is LIFETIME."
- `orderBillingPlan.ts`: "Metadata for merchant-managed recurring billing plans. Valid only during the saved payment method token or billing agreement creation."
- `planRequest.ts`: `billingCycles: SubscriptionBillingCycle[];`.
- `cycleFrequency.ts`: `intervalCount: ['interval_count', optional(number())]`.

## Boundaries

`SubscriptionStatus` adds response typing, not a new activation flow or payment proof. `BillingCycle`/`CycleFrequency` are distinct from `SubscriptionBillingCycle`/`Frequency`. Do not advertise LIFETIME subscription-plan support. Generated frequency documentation describes default/range constraints without explicit matching checks in the retained schema. External APIMATIC behavior is not collected. Build flags are diff evidence, not build verification. Upstream contribution guidance changes do not establish a license change; LICENSE is hash-unchanged. Examples authored for the wiki are illustrative, not live API tests.
