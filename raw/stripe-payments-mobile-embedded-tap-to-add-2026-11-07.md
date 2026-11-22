<!-- Source URL: https://docs.stripe.com/payments/mobile/embedded-tap-to-add -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Tap to add your card for Payment Element

Allow customers to add their card by tapping their card on their device.

> #### Want access to the tap to add your card feature?
> 
> The tap to add your card feature is in private preview. [Share your email address to request access.](https://docs.stripe.com/payments/mobile/embedded-tap-to-add.md#tap_to_add_payment_element_android_preview)

### Want access to the tap to add your card feature?

Enter your email to request access.

```bash
curl https://docs.stripe.com/preview/register \
  -X POST \
  -H "Content-Type: application/json" \
  -H "Referer: https://docs.stripe.com/payments/mobile/embedded-tap-to-add" \
  -d '{"email": "EMAIL", "preview": "tap_to_add_payment_element_android_preview"}'
```

> The tap to add your card feature is available on Android only.

The tap to add your card feature for Payment Element lets customers add a card to your app by tapping a physical card on a [compatible NFC-equipped Android device](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay.md?platform=android#supported-devices). This reduces manual card entry and friction at checkout while maintaining secure card-present authentication. After the tap, customers can save their card for future purchases and optionally enroll in Link. You can use this feature in your existing [Mobile Payment Element](https://docs.stripe.com/payments/mobile/accept-payment-embedded.md) integration to save cards for future payments.
![](https://docs.stripecdn.com/mpe_tap_to_add_demo.mp4)
This guide describes how you can allow customers to tap to add their card through your in-app payment integration.

## Before you begin

1. [Create a Stripe account](https://dashboard.stripe.com/register) or [sign in](https://dashboard.stripe.com/login).
2. Follow the steps in [Accept in-app payments](https://docs.stripe.com/payments/mobile/accept-payment-embedded.md) to integrate with the Payment Element.
3. Order a [physical test card](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards) to try tapping to add your card in a sandbox.

## Initialize the Terminal SDK

To allow customers to tap to add their card in a Payment Element, add the following Stripe Terminal dependencies to your project:

#### Kotlin

```kotlin
dependencies {
  // ...

  // Stripe Terminal SDK
  implementation("com.stripe:stripeterminal-core:5.4.1")
  implementation("com.stripe:stripeterminal-taptopay:5.4.1")
}
```

The tap to add your card feature uses the Terminal Tap to Pay infrastructure to operate in a dedicated process, making transactions more secure. In this process, we create a second instance of your `Application`. To avoid unexpected errors from running your code in this process, you can skip initialization in your `Application` by checking `TapToPay.isInTapToPayProcess()`. Learn more about the [Tap to Pay infrastructure](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay.md?platform=android).

```kotlin
// Substitute with your application name, and remember to keep it
// the same as your AndroidManifest.xml
class StripeApplication : Application() {
    override fun onCreate() {
        super.onCreate()

        // Skip initialization if running in the TTPA process.
        if (TapToPay.isInTapToPayProcess()) return

        // For example, this will be skipped.
        TerminalApplicationDelegate.onCreate(this)
    }
}
```

## Add an endpoint

This integration uses the following Stripe API objects:

- A SetupIntent is an object that represents your intent to set up a customer’s payment method for future payments. The payment methods that customers see during the checkout process are also included on the SetupIntent. You can let Stripe automatically pull payment methods from your Dashboard settings or you can list them manually.
- A `Customer` is an object that you use to set up future payments by attaching a payment method to it. Create a `Customer` object when your customer creates an account with your business. If your customer is making a payment as a guest, you can create a `Customer` object before payment and associate it with your own internal representation of the customer’s account later.

For security reasons, your app can’t create these objects. Instead, add an endpoint on your server that:

- Retrieves the Customer
- Creates a SetupIntent with a `card_present` payment method type and the Customer ID. If the SetupIntent doesn’t have a payment method type of `card_present`, the tapped card won’t be saved on the customer’s account.
- Returns the SetupIntent client secret to your app.

```javascript
// This example sets up an endpoint using the Express framework.
const stripe = require('stripe')('{{SANDBOX-API-KEY}}');

app.post('/create-card-present-setup-intent', async (req, res) => {
  const setupIntent = await stripe.setupIntents.create({
    // Use an existing customer ID
    customer: req.customer.id,
    payment_method_types: ['card_present'],
  });

  res.json({
    setupIntent: setupIntent.client_secret,
  })
});
```

## Implement your SetupIntent creation callback

To allow customers to tap to add their card in a Payment Element, you must implement a SetupIntent creation callback for tap to add using `createCardPresentSetupIntentCallback`.

After your customer taps their card, we attach the payment method to the SetupIntent created from your implementation and save the card for future use.

```kotlin
val embeddedBuilder = EmbeddedPaymentElement.Builder(
    createIntentCallback = { paymentMethod, canSave ->
        // Create intent on call
    },
    resultCallback = { result ->
        // Handle result
    },
)
    .createCardPresentSetupIntent {
        val response = server.createCardPresentSetupIntent(customerId)

        return if (response.isSuccess) {
            Result.success(response.body!!.clientSecret)
        } else {
            Result.failure(response.exception)
        }
    }

val embeddedPaymentElement = rememberEmbeddedPaymentElement(embeddedBuilder)
```

## Test your integration

You can test tapping to add your card by using a [device supported by the Tap to Pay infrastructure](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay.md?platform=android#supported-devices).

- To use the *simulated reader* (Stripe Terminal SDKs and server-driven integrations come with a built-in simulated card reader, so you can develop and test your app without connecting to physical hardware. Whether your integration is complete or you're still building it, use the simulated reader to emulate all the Terminal flows in your app), use a [sandbox API key](https://docs.stripe.com/keys.md#test-live-modes) and a debuggable build of your application.
- To use the real NFC reader, use a production build of your application with [physical test cards](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards) to tap on your device.

## Optional: Additional features

### Enable Link

Customers can optionally enroll in Link after they save a tapped card. To enable Link in the Mobile Payment Element, see [Link in the Mobile Payment Element](https://docs.stripe.com/payments/link/mobile-payment-element-link.md).
