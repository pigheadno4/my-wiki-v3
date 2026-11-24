<!-- Source URL: https://docs.stripe.com/terminal/features/extended-authorizations -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Extended authorizations

Capture a confirmed Stripe Terminal payment later.

Extended authorizations allow you to capture a *confirmed* (Confirming a PaymentIntent indicates that the customer intends to pay with the current or provided payment method. Upon confirmation, the PaymentIntent attempts to initiate a payment) [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) up to 30 days later, depending on the card brand and whether your business is in an eligible category. This is helpful if you need more than the typical 48 hours (or 5 days for Visa) between authorization and payment capture. For example, a hotel authorizes a payment in full when a guest checks in, but captures the payment when the guest checks out.

## Availability

Extended authorization is available on Visa, Mastercard, American Express and Discover. Extended authorizations aren’t supported on single-message payment methods like [Interac](https://docs.stripe.com/terminal/payments/regional.md?integration-country=CA#interac-payments) and [eftpos](https://docs.stripe.com/terminal/payments/regional.md?integration-country=AU#eftpos-payments).

> You can contact [support](https://support.stripe.com/contact) if you’re unsure about the eligibility of your merchant business category. If you’re a *Connect* (Connect is Stripe's solution for multi-party businesses, such as marketplace or software platforms, to route payments between sellers, customers, and other recipients) user, [set the merchant category code](https://docs.stripe.com/connect/setting-mcc.md) for your connected accounts to match their businesses.

## Request extended authorization support

When you create a `PaymentIntent`, you can request to extend the capture window of the payment. Set the [request_extended_authorization](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-card_present-request_extended_authorization) field to `true` and the [capture_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-capture_method) to `manual`.

> If you create the PaymentIntent with the iOS or Android SDK, set the capture method to manual explicitly. As of SDK 6.0.0, `captureMethod` defaults to automatic-asynchronous, so a PaymentIntent that doesn’t set it isn’t eligible for this feature. See the capture method migration guidance for [iOS](https://docs.stripe.com/terminal/references/sdk-migration-guide.md#ios-capture-method) or [Android](https://docs.stripe.com/terminal/references/sdk-migration-guide.md#android-capture-method).

#### Server-side

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=1000 \
  -d currency=usd \
  -d "allowed_payment_method_types[]=card_present" \
  -d capture_method=manual \
  -d "payment_method_options[card_present][request_extended_authorization]=true"
```

#### iOS

#### Swift

```swift
let cardPresentParams = try CardPresentParametersBuilder().setRequestExtendedAuthorization(true).build()
let paymentMethodOptionsParams = try PaymentMethodOptionsParametersBuilder(cardPresentParameters: cardPresentParams).build()
let params = try PaymentIntentParametersBuilder(amount: 1000, currency: "usd")
    .setPaymentMethodOptionsParameters(paymentMethodOptionsParams)
    .build()
Terminal.shared.createPaymentIntent(params) { createResult, createError in
    if let error = createError {
        print("createPaymentIntent failed: \(error)")
    } else if let paymentIntent = createResult {
        print("createPaymentIntent succeeded")
        // ...
    }
}
```

#### Android

#### Kotlin

```kotlin
val cardPresentParams = CardPresentParameters.Builder()
    .setRequestExtendedAuthorization(true)
    .build()

val paymentMethodOptionsParams = PaymentMethodOptionsParameters.Builder()
    .setCardPresentParameters(cardPresentParams)
    .build()

val params = PaymentIntentParameters.Builder()
    .setAmount(1000)
    .setCurrency("usd")
    .setPaymentMethodOptionsParameters(paymentMethodOptionsParams)
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

```tsx
const { paymentIntent, error } = await createPaymentIntent({
  amount: 1000,
  currency: 'usd',
  captureMethod: 'manual',
  paymentMethodOptions: {
    requestExtendedAuthorization: true,
  }
});

if (error) {
  console.log(`createPaymentIntent failed: ${error.message}`);
  return;
}

console.log('createPaymentIntent succeeded');
```

In the response, the [capture_before](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-capture_before) field indicates the time when the authorization expires. Failure to capture the payment by this time cancels the authorization and releases the funds. When this happens, the [PaymentIntent status](https://docs.stripe.com/payments/paymentintents/lifecycle.md) transitions to `canceled`.

## Authorization validity

Every card network and card brand has a different rule for how long an authorization is valid. With Terminal, an authorization for in-person payments is valid for at least two days. Because authorization rules can change without prior notice, use the [capture_before](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-capture_before) field to determine the validity window for an authorization.

> The `capture_before` field is located on the [Charge](https://docs.stripe.com/api/charges/object.md), so it’s only present after the `PaymentIntent` is confirmed.

| Card brand | Merchant category | Extended authorization validity window |
| --- | --- | --- |
| **Visa** | Hotel, lodging, vehicle rental, and cruise line | 30 days* |
| **Visa** | Aircraft rental, bicycle rental (including electric scooters), boat rental, clothing and costume rental, DVD and video rental, equipment and tool rental, furniture rental, motor home rental, motorcycle rental, and trailer parks and campgrounds | 10 days** |
| **Mastercard** (not including Maestro or Cirrus cards) | All merchant categories | 30 days |
| **American Express** | Lodging and vehicle rental | 30 days*** |
| **Discover** | Airline, bus charter/tour, car rental, cruise line, local/suburban commuter, passenger transportation including ferries, hotel, lodging, and passenger railway | 30 days |

\* The exact extended authorization window is 29 days and 18 hours, to allow time for clearing processes.\** The exact extended authorization window is 9 days and 18 hours, to allow time for clearing processes.\*** While your validity window is extended to 30 days, you must capture the authorized funds no later than the end of the duration of your customer’s stay or rental.
