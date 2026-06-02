<!-- Source URL: https://docs.stripe.com/billing/subscriptions/overview -->
<!-- Fetched: 2026-05-12 -->

# How subscriptions work

Manage recurring payments and subscription lifecycles.

Subscriptions let your customers make recurring payments to access a product. Unlike one-time purchases, subscriptions require you to store additional customer information for future charges. Stripe provides features that help you manage subscription billing.

- [Support for different pricing models ](https://docs.stripe.com/products-prices/pricing-models.md)
- [Subscription discount management](https://docs.stripe.com/billing/subscriptions/coupons.md)
- [Trial management](https://docs.stripe.com/billing/subscriptions/trials.md)
- [Prorations for modified subscriptions](https://docs.stripe.com/billing/subscriptions/prorations.md)
- [Customer self-service management](https://docs.stripe.com/customer-management.md)
- [Invoicing to collect payments](https://docs.stripe.com/billing/invoices/subscription.md)
- [Automated revenue recovery](https://docs.stripe.com/billing/revenue-recovery.md)
- [Reporting and analytics ](https://docs.stripe.com/billing/subscriptions/analytics.md)

## The subscription lifecycle

The following sections describe the recommended subscription lifecycle in Stripe.

### Create the subscription

Create a new subscription in the [Dashboard](https://dashboard.stripe.com/subscriptions?status=active) or with the [API](https://docs.stripe.com/api/subscriptions/create.md). Every time you create a subscription, this triggers an [event](https://docs.stripe.com/billing/subscriptions/webhooks.md#events). Listen for these events with [webhook endpoints](https://docs.stripe.com/billing/subscriptions/webhooks.md), and make sure that your integration properly handles them.

Optionally, create a [trial](https://docs.stripe.com/billing/subscriptions/trials.md) that doesn’t require payment for the subscription. In this case, the `status` is `trialing`. When the trial is over, the subscription moves to `active` and Stripe charges the subscribed customer.

#### Payment behavior

Set the `payment_behavior` of a subscription to [default_incomplete](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-payment_behavior) to help handle failed payments and complex payment flows like 3DS. This creates subscriptions with status `incomplete` if payment is required, which allows you to subsequently collect and confirm payment information to activate the subscription.

When you set `payment_behavior` to:

- `allow_incomplete`: Stripe immediately attempts to collect payment on the invoice. If the payment fails, the subscription’s status changes to `incomplete`.
- `error_if_incomplete`: If payment fails, the subscription creation fails entirely.

Subscriptions you create in the Dashboard default to the appropriate payment behavior depending on the payment method.

### Handle the invoice

When you create a subscription, Stripe automatically creates an [invoice](https://docs.stripe.com/billing/invoices/subscription.md) with the status `open`. Your customer has about 23 hours to make a successful payment. During this time, the subscription status is `incomplete` and the invoice status remains `open`.

The 23-hour window exists because your customer usually makes the first payment for a subscription while _on-session_ (A payment is described as on-session if it occurs while the customer is actively in your checkout flow and able to authenticate the payment method). If the customer returns to your application after 23 hours, create a new subscription for them.

### The customer pays

If your customer pays the invoice, the subscription updates to `active` and the invoice to `paid`. If they don’t make a payment, the subscription updates to `incomplete_expired` and the invoice becomes `void`.

To confirm whether the invoice has been paid:

- Set up a webhook endpoint or another type of event destination and listen for the `invoice.paid` event.
- Manually check the subscription object and look for `subscription.status=active`. The `status` becomes `active` when the invoice has been paid either through an automatic charge or having the customer pay manually.

For more details, see [Subscription statuses](https://docs.stripe.com/billing/subscriptions/overview.md#subscription-statuses) and [Payment statuses](https://docs.stripe.com/billing/subscriptions/overview.md#payment-status).

### Provision access to your product

When you create a subscription for a customer, this creates an active [entitlement](https://docs.stripe.com/billing/entitlements.md) for each feature associated with that product. When a customer accesses your services, use their active entitlements to grant them access to the features included in their subscription.

Alternatively, you can use [track active subscriptions](https://docs.stripe.com/billing/subscriptions/webhooks.md#active-subscriptions) with webhook events and provision the product for the customer based on that activity.

### Update the subscription

You can [modify existing subscriptions](https://docs.stripe.com/billing/subscriptions/change.md) as needed without having to cancel and recreate them. Some of the most significant changes you might make are [upgrading or downgrading](https://docs.stripe.com/billing/subscriptions/change-price.md) the subscription price or [pausing payment collection](https://docs.stripe.com/billing/subscriptions/pause-payment.md) for an active subscription.

You can listen to [subscription events](https://docs.stripe.com/billing/subscriptions/webhooks.md#events) with [webhook endpoints](https://docs.stripe.com/billing/subscriptions/webhooks.md) for changes to the subscription. For example, you might want to email a customer if a payment fails or revoke a customer’s access when they cancel their subscription.

For [Stripe Checkout](https://docs.stripe.com/payments/checkout.md) integrations, you can’t update the subscription or its invoice if the session’s subscription is `incomplete`. You can listen to the [checkout.session.completed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.completed) event to make the update after the session has completed. You can also [expire the session](https://docs.stripe.com/api/checkout/sessions/expire.md) instead if you want to cancel the session’s subscription, void the subscription invoice, or mark the invoice as uncollectible.

### Update the first invoice

You can update the first invoice for a subscription if the [collection_method](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-collection_method) is `send_invoice`. After the invoice is created, you have one hour to make any updates to the amounts, line items, description, metadata, and so on. You can’t update the invoice after it’s finalized and sent to the customer for payment.

The first invoice for a subscription with the `collection_method` set to `charge_automatically` is finalized and charged immediately. You can’t update the first invoice before it’s finalized, but you can update subsequent invoices for subscription renewals.

You also can’t update the first invoice for subscription schedules. The first invoice is always open, regardless of the collection method.

### Handle unpaid subscriptions

For subscriptions with unpaid invoices, the unpaid invoices remain open but further payment attempts are paused. The subscription continues to generate invoices each billing period, which remain in the `draft` status. To reactivate the subscription:

1. Collect new payment information if necessary.
1. Enable automatic collection by setting [auto_advance](https://docs.stripe.com/api/invoices/update.md#update_invoice-auto_advance) to `true` on draft invoices.
1. [Finalize](https://docs.stripe.com/api/invoices/finalize.md) and pay the open invoices. Paying the most recent non-voided invoice before its due date updates the subscription status to `active`.

Invoices marked as uncollectable keep the underlying subscription `active`. Stripe ignores voided invoices when determining subscription status and uses the most recent non-voided invoice instead.

The unpaid subscription’s `status` depends on your [failed payment settings](https://dashboard.stripe.com/settings/billing/automatic) in the Dashboard.

### Cancel the subscription

You can [cancel](https://docs.stripe.com/billing/subscriptions/cancel.md) a subscription at any time, including at the [end of a billing cycle](https://docs.stripe.com/billing/subscriptions/cancel.md#cancel-at-the-end-of-the-current-billing-period) or after a [set number of billing cycles](https://docs.stripe.com/billing/subscriptions/cancel.md#subscription-schedules).

By default, canceling a subscription disables creating new invoices and [stops automatic collection](https://docs.stripe.com/billing/subscriptions/cancel.md#handle-invoice-items-when-canceling-subscriptions) of all outstanding invoices from the subscription. It also deletes the subscription and you can no longer update it except for its [metadata](https://docs.stripe.com/metadata.md) and `cancellation_details`. If your customer wants to resubscribe, you need to collect new payment information from them and create a new subscription.

## Subscription statuses

Subscriptions can have the following statuses. The actions you can take on a subscription depend on its status.

| Status               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `trialing`           | The subscription is currently in a trial period and you can safely provision your product for your customer. The subscription transitions automatically to `active` when a customer makes the first payment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `active`             | The subscription is in good standing. For `past_due` subscriptions, paying the latest associated invoice or marking it uncollectible transitions the subscription to `active`. Note that `active` doesn’t indicate that all outstanding invoices associated with the subscription have been paid. You can leave other outstanding invoices open for payment, mark them as uncollectible, or void them as you see fit.                                                                                                                                                                                                                                                                                                       |
| `incomplete`         | The customer must make a successful payment within 23 hours to activate the subscription. Or the payment [requires action](https://docs.stripe.com/billing/subscriptions/overview.md#requires-action), such as customer authentication. Subscriptions can also be `incomplete` if there’s a pending payment and the PaymentIntent status is `processing`.                                                                                                                                                                                                                                                                                                                                                                   |
| `incomplete_expired` | The initial payment on the subscription failed and the customer didn’t make a successful payment within 23 hours of subscription creation. These subscriptions don’t bill customers. This status exists so you can track customers that failed to activate their subscriptions.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `past_due`           | Payment on the latest _finalized_ invoice either failed or wasn’t attempted. The subscription continues to create invoices. Your Dashboard [subscription settings](https://dashboard.stripe.com/settings/billing/automatic) determine the subscription’s next status. If the invoice is still unpaid after all attempted [smart retries](https://docs.stripe.com/billing/revenue-recovery/smart-retries.md), you can configure the subscription to move to `canceled`, `unpaid`, or leave it as `past_due`. To reactivate the subscription, have your customer pay the most recent invoice. The subscription status becomes `active` regardless of whether the payment is done before or after the latest invoice due date. |
| `canceled`           | The subscription was canceled. During cancellation, automatic collection for all unpaid invoices is disabled (`auto_advance=false`). This is a terminal state that can’t be updated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `unpaid`             | The latest invoice hasn’t been paid but the subscription remains in place. The latest invoice remains open and invoices continue to generate, but payments aren’t attempted. Revoke access to your product when the subscription is `unpaid` because payments were already attempted and retried while `past_due`. To move the subscription to `active`, pay the most recent invoice before its due date.                                                                                                                                                                                                                                                                                                                   |
| `paused`             | The subscription has ended its trial period without a default payment method and the [trial_settings.end_behavior.missing_payment_method](https://docs.stripe.com/billing/subscriptions/trials/free-trials.md#create-free-trials-without-payment) is set to `pause`. Invoices are no longer created for the subscription. After attaching a default payment method to the customer, you can [resume the subscription](https://docs.stripe.com/billing/subscriptions/trials/free-trials.md#resume-a-paused-subscription).                                                                                                                                                                                                    |

## Payment statuses

A [PaymentIntent](https://docs.stripe.com/payments/payment-intents.md) tracks the lifecycle of every payment. Whenever a payment is due for a subscription, Stripe generates an [invoice](https://docs.stripe.com/billing/invoices/subscription.md) and a PaymentIntent. The PaymentIntent ID attaches to the invoice and you can access it from the Invoice and Subscription objects.

The status of the PaymentIntent affects the status of the invoice and the subscription. Here’s how the different outcomes of a payment map to the different statuses:

| Payment outcome                 | PaymentIntent status      | Invoice status | Subscription status |
| ------------------------------- | ------------------------- | -------------- | ------------------- |
| Success                         | `succeeded`               | `paid`         | `active`            |
| Fails because of a card error   | `requires_payment_method` | `open`         | `incomplete`        |
| Fails because of authentication | `requires_action`         | `open`         | `incomplete`        |

Asynchronous payment methods, such as ACH Direct Debit, handle subscription status transitions differently from immediate payment methods. When you use an asynchronous payment method, a subscription can move directly to `active` after creation and bypass `incomplete`. If the payment fails later, Stripe voids the invoice but the subscription remains `active`. Use this behavior when you design your access control and retry logic.

The following sections explain these statuses and the actions to take for each.

### Payment succeeded

When the customer’s payment is successful:

- The `status` of the PaymentIntent moves to `succeeded`.
- The `status` of the subscription is `active`.
- The `status` of the invoice is `paid`.
- Stripe sends an `invoice.paid` event to your configured webhook endpoints.

For [payment methods](https://docs.stripe.com/payments/payment-methods/integration-options.md) with longer processing periods, subscriptions are immediately activated. In these cases, the status of the PaymentIntent might be `processing` for an `active` subscription until the payment succeeds.

With your subscription now activated, [provision access](https://docs.stripe.com/billing/subscriptions/overview.md#provision-access) to your product.

### Requires payment method

If payment fails because of a [card error](https://docs.stripe.com/api/errors.md#errors-card_error) such as a [decline](https://docs.stripe.com/declines.md#issuer-declines):

- The `status` of the PaymentIntent is `requires_payment_method`.
- The `status` of the subscription is `incomplete`.
- The `status` of the invoice is `open`.

To handle these scenarios:

- Notify the customer.
- Collect new payment information and [confirm the PaymentIntent](https://docs.stripe.com/api/payment_intents/confirm.md).
- Update the [default payment method](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-default_payment_method) on the subscription.
- Stripe re-attempts payment using [Smart Retries](https://docs.stripe.com/invoicing/automatic-collection.md#smart-retries) or based on your custom [retry rules](https://dashboard.stripe.com/account/billing/automatic).
- Use the [invoice.payment_failed](https://docs.stripe.com/billing/revenue-recovery/smart-retries.md#invoice-payment-failed-webhook) event to monitor subscription payment failure events and retry attempt updates. After a payment attempt on an invoice, its [next_payment_attempt](https://docs.stripe.com/api.md#invoice_object-next_payment_attempt) value is set using the current subscription settings in your Dashboard.

Learn how to [handle payment failures for subscriptions](https://docs.stripe.com/billing/subscriptions/webhooks.md#payment-failures).

### Requires action

Some payment methods require customer authentication with [3D Secure](https://docs.stripe.com/payments/3d-secure.md) (3DS) to complete the payment process. 3DS completes the authentication process. Whether a payment method requires authentication depends on your [Radar rules](https://docs.stripe.com/payments/3d-secure/authentication-flow.md#three-ds-radar) and the issuing bank for the card.

If payment fails because the customer needs to authenticate a payment:

- The `status` of the PaymentIntent is `requires_action`.
- The `status` of the subscription is `incomplete`.
- The `status` of the invoice is `open`.

To handle these scenarios:

- Monitor for the `invoice.payment_action_required` event notification with [webhook endpoints](https://docs.stripe.com/billing/subscriptions/webhooks.md). This indicates that authentication is required.
- Notify your customer that they must authenticate.
- Retrieve the client secret for the PaymentIntent and pass it in a call to [stripe.ConfirmCardPayment](https://docs.stripe.com/js/payment_intents/confirm_card_payment). This displays an authentication modal to your customers, attempts payment, then closes the modal and returns context to your application.
- Monitor the `invoice.paid` event on your event destination to verify that the payment succeeded. Users can leave your application before `confirmCardPayment()` finishes. Verifying whether the payment succeeded allows you to correctly provision your product.

## See also

- [Design a subscriptions integration](https://docs.stripe.com/billing/subscriptions/design-an-integration.md)
- [Subscriptions quickstart](https://docs.stripe.com/billing/quickstart.md)
- [Subscription with a fixed price example](https://github.com/stripe-samples/subscription-use-cases/tree/main/fixed-price-subscriptions)
