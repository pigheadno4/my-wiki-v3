<!-- Source URL: https://docs.stripe.com/payments/payment-method-configurations -->
<!-- Fetched: 2026-05-08 -->

# Payment method configurations

Create different sets of payment methods to display to customers based on specific checkout scenarios.

Payment method configurations allows [dynamic payment method](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md) users to display different sets of payment methods to customers for specific checkout scenarios.

You can create a configuration to:

- Display a unique set of payment methods for certain products
- Enable a set of payment methods for your one-time payment checkout flow and a different set of payment methods for your subscription checkout flow
- (Connect) Offer connected accounts access to additional payment methods for a different subscription fee

After you create a payment method configuration, you can toggle each payment method on or off for a given scenario directly in Dashboard—no code required. Then at checkout, select which configuration you want to use. Stripe ranks the payment methods that are enabled within that configuration to optimize for conversion.

## Before you begin

- You must use either the Stripe [Payment Element](https://docs.stripe.com/payments/payment-element.md) or [Checkout](https://docs.stripe.com/payments/checkout.md).
- You must use [Dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md) to enable additional payment methods from the Stripe Dashboard, which won’t require any code changes.
  - To set up dynamic payment methods for direct users, see the [payment method integration](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md) guide.
  - (Connect) To set up dynamic payment methods for Connect platforms, see [Upgrading to dynamic payment methods](https://docs.stripe.com/connect/dynamic-payment-methods.md).

## Create a payment method configuration

By default, you have one payment method configuration called **Default Config**. You can create additional payment method configurations using both the Stripe Dashboard and the API.

#### Dashboard

1. In your Dashboard, go to [Payment methods settings](https://dashboard.stripe.com/test/settings/payment_methods).
1. In the **Payment configurations** section, click the overflow menu (⋯) > **Create a configuration**.
1. Give your new configuration a name.
1. Click **Save configuration**.
   ![Payment method configuration page](assets/stripe-payment-method-configurations.png)

The page displays your new configuration. All payment methods are initially disabled by default.

To switch between configurations, use the **Select configuration** dropdown near the top of the page.

To make sure that the payment method configuration you want to enable is set to `active` in the Dashboard:

1. Go to your Payment methods settings.
1. Click a payment method in the **Payment configurations** section, then click the overflow menu (⋯) > **Manage configuration**.
1. Under **Configuration status**, enable the **Active** option.
1. Click **Save changes** to apply your updates.

#### API

Create a [payment method configuration](https://docs.stripe.com/api/payment_method_configurations/create.md) with the following parameters:

- `name`: A human-readable string that appears in the Dashboard.
- (Optional) One or more payment methods to turn on in this configuration. Set each value to `on`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethodConfiguration =
  await stripe.paymentMethodConfigurations.create({
    name: "MyConfig",
    affirm: {
      display_preference: {
        preference: "on",
      },
    },
    klarna: {
      display_preference: {
        preference: "on",
      },
    },
  });
```

After you create the configuration, you can add payment methods to it in the Dashboard.

## Enable payment methods

In the Dashboard, open the configuration and turn on the payment methods that you want to make available to buyers when using that configuration. A buyer sees only payment methods that are turned on and compatible with the payment location and currency.

> Some payment methods don’t show edit controls until you expand them.

## Display available payment methods in checkout

Copy the `configuration ID` in the Dashboard from the configuration you want to use in your checkout flow.

If you’re using the [deferred intent creation integration path](https://docs.stripe.com/payments/accept-a-payment-deferred.md), pass the `payment_method_configuration` ID when you create your Payment Element component. The Payment Element automatically pulls the payment methods associated with that configuration and ranks them to best convert buyers.

#### Web

```javascript
const options = {
  mode: "payment",
  amount: 1099,
  currency: "usd",
  paymentMethodConfiguration: "pmc_234",
};
```

#### iOS

```swift
let intentConfig = PaymentSheet.IntentConfiguration(
    mode: .payment(amount: 1099, currency: "USD"),
    paymentMethodConfigurationId: "pmc_234"
  ) { [weak self] _, intentCreationCallback in
    self?.handleConfirm(intentCreationCallback)
  }
```

#### Android

```kotlin
val intentConfig = PaymentSheet.IntentConfiguration(
  mode = PaymentSheet.IntentConfiguration.Mode.Payment(
    amount = 1099,
    currency = "usd",
  ),
  paymentMethodConfigurationId = "pmc_234",
  // Other configuration options...
)
```

If you aren’t using a Payment Element, pass the `payment_method_configuration` ID when you [create a Checkout session](https://docs.stripe.com/api/checkout/sessions/create.md).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  mode: "payment",
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  success_url: "https://example.com/success",
  currency: "usd",
  payment_method_configuration: "pmc_234",
});
```

### Payment methods

By default, Stripe enables cards and other common payment methods. You can turn individual payment methods on or off in the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods). In Checkout, Stripe evaluates the currency and any restrictions, then dynamically presents the supported payment methods to the customer.

To see how your payment methods appear to customers, enter a transaction ID or set an order amount and currency in the Dashboard.

You can enable Apple Pay and Google Pay in your [payment methods settings](https://dashboard.stripe.com/settings/payment_methods). By default, Apple Pay is enabled and Google Pay is disabled. However, in some cases Stripe filters them out even when they’re enabled. We filter Google Pay if you [enable automatic tax](https://docs.stripe.com/tax/checkout.md) without collecting a shipping address.

Checkout’s Stripe-hosted pages don’t need integration changes to enable Apple Pay or Google Pay. Stripe handles these payments the same way as other card payments.

## Create a PaymentIntent with the configuration

Create a PaymentIntent on your server using the payment method configuration.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: "usd",
  automatic_payment_methods: {
    enabled: true,
  },
  payment_method_configuration: "pmc_123",
});
```

In the latest version of the API, the `automatic_payment_methods` parameter is optional because it’s enabled by default.

## Exclude payment methods for a specific PaymentIntent

While you can manage payment methods on a per payment method configuration basis, you can also exclude specific payment methods on a per-transaction basis using the `excluded_payment_method_types` parameter when using PaymentIntents, [SetupIntents](https://docs.stripe.com/payments/setup-intents.md), [Checkout](https://docs.stripe.com/payments/checkout.md), or [PaymentElement](https://docs.stripe.com/payments/payment-element.md).

**Make multiple payment method configurations when**:

- You need to manage payment methods for broader categories of transactions. For example, you might want to configure different sets of payment methods for one-time purchases versus subscriptions. Use this approach when you want to establish consistent payment method offerings across similar transaction types.

**Use excluded_payment_method_types when**:

- You require more control over payment method combinations that would be impractical to implement with multiple payment method configurations.
- You want to control which payment methods you present. For example, you might want to exclude certain payment methods based on which items are included in the transaction.

You can use the `excluded_payment_methods_types` parameter together with payment method configurations to control the availability of payment methods.

> You can’t exclude Apple Pay, Google Pay, or Link on a per-transaction basis using `excluded_payment_method_types`. If you want to control the visibility of these payment methods for an individual transaction, use the wallets hash parameters that are specified per integration type. For example, see the [PaymentElements wallets parameter](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options-wallets).

Learn more about how to [exclude payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md#exclude-payment-methods).
