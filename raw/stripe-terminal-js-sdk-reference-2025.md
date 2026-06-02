<!-- Source URL: https://docs.stripe.com/terminal/references/api/js-sdk -->
<!-- Fetched: 2026-05-01 -->

# JavaScript API reference

Use our API reference to navigate the Stripe Terminal JavaScript SDK.

## API methods

- [StripeTerminal.create()](https://docs.stripe.com/terminal/references/api/js-sdk.md#stripeterminal-create)
- [discoverReaders()](https://docs.stripe.com/terminal/references/api/js-sdk.md#discover-readers)
- [connectReader()](https://docs.stripe.com/terminal/references/api/js-sdk.md#connect-reader)
- [disconnectReader()](https://docs.stripe.com/terminal/references/api/js-sdk.md#disconnect)
- [getConnectionStatus()](https://docs.stripe.com/terminal/references/api/js-sdk.md#get-connection-status)
- [getPaymentStatus()](https://docs.stripe.com/terminal/references/api/js-sdk.md#get-payment-status)
- [clearCachedCredentials()](https://docs.stripe.com/terminal/references/api/js-sdk.md#clear-cached-credentials)
- [collectPaymentMethod()](https://docs.stripe.com/terminal/references/api/js-sdk.md#collect-payment-method)
- [cancelCollectPaymentMethod()](https://docs.stripe.com/terminal/references/api/js-sdk.md#cancel-collect-payment-method)
- [processPayment()](https://docs.stripe.com/terminal/references/api/js-sdk.md#process-payment)
- [cancelProcessPayment()](https://docs.stripe.com/terminal/references/api/js-sdk.md#cancel-process-payment)
- [collectSetupIntentPaymentMethod()](https://docs.stripe.com/terminal/references/api/js-sdk.md#collect-setup-intent-payment-method)
- [cancelCollectSetupIntentPaymentMethod()](https://docs.stripe.com/terminal/references/api/js-sdk.md#cancel-collect-setup-intent-payment-method)
- [confirmSetupIntent()](https://docs.stripe.com/terminal/references/api/js-sdk.md#confirm-setup-intent)
- [cancelConfirmSetupIntent()](https://docs.stripe.com/terminal/references/api/js-sdk.md#cancel-confirm-setup-intent)
- [readReusableCard()](https://docs.stripe.com/terminal/references/api/js-sdk.md#read-reusable-card)
- [cancelReadReusableCard()](https://docs.stripe.com/terminal/references/api/js-sdk.md#cancel-read-reusable-card)
- [setReaderDisplay()](https://docs.stripe.com/terminal/references/api/js-sdk.md#set-reader-display)
- [clearReaderDisplay()](https://docs.stripe.com/terminal/references/api/js-sdk.md#clear-reader-display)
- [setSimulatorConfiguration()](https://docs.stripe.com/terminal/references/api/js-sdk.md#stripeterminal-setsimulatorconfig)
- [getSimulatorConfiguration()](https://docs.stripe.com/terminal/references/api/js-sdk.md#stripeterminal-getsimulatorconfig)
- [collectRefundPaymentMethod()](https://docs.stripe.com/terminal/references/api/js-sdk.md#stripeterminal-collectrefundpaymentmethod)
- [cancelCollectRefundPaymentMethod()](https://docs.stripe.com/terminal/references/api/js-sdk.md#stripeterminal-cancelcollectrefundpaymentmethod)
- [processRefund()](https://docs.stripe.com/terminal/references/api/js-sdk.md#stripeterminal-processrefund)
- [cancelProcessRefund()](https://docs.stripe.com/terminal/references/api/js-sdk.md#stripeterminal-cancelprocessrefund)
- [collectInputs()](https://docs.stripe.com/terminal/references/api/js-sdk.md#collect-inputs)
- [cancelCollectInputs()](https://docs.stripe.com/terminal/references/api/js-sdk.md#cancel-collect-inputs)
- [print()](https://docs.stripe.com/terminal/references/api/js-sdk.md#print)

### StripeTerminal.create([options])

Creates an instance of `StripeTerminal` with the given options:

| Option                                  | Description                                                                                                                                                                     |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **onFetchConnectionToken**              | An event handler that [fetches a connection token](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=js#connection-token) from your backend. |
| **onUnexpectedReaderDisconnect**        | An event handler called when a reader disconnects from your app.                                                                                                                |
| **onConnectionStatusChange** (optional) | An event handler called when the SDK’s ConnectionStatus changes.                                                                                                                |
| **onPaymentStatusChange** (optional)    | An event handler called when the SDK’s PaymentStatus changes.                                                                                                                   |
| **readerBehavior** (optional)           | An object that sets the behavior on the reader throughout the lifecycle of the SDK. See below for readerBehavior configuration options.                                         |

### Reader Behavior Configuration

Today, there is only one behavior configuration option:

| Behavior                | Description                                                                                                                        |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **allowCustomerCancel** | A Boolean that determines whether the customer can cancel `collectPaymentMethod` from the reader’s interface. Defaults to `false`. |

**Note:** This property isn’t broadly available, and we’re not accepting users at this time. |

### discoverReaders([options])

Begins discovering readers with the given options:

| Option                   | Description                                                                                                                                                                                  |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **simulated** (optional) | A Boolean value indicating whether to discover a [simulated reader](https://docs.stripe.com/terminal/references/testing.md#simulated-reader). If left empty, this value defaults to `false`. |
| **location** (optional)  | Return only readers assigned to the given `location`. This parameter is ignored when discovering a simulated reader.                                                                         |

For more information on using locations to filter discovered readers, see [Manage locations](https://docs.stripe.com/terminal/fleet/locations-and-zones.md). |

Returns a `Promise` that resolves to an object with the following fields:

- `discoveredReaders`: A list of discovered [Reader](https://docs.stripe.com/api/terminal/readers/object.md) objects, if the command succeeded.
- `error`: An [error](https://docs.stripe.com/terminal/references/api/js-sdk.md#errors), if the command failed.

> Before you can discover the Verifone P400 in your application, you must [register](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=internet#register-reader) the reader to your account.

### connectReader(reader, connectOptions)

Attempts to [connect](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=internet#connect-reader) to the given reader with the given options:

| Option                        | Description                                                                                                                                                 |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **fail_if_in_use** (optional) | A Boolean value indicating that the connection fails if the reader is currently connected to a Terminal SDK. If left empty, this value defaults to `false`. |

Returns a `Promise` that resolves to an object with the following fields:

- `reader`: The connected [Reader](https://docs.stripe.com/api/terminal/readers/object.md), if the command succeeded.
- `error`: An [error](https://docs.stripe.com/terminal/references/api/js-sdk.md#errors), if the command failed.

> Don’t cache the `Reader` object in your application. Connecting to a stale `Reader` can fail if the reader’s IP address has changed.

### disconnectReader()

Disconnects from the connected reader.

### getConnectionStatus()

Returns the current connection status.

ConnectionStatus can be one of `connecting`, `connected`, or `not_connected`.

### getPaymentStatus()

Returns the reader’s payment status.

PaymentStatus can be one of `not_ready`, `ready`, `waiting_for_input`, or `processing`.

### clearCachedCredentials()

Clears the current [ConnectionToken](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=js#connection-token), and any other cached credentials.

Use this method to switch accounts in your application (for example, to switch between live and test Stripe API keys on your backend). To switch accounts, follow these steps:

1. If a reader is connected, call `disconnectReader`.
1. Configure your `onFetchConnectionToken` handler to return connection tokens for the new account.
1. Call `clearCachedCredentials`.
1. Reconnect to a reader. The SDK requests a new connection token from your `onFetchConnectionToken` handler.

### collectPaymentMethod(request, options)

Begins [collecting a payment method](https://docs.stripe.com/terminal/payments/collect-card-payment.md#collect-payment) for a PaymentIntent. This method takes one required parameter, `request`:

- `request`: The `clientSecret` field from a `PaymentIntent` object created on your backend. Learn how to [create a PaymentIntent and pass its client secret](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=elements&api-integration=paymentintents#web-create-intent).
- `options`: An object containing additional payment parameters.

| Option                         | Description                                                                                                 |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------- |
| **config_override** (optional) | An object that allows you to specify configuration overrides per transaction. This object defaults to null. |

`skip_tipping`

- Optional, defaults to false. If true, the reader skips the tipping screen.

`tipping`

- An object that allows you to specify tipping-related options per transaction. It’s described below.

`update_payment_intent`

- A Boolean, when paired with `payment_intent_id`, instructs the call to update the `PaymentIntent` and return the attached `PaymentMethod` with card details.

`enable_customer_cancellation`

- Optional, defaults to false. If true, Android-based smart readers show a cancel button.

`allow_redisplay`

- Required if `setup_future_usage` is set; otherwise, it defaults to `unspecified`. An enum value indicating whether future checkout flows can show this payment method to its customer.

`moto`

- Optional, defaults to false. If true, Android-based smart readers start collection for a [mail order or telephone order](https://docs.stripe.com/terminal/features/mail-telephone-orders/payments.md) transaction.

````json
{
  update_payment_intent: boolean,
  payment_intent_id: string,
  enable_customer_cancellation: boolean,
  skip_tipping: boolean,
  tipping: object,
  allow_redisplay: string,
  moto: boolean,
}
``` |

The following option is available for the `tipping` object:

| Option                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **eligible\_amount** (optional) | A number that allows you to specify the amount of a transaction that percentage-based tips are calculated against. Set this value to 0 or higher.

If it’s equal to 0, tipping is skipped regardless of the value of `skip_tipping`.

If it’s equal to the PaymentIntent amount, the parameter is ignored and the tip is calculated based on the specified amount.

```json
{
  eligible_amount: number,
}
``` |

Returns a `Promise` that resolves to an object with the following fields:

- `paymentIntent`: The updated [PaymentIntent object](https://docs.stripe.com/api/payment_intents/object.md), if the command succeeded.
- `error`: An [error](https://docs.stripe.com/terminal/references/api/js-sdk.md#errors), if the command failed.

For more information on collecting payments, see our [Collecting Payments](https://docs.stripe.com/terminal/payments/collect-card-payment.md) guide.

### cancelCollectPaymentMethod()

Cancels an outstanding [collectPaymentMethod](https://docs.stripe.com/terminal/references/api/js-sdk.md#collect-payment-method) command.

Returns a `Promise` that resolves to an empty object when the command has been successfully canceled. If the cancellation fails, the `Promise` resolves to an object with an [error](https://docs.stripe.com/terminal/references/api/js-sdk.md#errors).

### processPayment(paymentIntent, options)

[Processes](https://docs.stripe.com/terminal/payments/collect-card-payment.md#process-payment) a payment after a payment method has been [collected](https://docs.stripe.com/terminal/payments/collect-card-payment.md#collect-payment).

This method takes one required parameter, `paymentIntent`:

- `paymentIntent`: A `PaymentIntent` object obtained from a successful call to `collectPaymentMethod`.
- `options`: An object containing additional payment parameters.

| Option                          | Description                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **config\_override** (optional) | An object that allows you to specify configuration overrides per transaction. This object defaults to null.

`return_url`

- The URL to redirect your customer back to after they authenticate or cancel their payment on the payment method’s app or site. We only use this parameter for redirect-based payment methods. The default is null.

```json
{
  return_url: string,
}
``` |

Returns a `Promise` that resolves to an object with the following fields:

- `paymentIntent`: The confirmed [PaymentIntent object](https://docs.stripe.com/api/payment_intents/object.md), if the command succeeded.
- `error`: An [error](https://docs.stripe.com/terminal/references/api/js-sdk.md#errors), if the command failed. For more information, see [Handling processing failures](https://docs.stripe.com/terminal/payments/collect-card-payment.md#handling-failures).

### cancelProcessPayment()

Cancels an outstanding [processPayment](https://docs.stripe.com/terminal/references/api/js-sdk.md#process-payment) command.

Returns a `Promise` that resolves to an empty object when the command has been successfully canceled. If the cancellation fails, the `Promise` resolves to an object with an [error](https://docs.stripe.com/terminal/references/api/js-sdk.md#errors).

### collectSetupIntentPaymentMethod(clientSecret, allowRedisplay, config)

Begins [collecting a payment method for online reuse](https://docs.stripe.com/terminal/features/saving-payment-details/overview.md) for a [SetupIntent](https://docs.stripe.com/api/setup_intents/object.md).

The method takes two required parameters:

- `clientSecret`: The `clientSecret` field from a `SetupIntent` object created on your backend.

- `allowRedisplay`: An enum value indicating whether future checkout flows can show this payment method to its customer.

- `config`: an optional object containing collection configuration.

| Option                             | Description                                                                                                                                                                                                 |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **enable\_customer\_cancellation** | Optional, defaults to false.

If true, Android-based smart readers show a cancel button.                                                                                                                  |
| **moto**                           | Optional, defaults to false.

If true, Android-based smart readers start saving a [mail order or telephone order](https://docs.stripe.com/terminal/features/mail-telephone-orders/save-directly.md) card. |

Returns a `Promise` that resolves to an object with the following fields:

- `setupIntent`: The updated [SetupIntent object](https://docs.stripe.com/api/setup_intents/object.md), if the command succeeded.
- `error`: An [error](https://docs.stripe.com/terminal/references/api/js-sdk.md#errors), if the command failed.

For more information on saving payment methods, see our [Saving payment details for online payments](https://docs.stripe.com/terminal/features/saving-payment-details/overview.md) guide.

### cancelCollectSetupIntentPaymentMethod()

Cancels an outstanding [collectSetupIntentPaymentMethod](https://docs.stripe.com/terminal/references/api/js-sdk.md#collect-setup-intent-payment-method) command.

Returns a `Promise` that resolves to an empty object when the command has been successfully canceled. If the cancellation fails, the `Promise` resolves to an object with an [error](https://docs.stripe.com/terminal/references/api/js-sdk.md#errors).

### confirmSetupIntent(setupIntent)

[Confirms](https://docs.stripe.com/terminal/features/saving-payment-details/save-directly.md#submit-payment-method) a SetupIntent after a payment method has been [collected](https://docs.stripe.com/terminal/features/saving-payment-details/save-directly.md#collect-payment-method).

This method takes a single parameter, a `SetupIntent` object obtained from a successful call to `collectSetupIntentPaymentMethod`.

Returns a `Promise` that resolves to an object with the following fields:

- `setupIntent`: The confirmed [SetupIntent object](https://docs.stripe.com/api/setup_intents/object.md), if the command succeeded.
- `error`: An [error](https://docs.stripe.com/terminal/references/api/js-sdk.md#errors), if the command failed.

### cancelConfirmSetupIntent()

Cancels an outstanding [confirmSetupIntent](https://docs.stripe.com/terminal/references/api/js-sdk.md#confirm-setup-intent) command.

Returns a `Promise` that resolves to an empty object when the command has been successfully canceled. If the cancellation fails, the `Promise` resolves to an object with an [error](https://docs.stripe.com/terminal/references/api/js-sdk.md#errors).

### readReusableCard()

Reads a card for [online reuse](https://docs.stripe.com/terminal/features/saving-payment-details/overview.md).

Online payments initiated from Terminal do *not* benefit from the [lower pricing](https://stripe.com/terminal#pricing) and *liability shift* (With some 3D Secure transactions, the liability for fraudulent chargebacks (stolen or counterfeit cards) shifts from you to the card issuer) given to [standard Terminal payments](https://docs.stripe.com/terminal/payments/collect-card-payment.md). Most integrations do *not* need to use `readReusableCard`. To only collect an in-person payment from a customer, use the [standard flow](https://docs.stripe.com/terminal/payments/collect-card-payment.md).

Returns a `Promise` that resolves to an object with the following fields:

- `payment_method`: The [PaymentMethod object](https://docs.stripe.com/api/payment_methods/object.md), if the command succeeded.
- `error`: An [error](https://docs.stripe.com/terminal/references/api/js-sdk.md#errors), if the command failed.

> Currently, you can’t use Stripe Terminal to save contactless cards and mobile wallets (for example, Apple Pay, Google Pay) for later reuse.

### cancelReadReusableCard()

Cancels an outstanding [readReusableCard](https://docs.stripe.com/terminal/references/api/js-sdk.md#read-reusable-card) command.

Returns a `Promise` that resolves to an empty object when the command has been successfully canceled. If the cancellation fails, the `Promise` resolves to an object with an [error](https://docs.stripe.com/terminal/references/api/js-sdk.md#errors).

### setReaderDisplay(displayInfo)

Updates the reader display with [cart details](https://docs.stripe.com/terminal/features/display.md).

This method takes a `DisplayInfo` object as input.

```json
{
type: 'cart',
cart: {
  line_items: [
    {
      description: string,
      amount: number,
      quantity: number,
    },
  ],
  tax: number,
  total: number,
  currency: string,
}
}
````

Returns a `Promise` that resolves to an empty object if the command succeeds. If the command fails, the `Promise` resolves to an object with an [error](https://docs.stripe.com/terminal/references/api/js-sdk.md#errors).

### clearReaderDisplay()

If the reader is displaying cart details set with `setReaderDisplay`, this method clears the screen and resets it to the splash screen.

Returns a `Promise` that resolves to an empty object if the command succeeds. If the command fails, the `Promise` resolves to an object with an [error](https://docs.stripe.com/terminal/references/api/js-sdk.md#errors).

### setSimulatorConfiguration(configuration)

Sets the configuration object for the [simulated card reader](https://docs.stripe.com/terminal/references/testing.md#simulated-reader).

This method only takes effect when connected to the simulated reader; it performs no action otherwise.

The simulated reader will follow the specified configuration only until `processPayment` is complete. At that point, the simulated reader will revert to its default behavior.

Note that this method overwrites any currently active configuration object; to add specific key-value pairs to the object, make sure to use a combination of this method and `getSimulatorConfiguration`.

The configuration options available are:

| Field                   | Values                                                                                                                 | Description                                                                                                                                                                                                                                             |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **testCardNumber**      | Refer to the [Simulated test cards](https://docs.stripe.com/terminal/references/testing.md#simulated-test-cards) list. | Configures the simulated reader to use a test card number as the payment method presented by the user. Use it to test different scenarios in your integration, such as payments with different card brands or processing errors like a declined charge. |
| **testPaymentMethod**   | Refer to the [Simulated test cards](https://docs.stripe.com/terminal/references/testing.md#simulated-test-cards) list. | Serves the same purpose as `testCardNumber`, but relies on test payment methods instead.                                                                                                                                                                |
| **tipAmount**           | Any amount or null.                                                                                                    | Configures the simulated reader to simulate an on-reader tip amount selected by the customer.                                                                                                                                                           |
| **collectInputsResult** | We support testing the following behaviors:                                                                            |

- Succeeded:
  - Not skipping inputs: `{ resultType: 'succeeded', skipBehavior: 'none' }`
  - Skipping non-required inputs: `{ resultType: 'succeeded', skipBehavior: 'all' }`
- Timeout: `{ resultType: 'timeout' }`

See [Test your integration](https://docs.stripe.com/terminal/features/collect-inputs.md?terminal-sdk-platform=js#test-your-integration) for more details. | Configures the simulated reader to simulate [collecting inputs](https://docs.stripe.com/terminal/features/collect-inputs.md?terminal-sdk-platform=js). |
| **paymentMethodType** (deprecated) | - `card_present` (default)

- `interac_present` | Determine the type of payment method created by the simulated reader when `collectPaymentMethod` is called. |

### getSimulatorConfiguration()

Returns the currently active configuration object.

The Stripe Terminal JavaScript SDK might overwrite this value as necessary, including (but not limited to) resetting the value after processPayment is complete, and removing unknown key-value pairs.

### collectRefundPaymentMethod(charge_id, amount, currency, options, config)

Begins collecting a payment method to be refunded. The method takes two required parameters:

- `charge_id`, the ID of the charge that will be refunded.
- `amount`: a number that represents the amount, in cents, that will be refunded from the charge. This number must be less than or equal to the amount that was charged in the original payment.
- `currency`: Three-letter [ISO code for the currency](https://docs.stripe.com/currencies.md), in lowercase. Must be a [supported currency](https://docs.stripe.com/currencies.md).
- `options`: an optional object containing additional refund parameters.

| Option                     | Description                                |
| -------------------------- | ------------------------------------------ |
| **refund_application_fee** | Optional, defaults to false. Connect only. |

Boolean indicating whether the application fee should be refunded when refunding this charge. If a full charge refund is given, the full application fee will be refunded. Otherwise, the application fee will be refunded in an amount proportional to the amount of the charge refunded.

An application fee can be refunded only by the application that created the charge. |
| **reverse_transfer** | Optional, defaults to false. Connect only.

Boolean indicating whether the transfer should be reversed when refunding this charge. The transfer will be reversed proportionally to the amount being refunded (either the entire or partial amount).

A transfer can be reversed only by the application that created the charge. |

- `config`: an optional object containing collection configuration.

| Option                           | Description                  |
| -------------------------------- | ---------------------------- |
| **enable_customer_cancellation** | Optional, defaults to false. |

If true, Android-based smart readers show a cancel button. |

Returns a `Promise` that resolves to either:

- an empty object if the payment method collection was successful, or
- an object with an [error](https://docs.stripe.com/terminal/references/api/js-sdk.md#errors) field if there was an error while collecting the refund payment method.

### cancelCollectRefundPaymentMethod()

Cancels an outstanding `collectRefundPaymentMethod` command.

Returns a `Promise` that resolves to an empty object when the command has been successfully canceled. If the cancellation fails, the `Promise` resolves to an object with an [error](https://docs.stripe.com/terminal/references/api/js-sdk.md#errors).

### processRefund()

Processes an in-progress refund. This method can only be successfully called after `collectRefundPaymentMethod` has returned successfully.

Returns a `Promise` that resolves to either:

- a refund object if the refund was successful, or
- an object with an [error](https://docs.stripe.com/terminal/references/api/js-sdk.md#errors) field if there was an error while processing the refund.

### cancelProcessRefund()

Cancels an outstanding [processRefund](https://docs.stripe.com/terminal/references/api/js-sdk.md#stripeterminal-processrefund) command.

Returns a `Promise` that resolves to an empty object when the command has been successfully canceled. If the cancellation fails, the `Promise` resolves to an object with an [error](https://docs.stripe.com/terminal/references/api/js-sdk.md#errors).

### collectInputs(collectInputsParameters)

Start displaying forms and collecting information from customers using [collect inputs](https://docs.stripe.com/terminal/features/collect-inputs.md).

This method takes a `ICollectInputsParameters` object as input.

Returns a `Promise` that resolves to the collected results if the command succeeds. If the command fails, the `Promise` resolves to an object with an [error](https://docs.stripe.com/terminal/references/api/js-sdk.md#errors).

### cancelCollectInputs()

Cancels an outstanding `collectInputs` command.

Returns a `Promise` that resolves to an empty object if the cancellation succeeds. If the command fails, the `Promise` resolves to an object with an [error](https://docs.stripe.com/terminal/references/api/js-sdk.md#errors).

### print(content)

> Printing is only available on the [Verifone V660p](https://stripe.com/terminal/v660p) reader. See the [integration guide](https://docs.stripe.com/terminal/features/print-content.md?terminal-sdk-platform=js) for more details.

Prints the specified content to the connected reader’s printer, if available. This method takes one required parameter, `content`:

- `content`: The content to be printed. This must be a `HTMLCanvasElement` object.

Returns a `Promise` that resolves to an empty object if the print command succeeds. If the command fails, the `Promise` resolves to an object with an [error](https://docs.stripe.com/terminal/references/api/js-sdk.md#errors).

## Errors

Errors returned by the JavaScript SDK include an error `code`, as well as a human-readable `message`.

For methods involving a PaymentIntent like [processPayment](https://docs.stripe.com/terminal/payments/collect-card-payment.md#handling-failures), the error may also include a `payment_intent` object.

#### Error codes

| Code                                       | Description                                                                                                                                                                          |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `no_established_connection`                | The command failed because no reader is connected.                                                                                                                                   |
| `no_active_collect_payment_method_attempt` | `cancelCollectPaymentMethod` can only be called when `collectPaymentMethod` is in progress.                                                                                          |
| `no_active_read_reusable_card_attempt`     | `cancelCollectReusableCard` can only be called when `readReusableCard` is in progress.                                                                                               |
| `canceled`                                 | The command was canceled.                                                                                                                                                            |
| `cancelable_already_completed`             | Cancellation failed because the operation has already completed.                                                                                                                     |
| `cancelable_already_canceled`              | Cancellation failed because the operation has already been canceled.                                                                                                                 |
| `network_error`                            | An unknown error occurred when communicating with the server or reader over the network. Refer to the error message for more information.                                            |
| `network_timeout`                          | The request timed out when communicating with the server or reader over the network. Make sure both your device and the reader are connected to the network with stable connections. |
| `already_connected`                        | `connectReader` failed because a reader is already connected.                                                                                                                        |
| `failed_fetch_connection_token`            | Failed to fetch a connection token. Make sure your connection token handler returns a promise that resolves to the connection token.                                                 |
| `discovery_too_many_readers`               | `discoverReaders` returned too many readers. Use [Locations](https://docs.stripe.com/terminal/fleet/locations-and-zones.md) to filter discovered readers by location.                |
| `invalid_reader_version`                   | The reader is running an unsupported software version. Please allow the reader to update and try again.                                                                              |
| `reader_error`                             | The reader returned an error while processing the request. Refer to the error message for more information.                                                                          |
| `command_already_in_progress`              | The action can’t be performed, because an in-progress action is preventing it.                                                                                                       |
| `printer_busy`                             | Another print operation is already in progress.                                                                                                                                      |
| `printer_paperjam`                         | The printer has a paper jam. Open the printer’s cover and manually clear the paper jam.                                                                                              |
| `printer_cover_open`                       | The printer’s cover or head assembly is open.                                                                                                                                        |
| `printer_out_of_paper`                     | The printer is out of paper.                                                                                                                                                         |
| `printer_absent`                           | The reader doesn’t have a printer.                                                                                                                                                   |
| `printer_unavailable`                      | The reader has a printer but it’s currently unavailable.                                                                                                                             |
| `printer_error`                            | The print operation failed for an unspecified reason.                                                                                                                                |

## Changelog

If you’re using an earlier version of the JavaScript SDK (before June 7, 2019), update to the latest release by changing the URL of the script your integration includes.

```html
<script src="https://js.stripe.com/terminal/v1/"></script>
```

For more information on migrating from the Stripe Terminal beta, see the [Terminal Beta Migration Guide](https://docs.stripe.com/terminal/references/sdk-migration-guide.md).

#### 2025-10-30

- Update: Added support for surcharge consent collection in `processPayment`. You can now display a surcharge consent screen on the reader and include a customized message that’s up to 220 characters long.

#### 2025-10-06

- Preview: Added a `print` method to enable printing images on the Verifone V660p reader.
  - If you’re interested in joining the preview, contact [Stripe support](https://support.stripe.com/).

#### 2025-06-02

- Update: Simulated readers support [input collection](https://docs.stripe.com/terminal/features/collect-inputs.md?terminal-sdk-platform=js#test-your-integration).
- Update: `processPayment`, `confirmSetupIntent`, and `processRefund` can now be canceled with `cancelProcessPayment`, `cancelConfirmSetupIntent`, and `cancelProcessRefund` respectively. This allows you to cancel the operation in certain scenarios, such as QR Code payment presentment.

#### v1

- Renamed `confirmPaymentIntent` to `processPayment`.
- Renamed the values for PaymentStatus. PaymentStatus can be one of `not_ready`, `ready`, `waiting_for_input`, or `processing`.
- Removed card details from the response to `collectPaymentMethod`, previously available in `response.paymentIntent.payment_method.card_payment`.
- Receipt information is now located in the `payment_intent.charges[0].payment_method_details.card_present` hash.
- Changed the API for discovering a simulated reader to `discoverReaders({ simulated: true })`.
- Renamed `readSource` to `readReusableCard`. A successful call to `readReusableCard` returns a [PaymentMethod](https://docs.stripe.com/api/payment_methods.md) instead of a Source. Payment Methods must be used with PaymentIntents. For more information, see the [Payment Methods API](https://docs.stripe.com/payments/payment-methods.md) overview.
- Changed the response of `connectReader` to `{ reader: Reader }`, removing the wrapper `Connection` object.
- Removed the `startReaderDiscovery` and `stopReaderDiscovery` methods. To repeatedly discover readers, you can use the JavaScript `setInterval` method.
- Renamed `clearConnectionToken` to `clearCachedCredentials`.
