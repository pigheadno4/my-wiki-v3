---
title: "Add Custom Payment Methods to the EmbeddedPaymentElement"
type: source
date_ingested: 2026-04-22
original_format: webpage
raw_files:
  - "stripe-inapp-embedded-custom-payment-methods-2025.md"
tags: [stripe, mobile, ios, android, react-native, embedded-payment-element, custom-payment-methods, cpmt, payment-records]
---

## Summary

EmbeddedPaymentElement-specific guide for Custom Payment Methods (`cpmt_` IDs). Same Dashboard setup as PaymentSheet CPMs — parallel page for the `EmbeddedPaymentElement` UI. Handler signatures differ from PaymentSheet (`EmbeddedPaymentElement.Configuration` vs `PaymentSheet.Configuration`; `EmbeddedPaymentElementResult` vs `PaymentSheetResult`).

> See also [[source-stripe-inapp-custom-payment-methods]] for the PaymentSheet/FlowController variant.

## Shared Facts (All Platforms)

- `cpmt_` IDs created in Dashboard → Settings → Payments → Custom Payment Methods; 50+ presets available
- CPMs appear after Stripe PMs by default — override with `paymentMethodOrder: ["card", "cpmt_..."]`
- Billing details disabled on CPMs by default — enable with `disableBillingDetailCollection = false`
- Recording: `paymentMethods.create({ type: 'custom' })` + `paymentRecords.reportPayment()` (server-side optional)
- Legal: merchant responsible for PSP agreement compliance

## iOS (Swift)

```swift
// Beta import required
@_spi(CustomPaymentMethodsBeta) import StripePaymentSheet

// Configuration
var configuration = EmbeddedPaymentElement.Configuration()
let customPaymentMethod = EmbeddedPaymentElement.CustomPaymentMethodConfiguration.CustomPaymentMethod(
    id: "cpmt_...", subtitle: "Optional subtitle"
)
configuration.customPaymentMethodConfiguration = .init(
    customPaymentMethods: [customPaymentMethod],
    customPaymentMethodConfirmHandler: handleCustomPaymentMethod(_:_:)
)

// Handler returns EmbeddedPaymentElementResult (not PaymentSheetResult)
func handleCustomPaymentMethod(
    _ type: EmbeddedPaymentElement.CustomPaymentMethodConfiguration.CustomPaymentMethod,
    _ billingDetails: STPPaymentMethodBillingDetails
) async -> EmbeddedPaymentElementResult {
    return .failed(error: myError)  // or .completed / .canceled
}
```

## Android (Kotlin/Compose)

```kotlin
EmbeddedPaymentElement.Builder(
    createIntentCallback = { ... },
    resultCallback = { result -> ... }
).apply {
    confirmCustomPaymentMethodCallback(viewModel.customPaymentMethodHandler)
}

class CheckoutCustomPaymentMethodHandler : ConfirmCustomPaymentMethodCallback {
    override fun onConfirmCustomPaymentMethod(
        customPaymentMethod: PaymentSheet.CustomPaymentMethod,
        billingDetails: PaymentMethod.BillingDetails,
    ) {
        CustomPaymentMethodResultHandler.handleCustomPaymentMethodResult(
            context,
            CustomPaymentMethodResult.failed(displayMessage = "Error shown to user")
        )
    }
}
```

- If implementation might exit without confirming: must still call `handleCustomPaymentMethodResult` with `.canceled`

## React Native

```javascript
const handleCustomPaymentMethod = (
    customPaymentMethod: CustomPaymentMethod,
    billingDetails: BillingDetails | null,
    resultHandler: (result: CustomPaymentMethodResult) => void
) => {
    resultHandler({ status: CustomPaymentMethodResultStatus.Completed });
    // or: { status: Failed, error: 'Message shown to user' }
    // or: { status: Canceled }
};
```

## Related Pages

- [[stripe-inapp-payments]] — in-app payments concept page
- [[source-stripe-inapp-custom-payment-methods]] — PaymentSheet/FlowController CPM variant
- [[source-stripe-inapp-accept-payment-embedded]] — EmbeddedPaymentElement integration guide

## Raw Sources

- [[stripe-inapp-embedded-custom-payment-methods-2025]] — verbatim guide (573 lines, iOS+Android+React Native, 1 image)
