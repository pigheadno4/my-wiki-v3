---
title: "India e-mandate support for Stripe invoices"
type: source
date_ingested: 2026-07-31
canonical_url: "https://docs.metronome.com/guides/customers-billing/optimize-customer-experience/india-e-mandates"
original_format: webpage
raw_files:
  - "metronome/guides/customers-billing/optimize-customer-experience/india-e-mandates-2026-07-13.md"
tags: [metronome, stripe, india, e-mandates, recurring-payments, off-session-payments]
---

## Overview

Metronome documents how invoices for Indian credit cards can use a mandate created and managed in Stripe. The merchant collects the card on-session and confirms a Stripe SetupIntent, waits for the resulting mandate to become active, stores the mandate ID in a Metronome contract custom field, and maps that field to the Stripe invoice default-mandate setting. The page presents this as an implementation for RBI pre-authorization requirements; it is not an independent statement of those regulatory requirements.

## Key takeaways

- Stripe creates the mandate during on-session SetupIntent confirmation and owns its status and lifecycle.
- Threshold-triggered recharges use a sporadic interval and a maximum amount, while recurring fees use their corresponding cadence and can use fixed or maximum amounts according to whether the charge is known or variable.
- A new mandate can remain pending for up to 30 minutes. The integration must wait for active status; an inactive mandate cannot be used and requires new customer authorization.
- A Metronome contract custom field can be mapped to Stripe `invoice.payment_settings` → `default_mandate`; invoices sent to Stripe then attempt to attach that mandate. Attachment does not guarantee successful payment.
- Stripe can emit `invoice.payment_action_required`. Metronome does not expose a mandate-management API or manage mandate lifecycle events, so the integrator must update mandates in Stripe and act before retrying.

## Setup and configuration

### Create the mandate in Stripe

Collect the Indian card while the customer is on-session and confirm a Stripe SetupIntent so the customer can authenticate. The example configures card `mandate_options` with `amount_type`, `amount`, `currency`, `interval`, `reference`, and `start_date`; its sample values are illustrative and do not establish regulatory limits or general defaults.

For threshold billing, the guide uses `interval: sporadic`, `amount_type: maximum`, and an amount high enough for variable recharge amounts. For subscriptions or recurring fees, the interval should match the recurrence, while `amount_type` is fixed for a known amount or maximum for a variable amount.

### Wait for active status

A mandate may remain `pending` for up to 30 minutes. Readiness can be detected from Stripe's `mandate.updated` event or by retrieving the mandate ID from the SetupIntent and polling. If the mandate becomes `inactive`, the customer must authorize a new one.

### Map the mandate into invoice delivery

Create a contract custom field such as `stripe_mandate_id`, map it through the Metronome entity-mapping UI to Stripe `invoice.payment_settings` → `default_mandate`, and populate it with the Stripe mandate ID when creating the contract. The guide says all invoices sent to Stripe attempt to attach that mandate.

## Payment action and failure

After an invoice is created with the mandate, its Stripe PaymentIntent can require customer action, signaled by Stripe's `invoice.payment_action_required` event. The guide says customer approval completes payment and releases the balance, while no response or an inactive mandate enters the normal failure flow and requires a newly authorized active mandate before a future recharge can succeed. The balance-release and future-recharge wording is explicit for the documented recharge flow and should not be generalized into a separate subscription-entitlement or invoice-retry guarantee.

## Responsibility boundaries

Mandates are created and managed entirely in Stripe. In this integration, SetupIntent setup is required because the page characterizes every charge, including the first, as off-session. Metronome stores and returns the contract custom-field value, maps it into Stripe invoice settings, and surfaces payment failures through its normal failure path; it does not expose a mandate API or manage mandate lifecycle events. The integrator owns replacing or updating the mandate in Stripe and taking appropriate action before retrying.

## Documentation boundaries

> [!warning] Regional and regulatory scope
> The page labels the flow RBI-compliant and links to Stripe's RBI e-mandate guide, but it does not define RBI rules, eligibility, customer-notification duties, mandate limits, exemptions, or legal-compliance scope. Do not infer those details from the sample amount or configuration.

The page does not define the exact Metronome webhook or failure state, retry mechanics, idempotency, amount denomination for the SetupIntent example, which invoice classes are eligible, or whether mandate attachment can fail independently. Its statement that invoices attempt to attach the mandate is not a payment-success guarantee.

## Related

- Companies: [[metronome]], [[stripe]]
- Concepts: [[metronome-invoicing]], [[metronome-integrations]], [[metronome-credits-and-commits]], [[metronome-subscriptions]], [[stripe-saved-payment-methods]]
- Related sources: [[source-metronome-integrations-invoice-integrations-stripe]], [[source-metronome-guides-customers-billing-optimize-customer-experience-prepaid-balance-thresholds]], [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-manual-payment-gated-commits]]

## Raw Sources

- [[raw/metronome/guides/customers-billing/optimize-customer-experience/india-e-mandates-2026-07-13|2026-07-13 snapshot — Indian-card Stripe mandate setup, mapping, and responsibility boundaries]]
