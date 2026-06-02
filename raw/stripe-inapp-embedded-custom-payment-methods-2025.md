<!-- Source URL: https://docs.stripe.com/payments/mobile/embedded-custom-payment-methods -->
<!-- Fetched: 2026-04-22 -->

# Add custom payment methods

Add custom payment methods to the Payment Element.

[In-app Payments](https://docs.stripe.com/payments/mobile.md) let your users pay with many [payment methods](https://docs.stripe.com/payments/payment-methods/payment-method-support.md) through a single integration. Use custom payment methods if you need to display additional payment methods that aren’t processed through Stripe. If you use custom payment methods, you can optionally record purchases processed outside of Stripe to your Stripe account for reporting purposes.

To configure a custom payment method, create it in your Stripe Dashboard, and provide a display name and icon that In-app Payments also display. The Stripe Dashboard also provides access to over 50 preset custom payment methods. After you create the payment method, follow the guide below to configure the In-app Payments. Setting up the In-app Payments requires some additional configuration work because custom payment method transactions process and finalize outside of Stripe.

> When integrating with a third-party payment processor, you’re responsible for complying with [applicable legal requirements](https://docs.stripe.com/payments/payment-methods/custom-payment-methods.md#compliance), including your agreement with your PSP, applicable laws, and so on.

# iOS

> This is a iOS for when platform is ios. View the full page at https://docs.stripe.com/payments/mobile/embedded-custom-payment-methods?platform=ios.

## Before you begin

1. [Create a Stripe account](https://dashboard.stripe.com/register) or [sign in](https://dashboard.stripe.com/login).
1. Follow the guide to [accept in-app payments](https://docs.stripe.com/payments/mobile/accept-payment-embedded.md?platform=ios&type=payment) to complete a payments integration.

## Create your custom payment method in the Dashboard [Dashboard]

Go to **Settings** > **Payments** > [Custom Payment Methods](https://dashboard.stripe.com/settings/custom_payment_methods) to get to the custom payment methods page. Create a new custom payment method and provide the display name and logo that the Payment Element displays.

#### Choose the right logo

- If you provide a logo with a transparent background, consider the background color of the Payment Element on your page and make sure that it displays clearly.
- If you provide a logo with a background fill, provide rounded corners in your file because we won’t provide them.
- Choose a logo variant that can scale down to 16 pixels × 16 pixels. This is often the standalone logo mark for a brand.

After creating the custom payment method, the Dashboard displays the custom payment method ID (beginning with `cpmt_`) needed in step 2.

## Add custom payment method types

When you create your `EmbeddedPaymentElement.Configuration` object and initialize the `EmbeddedPaymentElement`, specify the custom payment methods that you want to add to the Payment Element and a handler to complete the payment.

```swift
@_spi(CustomPaymentMethodsBeta) import StripePaymentSheet

class MyCheckoutVC: UIViewController {
  func createEmbeddedPaymentElement() async throws -> EmbeddedPaymentElement {
      // ...
      var configuration = EmbeddedPaymentElement.Configuration()let customPaymentMethod = EmbeddedPaymentElement.CustomPaymentMethodConfiguration.CustomPaymentMethod(id: "cpmt_...",
                                                                                                            subtitle: "Optional subtitle")
      configuration.customPaymentMethodConfiguration = .init(customPaymentMethods: [customPaymentMethod],
                                                             customPaymentMethodConfirmHandler: handleCustomPaymentMethod(_:_:))
      // ...
  }
func handleCustomPaymentMethod(
        _ customPaymentMethodType: EmbeddedPaymentElement.CustomPaymentMethodConfiguration.CustomPaymentMethod,
        _ billingDetails: STPPaymentMethodBillingDetails
    ) async -> EmbeddedPaymentElementResult {
      // ...explained in the next step
  }
}
```

## Complete the payment

When you call [confirm](https://github.com/stripe/stripe-ios/blob/2d7f339e82dac62a9c509c213d48d85e1fc42b7c/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Embedded/EmbeddedPaymentElement.swift#L196C25-L196C26) on your `EmbeddedPaymentElement` instance and the customer has selected a custom payment method, it calls the handler with the custom payment method, and uses any billing details that you collected in the sheet.

Your implementation completes the payment (for example, by using your custom payment method provider’s SDK) and returns from the function with the result of the payment: `completed`, `canceled`, or `failure(error:)`.

```swift
@_spi(CustomPaymentMethodsBeta) import StripePaymentSheet

class MyCheckoutVC: UIViewController {
    func createEmbeddedPaymentElement() async throws -> EmbeddedPaymentElement {
        // ...
        var configuration = EmbeddedPaymentElement.Configuration()
        let customPaymentMethod = EmbeddedPaymentElement.CustomPaymentMethodConfiguration.CustomPaymentMethod(id: "cpmt_...",
                                                                                                              subtitle: "Optional subtitle")
        configuration.customPaymentMethodConfiguration = .init(customPaymentMethods: [customPaymentMethod],
                                                              customPaymentMethodConfirmHandler: handleCustomPaymentMethod(_:_:))
        // ...
    }

    func handleCustomPaymentMethod(
        _ customPaymentMethodType: EmbeddedPaymentElement.CustomPaymentMethodConfiguration.CustomPaymentMethod,
        _ billingDetails: STPPaymentMethodBillingDetails
    ) async -> EmbeddedPaymentElementResult {// Your implementation needs to complete the payment with the payment method provider
        // When the payment completes, cancels, or fails, return the result.
        // This example code just immediately fails:
        let exampleError = NSError(domain: "MyErrorDomain", code: 0, userInfo: [NSLocalizedDescriptionKey: "Failed to complete payment!"])
        return .failed(error: exampleError)
    }
}
```

## Optional: Specify the order of custom payment methods

Stripe’s smart ordering logic can’t rank custom payment methods because it has no context for them. By default, they appear after Stripe-supported payment methods. To explicitly position a custom payment method in the Mobile Payment Element, set `EmbeddedPaymentElement.Configuration.paymentMethodOrder`. We still intelligently rank the Stripe-supported payment methods following the custom payment method.

```swift
var configuration = EmbeddedPaymentElement.Configuration()// Show cards first, followed by cpmt_, followed by all other payment methods
configuration.paymentMethodOrder = ["card", "cpmt_..."]
```

## Collect billing details

You can collect billing details using [billingDetailsCollectionConfiguration on the Payment Element configuration](https://docs.stripe.com/payments/mobile/accept-payment.md?platform=ios#billing-details-collection). However, custom payment methods don’t collect billing details by default. To enable billing detail collection, set `disableBillingDetailCollection` to `false` on your `CustomPaymentMethod`.

```swift
var customPaymentMethod = EmbeddedPaymentElement.CustomPaymentMethodConfiguration.CustomPaymentMethod(id: "cpmt_...",
                                                                                                      subtitle: "Optional subtitle")customPaymentMethod.disableBillingDetailCollection = false
```

## Test your integration

1. Go through your checkout flow and verify that the Mobile Payment Element displays your custom payment method. This example configures your custom payment method in the second position after cards.
1. Choose your custom payment method.
1. Click **Pay now** to test your custom payment method integration. Verify that your integration completes the transaction and that any post-payment actions (for example, displaying a confirmation page, success message, or failure message) still work with your custom payment method integration.

## Optional: Record the payment to your Stripe account [Server-side]

While you handle custom payment method transactions outside of Stripe, you can still [record the transaction details](https://docs.stripe.com/api/payment-record/report-payment/report.md) to your Stripe account to unify reporting and build back office workflows, such as issuing receipts or creating reports.

```javascript

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = new Stripe('<<YOUR_SECRET_KEY>>', {
  apiVersion: '2026-03-25.dahlia; invoice_partial_payments_beta=v3'
});

app.get('/process-cpm-payment', async (req, res) => {
  const paymentResult = processMyCustomPayment(...)

  // Create an instance of a custom payment method
  const paymentMethod = await stripe.paymentMethods.create({
    type: 'custom',
    custom: {
      type: '{{CUSTOM_PAYMENT_METHOD_TYPE_ID}}', // Identifier of the custom payment method type created in the Dashboard.
    }
  });

  // Report successful payment
  const paymentRecord = await stripe.paymentRecords.reportPayment({
    amount_requested: {
      value: paymentResult.amount,
      currency: paymentResult.currency
    },
    payment_method_details: {
      payment_method: paymentMethod.id
    },
    customer_details: {
      customer: paymentResult.customer.id
    },
    processor_details: {
      type: 'custom',
      custom: {
        payment_reference: paymentResult.id
      }
    },
    initiated_at: paymentResult.initiated_at,
    customer_presence: 'on_session',
    outcome: 'guaranteed',
    guaranteed: {
      guaranteed_at: paymentResult.completed_at
    }
  });

  // Respond to frontend to finish buying experience
  return res.json(...)
});

```

# Android

> This is a Android for when platform is android. View the full page at https://docs.stripe.com/payments/mobile/embedded-custom-payment-methods?platform=android.

## Before you begin

1. [Create a Stripe account](https://dashboard.stripe.com/register) or [sign in](https://dashboard.stripe.com/login).
1. Follow the guide to [accept in-app payments](https://docs.stripe.com/payments/mobile/accept-payment-embedded.md?platform=android&type=payment) to complete a payments integration.

## Create your custom payment method in the Dashboard [Dashboard]

Go to **Settings** > **Payments** > [Custom Payment Methods](https://dashboard.stripe.com/settings/custom_payment_methods) to get to the custom payment methods page. Create a new custom payment method and provide the display name and logo that the Payment Element displays.

#### Choose the right logo

- If you provide a logo with a transparent background, consider the background color of the Payment Element on your page and make sure that it displays clearly.
- If you provide a logo with a background fill, provide rounded corners in your file because we won’t provide them.
- Choose a logo variant that can scale down to 16 pixels × 16 pixels. This is often the standalone logo mark for a brand.

After creating the custom payment method, the Dashboard displays the custom payment method ID (beginning with `cpmt_`) needed in step 2.

## Add custom payment method types

When you create your `EmbeddedPaymentElement.Configuration` object and initialize the `EmbeddedPaymentElement`, specify the custom payment methods to include in the Mobile Payment Element and a handler to complete the payment.

```kotlin
import com.stripe.android.paymentelement.EmbeddedPaymentElement

@Composable
fun CheckoutScreen() {
    val embeddedPaymentElementBuilder = remember {
        EmbeddedPaymentElement.Builder(
            createIntentCallback = { paymentMethod, shouldSavePaymentMethod ->
                // Create intent
            },
            resultCallback = { result ->
                when (result) {
                    is EmbeddedPaymentElement.Result.Completed -> showToast("Payment complete!")
                    is EmbeddedPaymentElement.Result.Canceled -> showToast("Payment canceled!")
                    is EmbeddedPaymentElement.Result.Failed -> showToast(result.error.localizedMessage ?: result.error.message)
                }
            },
        ).apply {confirmCustomPaymentMethodCallback(viewModel.customPaymentMethodHandler)
        }
    }

    val embeddedPaymentElement = rememberEmbeddedPaymentElement(embeddedPaymentElementBuilder)

    LaunchedEffect(embeddedPaymentElement) {val customPaymentMethod = PaymentSheet.CustomPaymentMethod(
            id = "cpmt_...",
            subtitle = "Optional subtitle"
        )

        embeddedPaymentElement.configure(
            configuration = EmbeddedPaymentElement.Configuration.Builder("Powdur").customPaymentMethods(listOf(customPaymentMethod))
                .build(),
            intentConfiguration = PaymentSheet.IntentConfiguration.Builder().build(),
        )
    }

    embeddedPaymentElement.Content()
}
class CheckoutCustomPaymentMethodHandler(...) : ConfirmCustomPaymentMethodCallback {
    override fun onConfirmCustomPaymentMethod(
        customPaymentMethod: PaymentSheet.CustomPaymentMethod,
        billingDetails: PaymentMethod.BillingDetails,
    ) {
      // ...explained in the next step
    }
}
```

## Complete the payment

When the customer selects a custom payment method and you call `confirm` on your `EmbeddedPaymentElement` instance, it calls the handler with the custom payment method and any billing details that you collected.

Your implementation then completes the payment (for example, by using your custom payment method provider’s SDK) and calls `CustomPaymentMethodResultHandler.handleCustomPaymentMethodResult()` with the result of the payment.

If your implementation might exit without confirming payment, make sure that you call `CustomPaymentMethodResultHandler.handleCustomPaymentMethodResult` for a canceled result.

```kotlin
import com.stripe.android.paymentelement.ConfirmCustomPaymentMethodCallback
import com.stripe.android.paymentelement.CustomPaymentMethodResult
import com.stripe.android.paymentelement.CustomPaymentMethodResultHandler

class CheckoutCustomPaymentMethodHandler(
    private val context: Context,
    /* Any other parameters required to complete payment. */
) : ConfirmCustomPaymentMethodCallback {
    override fun onConfirmCustomPaymentMethod(
        customPaymentMethod: PaymentSheet.CustomPaymentMethod,
        billingDetails: PaymentMethod.BillingDetails,
    ) {/* Your implementation must complete the payment with the
         * payment method provider. When the payment succeeds, cancels,
         * or fails, call `CustomPaymentMethodResultHandler.handleCustomPaymentMethodResult`
         * with the result. This example code just immediately fails:
         */
        CustomPaymentMethodResultHandler.handleCustomPaymentMethodResult(
            context,
            CustomPaymentMethodResult.failed(displayMessage = "Failed to complete payment"),
        )
    }
}
```

## Optional: Specify the order of custom payment methods

The Stripe smart ordering logic can’t rank custom payment methods because it has no context for them. By default, they appear after Stripe-supported payment methods. To explicitly position a custom payment method in the Mobile Payment Element, set `EmbeddedPaymentElement.Configuration.paymentMethodOrder`. We still intelligently rank the Stripe-supported payment methods following the custom payment method.

```kotlin
val configuration = EmbeddedPaymentElement.Configuration.Builder("Powdur")// Show cards first, followed by cpmt_..., followed by all other payment methods
    .paymentMethodOrder(listOf("card", "cpmt_..."))
    .build()
```

## Collect billing details

You can collect billing details using [billingDetailsCollectionConfiguration on the Payment Element configuration](https://docs.stripe.com/payments/mobile/accept-payment.md?platform=android#billing-details-collection). However, custom payment methods don’t collect billing details by default. To enable billing detail collection, set `disableBillingDetailCollection` to `false` on your `CustomPaymentMethod`.

```kotlin
val customPaymentMethod = PaymentSheet.CustomPaymentMethod(
    id = "cpmt_...",
    subtitle = "Optional subtitle"
)customPaymentMethod.disableBillingDetailCollection = false
```

## Test your integration

1. Go through your checkout flow and verify that the Mobile Payment Element displays your custom payment method. This example configures your custom payment method in the second position after cards.
1. Choose your custom payment method.
1. Click **Pay now** to test your custom payment method integration. Verify that your integration completes the transaction and that any post-payment actions (for example, displaying a confirmation page, success message, or failure message) still work with your custom payment method integration.

## Optional: Record the payment to your Stripe account [Server-side]

While you handle custom payment method transactions outside of Stripe, you can still [record the transaction details](https://docs.stripe.com/api/payment-record/report-payment/report.md) to your Stripe account to unify reporting and build back office workflows, such as issuing receipts or creating reports.

```javascript

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = new Stripe('<<YOUR_SECRET_KEY>>', {
  apiVersion: '2026-03-25.dahlia; invoice_partial_payments_beta=v3'
});

app.get('/process-cpm-payment', async (req, res) => {
  const paymentResult = processMyCustomPayment(...)

  // Create an instance of a custom payment method
  const paymentMethod = await stripe.paymentMethods.create({
    type: 'custom',
    custom: {
      type: '{{CUSTOM_PAYMENT_METHOD_TYPE_ID}}', // Identifier of the custom payment method type created in the Dashboard.
    }
  });

  // Report successful payment
  const paymentRecord = await stripe.paymentRecords.reportPayment({
    amount_requested: {
      value: paymentResult.amount,
      currency: paymentResult.currency
    },
    payment_method_details: {
      payment_method: paymentMethod.id
    },
    customer_details: {
      customer: paymentResult.customer.id
    },
    processor_details: {
      type: 'custom',
      custom: {
        payment_reference: paymentResult.id
      }
    },
    initiated_at: paymentResult.initiated_at,
    customer_presence: 'on_session',
    outcome: 'guaranteed',
    guaranteed: {
      guaranteed_at: paymentResult.completed_at
    }
  });

  // Respond to frontend to finish buying experience
  return res.json(...)
});

```

# React Native

> This is a React Native for when platform is react-native. View the full page at https://docs.stripe.com/payments/mobile/embedded-custom-payment-methods?platform=react-native.

## Before you begin

1. [Create a Stripe account](https://dashboard.stripe.com/register) or [sign in](https://dashboard.stripe.com/login).
1. Follow the [Accept In-app payments](https://docs.stripe.com/payments/mobile/accept-payment-embedded.md) guide to integrate with the Payment Element.

## Create your custom payment method in the Dashboard [Dashboard]

Go to **Settings** > **Payments** > [Custom Payment Methods](https://dashboard.stripe.com/settings/custom_payment_methods) to get to the custom payment methods page. Create a new custom payment method and provide the display name and logo that the Payment Element displays.

#### Choose the right logo

- If you provide a logo with a transparent background, consider the background color of the Payment Element on your page and make sure that it displays clearly.
- If you provide a logo with a background fill, provide rounded corners in your file because we won’t provide them.
- Choose a logo variant that can scale down to 16 pixels × 16 pixels. This is often the standalone logo mark for a brand.

After creating the custom payment method, the Dashboard displays the custom payment method ID (beginning with `cpmt_`) needed in step 2.

## Add custom payment method types

When you create your Payment Element configuration, specify the custom payment methods to include in the Payment Element and a handler to complete the payment.

```javascript
import {
  useEmbeddedPaymentElement,
  EmbeddedPaymentElementConfiguration,
} from '@stripe/stripe-react-native';
import type {
  BillingDetails,
  CustomPaymentMethod,
  CustomPaymentMethodResult,
  CustomPaymentMethodResultStatus,
} from '@stripe/stripe-react-native';

export default function CheckoutScreen() {
  const initialize = async () => {const customPaymentMethod: CustomPaymentMethod = {
      id: 'cpmt_...',
      subtitle: Optional subtitle,
    };

    const elementConfig: EmbeddedPaymentElementConfiguration = {
      // ... other configuration optionscustomPaymentMethodConfiguration: {
        customPaymentMethods: [customPaymentMethod],
        confirmCustomPaymentMethodCallback: handleCustomPaymentMethod,
      },
    };
  };
const handleCustomPaymentMethod = (
    customPaymentMethod: CustomPaymentMethod,
    billingDetails: BillingDetails | null,
    resultHandler: (result: CustomPaymentMethodResult) => void
  ) => {
    // ...explained in the next step
  };
}
```

## Complete the payment

When the customer selects a custom payment method and confirms payment in the Payment Element, it calls the handler with the custom payment method and any billing details that you collected.

Your implementation completes the payment (for example, by using your custom payment method provider’s SDK) and calls the `resultHandler` with the result of the payment: `Completed`, `Canceled`, or `Failed`.

If you pass `Failed` with an error message, the Payment Element displays the error message.

```javascript
import { Alert } from 'react-native';
import {
  useEmbeddedPaymentElement,
  EmbeddedPaymentElementConfiguration,
} from '@stripe/stripe-react-native';
import type {
  BillingDetails,
  CustomPaymentMethod,
  CustomPaymentMethodResult,
  CustomPaymentMethodResultStatus,
} from '@stripe/stripe-react-native';

export default function CheckoutScreen() {
  const initialize = async () => {
    const customPaymentMethod: CustomPaymentMethod = {
      id: 'cpmt_...',
      subtitle: Optional subtitle,
    };

    const elementConfig: EmbeddedPaymentElementConfiguration = {
      // ... other configuration options
      customPaymentMethodConfiguration: {
        customPaymentMethods: [customPaymentMethod],
        confirmCustomPaymentMethodCallback: handleCustomPaymentMethod,
      },
    };
  };

  const handleCustomPaymentMethod = (
    customPaymentMethod: CustomPaymentMethod,
    billingDetails: BillingDetails | null,
    resultHandler: (result: CustomPaymentMethodResult) => void
  ) => {// Your implementation needs to complete the payment with the payment method provider
    // When the payment completes, cancels, or fails, call resultHandler with the result.
    // This example code shows an alert for demonstration:
    Alert.alert(
      'Custom Payment Method',
      `Processing payment with ${customPaymentMethod.id}`,
      [
        {
          text: 'Success',
          onPress: () => resultHandler({ status: CustomPaymentMethodResultStatus.Completed }),
        },
        {
          text: 'Fail',
          style: 'destructive',
          onPress: () => resultHandler({
            status: CustomPaymentMethodResultStatus.Failed,
            error: 'Failed to complete payment!'
          }),
        },
        {
          text: 'Cancel',
          style: 'cancel',
          onPress: () => resultHandler({ status: CustomPaymentMethodResultStatus.Canceled }),
        },
      ]
    );
  };
}
```

## Optional: Specify the order of custom payment methods

Stripe’s smart ordering logic can’t rank custom payment methods because it doesn’t have context for them. By default, they appear after Stripe-supported payment methods. To explicitly position a custom payment method in the Payment Element, set `paymentMethodOrder` in your element configuration. The ordering logic still ranks the Stripe-supported payment methods following the custom payment method.

```javascript
const elementConfig: EmbeddedPaymentElementConfiguration = {
  // ... other configuration options// Show cards first, followed by cpmt_..., followed by all other payment methods
  paymentMethodOrder: ['card', 'cpmt_...'],
  customPaymentMethodConfiguration: {
    customPaymentMethods: [customPaymentMethod],
    confirmCustomPaymentMethodCallback: handleCustomPaymentMethod,
  },
};
```

## Collect billing details

You can collect billing details using [defaultBillingDetails in your Payment Element configuration](https://docs.stripe.com/payments/mobile/accept-payment-embedded.md?platform=react-native#billing-details-collection). However, custom payment methods don’t collect billing details by default. To enable billing detail collection, set `disableBillingDetailCollection` to `false` on your `CustomPaymentMethod`.

```javascript
const customPaymentMethod: CustomPaymentMethod = {
  id: 'cpmt_...',
  subtitle: Optional subtitle,disableBillingDetailCollection: false,
};
```

## Test your integration

1. Go through your checkout flow and verify that the Payment Element displays your custom payment method. This example configures your custom payment method in the second position after cards.
1. Choose your custom payment method.
1. Click **Pay now** to test your custom payment method integration. Verify that your integration completes the transaction and that any post-payment actions (for example, displaying a confirmation page, success message, or failure message) still work with your custom payment method integration.
   ![The Mobile Payment Element when a card brand is disallowed](assets/stripe-inapp-custom-payment-methods-test-ui.png)

## Optional: Record the payment to your Stripe account [Server-side]

While you handle custom payment method transactions outside of Stripe, you can still [record the transaction details](https://docs.stripe.com/api/payment-record/report-payment/report.md) to your Stripe account to unify reporting and build back office workflows, such as issuing receipts or creating reports.

```javascript

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = new Stripe('<<YOUR_SECRET_KEY>>', {
  apiVersion: '2026-03-25.dahlia; invoice_partial_payments_beta=v3'
});

app.get('/process-cpm-payment', async (req, res) => {
  const paymentResult = processMyCustomPayment(...)

  // Create an instance of a custom payment method
  const paymentMethod = await stripe.paymentMethods.create({
    type: 'custom',
    custom: {
      type: '{{CUSTOM_PAYMENT_METHOD_TYPE_ID}}', // Identifier of the custom payment method type created in the Dashboard.
    }
  });

  // Report successful payment
  const paymentRecord = await stripe.paymentRecords.reportPayment({
    amount_requested: {
      value: paymentResult.amount,
      currency: paymentResult.currency
    },
    payment_method_details: {
      payment_method: paymentMethod.id
    },
    customer_details: {
      customer: paymentResult.customer.id
    },
    processor_details: {
      type: 'custom',
      custom: {
        payment_reference: paymentResult.id
      }
    },
    initiated_at: paymentResult.initiated_at,
    customer_presence: 'on_session',
    outcome: 'guaranteed',
    guaranteed: {
      guaranteed_at: paymentResult.completed_at
    }
  });

  // Respond to frontend to finish buying experience
  return res.json(...)
});

```
