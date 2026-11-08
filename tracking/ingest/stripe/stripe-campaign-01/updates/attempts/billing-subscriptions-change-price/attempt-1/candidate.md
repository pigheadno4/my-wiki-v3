---
title: "Stripe Subscriptions — Change the Price of Existing Subscriptions"
type: source
date_ingested: 2026-11-08
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/subscriptions/change-price"
raw_files:
  - "stripe-billing-subscriptions-change-price-2026-11-07.md"
  - "stripe-subscriptions-change-price-2026.md"
tags: [stripe, billing, subscriptions, upgrade, downgrade, price-change, prorations]
---

## Overview

Stripe's Subscriptions API guide describes changing a subscription item's price to upgrade or downgrade an existing subscription. The 2026-11-07 capture presents curl examples where the 2026-05-13 capture used Node SDK examples; the central documented behavior remains the same. These are guide examples, not tested requests or successful billing outcomes. See [[stripe-subscriptions]] and [[stripe]].

## Two update methods

### Update the subscription

Find the subscription and item identifiers using a relevant filter, such as the customer-configured Account or Customer ID. The captured list example uses `customer={{CUSTOMER_ID}}`; it does not establish every Account filter's wire format. On a subscription update, pass the existing item ID with the replacement price. Omitting the item ID **adds another item**, leaving both prices active. The May Node example illustrates the replacement call:

```js
stripe.subscriptions.update(subId, {
  items: [{ id: subItemId, price: newPriceId }]
})
```

An alternative documented path deletes the old item and creates one at the new price in the same subscription update. See November raw lines 62–87 and May raw lines 65–108 for the dated requests.

### Update the subscription item directly

Update the item's `price` when no other subscription-level change is needed. The May Node example is `stripe.subscriptionItems.update(subItemId, { price: newPriceId })`; the November curl example is at lines 89–102.

## Quantity and billing periods

Changing price resets item `quantity` to `1`; pass the existing quantity when it must be preserved. When the old and new prices have the same `interval` and `interval_count`, billing dates remain the same in the guide's general case. Different billing periods start the new interval on the change date; adding a trial moves the billing date to the trial conclusion. The separate zero-price exception below also resets the period. For end-of-period changes, the guide says to consider a subscription schedule and follow its best practices to prevent unexpected overwrites.

## Proration and payment state

Price changes **often** result in prorations; the guide links to a separate proration-preview page and a disable-prorations route. Neither capture establishes `stripe.invoices.retrieveUpcoming` as the specific preview method for this guide.

For a change on the same billing period, `proration_behavior=always_invoice` calculates the proration and immediately **generates an invoice** after the switch. Invoice creation is distinct from payment success. The guide suggests combining it with pending updates so the subscription does not update unless payment on the new invoice succeeds. Separately, a billing-cycle-anchor reset immediately **attempts payment**. If required immediate payment fails, the change request can succeed while the subscription transitions to `past_due`. Credit-proration calculation depends on the subscription's `billing_mode`; the detailed methods are in the linked proration guide.

## Usage and zero-amount cases

- For a price attached to a Billing Meter, `clear_usage` has no effect. The guide routes mid-cycle meter-price details to the pricing-models page.
- For a metered price backed by legacy Usage Records, usage transfers to the new Usage Records price on update. The November curl and May Node examples are at raw lines 116–126 and 141–159 respectively.
- Changing a zero-amount price to a nonzero price generates an invoice and resets the billing period to the change date.
- Increasing a zero quantity on a nonzero price to a nonzero quantity does **not** generate an invoice or reset the billing period.

## Detail locators

- Identifier retrieval and customer-scoped examples: November raw lines 15–60; May lines 14–63.
- Replacement, delete/create alternative, direct item update, and quantity preservation: November lines 62–102; May lines 65–127.
- Billing-period and schedule cautions: November lines 104–110; May lines 129–135.
- Conditional prorations, invoice generation, payment attempt and failure state: November lines 128–142; May lines 161–175.
- Zero-amount and zero-quantity cases: November lines 144–148; May lines 177–181. The captures state no API-version floor for these examples and do not establish a paid invoice or completed state transition.

## Related

- [[stripe-subscriptions]] — subscriptions concept and reciprocal source route
- [[source-stripe-subscriptions-modify]] — subscription update overview
- [[stripe]] — company page

## Raw Sources

- [[raw/stripe-billing-subscriptions-change-price-2026-11-07|Stripe change-price guide, captured 2026-11-07]] — full guide, curl examples
- [[raw/stripe-subscriptions-change-price-2026|Stripe change-price guide, captured 2026-05-13]] — prior full guide, Node examples
