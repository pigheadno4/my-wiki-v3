---
title: "Stripe: Set Up a Pay-As-You-Go Pricing Model"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/subscriptions/usage-based/implementation-guide"
raw_files:
  - "stripe-billing-subscriptions-usage-based-implementation-guide-2026-11-07.md"
  - "stripe-usage-based-billing-payg-2025.md"
tags: [stripe, billing, usage-based, meters, subscriptions, pricing, pay-as-you-go]
---

## Overview

Stripe's guide describes a basic pay-as-you-go **Billing Meters** workflow: create a meter and metered price, create a customer and subscription, report meter events, preview an invoice, and optionally query usage summaries. Its Hypernian rate of 0.04 USD per 100 tokens is a fictional example, not an executed billing result. The Billing Meters examples use `/v1/billing/meters`, `/v1/prices`, `/v1/subscriptions`, and `/v1/billing/meter_events`; the separate customer-configured Account example uses `/v2/core/accounts`.

> [!warning] 2026-11-07 guide scope
> Stripe now directs **new** usage-based integrations, including users adding metering to existing flat-rate subscriptions, to Metronome instead of this basic Billing Meters guide. Existing Billing Meters integrations need not migrate and may continue using this guide. This captured recommendation does not establish deprecation, forced migration, merchant-specific Metronome access, or a successful payment or tax outcome.

## Key takeaways

- **Meter and price:** A meter aggregates reported events; the Hypernian example uses `sum` for tokens. The metered monthly price attaches the meter through `recurring.meter` and applies a per-package transform of 100 units. Dashboard choices also include `count` and `last` aggregation, and per-unit or per-tier pricing. See the meter and price steps in the November raw at lines 49–124.
- **Customer object:** The 2026-05-05 capture offered a one-sentence Accounts v2 alternative to a Customer. The November capture provides separate customer-configured Account and Customers v1 creation examples. It says Accounts v2 is generally available for Connect users and in public preview for other Stripe users; preview participants need a preview version. This does not verify any particular account's access. See November lines 126–179.
- **Subscription:** The November Accounts v2 example creates a `/v1/subscriptions` subscription with `customer_account`; the Customers v1 example uses `customer` (lines 181–222). For `billing_mode=flexible`, Stripe excludes metered lines from the first invoice when there is no prior usage, but creates an invoice for a backdated subscription with accrued usage or pending invoice items. `billing_mode=classic` generates a zero monetary value line for each metered item (November line 191; May line 153). Neither capture recommends flexible mode.
- **Meter event:** The November `/v1/billing/meter_events` curl example sends `payload[stripe_customer_id]={{CUSTOMER_ID}}` and `payload[value]=25`. The May Node example represented `value` as the string `"25"`; that example does not establish a universal string-only payload rule. The November guide does not explain the exact meter-event identifier mapping for its customer-configured Account example, so that mapping needs separate authority. See November lines 224–249 and May lines 183–214.
- **Preview and summaries:** The guide shows a preview invoice by subscription ID and an optional meter-event summary for a custom time window. Meter events process asynchronously, so upcoming invoice previews and summaries may lag recently received events. For customer-configured Accounts, the November summary instructions say to pass the Account ID to the `customer` parameter. These previews and examples do not verify an executed invoice or payment (November lines 251–294).

## Detail locators

- The 2026-05-05 capture has Node SDK examples for meter, price, Customer, subscription, meter event, invoice preview and event summaries (lines 43–62, 93–115, 133–141, 168–181, 202–214, 238–269). The 2026-11-07 capture renders corresponding curl examples (lines 70–80, 112–124, 152–179, 208–222, 243–249, 274–294). This presentation change alone does not establish SDK removal or a runtime behavior change.
- The November guide's comparison says Billing Meters update only at invoice time (line 29), while its own custom-window meter-event-summary section describes asynchronous interim summaries (lines 280–286). Do not read the comparison as eliminating interim summary retrieval.

## Related

- [[stripe]] — Stripe provider.
- [[stripe-usage-based-billing]] — usage-based billing concepts and other source routes.

## Raw Sources

- [[raw/stripe-billing-subscriptions-usage-based-implementation-guide-2026-11-07|Stripe pay-as-you-go guide, 2026-11-07]] — current captured guide and dated Metronome recommendation.
- [[raw/stripe-usage-based-billing-payg-2025|Stripe pay-as-you-go guide, 2026-05-05]] — earlier captured guide with Node examples.
