---
title: "Stripe: Set Up a Credit-Based Pricing Model"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/subscriptions/usage-based/use-cases/credits-based-pricing-model"
raw_files:
  - "stripe-billing-subscriptions-usage-based-use-cases-credits-based-pricing-model-2026-11-07.md"
  - "stripe-usage-based-billing-credits-2025.md"
tags: [stripe, billing, usage-based, meters, subscriptions, pricing, credits, credit-grants]
---

## Overview

Stripe's May 5 and November 7, 2026 captures of this credit-based pricing guide describe the basic Billing Meters path: customers pre-purchase a monetary amount for eligible metered usage, with a two-meter Hypernian example, Credit Grants, balance and transaction lookups, and optional invoice funding. The November guide recommends Metronome for new usage-based integrations unless maintaining an existing Billing Meters integration. This is dated product guidance, not a statement that Billing Meters is deprecated or that an account has Metronome access. See [[stripe]] and [[stripe-usage-based-billing]].

## Key takeaways

- The Hypernian example has separate input and output token meters and monthly metered prices of 0.03 USD and 0.05 USD per token on one subscription. The May Node SDK price examples use `Decimal.from("3")` and `Decimal.from("5")`; the November curl examples use `unit_amount_decimal=3` and `=5`. These are capture-specific examples, not a general Node SDK requirement or evidence of Node SDK removal.
- In this basic Billing Meters flow, credits burn when an invoice is created at the end of the billing period. After the invoice finalizes, Stripe applies applicable billing credits and updates the grant's available balance. Customers may exceed their prepaid balance during a cycle; this guide does not describe real-time credit burndown. The November guide labels advanced usage-based billing with real-time grants a private preview.
- Billing credits apply only to subscription line items linked to meter prices, not Usage Records API items. A grant can optionally be limited to specified usage-based prices and given a priority.
- The November guide describes customer-configured Accounts v2 as generally available for Connect users and in public preview for other Stripe users. Preview participants need a preview API version; its Account creation example sets `configuration.customer` and uses `Stripe-Version: 2026-10-28.preview`. The guide recommends customer-configured Accounts for most use cases, while also retaining Customers v1 examples. This capture does not establish an individual account's preview access.
- In the November API examples, Credit Grant, Subscription, Credit Balance Summary, Credit Balance Transaction, invoice and invoice-item requests use `customer_account` for Accounts v2 versus `customer` for Customers v1. The May guide had a generic customer-configured Account substitution note but showed Node Customer examples.
- The guide permits available-balance lookup and custom-period meter-event summaries. Because meter events process asynchronously, summaries and upcoming invoices may lag; these lookups are not a live, reconciled mid-cycle credit balance.

> [!warning] Contradiction
> Both captures say credits apply "indiscriminately across meters," while their grant setup permits optional Eligibility limited to selected usage-based prices. The broad example must not be read as an unconditional all-meter guarantee.

> [!warning] Contradiction
> The November comparison says basic Billing Meters users cannot see live credit balances or usage totals mid-cycle, but later sections provide balance lookup and custom-period usage summaries. Read the comparison as a lack of real-time reconciliation, not an absence of any mid-cycle query.

> [!warning] Contradiction
> The November event-summary prose says to pass an Account ID to its `customer` parameter for customer-configured Accounts, yet its curl example retains `CUSTOMER_ID`. Its meter-event example likewise uses `CUSTOMER_ID` with no Accounts v2-specific payload example. These examples do not prove an Account-based meter-event payload shape.

## Detail locators

- Meters, optional dimensions, Hypernian prices and subscription: November raw lines 43–160, 272–315; May raw lines 25–183, 261–302.
- Customer identity and preview scope: November raw lines 163–215, including the preview header at 193–206; May raw lines 185–209.
- Grant configuration, optional Eligibility and timing: November raw lines 218–269, 373–381; May raw lines 211–259, 369–377.
- Meter events and asynchronous invoice preview: November raw lines 317–370; May raw lines 304–366.
- Balance and transaction API route pairs: November raw lines 383–441; May raw lines 379–429.
- Optional funding: create a one-off invoice and invoice item, then listen for `invoice.paid` before granting credits. The November Accounts v2 examples show invoice and item creation, while only the Customers v1 example shows finalization; that omission does not prove a different finalization rule. See November raw lines 444–500 and May raw lines 432–478.
- Custom-period meter-event summary and Account-ID wording: November raw lines 502–516; May raw lines 480–501.
- The May capture contains Node SDK examples, including `Decimal.from("1000")` for an invoice item. The November capture uses curl. See the pinned raw for exact request examples; neither capture is an executed payment or invoice result.

## Related

- [[stripe-usage-based-billing]] — basic Billing Meters concepts and related source routes
- [[source-stripe-usage-based-billing-credits-overview]] — Billing Credits eligibility and grant lifecycle
- [[source-stripe-usage-based-billing-credits-setup]] — broader Credit Grant setup

## Raw Sources

- [[raw/stripe-billing-subscriptions-usage-based-use-cases-credits-based-pricing-model-2026-11-07|Stripe credit-based pricing guide, captured 2026-11-07]]
- [[raw/stripe-usage-based-billing-credits-2025|Stripe credit-based pricing guide, captured 2026-05-05]]
