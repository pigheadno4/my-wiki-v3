<!-- Source URL: https://docs.stripe.com/payments/payment-intents/upgrade-to-handle-actions -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Migrate your basic card integration

Migrate to an integration that can handle bank requests for card authentication.

If you followed the [Card payments without bank authentication](https://docs.stripe.com/payments/without-card-authentication.md) guide, your integration creates payments that decline when a bank asks the customer to authenticate the purchase.

If you start seeing many failed payments like the one in the Dashboard below or with an error code of `requires_action_not_handled` in the API, upgrade your basic integration to handle, rather than decline, these payments.
![Dashboard showing a failed payment that says that this bank required authentication for this payment](https://b.stripecdn.com/docs-statics-srv/assets/failed-payment-dashboard.9e22ec31f3c7063665911e26e389c5dc.png)

Use this guide to learn how to upgrade the integration you built in the previous guide to add server and client code that prompts the customer to authenticate the payment by displaying a modal.

> See a [full sample](https://github.com/stripe-samples/accept-a-payment/tree/master/custom-payment-flow) of this integration on GitHub.

## Check if the payment requires authentication [Server-side]

Make two changes to the endpoint on your server that creates the PaymentIntent:

1. **Remove** the [error_on_requires_action](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-error_on_requires_action) parameter to no longer fail payments that require authentication. Instead, the PaymentIntent status changes to `requires_action`.
2. **Add** the `confirmation_method` parameter to indicate that you want to explicitly (manually) confirm the payment again on the server after handling authentication requests.

#### curl

```bash
curl https://api.stripe.com/v1/payment_intents \
  -u <<YOUR_SECRET_KEY>>: \
  -d amount=1099 \
  -d currency=usd \
  -d allowed_payment_method_types[]=card \
  -d confirm=true \
  -d payment_method="{{PAYMENT_METHOD_ID}}" \
  -d confirmation_method=manual
```

Then update your “generate response” function to handle the `requires_action` state instead of erroring:

#### curl

```bash
# If the request succeeds, check the
# PaymentIntent's `status` and handle
# its `next_action`.
```

## Ask the customer to authenticate [Client-side]

Next, update your client-side code to tell Stripe to show a modal if the customer needs to authenticate.

Use [stripe.handleCardAction](https://docs.stripe.com/js.md#stripe-handle-card-action) when a PaymentIntent has a status of `requires_action`. If successful, the PaymentIntent will have a status of `requires_confirmation` and you need to confirm the PaymentIntent again on your server to finish the payment.

```javascript
const handleServerResponse = async (responseJson) => {
  if (responseJson.error) {
    // Show error from server on payment form
  } else if (responseJson.requiresAction) {
    // Use Stripe.js to handle the required card action
    const { error: errorAction, paymentIntent } =
      await stripe.handleCardAction(responseJson.clientSecret);

    if (errorAction) {
      // Show error from Stripe.js in payment form
    } else {
      // The card action has been handled
      // The PaymentIntent can be confirmed again on the server
      const serverResponse = await fetch('/pay', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ payment_intent_id: paymentIntent.id })
      });
      handleServerResponse(await serverResponse.json());
    }
  } else {
    // Show success message
  }
}
```

## Confirm the PaymentIntent again [Server-side]

Using the same endpoint you set up earlier, *confirm* (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) the PaymentIntent again to finalize the payment and fulfill the order. The payment attempt fails and transitions back to `requires_payment_method` if it isn’t confirmed again within one hour.

#### curl

```bash
curl https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT_ID}}/confirm \
  -u <<YOUR_SECRET_KEY>>: \
  -X "POST"
```

## Test the integration

Use our test cards in a sandbox to verify that your integration was properly updated. Stripe displays a fake authentication page inside the modal in a sandbox that lets you simulate a successful or failed authentication attempt. In live mode the bank controls the UI of what’s displayed inside the modal.

| Number | Description |
| --- | --- |
| 4242424242424242 | Succeeds and immediately processes the payment. |
| 4000000000009995 | Always fails with a decline code of `insufficient_funds`. |
| 4000002500003155 | Requires authentication, which in this integration will fail with a decline code of `authentication_not_handled`. |
