---
title: "Manage contract lifecycle transitions"
type: source
review_level: mechanical
date_ingested: 2026-08-04
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/customers-billing/manage-customers/manage-customer-lifecycle.md"
raw_files:
  - "metronome/guides/customers-billing/manage-customers/manage-customer-lifecycle-2026-07-13.md"
tags: [metronome, contracts, contract-lifecycle, enterprise-commitments, entitlements, renewals]
---

## Overview

This guide uses a Moogle example to show Metronome contract lifecycle transitions across enterprise provisioning, mid-term add-ons, renewal, and early termination. It presents contract terms, pricing, schedules, commitments, entitlement checks, and audit visibility as parts of lifecycle management. The page illustrates the flows with /contracts/create, /v2/contracts/edit, /contracts/get, and /contracts/updateEndDate examples; it does not define complete endpoint contracts.

## Key takeaways

- An enterprise setup sequences billable metrics, products, a rate card, a downstream invoice provider, a customer, and a contract. The guide says /contracts/get can confirm an active contract before Product A access is allowed.
- For a mid-term Product B add-on, the rate card's default entitlement is set to false; the existing contract is edited to make entitlement true on October 1, add a Product-B-only prepaid commit, and apply a 20% discount.
- Renewal is shown as a new contract with transition.type: renewal linked to the prior contract. The example rolls remaining Product A prepaid value forward and burns it before the new Product A/Product B commit.
- To end early, schedule the contract end date and use a low-commit-balance alert webhook to tell the merchant entitlement system to gate access. The example says the prepaid renewal commit was invoiced at start and the remaining balance reaches $0.00 at the end date.
- Numeric amount values in request examples are not given a denomination by the page; verify the examples against the current API schema.

## Details

### Enterprise contract motion

The guide says enterprise terms may include special access to non-public products, SKU-level discounts, and prepaid or postpaid commitments. Its Moogle example is a one-year Product A contract beginning January 1, 2025 with a $100,000 prepaid commitment and a 10% discount from Product A's standard list price. The setup sequence is to configure billable metrics, create SKU products, set up a rate card, connect a downstream invoice provider such as Stripe, create the customer, and create the associated contract.

The /contracts/create example includes a rate card, start and end dates, a prepaid commit with separate access and invoice schedules, a rollover fraction, a priority, product applicability, and an entitled multiplier override. After creation, the guide recommends /contracts/get to confirm that Moogle's contract is active before allowing Product A use.

### Mid-term add-on

For a Product B beta launch on October 1, 2025, the guide sets Product B's rate-card entitlement to false by default so only customers with access to Product B are charged for its usage. It then edits the existing Moogle contract to set Product B entitlement true on that date, add a $10,000 prepaid commit scoped only to Product B usage, and override Product B's list rate with a 20% discount. The worked request uses /v2/contracts/edit.

### Renewal transition

In the December 1, 2025 scenario, Moogle renews for another year beginning January 1, 2026. The guide instructs the caller to create a new contract with transition type renewal linked to the previous contract, add a $200,000 prepaid commitment covering Products A and B, and send one $200,000 invoice on the start date. Because the original $100,000 Product A commitment has $10,000 remaining and a 50% rollover setting, the example says all $10,000 rolls to the new contract. The new contract therefore has a Product-A-only rollover commit that burns down before the new Product A/Product B commit.

### Ending a contract

The guide frames early termination as both meeting the contract's financial obligations and gating product access. For the Moogle example, the renewed contract ends on March 1, 2026 through /contracts/updateEndDate. The recommended access-control pattern is an alert webhook when a commit reaches a low balance of $0.00, with the merchant's entitlement system listening and immediately gating access. The guide says the $200,000 prepaid commit was already invoiced at contract start and that the remaining prepaid balance reaches $0.00 on March 1.

### Scope and unknowns

The page does not provide response bodies, validation rules, error behavior, idempotency, retry behavior, concurrency semantics, or alert payload and delivery guarantees for these examples. It also does not explain the denomination of numeric amount fields in the request snippets, a general rollover algorithm beyond the Moogle scenario, or whether Metronome itself enforces product access rather than signaling the merchant's entitlement system. The general end-motion description refers to remaining financial obligations, while the worked prepaid example says the commitment was invoiced at contract start; no separate early-end invoice calculation or reconciliation is specified.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-customers-and-contracts]], [[metronome-credits-and-commits]], [[metronome-products-and-rate-cards]], [[metronome-alerts-and-notifications]], [[metronome-invoicing]]
- Related sources: [[source-metronome-guides-pricing-packaging-billing-model-guides-enterprise-commit]], [[source-metronome-api-reference-contracts-create-a-contract]], [[source-metronome-guides-customers-billing-manage-customers-manage-product-access]], [[source-metronome-guides-customers-billing-set-up-notifications-create-and-manage-notifications]]

## Raw Sources

- [[raw/metronome/guides/customers-billing/manage-customers/manage-customer-lifecycle-2026-07-13|2026-07-13 snapshot — contract lifecycle transitions, enterprise add-ons, renewals, and end-of-contract gating]]
