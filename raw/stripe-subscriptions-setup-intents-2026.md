<!-- Source URL: https://docs.stripe.com/billing/subscriptions/setup-intents -->
<!-- Fetched: 2026-05-12 -->

# Set up payment methods for subscriptions with no initial payment

Authorize and store a payment method for future payments when a subscription doesn't require an initial payment.

Subscriptions that include [free trials](https://docs.stripe.com/billing/subscriptions/trials.md), [usage-based billing](https://docs.stripe.com/products-prices/pricing-models.md#usage-based-pricing), invoices with coupons, or applied customer credit balances often result in non-payment invoices. This means you don’t immediately charge your customer when you create the subscription.

Although you don’t charge customers for the first invoice, authenticating and authorizing their card can help increase successful completion of the first non-zero payment. These types of payments are known as _off-session payments_ (A payment is described as off-session if it occurs without the direct involvement of the customer, using previously-collected payment information). To manage these scenarios, Stripe uses [SetupIntents](https://docs.stripe.com/api/setup_intents.md).

## Use SetupIntents

You can use [SetupIntents](https://docs.stripe.com/api/setup_intents.md) to:

- Collect payment information.
- Authenticate your customer’s card to claim _exemptions_ (Some transactions that are deemed low risk, based on the volume of fraud rates associated with the payment provider or bank, may be exempt from Europe's Strong Customer Authentication requirements) later.
- Authorize your customer’s card without charging it.

Authenticating payments allows your customer to grant permissions to charge their card. [Strong Customer Authentication](https://docs.stripe.com/strong-customer-authentication.md) requires this, and [3DS](https://docs.stripe.com/payments/3d-secure.md) is a common way to complete it. Collecting payment method information and authorizing it ensures that you can successfully charge the payment method.

In off-session scenarios, SetupIntents enable you to charge customers for their first non-zero payment without having to return them to your website or app for authentication. This reduces friction for your customers.

Stripe automatically creates SetupIntents for subscriptions that don’t require an initial payment. The authentication and authorization process also completes at this point, if required. If both succeed or aren’t required, no action is necessary, and the `subscription.pending_setup_intent` field is `null`. If either step fails, Stripe recommends using the SetupIntent on your front end to resolve the issue while your customer is on-session.

The [pending_setup_intent](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-pending_setup_intent) field on a subscription doesn’t cancel automatically when the subscription ends. Listen for [customer.subscription.deleted](https://docs.stripe.com/billing/subscriptions/webhooks.md#events) events and manually [cancel a subscription SetupIntent](https://docs.stripe.com/api/setup_intents/cancel.md) if needed.

The next two sections explain how to manage scenarios where authentication or authorization fail.

## Manage authentication failures (Client-side)

Authentication failures occur when Stripe is unable to authenticate your customer with their card issuer. When this happens, the `status` of the SetupIntent is set to `requires_action`.
![How to handle subscription payment authentication failures.](assets/stripe-subs-authentication-failure.svg)

To resolve these scenarios, call [confirmCardSetup](https://docs.stripe.com/js.md#stripe-confirm-card-setup) on your front end so your customer can complete the authentication flow manually. The code example below [expands](https://docs.stripe.com/api/expanding_objects.md) the [pending_setup_intent](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-pending_setup_intent) to complete the flow.

```javascript
const { pending_setup_intent } = subscription;

if (pending_setup_intent) {
  const { client_secret, status } = subscription.pending_setup_intent;

  if (status === "requires_action") {
    const { setupIntent, error } = await stripe.confirmCardSetup(client_secret);

    if (error) {
      // Display error.message in your UI.
    } else {
      // The setup has succeeded. Display a success message.
    }
  }
}
```

After completing this flow, authorization executes if it’s required. If authorization succeeds, or if it’s not required, `pending_setup_intent` is updated to `null` upon completion.

## Manage authorization failures (Client-side)

Payment authorization failures occur when Stripe can’t verify that a card can be charged. This sets the [status](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-status) of the SetupIntent to `requires_payment_method`, which usually means that subsequent charges with that card fail.
![How to handle subscription payment authorization failures.](assets/stripe-subs-authorization-failure.svg)

To resolve these scenarios, [collect a new payment method](https://docs.stripe.com/billing/subscriptions/overview.md#requires-payment-method), then update the default payment method for your customer or the subscription. The code example below [expands](https://docs.stripe.com/api/expanding_objects.md) the [pending_setup_intent](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-pending_setup_intent) to complete the flow.

```javascript
const { pending_setup_intent, latest_invoice } = subscription;

if (pending_setup_intent) {
  const { client_secret, status } = subscription.pending_setup_intent;

  if (status === "requires_action") {
    const { setupIntent, error } = await stripe.confirmCardSetup(client_secret);

    if (error) {
      // Display error.message in your UI.
    } else {
      // The setup has succeeded. Display a success message.
    }
  } else if (status === "requires_payment_method") {
    // Collect new payment method.
  }
}
```
