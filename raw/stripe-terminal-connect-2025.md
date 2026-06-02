<!-- Source: Stripe Terminal — Use Terminal with Connect -->
<!-- Fetched: 2026-04-24 -->

# Use Terminal with Connect

Integrate Stripe Terminal with your Connect platform.

Stripe Terminal is compatible with _Connect_ (Connect is Stripe's solution for multi-party businesses, such as marketplace or software platforms, to route payments between sellers, customers, and other recipients), allowing your platform and connected accounts to accept in-person payments.

Integrate Terminal with Connect according to how your platform processes payments for your connected accounts.

- If you use [direct charges](https://docs.stripe.com/connect/direct-charges.md), you submit Terminal API requests to configure readers and accept payments using your platform’s API key and the `Stripe-Account` header to identify the connected account.
- If you use [destination charges](https://docs.stripe.com/connect/destination-charges.md), you submit Terminal API requests to configure readers and accept payments using your platform API key and identify the connected account using metadata.
- If you use [separate charges and transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md), you submit Terminal API requests using your platform API key to create charges on your platform account, then create separate transfers to move funds to your connected accounts.

In all cases, use [locations](https://docs.stripe.com/api/terminal/locations.md) to group readers applicably.

> Terminal connected accounts must have the `card_payments` capability to perform transactions.

# Direct charges

> This is a Direct charges for when connect-charge-type is direct. View the full page at https://docs.stripe.com/terminal/features/connect?connect-charge-type=direct.

## Connected accounts own readers

With this integration, all API resources belong to the connected account rather than your platform. The connected account is responsible for the cost of Stripe fees, refunds, and chargebacks.

In the Dashboard, you can view your Terminal data by logging in as the connected account.

### Create locations and readers (Server-side)

Create [Locations](https://docs.stripe.com/terminal/fleet/locations-and-zones.md?dashboard-or-api=dashboard#create-locations-and-zones) and [Readers](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=internet) for connected accounts by including the `Stripe-Account` header in the API requests. You can also register the reader by clicking **View as** in the Stripe Dashboard for your connected account.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create(
  {
    display_name: "HQ",
    address: {
      line1: "1272 Valencia Street",
      city: "San Francisco",
      state: "CA",
      country: "US",
      postal_code: "94110",
    },
  },
  {
    stripeAccount: "{{CONNECTEDACCOUNT_ID}}",
  },
);
```

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const reader = await stripe.terminal.readers.create(
  {
    registration_code: "{{READER_REGISTRATION_CODE}}",
    label: "Alice's reader",
    location: "{{TERMINALLOCATION_ID}}",
  },
  {
    stripeAccount: "{{CONNECTEDACCOUNT_ID}}",
  },
);
```

### Create connection tokens (Server-side)

> When using [Connect OAuth](https://docs.stripe.com/connect/oauth-reference.md) authentication, you must authorize the connected account separately for live mode and sandboxes using each mode’s respective application Client ID.

When creating a [ConnectionToken](https://docs.stripe.com/api/terminal/connection_tokens.md) for the Terminal SDK, set the `Stripe-Account` header to the connected account accepting payments. You can also provide a `location` parameter to control access to readers. If you provide a location, only readers assigned to that location can use the `ConnectionToken`. If you don’t provide a location, all readers can use the `ConnectionToken`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const connectionToken = await stripe.terminal.connectionTokens.create(
  {
    location: "{{TERMINALLOCATION_ID}}",
  },
  {
    stripeAccount: "{{CONNECTEDACCOUNT_ID}}",
  },
);
```

If you’re using a server-driven integration, you don’t need to create a connection token.

### Create PaymentIntents (Client-side) (Server-side)

With the iOS, Android, and React Native SDKs, you can create a `PaymentIntent` on the client or server. The JavaScript SDK only supports server-side creation.

#### Client-side

When creating a `PaymentIntent` client-side for direct charges, don’t specify any additional parameters for the `PaymentIntent`. Instead, create a `ConnectionToken` with the `Stripe-Account` header for the connected account accepting payments. The client SDKs create the `PaymentIntent` on the same connected account the `ConnectionToken` belongs to. For more information, see [Create PaymentIntents client-side](https://docs.stripe.com/terminal/payments/collect-card-payment.md#create-client-side).

#### Server-side

The JavaScript SDK requires you to create the `PaymentIntent` on your server. For the other client SDKs, you might want to create the `PaymentIntent` on your server if the information required to start a payment isn’t readily available in your app. For more information, see [Create PaymentIntents Server-side](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=js#create-payment).

When creating a `PaymentIntent` server-side for direct charges, set the `Stripe-Account` header to the connected account.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create(
  {
    amount: 1000,
    currency: "usd",
    payment_method_types: ["card_present"],
    capture_method: "manual",
  },
  {
    stripeAccount: "{{CONNECTEDACCOUNT_ID}}",
  },
);
```

Then follow the steps to [collect a payment](https://docs.stripe.com/terminal/payments/collect-card-payment.md) to process the PaymentIntent.

## Platform-owned readers (Private preview)

> [Contact us](mailto:stripe-terminal-betas@stripe.com) if you’re interested in letting the platform own and manage readers with direct charges. This private preview feature is currently available for [smart readers](https://docs.stripe.com/terminal/smart-readers.md) using a [server-driven integration](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=server-driven). This integration works only with connected accounts that you control through a single platform.

With this integration, your platform owns device resources like [Locations](https://docs.stripe.com/api/terminal/locations.md) and [Readers](https://docs.stripe.com/api/terminal/readers.md), and your connected accounts own payment resources like [PaymentIntents](https://docs.stripe.com/api/payment_intents.md). This allows your platform to manage a single reader that processes payments for multiple connected accounts. The connected accounts are responsible for the cost of Stripe fees, refunds, and chargebacks.

In the Dashboard, you can view your Terminal device management data directly when logged into your platform account. You can view payment data by logging in as the connected account.

### Create locations and readers

The best way to group Reader objects by connected account is by assigning them to `Locations`. On your platform account, [create a Location](https://docs.stripe.com/terminal/fleet/locations-and-zones.md?dashboard-or-api=dashboard#create-locations-and-zones) for a connected account using a display name that identifies the account.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "1272 Valencia Street",
    city: "San Francisco",
    state: "CA",
    country: "US",
    postal_code: "94110",
  },
});
```

Before you can connect your application to a [smart reader](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=internet), you must register the reader to your platform account.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const reader = await stripe.terminal.readers.create({
  registration_code: "{{READER_REGISTRATION_CODE}}",
  label: "Alice's reader",
  location: "{{TERMINALLOCATION_ID}}",
});
```

### Create PaymentIntents

When creating a `PaymentIntent` for direct charges, set the `Stripe-Account` header to the connected account.

> The platform can only process PaymentIntents later if you create them for connected accounts that you control through a single platform.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create(
  {
    amount: 1000,
    currency: "usd",
    payment_method_types: ["card_present"],
    capture_method: "manual",
  },
  {
    stripeAccount: "{{CONNECTEDACCOUNT_ID}}",
  },
);
```

### Process PaymentIntents

The platform can process the connected account’s `PaymentIntent` with the platform-owned reader.

> The PaymentIntent can only be processed if you create it using the `Stripe-Account` header.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const reader = await stripe.terminal.readers.processPaymentIntent(
  "{{TERMINALREADER_ID}}",
  {
    payment_intent: "{{PAYMENTINTENT_ID}}",
  },
);
```

# Destination charges

> This is a Destination charges for when connect-charge-type is destination. View the full page at https://docs.stripe.com/terminal/features/connect?connect-charge-type=destination.

When using [destination charges](https://docs.stripe.com/connect/destination-charges.md), your platform owns API resources like [PaymentIntents](https://docs.stripe.com/api/payment_intents.md) and [Locations](https://docs.stripe.com/api/terminal/locations.md). Each payment creates a transfer to a connected account automatically.

In the Dashboard, you can view your Terminal data directly when logged into your platform account.

## Create locations and readers (Server-side)

Group Reader objects by connected account by assigning them to `Locations`. On your platform account, [create a Location](https://docs.stripe.com/terminal/fleet/locations-and-zones.md?dashboard-or-api=dashboard#create-locations-and-zones) for a connected account using a display name that identifies the account.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "1272 Valencia Street",
    city: "San Francisco",
    state: "CA",
    country: "US",
    postal_code: "94110",
  },
});
```

Before you can connect your application to a [smart reader](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=internet), you must register the reader to your platform account.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const reader = await stripe.terminal.readers.create({
  registration_code: "{{READER_REGISTRATION_CODE}}",
  label: "Alice's reader",
  location: "{{TERMINALLOCATION_ID}}",
});
```

## Create connection tokens (Server-side)

When creating a `ConnectionToken` for the Terminal SDK, use your platform account’s secret key. Don’t set the `Stripe-Account` header. Provide a `location` parameter to control access to readers. If you provide a location, the `ConnectionToken` is only usable with readers assigned to that location. If you don’t provide a location, the `ConnectionToken` is usable with all readers.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const connectionToken = await stripe.terminal.connectionTokens.create({
  location: "{{TERMINALLOCATION_ID}}",
});
```

If you’re using a server-driven integration, you don’t need to create a connection token.

## Create PaymentIntents (Client-side) (Server-side)

When creating a `PaymentIntent` using destination charges, provide the [on_behalf_of](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-on_behalf_of) and [transfer_data[destination]](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-transfer_data-destination), and [application_fee_amount](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-application_fee_amount) parameters.

The `on_behalf_of` parameter is the ID of the connected account that becomes the settlement merchant for the payment. For Terminal transactions, you must set this parameter if the platform country isn’t the same as the connected account country. When you set `on_behalf_of`, Stripe automatically:

- Settles charges in the country of the specified account, minimizing declines and avoiding currency conversions.
- Uses the fee structure for the connected account’s country.
- Lists the connected account’s address and phone number instead of your platform’s address and phone number on the customer’s credit card statement. (Only if the account and platform are in different countries.)

For `transfer_data[destination]`, set the ID of the connected account that receives the transfer.

Finally, you can withhold an application fee for your platform by providing the [application_fee_amount](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-application_fee_amount) parameter.

### Client-side

With the iOS, Android, and React Native SDKs, you can create a `PaymentIntent` client-side and provide the `onBehalfOf`, `transferDataDestination`, and `applicationFeeAmount` parameters.

#### JavaScript

> Client-side `PaymentIntent` creation is possible with the other SDKs. If you’re using the JavaScript SDK for Stripe Terminal, create a `PaymentIntent` server-side.

#### iOS

- [PaymentIntentParameters (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPPaymentIntentParameters.html)

> If your app is connected to the Verifone P400, you can’t create a `PaymentIntent` from the iOS SDK.
>
> Instead, you must [create the PaymentIntent server-side](https://docs.stripe.com/terminal/payments/collect-card-payment.md#create-server-side), and retrieve the `PaymentIntent` in your app using the `Terminal.retrievePaymentIntent` method in the SDK.

#### Swift

```swift
import UIKit
import StripeTerminal

class PaymentViewController: UIViewController {

    // ...

    // Action for a "Checkout" button
    func checkoutAction() throws {
        let params = try PaymentIntentParametersBuilder(amount: 1000, currency: "sgd")
            .setOnBehalfOf(""{{CONNECTED_ACCOUNT_ID}}"")
            .setTransferDataDestination(""{{CONNECTED_ACCOUNT_ID}}"")
            .setApplicationFeeAmount(200)
            .build()
        Terminal.shared.createPaymentIntent(params) { createResult, createError in
            if let error = createError {
                print("createPaymentIntent failed: \(error)")
            }
            else if let paymentIntent = createResult {
                print("createPaymentIntent succeeded")
                // ...
            }

        }
    }

    // ...
}
```

#### Android

- [PaymentIntentParameters (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-payment-intent-parameters/index.html)

> If your app is connected to the Verifone P400, you can’t create a `PaymentIntent` from the Android SDK.
>
> Instead, you must [create the PaymentIntent server-side](https://docs.stripe.com/terminal/payments/collect-card-payment.md#create-server-side), and retrieve the `PaymentIntent` in your app using the `Terminal.retrievePaymentIntent` method in the SDK.

#### Kotlin

```kotlin
    val params = PaymentIntentParameters.Builder()
        .setAmount(1000)
        .setCurrency("sgd")
        .setOnBehalfOf(""{{CONNECTED_ACCOUNT_ID}}"")
        .setTransferDataDestination(""{{CONNECTED_ACCOUNT_ID}}"")
        .setApplicationFeeAmount(200)
        .build()
    Terminal.getInstance().createPaymentIntent(
        params,
        object : PaymentIntentCallback {
            override fun onSuccess(paymentIntent: PaymentIntent) {
                // Placeholder for handling successful operation
            }

            override fun onFailure(e: TerminalException) {
                // Placeholder for handling exception
            }
        }
    )
```

#### React Native

- [CreatePaymentIntentParams (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/index.html#CreatePaymentIntentParams)

> If your app is connected to the Verifone P400, you can’t create a `PaymentIntent` from the React Native SDK.
>
> Instead, you must [create the PaymentIntent server-side](https://docs.stripe.com/terminal/payments/collect-card-payment.md#create-server-side), and retrieve the `PaymentIntent` in your app using the `retrievePaymentIntent` method in the SDK.

```js
const { paymentIntent, error } = await createPaymentIntent({
  amount: 1000,
  currency: "sgd",
  onBehalfOf: "{{CONNECTED_ACCOUNT_ID}}",
  transferDataDestination: "{{CONNECTED_ACCOUNT_ID}}",
  applicationFeeAmount: 200,
});

if (error) {
  // Placeholder for handling exception
  return;
}

// Placeholder for collecting a payment method with PaymentIntent
```

### Server-side

The JavaScript SDK requires you to create the `PaymentIntent` on your server. For the other client SDKs, you want to create the `PaymentIntent` on your server if the information required to start a payment isn’t readily available in your app. For more information, see [Create PaymentIntents Server-side](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=js#create-payment).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: "usd",
  payment_method_types: ["card_present"],
  capture_method: "manual",
  application_fee_amount: 200,
  on_behalf_of: "{{CONNECTEDACCOUNT_ID}}",
  transfer_data: {
    destination: "{{CONNECTEDACCOUNT_ID}}",
  },
});
```

Then follow the steps to [collect a payment](https://docs.stripe.com/terminal/payments/collect-card-payment.md) to process the PaymentIntent.

# Separate charges and transfers

> This is a Separate charges and transfers for when connect-charge-type is separate. View the full page at https://docs.stripe.com/terminal/features/connect?connect-charge-type=separate.

When using [separate charges and transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md), your platform owns API resources like [PaymentIntents](https://docs.stripe.com/api/payment_intents.md) and [locations](https://docs.stripe.com/api/terminal/locations.md). You create a charge on your platform’s account first, then create separate transfers to move funds to your connected accounts. This allows you to split payments between multiple connected accounts.

In the Dashboard, you can view your Terminal data directly when logged into your platform account.

## Create locations and readers (Server-side)

Group `Reader` objects by connected account by assigning them to `locations`. On your platform account, [create a location](https://docs.stripe.com/terminal/fleet/locations-and-zones.md?dashboard-or-api=dashboard#create-locations-and-zones) for a connected account using a display name that identifies the account.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "1272 Valencia Street",
    city: "San Francisco",
    state: "CA",
    country: "US",
    postal_code: "94110",
  },
});
```

Before you can connect your application to a [smart reader](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=internet), you must register the reader to your platform account.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const reader = await stripe.terminal.readers.create({
  registration_code: "{{READER_REGISTRATION_CODE}}",
  label: "Alice's reader",
  location: "{{TERMINALLOCATION_ID}}",
});
```

## Create connection tokens (Server-side)

When creating a `ConnectionToken` for the Terminal SDK, use your platform account’s secret key. Don’t set the `Stripe-Account` header. Provide a `location` parameter to control access to readers. If you provide a location, the `ConnectionToken` is only usable with readers assigned to that location. If you don’t provide a location, the `ConnectionToken` is usable with all readers.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const connectionToken = await stripe.terminal.connectionTokens.create({
  location: "{{TERMINALLOCATION_ID}}",
});
```

If you’re using a server-driven integration, you don’t need to create a connection token.

## Create PaymentIntents (Server-side)

Create a `PaymentIntent` on your platform account. You can optionally provide a `transfer_group` parameter to identify related payments and transfers for tracking purposes.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: "usd",
  payment_method_types: ["card_present"],
  capture_method: "manual",
  transfer_group: "ORDER_95",
});
```

Then follow the steps to [collect a payment](https://docs.stripe.com/terminal/payments/collect-card-payment.md) to process the PaymentIntent.

## Create transfers (Server-side)

After you capture the `PaymentIntent`, you can create one or more [transfers](https://docs.stripe.com/api/transfers.md) to move funds to your connected accounts.

Create a transfer specifying the connected account as the destination. You can optionally include the `transfer_group` to associate the transfer with the original payment:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const transfer = await stripe.transfers.create({
  amount: 700,
  currency: "usd",
  destination: "{{CONNECTEDACCOUNT_ID}}",
  transfer_group: "ORDER100",
});
```

### Transfer availability

By default, a transfer request fails when the amount exceeds your platform’s available account balance. To avoid this, you can tie the transfer to the specific charge by using the [source_transaction](https://docs.stripe.com/api/transfers/create.md#create_transfer-source_transaction) parameter. This allows the transfer request to succeed even if the funds haven’t settled yet in your available balance. The transfer executes automatically when the funds from the associated charge become available.

To use a `source_transaction`, first retrieve the charge ID from the PaymentIntent’s [latest_charge](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-latest_charge) attribute:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const transfer = await stripe.transfers.create({
  amount: 700,
  currency: "usd",
  destination: "{{CONNECTEDACCOUNT_ID}}",
  source_transaction: "{{CHARGE_ID}}",
  transfer_group: "ORDER100",
});
```

### Split payments between multiple accounts

To split a payment between multiple connected accounts, create separate transfers for each account:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const transfer = await stripe.transfers.create({
  amount: 400,
  currency: "usd",
  destination: "{{CONNECTEDACCOUNT_ID}}",
  transfer_group: "ORDER100",
});
```

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const transfer = await stripe.transfers.create({
  amount: 300,
  currency: "usd",
  destination: "{{OTHER_CONNECTED_ACCOUNT_ID}}",
  transfer_group: "ORDER100",
});
```

## See also

- [Cart display](https://docs.stripe.com/terminal/features/display.md)
- [Receipts](https://docs.stripe.com/terminal/features/receipts.md)
