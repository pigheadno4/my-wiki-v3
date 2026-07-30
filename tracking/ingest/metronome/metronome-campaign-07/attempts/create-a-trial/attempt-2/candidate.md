---
title: "Metronome Create a Free Trial"
type: source
date_ingested: 2026-07-30
canonical_url: "https://docs.metronome.com/guides/pricing-packaging/billing-model-guides/create-a-trial"
original_format: webpage
raw_files:
  - "metronome/guides/pricing-packaging/billing-model-guides/create-a-trial-2026-07-13.md"
tags: [metronome, free-trials, usage-based-billing, credits, contracts, alerts, overrides]
---

## Overview

This guide presents two Metronome contract configurations for a one-week usage-based free trial. A capped path combines time-bound credits, optional entitlement overrides, and a credit-balance alert; an uncapped path applies a time-bound zero-price multiplier and can use the same entitlement-override pattern. These are worked examples for trial pricing and signaling, not a complete contract, alert, webhook, or product-access specification.

## Key takeaways

- The capped example grants up to $100 of usage for one week, then treats either credit depletion or expiration as the end of the trial.
- Its contract credit uses a fixed credit product, an access schedule aligned to the trial window, and priority `1`; leaving applicable products and tags blank makes the credit track all customer usage.
- Product availability is separate from credit applicability. A time-bound `entitled: false` override can mark selected products or tags unavailable, but the merchant's product must read and enforce that override.
- After the credit is depleted or expires, later usage is rated and charged in arrears at list pricing unless the merchant uses the alert signal to change access.
- A customer-scoped **Contract credit balance** alert at $0 can send a webhook when the trial balance is exhausted or expires; the documented merchant actions include notifying the customer, disabling access, or re-enabling the full feature set.
- The uncapped example applies a one-week multiplier of `0` to selected products or tags. When the override ends, subsequent usage is automatically charged in arrears at list prices.

## Credit-based free trial

### Contract and credit schedule

The example starts from an existing customer and rate card, then creates a contract with its own name, term, and billing frequency. The displayed API request keeps the contract active for one year while limiting the trial credit and entitlement overrides to the first week, so the trial window is a time-bounded part of a longer commercial contract rather than the contract's entire term.

The credit is associated with a fixed product named **Trial credits**. In the app flow, that product's name is customer-visible while the optional description is internal metadata. Leaving **Applicable products** and **Applicable tags** blank makes the grant track all customer usage. Its access schedule starts with the contract, ends before the one-week boundary, and carries a $100 amount; the API example represents that amount as `10000`. The guide recommends a lower numeric priority than other grants and uses priority `1` so the trial credit is consumed first.

### Product access and trial completion

The guide scopes trial feature access independently with an optional entitlement override. Its example disables products tagged **Fine tuning** and **Images modeled** from the contract start through the end of the trial week. Metronome exposes the override for the merchant's product to read; this page does not claim that Metronome itself blocks those features.

Metronome can expose real-time usage through a customer usage dashboard. Once the $100 grant is fully spent, or once the week passes and the grant expires, subsequent usage is rated and charged in arrears using the contract's list pricing and billing frequency. Consequently, credit exhaustion is not itself documented as a billing stop: the merchant may instead use the notification below to disable access or ask the customer to upgrade.

### Alert definition and webhook delivery

The worked alert is customer-scoped to **AcmeCorp**, uses type **Contract credit balance**, and sets the threshold to **reaches $0 USD**. The guide says this alert can signal either usage exhaustion or credit expiration. It is a signal for merchant-owned action, such as sending an email, disabling product access until purchase, or re-enabling the broader feature set after trial completion; Metronome is not documented as performing those product actions itself.

Webhook delivery is a separate integration concern. A configured endpoint receives an example notification with type `alerts.low_remaining_contract_credit_and_commit_balance_reached` and properties `customer_id`, `alert_id`, `threshold`, `alert_name`, `credit_type_id`, `remaining_balance`, and `triggered_by`; the displayed payload has `remaining_balance: 0` and `triggered_by: "usage"`.

## Uncapped free trial

The uncapped configuration replaces the capped credit with a time-bound contract price override. It targets the products or product tags offered in the trial, aligns the override with the one-week window, and applies a multiplier of `0`; the API example targets **Language models**. An optional separate `entitled: false` override can disable excluded product tags during that same window.

After the zero-multiplier override expires, the longer-lived contract remains and subsequent usage is charged in arrears at list prices. The page describes that outcome as an automatic transition to paid usage, but it does not document a distinct subscription-state or customer-state transition.

## Documentation boundaries

- The one-week and $100 values are example terms, not documented platform minima, maxima, or defaults.
- The app labels the credit as $100 while the request uses `amount: 10000`; this page does not define monetary denomination or precision, so the dedicated API schema remains authoritative.
- The guide does not provide the complete contract or alert request schemas, authentication, idempotency, validation errors, alert aggregation rules, or precedence for overlapping credits, commits, rates, and overrides.
- The alert instructions identify a customer and show `credit_type_id` in the payload, but do not explain whether the $0 threshold aggregates other contract balances or isolates the trial credit, or whether `triggered_by` distinguishes expiration from usage when expiration or simultaneous triggers occur.
- Although the guide uses the phrase "real-time" for the end-of-trial notification, it defines no specific evaluation or delivery latency guarantee.
- The example webhook body does not define delivery retry, ordering, deduplication, or signature-verification behavior; use the dedicated webhook guide for those mechanics.
- Neither path documents payment-method collection, billing-provider setup, failed payment handling, tax, invoice finalization, proration, conversion consent, or an account/subscription lifecycle. The uncapped path's paid conversion is the expiry of a pricing override, and the capped path may charge subsequent usage unless the merchant changes access.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-customers-and-contracts]], [[metronome-credits-and-commits]], [[metronome-products-and-rate-cards]], [[metronome-alerts-and-notifications]], [[metronome-webhooks]], [[metronome-usage-based-billing]]
- Related sources: [[source-metronome-api-reference-contracts-create-a-contract]], [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-create-a-pre-paid-commit]], [[source-metronome-guides-platform-configuration-setup-webhooks]]

## Raw Sources

- [[raw/metronome/guides/pricing-packaging/billing-model-guides/create-a-trial-2026-07-13|2026-07-13 snapshot — capped and uncapped usage-based trial configurations]]
