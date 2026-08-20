---
title: "Launch a prepaid credits business model"
type: source
date_ingested: 2026-08-19
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/pricing-packaging/billing-model-guides/prepaid-credits.md"
raw_files:
  - "metronome/guides/pricing-packaging/billing-model-guides/prepaid-credits-2026-07-13.md"
tags: [metronome, prepaid-credits, payment-gating, auto-recharge, entitlements, stripe]
---

## Overview

This guide assembles a prepaid-credit business model on Metronome: customers pay before receiving usable balance, usage burns that balance down, and the merchant application controls product access. Its worked Stripe flow links customer and contract provisioning, a payment-gated commit purchase, balance alerts, an application-owned entitlement flag, automatic recharge, and customer-facing balance display. The page is architectural guidance rather than a complete API contract, and several request examples conflict internally or with the dedicated current guides.

## Key takeaways

- The model requires positive prepaid balance for access, but Metronome does not perform the application request denial shown here. The merchant stores and checks its own entitlement state, then changes that state from payment and zero-balance signals.
- In the documented manual purchase flow, Metronome initiates a Stripe payment from a contract edit. Success creates a commit that increases balance and emits a success webhook; failure is described here as voiding the commit object and emitting a failure webhook.
- A fixed product represents the prepaid purchase charge, while usage-based products and rate-card rates determine how usage consumes spend. The guide calls the commercial unit a credit but implements the purchase through `add_commits`.
- Automatic recharge is contract-scoped and asynchronous: it purchases only the difference between the threshold balance and recharge target. A failed payment disables `is_enabled`; re-enabling it after billing remediation triggers another recharge evaluation.
- `listBalances` can support a customer-facing balance view, but the page's "real time" wording provides no freshness, consistency, ordering, or latency guarantee.

## Provisioning and manual purchase flow

The merchant first creates corresponding customers in Stripe and Metronome, stores the Stripe customer ID in the Metronome billing-provider configuration, sets a default Stripe payment method, and creates a Metronome contract. The guide recommends first-of-month billing to group spend and revenue data by calendar-month boundaries even though the prepaid model does not bill usage in arrears. Before the first purchase, the merchant-owned entitlement state is false.

For an ad-hoc purchase, the merchant submits `POST /v2/contracts/edit` with `add_commits`, an access schedule, invoice schedule, priority, fixed `product_id`, and `payment_gate_type: "STRIPE"`. The page says successful payment creates the commit and prompts the merchant to set entitlement true. Its failure wording says Metronome voids the commit object. That description conflicts with the more specific manual-payment-gated-commit guide, which says the associated Metronome and Stripe invoices are voided and no commit is created; implementation should use the dedicated guide and API reference for resource-state semantics.

## Merchant-owned entitlement and alerts

The entitlement flag belongs in the merchant's own system and database so it can meet the application's access-check latency and remain available through failures between the application and Metronome. Before each protected action, the application checks that flag; after an allowed action, it sends usage to Metronome.

The guide recommends a customer balance alert at zero as the signal to set entitlement false. Its example event is `alerts.low_remaining_contract_credit_and_commit_balance_reached` and includes customer, alert, credit type, remaining balance, threshold, timestamp, and `triggered_by` fields. This is an action signal, not automatic access enforcement. The linked setup-webhooks source establishes retry and duplicate-delivery behavior, so the guide's "real-time webhook" language must not be treated as an access-cutoff latency or ordering guarantee.

## Automatic recharge and balance display

The example describes recharging from $5 back to $20 as a $15 purchase. It says recharge actions occur asynchronously from customer usage and that payment success or failure is reported by webhook. After a failure, Metronome disables the recharge configuration; the merchant prompts the customer to repair billing information and re-enables `is_enabled` to trigger another attempt.

The auto-recharge instructions are internally inconsistent about the configuration key: the prose names `threshold_billing_configuration`, while the JSON uses `credit_balance_threshold_configuration`. The dedicated prepaid-balance-threshold guide and current concept material use `prepaid_balance_threshold_configuration`. This source does not establish that the three names are aliases, so callers should verify the current create-contract schema rather than copying this payload. The sample also targets the staging API and does not state the units behind `threshold_amount: 300` and `recharge_to_amount: 2000`.

For customer display, the page calls `/v1/contracts/customerBalances/list` with customer and balance IDs plus `include_balance` and `include_contracts_balances`. The dedicated balance guide is the authority for aggregation, ledgers, fractional amounts, effective timestamps, and freshness limitations.

## Documentation cautions

> [!warning] Contradiction
> The manual purchase's access schedule sets `ending_before` to 2025-04-01 and `starting_at` to 2026-04-01, so the shown access interval ends before it begins. Although the use case says the 2,000 credits expire after one year, this payload cannot demonstrate that lifecycle. Verify corrected dates and current schedule validation before implementation.

> [!warning] Contradiction
> The auto-recharge prose names `threshold_billing_configuration`, its payload uses `credit_balance_threshold_configuration`, and the dedicated threshold guide uses `prepaid_balance_threshold_configuration`. Treat the dedicated current schema as authoritative; this page does not say these keys are aliases.

> [!warning] Commit failure wording
> This page says a failed manual purchase voids the commit object. The dedicated manual-payment-gated guide instead says the invoices are voided and no commit is created. The pre-success resource identity and state are therefore unresolved here.

The page does not define idempotency, duplicate purchase or recharge suppression, concurrent balance evaluation, webhook ordering, payment retry beyond re-enabling recharge, exact access-cutoff timing, units for the shown amounts, or read-after-write consistency. It also does not establish provider-agnostic behavior beyond the concrete Stripe examples.

## Related

- Companies: [[metronome]], [[stripe]]
- Concepts: [[metronome-credits-and-commits]], [[metronome-customers-and-contracts]], [[metronome-alerts-and-notifications]], [[metronome-webhooks]], [[metronome-integrations]]
- Related sources: [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-manual-payment-gated-commits]], [[source-metronome-guides-customers-billing-optimize-customer-experience-prepaid-balance-thresholds]], [[source-metronome-guides-customers-billing-optimize-customer-experience-get-remaining-balance]], [[source-metronome-guides-platform-configuration-setup-webhooks]], [[source-metronome-integrations-invoice-integrations-stripe]]

## Raw Sources

- [[raw/metronome/guides/pricing-packaging/billing-model-guides/prepaid-credits-2026-07-13|2026-07-13 snapshot — prepaid-credit provisioning, Stripe-gated purchase, merchant entitlement, auto-recharge, and balance display]]
