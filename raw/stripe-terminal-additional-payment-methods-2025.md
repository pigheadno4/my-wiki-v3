<!-- Source: Stripe Terminal — Additional payment methods (QR code: WeChat Pay, Affirm, PayNow) -->
<!-- Fetched: 2026-04-24 -->

# Additional payment methods

Accept supported payment methods by displaying a QR code on Terminal readers.

In addition to cards, Terminal supports QR code-based [payment methods](https://docs.stripe.com/payments/payment-methods/overview.md). Your customers can scan a QR code to complete their checkout on their mobile devices.

**Supported payment methods**: [WeChat Pay](https://docs.stripe.com/payments/wechat-pay.md)1, [Affirm](https://docs.stripe.com/payments/affirm.md), and [PayNow](https://docs.stripe.com/payments/paynow.md)

**Supported readers**: [Smart readers](https://docs.stripe.com/terminal/smart-readers.md) and [Tap to Pay readers](https://docs.stripe.com/terminal/tap-to-pay-readers.md)

1WeChat Pay isn’t available for Terminal in Japan due to regional limitations.

> Connected accounts must have the [requisite capability](https://docs.stripe.com/connect/account-capabilities.md#payment-methods) to perform transactions for each payment method. Learn more about Connect compatibility with [Affirm](https://docs.stripe.com/payments/affirm.md#connect), [WeChat Pay](https://docs.stripe.com/payments/wechat-pay.md#connect), and [PayNow](https://docs.stripe.com/payments/paynow.md#connect).
>
> To test non-card payment methods on Stripe Terminal, use a physical reader. The simulated reader isn’t supported.
>
> All transactions must be made with a functional network connection, not while [offline](https://docs.stripe.com/terminal/features/operate-offline/overview.md).

## Smart readers and Tap to Pay on Android

- [setReaderDisplay (Android)](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/set-reader-display.html)

For [smart readers](https://docs.stripe.com/terminal/smart-readers.md) with built-in displays and [Tap to Pay on Android](https://docs.stripe.com/terminal/tap-to-pay-readers.md), the reader displays the QR code directly on its screen.

If you only want to accept non-card payment methods, the reader can bypass the **tap or insert** prompt used for card payment methods. If you’ve enabled a single non-card payment method, the reader loads the QR code directly. Otherwise, the reader displays a list of non-card payment method options.

> #### US-based readers
>
> In the United States, if you plan on deploying readers with only non-card payment methods, [displaying cart details](https://docs.stripe.com/terminal/features/display.md) isn’t supported at this time. Displaying cart details shows the NFC logo and supports pre-dipping cards to tokenize card details before a PaymentIntent is created.
> ![The collect payment method screen with button reading more ways to pay](assets/stripe-terminal-s700-more-ways-to-pay.png)

Collect payment method screen
![The payment method selection screen with buttons for paying with card, Affirm, or WeChat Pay](assets/stripe-terminal-s700-pay-with-screen.png)

Payment method selection screen
![The payment loading screen](assets/stripe-terminal-s700-loading-screen.png)

Loading screen
![The screen displaying a WeChat Pay QR code to scan](assets/stripe-terminal-s700-wechat-pay-qr-code.png)

Scan QR code screen
![The screen displaying Approved](assets/stripe-terminal-s700-approved-screen.png)

Approved screen

## Tap to Pay on iPhone

For [Tap to Pay on iPhone](https://docs.stripe.com/terminal/tap-to-pay-readers.md), your app must handle displaying the QR code. See the [implementation details](https://docs.stripe.com/terminal/payments/additional-payment-methods.md#handle-payment).

# Server-driven

> This is a Server-driven for when terminal-sdk-platform is server-driven. View the full page at https://docs.stripe.com/terminal/payments/additional-payment-methods?terminal-sdk-platform=server-driven.

## Create a PaymentIntent

To accept non-card payment methods through the QR code interface, [create a PaymentIntent](https://docs.stripe.com/api/payment_intents.md) and include your preferred payment method types in the `payment_method_types` parameter.

- To present your customer all payment method options in the checkout flow, combine `card_present` with non-card payment method types. We recommend enabling this if you operate in a heavily [offline](https://docs.stripe.com/terminal/features/operate-offline/overview.md) environment because only cards are supported in offline mode.
- If you don’t want to accept cards, support only non-card payment method types.
- If you know which payment method you want to direct your customer to checkout to, select a single payment method type.

### Capture type

Not all payment methods support [manual capture](https://docs.stripe.com/terminal/payments/collect-card-payment.md#capture-payment). The following table shows which payment methods support manual capture:

| Payment method | Manual capture   |
| -------------- | ---------------- |
| `card_present` | ✓ Supported      |
| `affirm`       | ✓ Supported      |
| `wechat_pay`   | ❌ Not supported |
| `paynow`       | ❌ Not supported |

To support the broadest set of payment methods, create your PaymentIntent with `capture_method` set to `automatic`. To support manual capture for card payments and Affirm while also accepting payment methods that require automatic capture, set `capture_method` on the nested `payment_method_options.card_present` attribute to `manual`.

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=1000 \
  -d currency=usd \
  -d "payment_method_types[]=card_present" \
  -d "payment_method_types[]=wechat_pay" \
  -d capture_method=automatic \
  -d "payment_method_options[card_present][capture_method]=manual"
```

## Handle the payment

Unlike card payments, processing QR code payments occurs asynchronously. When processing a PaymentIntent with a QR code payment method, Stripe generates a QR code unique to that payment.

After processing the payment, the reader displays the QR code for the customer to scan with their mobile device. Shortly after the customer completes the payment on their device, the reader updates to reflect the completed payment.

> The time it takes for the reader to display the result of the payment might differ depending on the payment method used. The reader usually updates after a few seconds.

QR code payments support both processing the payment immediately and the two-step collect-and-confirm flow.

#### Process immediately

- [Process a PaymentIntent](https://docs.stripe.com/api/terminal/readers/process_payment_intent.md)

To collect payment, make a request to Stripe with the ID of the PaymentIntent you created and the reader you want to use for the transaction.

Some payment methods (for example, Affirm) require a [return_url](https://docs.stripe.com/api/terminal/readers/process_payment_intent.md#process_payment_intent-process_config-return_url) when confirming a PaymentIntent to redirect your customer to after they authenticate or cancel their payment on the payment method’s app or site. You can provide your own [return_url](https://docs.stripe.com/api/terminal/readers/process_payment_intent.md#process_payment_intent-process_config-return_url) when processing the PaymentIntent. If you don’t provide one, the customer sees a [generic landing page](https://terminal-statics.stripe.com/terminal-checkout/assets/index.html) hosted by Stripe.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const reader = await stripe.terminal.readers.processPaymentIntent("tmr_xxx", {
  payment_intent: "pi_xxx",
  process_config: {
    return_url: "https://my.store.com/payment-completed",
  },
});
```

When you process a payment, Stripe immediately responds to the request with an HTTP `200` status code as an acknowledgement that the reader received the action. In most cases, the request returns a [reader](https://docs.stripe.com/api/terminal/readers.md) with an `in_progress` status. However, because processing occurs asynchronously, the action status might already reflect the final state (`succeeded` or `failed`) if the payment completes quickly.

Simultaneously, the reader screen switches to a UI that prompts the customer to insert their card or select a QR code payment method. For QR code payments, the customer completing the payment on their device updates the status of the payment. To [verify the reader state](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=server-driven#verify-reader), listen to the `terminal.reader.action_succeeded` webhook or poll the Reader and PaymentIntent status to receive the status of the payment.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const reader = await stripe.terminal.readers.retrieve("tmr_xxx");
```

```json
{
  "id": "tmr_xxx",
  "object": "terminal.reader",
  ...
  "status": "online",
  "action": {
    "type": "process_payment_intent",
    "process_payment_intent": {
      "payment_intent": "pi_xxx"
    },
    "status": "in_progress",
    "failure_code": null,
    "failure_message": null
  }
}
```

#### Collect, inspect, and confirm

### Collect a PaymentMethod

- [Collect a payment method](https://docs.stripe.com/api/terminal/readers/collect_payment_method.md)

To collect payment, make a request to Stripe with the ID of the PaymentIntent you created and the reader you want to use for the transaction.

When you start collecting a payment method, Stripe immediately responds to the request with an HTTP `200` status code and returns a [reader](https://docs.stripe.com/api/terminal/readers.md) with an action status of `in_progress`. Simultaneously, the reader screen switches to a UI that prompts the customer to insert their card or select a QR code payment method.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const reader = await stripe.terminal.readers.collectPaymentMethod("tmr_xxx", {
  payment_intent: "pi_xxx",
});
```

After the reader collects payment method data, the PaymentMethod attaches to the server-side PaymentIntent and it’s stored on the Reader object as `action.collect_payment_method.payment_method`. To [verify the reader state](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=server-driven#verify-reader), listen to the `terminal.reader.action_updated` or poll the Reader action status to inspect the PaymentMethod. At this point, you can determine the payment method type selected and see other data from the PaymentMethod.

### Process the PaymentIntent

- [Confirm a PaymentIntent](https://docs.stripe.com/api/terminal/readers/confirm_payment_intent.md)

After successfully collecting a payment method, you can proceed to processing the PaymentIntent.

Confirming the PaymentIntent is asynchronous. You can listen to the `terminal.reader.action_succeeded` webhook or poll the Reader and PaymentIntent status to receive the status of the payment.

Some payment methods (for example, Affirm) require a [return_url](https://docs.stripe.com/api/terminal/readers/process_payment_intent.md#confirm_payment_intent-confirm_config-return_url) when confirming a PaymentIntent to redirect your customer to after they authenticate or cancel their payment on the payment method’s app or site. You can provide your own [return_url](https://docs.stripe.com/api/terminal/readers/process_payment_intent.md#confirm_payment_intent-confirm_config-return_url) when confirming the PaymentIntent. If you don’t provide one, the customer sees a [generic landing page](https://terminal-statics.stripe.com/terminal-checkout/assets/index.html) hosted by Stripe.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const reader = await stripe.terminal.readers.confirmPaymentIntent("tmr_xxx", {
  payment_intent: "pi_xxx",
  confirm_config: {
    return_url: "https://my.store.com/payment-completed",
  },
});
```

For QR code payments, after confirming the payment, the reader screen switches to a UI displaying the QR code for the customer to scan. The customer completing the payment on their device updates the payment which delivers the `terminal.reader.action_succeeded` event.

If the customer chooses to cancel paying with the QR code and taps the back button, confirming the payment intent fails with the `terminal.reader.action_failed` event and the reader returns to the splash screen.

### Free up the reader to take another payment

It might take multiple minutes for a customer to complete the payment on their device. Instead of waiting for the reader to reflect the result of the completed payment, you can free up the reader to take a payment for a different customer.

After the customer scans the QR code and switches to their device to complete the payment, use the [cancel_action](https://docs.stripe.com/api/terminal/readers/object.md#terminal_reader_object-action-cancel_action) endpoint to reset the reader.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const reader = await stripe.terminal.readers.cancelAction("tmr_xxx");
```

After you cancel the reader’s action to process the payment, the payment intent remains in the `requires_action` state, allowing the customer to complete the payment. Use the `payment_intent.succeeded` and `payment_intent.payment_failed` webhooks to reconcile the result of the completed payment. Learn how to [monitor a PaymentIntent with webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks).

## Customer experience

After you [process](https://docs.stripe.com/terminal/payments/additional-payment-methods.md#handle-payment) the PaymentIntent, the customer scans a QR code displayed on the reader screen.

Depending on the payment method, the customer might quickly finalize the payment in their mobile application (most digital wallets), or complete a more extended process of evaluating financing offers (BNPL payment methods). The following sections demonstrate the payment flow for supported payment methods with smart readers:

#### Affirm

Learn more about how to provide the best customer experience and promote awareness of BNPL options in a store through these [Affirm training resources](https://businesshub.affirm.com/hc/en-us/articles/30660865631892-Stripe-User-Affirm-Resources).
![](https://d37ugbyn3rpeym.cloudfront.net/videos/terminal/affirm-customer-experience.mp4)

#### WeChat Pay

![](https://d37ugbyn3rpeym.cloudfront.net/videos/terminal/wechat-pay-customer-experience.mp4)

#### PayNow

![](https://docs.stripecdn.com/50c48b010444a4c4db73126c3ecc68f555ab3a59940349a72558d934f274b666.mp4)

## Testing

In a _sandbox_ (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes), you can scan the QR code using a QR code scanning application on your mobile phone. The QR code payload contains a URL that goes to a Stripe-hosted test payment page where you can authorize or decline the test payment.

### Affirm sandbox

If your account is onboarded with Affirm, the QR code URL takes you to an Affirm-hosted sandbox page where you can complete the payment process. When you’re redirected to the Affirm sandbox, you might receive a prompt to enter the last four digits of your SSN. Affirm recommends using either `0000` or `5678` for testing purposes.

If your account isn’t onboarded with Affirm, you’ll be directed to the Stripe-hosted test payment page.

> The [present_payment_method](https://docs.stripe.com/api/terminal/readers/present_payment_method.md) endpoint doesn’t support specifying QR code payment method types.

# JavaScript

> This is a JavaScript for when terminal-sdk-platform is js. View the full page at https://docs.stripe.com/terminal/payments/additional-payment-methods?terminal-sdk-platform=js.

> #### Recommendation for smart readers
>
> For smart readers, such as the [BBPOS WisePOS E reader](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepos-e.md), [Stripe Reader S700/S710](https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710.md), and [Verifone readers](https://docs.stripe.com/terminal/payments/setup-reader/verifone.md), we recommend using the [server-driven integration](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=server-driven) instead of the JavaScript SDK.
>
> The JavaScript SDK requires your POS and reader on the same local network with working local DNS. The server-driven integration uses the Stripe API instead, which can be simpler in complex network environments. See our [platform comparison](https://docs.stripe.com/terminal/payments/setup-reader.md#sdk) to help you choose the best platform for your needs.

## Create a PaymentIntent

To accept non-card payment methods through the QR code interface, [create a PaymentIntent](https://docs.stripe.com/api/payment_intents.md) and include your preferred payment method types in the `payment_method_types` parameter.

- To present your customer all payment method options in the checkout flow, combine `card_present` with non-card payment method types. We recommend enabling this if you operate in a heavily [offline](https://docs.stripe.com/terminal/features/operate-offline/overview.md) environment because only cards are supported in offline mode.
- If you don’t want to accept cards, support only non-card payment method types.
- If you know which payment method you want to direct your customer to checkout to, select a single payment method type.

### Capture type

Not all payment methods support [manual capture](https://docs.stripe.com/terminal/payments/collect-card-payment.md#capture-payment). The following table shows which payment methods support manual capture:

| Payment method | Manual capture   |
| -------------- | ---------------- |
| `card_present` | ✓ Supported      |
| `affirm`       | ✓ Supported      |
| `wechat_pay`   | ❌ Not supported |
| `paynow`       | ❌ Not supported |

To support the broadest set of payment methods, create your PaymentIntent with `capture_method` set to `automatic`. To support manual capture for card payments and Affirm while also accepting payment methods that require automatic capture, set `capture_method` on the nested `payment_method_options.card_present` attribute to `manual`.

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=1000 \
  -d currency=usd \
  -d "payment_method_types[]=card_present" \
  -d "payment_method_types[]=wechat_pay" \
  -d capture_method=automatic \
  -d "payment_method_options[card_present][capture_method]=manual"
```

## Handle the payment

Unlike card payments, processing QR code payments occurs asynchronously. When processing a PaymentIntent with a QR code payment method, Stripe generates a QR code unique to that payment.

After processing the payment, the reader displays the QR code for the customer to scan with their mobile device. Shortly after the customer completes the payment on their device, the reader updates to reflect the completed payment.

> The time it takes for the reader to display the result of the payment might differ depending on the payment method used. The reader usually updates after a few seconds.

#### Collect, inspect, and confirm

### Collect a PaymentMethod

- [collectPaymentMethod (JavaScript)](https://docs.stripe.com/terminal/references/api/js-sdk.md#collect-payment-method)

To collect payment, pass the PaymentIntent object you created to the SDK. Your app needs to be connected to a reader to collect a payment method.

When you start collecting a payment method, the reader prompts the customer to tap, insert their card, or use “more ways to pay,” which includes QR code payment methods.

```javascript
async () => {
  // clientSecret is the client_secret from the PaymentIntent you created in Step 1.
  const result = await terminal.collectPaymentMethod(clientSecret);
  if (result.error) {
    // Placeholder for handling result.error
  } else {
    // Placeholder for processing result.paymentIntent
  }
};
```

This method collects payment method data using the connected reader, and associates the data with the local PaymentIntent. At this point, you can determine the payment method type selected.

### Process the PaymentIntent

- [processPayment (JavaScript)](https://docs.stripe.com/terminal/references/api/js-sdk.md#process-payment)

After successfully collecting a payment method, you can proceed to processing the PaymentIntent.

Processing the PaymentIntent with the SDK is synchronous, calling `processPayment` is blocked until the payment completes.

For QR code payments, this method switches the reader screen to a UI displaying the QR code for the customer to scan. The customer completing the payment on their device updates the payment and allows the method to return.

If the customer cancels the payment, the SDK returns an error.

Some payment methods (for example, Affirm) require a [return_url](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-return_url) when confirming a PaymentIntent to redirect your customer to after they authenticate or cancel their payment on the payment method’s app or site. You can provide your own [return_url](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-return_url) when confirming the PaymentIntent. If you don’t provide one, the customer sees a [generic landing page](https://terminal-statics.stripe.com/terminal-checkout/assets/index.html) hosted by Stripe.

```javascript
async () => {
  const result = await terminal.processPayment(paymentIntent, {
    config_override: { return_url: "https://stripe.com" },
  });
  if (result.error) {
    // Placeholder for handling result.error
  } else if (result.paymentIntent) {
    // Placeholder for notifying your backend to capture result.paymentIntent.id
  }
};
```

### Free up the reader to take another payment

It might take multiple minutes for a customer to complete the payment on their device. Instead of waiting for the reader to reflect the result of the completed payment, you can free up the reader to take a payment for a different customer.

- [cancelProcessPayment](https://docs.stripe.com/terminal/references/api/js-sdk.md#cancel-process-payment)

After the customer scans the QR code and switches to their device to complete the payment, call [cancelProcessPayment](https://docs.stripe.com/terminal/references/api/js-sdk.md#cancel-process-payment) to reset the reader.

After you cancel the reader’s action to process the payment, the payment intent remains in the `requires_action` state, allowing the customer to complete the payment. Use the `payment_intent.succeeded` and `payment_intent.payment_failed` webhooks to reconcile the result of the completed payment. Learn how to [monitor a PaymentIntent with webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks).

## Customer experience

After you [process](https://docs.stripe.com/terminal/payments/additional-payment-methods.md#handle-payment) the PaymentIntent, the customer scans a QR code displayed on the reader screen.

Depending on the payment method, the customer might quickly finalize the payment in their mobile application (most digital wallets), or complete a more extended process of evaluating financing offers (BNPL payment methods). The following sections demonstrate the payment flow for supported payment methods with smart readers:

#### Affirm

Learn more about how to provide the best customer experience and promote awareness of BNPL options in a store through these [Affirm training resources](https://businesshub.affirm.com/hc/en-us/articles/30660865631892-Stripe-User-Affirm-Resources).
![](https://d37ugbyn3rpeym.cloudfront.net/videos/terminal/affirm-customer-experience.mp4)

#### WeChat Pay

![](https://d37ugbyn3rpeym.cloudfront.net/videos/terminal/wechat-pay-customer-experience.mp4)

#### PayNow

![](https://docs.stripecdn.com/50c48b010444a4c4db73126c3ecc68f555ab3a59940349a72558d934f274b666.mp4)

## Testing

In a _sandbox_ (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes), you can scan the QR code using a QR code scanning application on your mobile phone. The QR code payload contains a URL that goes to a Stripe-hosted test payment page where you can authorize or decline the test payment.

### Affirm sandbox

If your account is onboarded with Affirm, the QR code URL takes you to an Affirm-hosted sandbox page where you can complete the payment process. When you’re redirected to the Affirm sandbox, you might receive a prompt to enter the last four digits of your SSN. Affirm recommends using either `0000` or `5678` for testing purposes.

If your account isn’t onboarded with Affirm, you’ll be directed to the Stripe-hosted test payment page.

# iOS

> This is a iOS for when terminal-sdk-platform is ios. View the full page at https://docs.stripe.com/terminal/payments/additional-payment-methods?terminal-sdk-platform=ios.

## Create a PaymentIntent

To accept non-card payment methods through the QR code interface, [create a PaymentIntent](https://docs.stripe.com/api/payment_intents.md) and include your preferred payment method types in the `payment_method_types` parameter.

- To present your customer all payment method options in the checkout flow, combine `card_present` with non-card payment method types. We recommend enabling this if you operate in a heavily [offline](https://docs.stripe.com/terminal/features/operate-offline/overview.md) environment because only cards are supported in offline mode.
- If you don’t want to accept cards, support only non-card payment method types.
- If you know which payment method you want to direct your customer to checkout to, select a single payment method type.

### Capture type

Not all payment methods support [manual capture](https://docs.stripe.com/terminal/payments/collect-card-payment.md#capture-payment). The following table shows which payment methods support manual capture:

| Payment method | Manual capture   |
| -------------- | ---------------- |
| `card_present` | ✓ Supported      |
| `affirm`       | ✓ Supported      |
| `wechat_pay`   | ❌ Not supported |
| `paynow`       | ❌ Not supported |

To support the broadest set of payment methods, create your PaymentIntent with `capture_method` set to `automatic`. To support manual capture for card payments and Affirm while also accepting payment methods that require automatic capture, set `capture_method` on the nested `payment_method_options.card_present` attribute to `manual`.

#### Swift

```swift
import UIKit
import StripeTerminal

class PaymentViewController: UIViewController {

    // ...

    // Action for a "Checkout" button
    func checkoutAction() throws {
        let params = try PaymentIntentParametersBuilder(amount: 1000, currency: "sgd")
            .setPaymentMethodTypes(
                [PaymentMethodType.cardPresent, PaymentMethodType.wechatPay]
            )
            .setCaptureMethod(CaptureMethod.automatic)
            .setPaymentMethodOptionsParameters(
                PaymentMethodOptionsParametersBuilder(
                    cardPresentParameters: CardPresentParametersBuilder()
                        .setCaptureMethod(CardPresentCaptureMethod.manual)
                        .build()
                )
                .build()
            )
            .build()

        Terminal.shared.createPaymentIntent(params) { createResult, createError in
            if let error = createError {
                print("createPaymentIntent failed: \(error)")
            } else if let paymentIntent = createResult {
                print("createPaymentIntent succeeded")
            // ...
            }
        }

    }

    // ...
}
```

## Handle the payment

Unlike card payments, processing QR code payments occurs asynchronously. When confirming a PaymentIntent with a QR code payment method, Stripe generates a QR code unique to that payment.

After confirming the payment, the reader displays the QR code for the customer to scan with their mobile device. Shortly after the customer completes the payment on their device, the reader updates to reflect the completed payment.

> The time it takes for the reader to display the result of the payment might differ depending on the payment method used. The reader usually updates after a few seconds.

#### Collect, inspect, and confirm

### Collect a PaymentMethod

- [collectPaymentMethod (iOS)](<https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)collectPaymentMethod:delegate:completion:>)

To collect payment, pass the PaymentIntent object you created to the SDK. Your app needs to be connected to a reader to collect a payment method.

When you start collecting a payment method, the reader prompts the customer to tap, insert their card, or to use “more ways to pay”, which includes QR code payment methods. The reader handles displaying the payment method selection and QR code automatically.

#### Swift

```swift


import UIKit
import StripeTerminal

class PaymentViewController: UIViewController, ReaderDisplayDelegate {


    // Label for displaying messages from the card reader
    let readerMessageLabel = UILabel(frame: .zero)
    var collectCancelable: Cancelable? = nil

    // ...

    // Action for a "Checkout" button
    func checkoutAction() throws {
        let params = try PaymentIntentParametersBuilder(amount: 1000, currency: "sgd").build()
        Terminal.shared.createPaymentIntent(params) { createResult, createError in
            if let error = createError {
                print("createPaymentIntent failed: \(error)")
            }
            else if let paymentIntent = createResult {
                print("createPaymentIntent succeeded")
                self.collectCancelable = Terminal.shared.collectPaymentMethod(paymentIntent) { collectResult, collectError in
                    if let error = collectError {
                        print("collectPaymentMethod failed: \(error)")
                    }
                    else if let paymentIntent = collectResult {
                        print("collectPaymentMethod succeeded")
                        // ... Confirm the payment
                    }
                }
            }

        }
    }
 }

 // MARK: MobileReaderDelegate - only needed for mobile readers, this is the delegate set during connectReader

 func reader(_ reader: Reader, didRequestReaderInput inputOptions: ReaderInputOptions = []) {
     readerMessageLabel.text = Terminal.stringFromReaderInputOptions(inputOptions)
 }

 func reader(_ reader: Reader, didRequestReaderDisplayMessage displayMessage: ReaderDisplayMessage) {
     readerMessageLabel.text = Terminal.stringFromReaderDisplayMessage(displayMessage)
 }
 // MARK: ReaderDisplayDelegate

 func terminal(_ terminal: Terminal, didRequestReaderInput inputOptions: ReaderInputOptions = []) {
     readerMessageLabel.text = Terminal.stringFromReaderInputOptions(inputOptions)
 }

 func terminal(_ terminal: Terminal, didRequestReaderDisplayMessage displayMessage: ReaderDisplayMessage) {
     readerMessageLabel.text = Terminal.stringFromReaderDisplayMessage(displayMessage)
 }
```

This method collects payment method data using the connected reader, and associates the data with the local PaymentIntent. At this point, you can determine the payment method type selected.

### Confirm the PaymentIntent

- [confirmPaymentIntent (iOS)](<https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)confirmPaymentIntent:completion:>)

After successfully collecting a payment method, you can proceed to confirming the PaymentIntent.

Confirming the PaymentIntent with the SDK is synchronous, calling `confirmPaymentIntent` is blocked until the payment completes.

For QR code payments, this method switches the reader screen to a UI displaying the QR code for the customer to scan. The reader handles the QR code display automatically. The customer completing the payment on their device updates the payment and allows the method to return.

If the customer cancels the payment, the SDK returns an error.

Some payment methods (for example, Affirm) require a [return_url](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-return_url) when confirming a PaymentIntent to redirect your customer to after they authenticate or cancel their payment on the payment method’s app or site. You can provide your own [return_url](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-return_url) when confirming the PaymentIntent. If you don’t provide one, the customer sees a [generic landing page](https://terminal-statics.stripe.com/terminal-checkout/assets/index.html) hosted by Stripe.

#### Swift

```swift


let confirmConfig = try ConfirmPaymentIntentConfigurationBuilder().setReturnUrl("https://stripe.com").build()

// ... Confirm the payment
self.confirmCancelable = Terminal.shared.confirmPaymentIntent(collectPaymentMethodPaymentIntent, confirmConfig: confirmConfig) { confirmResult, confirmError in
    if let error = confirmError {
        print("confirmPaymentIntent failed: \(error)")
    } else if let confirmedPaymentIntent = confirmResult {
        print("confirmPaymentIntent succeeded")
        // Notify your backend to capture the PaymentIntent
        if let stripeId = confirmedPaymentIntent.stripeId {
            APIClient.shared.capturePaymentIntent(stripeId) { captureError in
                if let error = captureError {
                    print("capture failed: \(error)")
                } else {
                    print("capture succeeded")
                }
            }
        } else {
            print("Payment collected offline");
        }
    }
}
```

### Free up the reader to take another payment

It might take multiple minutes for a customer to complete the payment on their device. Instead of waiting for the reader to reflect the result of the completed payment, you can free up the reader to take a payment for a different customer.

- [Cancelable (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPCancelable.html)

After the customer scans the QR code and switches to their device to complete the payment, use the `Cancelable` object returned by the iOS SDK to cancel the action and reset the reader.

After you cancel the reader’s action to confirm the payment, the payment intent remains in the `requires_action` state, allowing the customer to complete the payment. Use the `payment_intent.succeeded` and `payment_intent.payment_failed` webhooks to reconcile the result of the completed payment. Learn how to [monitor a PaymentIntent with webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks).

## Customer experience

After you [confirm](https://docs.stripe.com/terminal/payments/additional-payment-methods.md#handle-payment) the PaymentIntent, the customer scans a QR code displayed on the reader screen.

Depending on the payment method, the customer might quickly finalize the payment in their mobile application (most digital wallets), or complete a more extended process of evaluating financing offers (BNPL payment methods). The following sections demonstrate the payment flow for supported payment methods with smart readers:

#### Affirm

Learn more about how to provide the best customer experience and promote awareness of BNPL options in a store through these [Affirm training resources](https://businesshub.affirm.com/hc/en-us/articles/30660865631892-Stripe-User-Affirm-Resources).
![](https://d37ugbyn3rpeym.cloudfront.net/videos/terminal/affirm-customer-experience.mp4)

#### WeChat Pay

![](https://d37ugbyn3rpeym.cloudfront.net/videos/terminal/wechat-pay-customer-experience.mp4)

#### PayNow

![](https://docs.stripecdn.com/50c48b010444a4c4db73126c3ecc68f555ab3a59940349a72558d934f274b666.mp4)

## Testing

In a _sandbox_ (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes), you can scan the QR code using a QR code scanning application on your mobile phone. The QR code payload contains a URL that goes to a Stripe-hosted test payment page where you can authorize or decline the test payment.

### Affirm sandbox

If your account is onboarded with Affirm, the QR code URL takes you to an Affirm-hosted sandbox page where you can complete the payment process. When you’re redirected to the Affirm sandbox, you might receive a prompt to enter the last four digits of your SSN. Affirm recommends using either `0000` or `5678` for testing purposes.

If your account isn’t onboarded with Affirm, you’ll be directed to the Stripe-hosted test payment page.

# Android

> This is a Android for when terminal-sdk-platform is android. View the full page at https://docs.stripe.com/terminal/payments/additional-payment-methods?terminal-sdk-platform=android.

## Create a PaymentIntent

To accept non-card payment methods through the QR code interface, [create a PaymentIntent](https://docs.stripe.com/api/payment_intents.md) and include your preferred payment method types in the `payment_method_types` parameter.

- To present your customer all payment method options in the checkout flow, combine `card_present` with non-card payment method types. We recommend enabling this if you operate in a heavily [offline](https://docs.stripe.com/terminal/features/operate-offline/overview.md) environment because only cards are supported in offline mode.
- If you don’t want to accept cards, support only non-card payment method types.
- If you know which payment method you want to direct your customer to checkout to, select a single payment method type.

### Capture type

Not all payment methods support [manual capture](https://docs.stripe.com/terminal/payments/collect-card-payment.md#capture-payment). The following table shows which payment methods support manual capture:

| Payment method | Manual capture   |
| -------------- | ---------------- |
| `card_present` | ✓ Supported      |
| `affirm`       | ✓ Supported      |
| `wechat_pay`   | ❌ Not supported |
| `paynow`       | ❌ Not supported |

To support the broadest set of payment methods, create your PaymentIntent with `capture_method` set to `automatic`. To support manual capture for card payments and Affirm while also accepting payment methods that require automatic capture, set `capture_method` on the nested `payment_method_options.card_present` attribute to `manual`.

#### Kotlin

```kotlin
val paymentMethodTypes =
    listOf(PaymentMethodType.CARD_PRESENT,PaymentMethodType.WECHAT_PAY)

val params = PaymentIntentParameters.Builder(
    paymentMethodTypes = paymentMethodTypes
)
    .setAmount(1000)
    .setCurrency("sgd")
    .setCaptureMethod(CaptureMethod.Automatic)
    .setPaymentMethodOptionsParameters(
        PaymentMethodOptionsParameters.Builder()
          .setCardPresentParameters(
              CardPresentParameters.Builder()
                  .setCaptureMethod(CardPresentCaptureMethod.Manual)
                  .build()
          )
          .build()
    )
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

## Handle the payment

Unlike card payments, processing QR code payments occurs asynchronously. When confirming a PaymentIntent with a QR code payment method, Stripe generates a QR code unique to that payment.

After confirming the payment, the reader displays the QR code for the customer to scan with their mobile device. Shortly after the customer completes the payment on their device, the reader updates to reflect the completed payment.

> The time it takes for the reader to display the result of the payment might differ depending on the payment method used. The reader usually updates after a few seconds.

#### Collect, inspect, and confirm

### Collect a PaymentMethod

- [collectPaymentMethod (Android)](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/collect-payment-method.html)

To collect payment, pass the PaymentIntent object you created to the SDK. Your app needs to be connected to a reader to collect a payment method.

When you start collecting a payment method, the reader prompts the customer to tap, insert their card, or to use “more ways to pay”, which includes QR code payment methods. The reader handles displaying the payment method selection and QR code automatically.

#### Kotlin

```kotlin
val cancelable = Terminal.getInstance().collectPaymentMethod(
    paymentIntent,
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

This method collects payment method data using the connected reader, and associates the data with the local PaymentIntent. At this point, you can determine the payment method type selected.

### Confirm the PaymentIntent

- [confirmPaymentIntent (Android)](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/confirm-payment-intent.html)

After successfully collecting a payment method, you can proceed to confirming the PaymentIntent.

Confirming the PaymentIntent with the SDK is synchronous, calling `confirmPaymentIntent` is blocked until the payment completes.

For QR code payments, this method switches the reader screen to a UI displaying the QR code for the customer to scan. The reader handles the QR code display automatically. The customer completing the payment on their device updates the payment and allows the method to return.

If the customer cancels the payment, the SDK returns an error.

Some payment methods (for example, Affirm) require a [return_url](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-return_url) when confirming a PaymentIntent to redirect your customer to after they authenticate or cancel their payment on the payment method’s app or site. You can provide your own [return_url](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-return_url) when confirming the PaymentIntent. If you don’t provide one, the customer sees a [generic landing page](https://terminal-statics.stripe.com/terminal-checkout/assets/index.html) hosted by Stripe.

#### Kotlin

```kotlin

val confirmConfig = ConfirmPaymentIntentConfiguration.Builder().setReturnUrl("https://stripe.com/").build()

val cancelable = Terminal.getInstance().confirmPaymentIntent(
    paymentIntent,
    object : PaymentIntentCallback {
        override fun onSuccess(paymentIntent: PaymentIntent) {
            // Placeholder handling successful operation
        }

        override fun onFailure(e: TerminalException) {
            // Placeholder for handling exception
        }
    },
    confirmConfig
)
```

### Free up the reader to take another payment

It might take multiple minutes for a customer to complete the payment on their device. Instead of waiting for the reader to reflect the result of the completed payment, you can free up the reader to take a payment for a different customer.

- [Cancelable (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.callable/-cancelable/index.html)

After the customer scans the QR code and switches to their device to complete the payment, use the `Cancelable` object returned by the Android SDK to cancel the action and reset the reader.

After you cancel the reader’s action to confirm the payment, the payment intent remains in the `requires_action` state, allowing the customer to complete the payment. Use the `payment_intent.succeeded` and `payment_intent.payment_failed` webhooks to reconcile the result of the completed payment. Learn how to [monitor a PaymentIntent with webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks).

## Customer experience

After you [confirm](https://docs.stripe.com/terminal/payments/additional-payment-methods.md#handle-payment) the PaymentIntent, the customer scans a QR code displayed on the reader screen.

Depending on the payment method, the customer might quickly finalize the payment in their mobile application (most digital wallets), or complete a more extended process of evaluating financing offers (BNPL payment methods). The following sections demonstrate the payment flow for supported payment methods with smart readers:

#### Affirm

Learn more about how to provide the best customer experience and promote awareness of BNPL options in a store through these [Affirm training resources](https://businesshub.affirm.com/hc/en-us/articles/30660865631892-Stripe-User-Affirm-Resources).
![](https://d37ugbyn3rpeym.cloudfront.net/videos/terminal/affirm-customer-experience.mp4)

#### WeChat Pay

![](https://d37ugbyn3rpeym.cloudfront.net/videos/terminal/wechat-pay-customer-experience.mp4)

#### PayNow

![](https://docs.stripecdn.com/50c48b010444a4c4db73126c3ecc68f555ab3a59940349a72558d934f274b666.mp4)

## Testing

In a _sandbox_ (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes), you can scan the QR code using a QR code scanning application on your mobile phone. The QR code payload contains a URL that goes to a Stripe-hosted test payment page where you can authorize or decline the test payment.

### Affirm sandbox

If your account is onboarded with Affirm, the QR code URL takes you to an Affirm-hosted sandbox page where you can complete the payment process. When you’re redirected to the Affirm sandbox, you might receive a prompt to enter the last four digits of your SSN. Affirm recommends using either `0000` or `5678` for testing purposes.

If your account isn’t onboarded with Affirm, you’ll be directed to the Stripe-hosted test payment page.

# React Native

> This is a React Native for when terminal-sdk-platform is react-native. View the full page at https://docs.stripe.com/terminal/payments/additional-payment-methods?terminal-sdk-platform=react-native.

## Create a PaymentIntent

To accept non-card payment methods through the QR code interface, [create a PaymentIntent](https://docs.stripe.com/api/payment_intents.md) and include your preferred payment method types in the `payment_method_types` parameter.

- To present your customer all payment method options in the checkout flow, combine `card_present` with non-card payment method types. We recommend enabling this if you operate in a heavily [offline](https://docs.stripe.com/terminal/features/operate-offline/overview.md) environment because only cards are supported in offline mode.
- If you don’t want to accept cards, support only non-card payment method types.
- If you know which payment method you want to direct your customer to checkout to, select a single payment method type.

### Capture type

Not all payment methods support [manual capture](https://docs.stripe.com/terminal/payments/collect-card-payment.md#capture-payment). The following table shows which payment methods support manual capture:

| Payment method | Manual capture   |
| -------------- | ---------------- |
| `card_present` | ✓ Supported      |
| `affirm`       | ✓ Supported      |
| `wechat_pay`   | ❌ Not supported |
| `paynow`       | ❌ Not supported |

To support the broadest set of payment methods, create your PaymentIntent with `capture_method` set to `automatic`. To support manual capture for card payments and Affirm while also accepting payment methods that require automatic capture, set `capture_method` on the nested `payment_method_options.card_present` attribute to `manual`.

```js
const { error, paymentIntent } = await createPaymentIntent({
  amount: 1000,
  currency: "sgd",
  paymentMethodTypes: ["card_present", "wechat_pay"],
  captureMethod: "automatic",
  paymentMethodOptions: {
    captureMethod: "manual",
  },
});
```

## Handle the payment

Unlike card payments, processing QR code payments occurs asynchronously. When confirming a PaymentIntent with a QR code payment method, Stripe generates a QR code unique to that payment.

After confirming the payment, the reader displays the QR code for the customer to scan with their mobile device. Shortly after the customer completes the payment on their device, the reader updates to reflect the completed payment.

> The time it takes for the reader to display the result of the payment might differ depending on the payment method used. The reader usually updates after a few seconds.

#### Collect, inspect, and confirm

### Collect a PaymentMethod

- [collectPaymentMethod (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#collectpaymentmethod)

To collect payment, pass the PaymentIntent object you created to the SDK. Your app needs to be connected to a reader to collect a payment method.

When you start collecting a payment method, the reader prompts the customer to tap, insert their card, or to use “more ways to pay”, which includes QR code payment methods. The reader handles displaying the payment method selection and QR code automatically.

```js
const { paymentIntent, error } = await collectPaymentMethod({
  paymentIntent: paymentIntent,
});

if (error) {
  // Placeholder for handling exception
}

// Placeholder for processing PaymentIntent
```

This method collects payment method data using the connected reader, and associates the data with the local PaymentIntent. At this point, you can determine the payment method type selected.

### Confirm the PaymentIntent

- [confirmPaymentIntent (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#confirmpaymentintent)

After successfully collecting a payment method, you can proceed to confirming the PaymentIntent.

Confirming the PaymentIntent with the SDK is synchronous, calling `confirmPaymentIntent` is blocked until the payment completes.

For QR code payments, this method switches the reader screen to a UI displaying the QR code for the customer to scan. The reader handles the QR code display automatically. The customer completing the payment on their device updates the payment and allows the method to return.

If the customer cancels the payment, the SDK returns an error.

Some payment methods (for example, Affirm) require a [return_url](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-return_url) when confirming a PaymentIntent to redirect your customer to after they authenticate or cancel their payment on the payment method’s app or site. You can provide your own [return_url](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-return_url) when confirming the PaymentIntent. If you don’t provide one, the customer sees a [generic landing page](https://terminal-statics.stripe.com/terminal-checkout/assets/index.html) hosted by Stripe.

```js
const { paymentIntent, error } = await confirmPaymentIntent(paymentIntent);

if (error) {
  // Placeholder for handling exception
  return;
}

// Placeholder for notifying your backend to capture paymentIntent.id
```

### Free up the reader to take another payment

It might take multiple minutes for a customer to complete the payment on their device. Instead of waiting for the reader to reflect the result of the completed payment, you can free up the reader to take a payment for a different customer.

- [cancelConfirmPaymentIntent (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#cancelconfirmpaymentintent)

After the customer scans the QR code and switches to their device to complete the payment, call [cancelConfirmPaymentIntent](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#cancelconfirmpaymentintent) to reset the reader.

After you cancel the reader’s action to confirm the payment, the payment intent remains in the `requires_action` state, allowing the customer to complete the payment. Use the `payment_intent.succeeded` and `payment_intent.payment_failed` webhooks to reconcile the result of the completed payment. Learn how to [monitor a PaymentIntent with webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks).

## Customer experience

After you [confirm](https://docs.stripe.com/terminal/payments/additional-payment-methods.md#handle-payment) the PaymentIntent, the customer scans a QR code displayed on the reader screen.

Depending on the payment method, the customer might quickly finalize the payment in their mobile application (most digital wallets), or complete a more extended process of evaluating financing offers (BNPL payment methods). The following sections demonstrate the payment flow for supported payment methods with smart readers:

#### Affirm

Learn more about how to provide the best customer experience and promote awareness of BNPL options in a store through these [Affirm training resources](https://businesshub.affirm.com/hc/en-us/articles/30660865631892-Stripe-User-Affirm-Resources).
![](https://d37ugbyn3rpeym.cloudfront.net/videos/terminal/affirm-customer-experience.mp4)

#### WeChat Pay

![](https://d37ugbyn3rpeym.cloudfront.net/videos/terminal/wechat-pay-customer-experience.mp4)

#### PayNow

![](https://docs.stripecdn.com/50c48b010444a4c4db73126c3ecc68f555ab3a59940349a72558d934f274b666.mp4)

## Testing

In a _sandbox_ (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes), you can scan the QR code using a QR code scanning application on your mobile phone. The QR code payload contains a URL that goes to a Stripe-hosted test payment page where you can authorize or decline the test payment.

### Affirm sandbox

If your account is onboarded with Affirm, the QR code URL takes you to an Affirm-hosted sandbox page where you can complete the payment process. When you’re redirected to the Affirm sandbox, you might receive a prompt to enter the last four digits of your SSN. Affirm recommends using either `0000` or `5678` for testing purposes.

If your account isn’t onboarded with Affirm, you’ll be directed to the Stripe-hosted test payment page.
