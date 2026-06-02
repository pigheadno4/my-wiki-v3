<!-- Source URL: https://docs.stripe.com/billing/subscriptions/pause -->
<!-- Fetched: 2026-05-13 -->

# Pause subscriptions

Learn how to pause subscriptions, halting both service delivery and invoice generation.

Pausing a subscription lets you temporarily suspend both service delivery and invoice generation. The ability to pause a subscription helps you support customer scenarios such as vacations, temporary non‑usage, or goodwill pauses to prevent churn.

To use the Pause subscription endpoint, the subscription must use [flexible billing mode](https://docs.stripe.com/billing/subscriptions/billing-mode.md).

Other similar pause behaviors currently supported on a subscription are:

- [Pause payment collection](https://docs.stripe.com/billing/subscriptions/pause-payment.md): Service delivery and invoice generation continue, but collection on invoices is paused.
- [Pause on free trial-end without a payment method](https://docs.stripe.com/billing/subscriptions/trials/free-trials.md#create-free-trials-without-payment): The trial-end pause behaves more like a true pause, but it only applies to a specific, system-triggered scenario.

The ability to pause subscriptions is useful for:

- Merchant teams that want API control over subscription lifecycle without canceling subscriptions.
- Backend engineers building retention flows or support tooling that needs a true pause state.
- Developers validating billing, entitlement revocation, and webhook handling for paused windows.

## Pause subscriptions

You can pause subscriptions with the Pause subscription endpoint. The pause takes effect immediately. After a subscription is paused:

- The subscription status updates to `paused`.
- You get notified about the status change via the [customer.subscription.paused](https://docs.stripe.com/api/events/types.md#event_types-customer.subscription.paused), [customer.subscription.updated](https://docs.stripe.com/api/events/types.md#event_types-customer.subscription.updated), and [entitlements.active_entitlement_summary.updated](https://docs.stripe.com/api/events/types.md#event_types-entitlements.active_entitlement_summary.updated) webhooks, enabling you to de-provision service delivery accordingly.
- Invoice generation is paused for the entire pause duration, though existing subscription invoices advance without affecting the paused status.
- The [current_period_end](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-items-data-current_period_end) updates to the time when you paused the subscription.
- You can use the `bill_for` parameter to control billing behavior at pause time, including creating credit prorations for unused licensed time and creating debits for metered usage in the current period. You can invoice immediately or create pending invoice items.

You can’t pause a subscription if it:

- Uses [send_invoice](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-collection_method) collection
- Uses billing mode [classic](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-billing_mode-type)
- Is in a trial period, or has an active trial offer
- Has `paused`, `incomplete`, `incomplete_expired`, or `canceled` status
- Has an attached [schedule](https://docs.stripe.com/billing/subscriptions/subscription-schedules.md)
- Has an attached [cadence](https://docs.stripe.com/api/v2/billing-cadences.md?api-version=preview)

Similarly, you can’t attach a schedule or cadence to a paused subscription.

If you pause a subscription that uses a coupon, the coupon retains its original validity and the pause doesn’t extend its duration.

This example demonstrates how to use the API to immediately pause an active subscription:

```curl
curl https://api.stripe.com/v1/subscriptions/sub_1234567890/pause \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: preview" \
  -d type=subscription \
  -d "bill_for[unused_time_from][type]=now" \
  -d "bill_for[outstanding_usage_through][type]=now" \
  -d invoicing_behavior=pending_invoice_item
```

The customer portal reflects that a subscription is paused, but your subscribers can’t use it to pause subscriptions themselves.

## Resume subscriptions

You need to manually resume the subscription using the [Resume subscription API](https://docs.stripe.com/api/subscriptions/resume.md). Resume is only available on subscriptions that use [charge_automatically](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-collection_method) collection.

If resuming doesn’t generate an invoice, the subscription status updates to `active` immediately.

If Stripe generates a resumption invoice:

- Stripe finalizes the resumption invoice immediately.
- Stripe doesn’t attempt payment in the resume response. Collect payment using the [Pay invoice](https://docs.stripe.com/api/invoices/pay.md) endpoint.
- When the invoice is paid or marked uncollectible, the subscription becomes `active`.
- If a payment attempt fails, the subscription becomes `past_due`.
- If you void the resumption invoice before a payment attempt, the subscription stays `paused`.
- If there’s not a successful payment within 23 hours, Stripe voids the invoice and the subscription stays `paused`.

After a subscription’s status updates to `active`:

- Invoicing resumes.
- The billing cycle anchor is optionally reset.
- You get notified about the status change via the [customer.subscription.resumed](https://docs.stripe.com/api/events/types.md#event_types-customer.subscription.resumed), [customer.subscription.updated](https://docs.stripe.com/api/events/types.md#event_types-customer.subscription.updated), and [entitlements.active_entitlement_summary.updated](https://docs.stripe.com/api/events/types.md#event_types-entitlements.active_entitlement_summary.updated) webhooks, enabling you to re-provision service delivery accordingly.

This example demonstrates how to immediately resume a paused subscription using the API:

```curl
curl https://api.stripe.com/v1/subscriptions/sub_1234567890/resume \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: preview" \
  -d billing_cycle_anchor=unchanged \
  -d proration_behavior=create_prorations
```

## Identify pause and resume events

Stripe sends the following events for paused and resumed subscriptions.

| Event                                                                                                                                                                          | Description                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------- |
| [customer.subscription.paused](https://docs.stripe.com/api/events/types.md?api-version=preview#event_types-customer.subscription.paused)                                       | Emitted when a subscription pauses.                        |
| [customer.subscription.resumed](https://docs.stripe.com/api/events/types.md?api-version=preview#event_types-customer.subscription.resumed)                                     | Emitted when a subscription resumes.                       |
| [customer.subscription.updated](https://docs.stripe.com/api/events/types.md?api-version=preview#event_types-customer.subscription.updated)                                     | Emitted when a subscription pauses or resumes.             |
| [entitlements.active_entitlement_summary.updated](https://docs.stripe.com/api/events/types.md?api-version=preview#event_types-entitlements.active_entitlement_summary.updated) | Emitted when entitlements change due to a pause or resume. |

Example webhook payload for `customer.subscription.paused` (key fields shown):

```json
{
  "id": "evt_1SrpXjRnJ89Z4rKkFxe9waAz",
  "object": "event",
  ...
  "data": {
    "object": {
      "id": "sub_1SrpWtRnJ89Z4rKknfSwXkBc",
      "object": "subscription",
      ...
      "latest_invoice": "in_1SrpWtRnJ89Z4rKkzYBCF1MY",
      ...
      "status": "paused",
      ...
    }
  },
  ...
  "type": "customer.subscription.paused"
}
```
