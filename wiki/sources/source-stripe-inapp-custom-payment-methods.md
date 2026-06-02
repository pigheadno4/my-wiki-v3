---
title: "Add Custom Payment Methods to Mobile Payment Element"
type: source
date_ingested: 2026-04-22
original_format: webpage
raw_files:
  - "stripe-inapp-custom-payment-methods-2025.md"
tags: [stripe, mobile, ios, android, react-native, custom-payment-methods, cpmt, payment-sheet, payment-records]
---

## Summary

Mobile-specific integration for Custom Payment Methods (`cpmt_` IDs) across iOS, Android, and React Native. Same Dashboard setup as web CPMs, but platform-specific SDK integration. Transactions processed outside Stripe; optional recording via `paymentRecords.reportPayment()`.

## Shared Facts (All Platforms)

- `cpmt_` IDs created in Dashboard → Settings → Payments → Custom Payment Methods; 50+ presets available
- CPMs appear after Stripe PMs by default — override with `paymentMethodOrder: ["card", "cpmt_..."]`
- Billing details disabled on CPMs by default — enable with `disableBillingDetailCollection = false`
- Recording: `paymentMethods.create({ type: 'custom' })` + `paymentRecords.reportPayment()` (beta API version required)
- Legal: merchant responsible for PSP agreement compliance

## iOS (Swift)

```swift
// Beta import required
@_spi(CustomPaymentMethodsBeta) import StripePaymentSheet

// Handler signature
func handleCustomPaymentMethod(
    _ customPaymentMethodType: PaymentSheet.CustomPaymentMethodConfiguration.CustomPaymentMethod,
    _ billingDetails: STPPaymentMethodBillingDetails
) async -> PaymentSheetResult {
    // Return .completed, .canceled, or .failed(error:)
}
```

- Error displayed via `errorDescription` (Swift) or `localizedDescription` (NSError)
- FlowController: same handler pattern; can `presentedViewController` to show UI on top

## Android (Kotlin)

```kotlin
// Implement ConfirmCustomPaymentMethodCallback
class Handler : ConfirmCustomPaymentMethodCallback {
    override fun onConfirmCustomPaymentMethod(
        customPaymentMethod: PaymentSheet.CustomPaymentMethod,
        billingDetails: PaymentMethod.BillingDetails
    ) {
        // Call when done:
        CustomPaymentMethodResultHandler.handleCustomPaymentMethodResult(
            context,
            CustomPaymentMethodResult.failed(displayMessage = "Error message shown to user")
        )
    }
}
```

- FlowController: **must** call handler even on cancel — otherwise UI hangs
- `displayMessage` shown directly to customer on failure

## React Native

```javascript
const handleCustomPaymentMethod: ConfirmCustomPaymentMethodCallback = (
    customPaymentMethod, billingDetails, resultHandler
) => {
    resultHandler({ status: CustomPaymentMethodResultStatus.Completed });
    // or: { status: CustomPaymentMethodResultStatus.Failed, error: 'Message shown to user' }
    // or: { status: CustomPaymentMethodResultStatus.Canceled }
};
```

## Related Pages

- [[stripe-custom-payment-methods]] — web CPM concept page (same cpmt_ IDs, same recording pattern)
- [[stripe-inapp-payments]] — in-app payments concept page
- [[source-stripe-inapp-payments-overview]] — in-app payments overview

## Raw Sources

- [[stripe-inapp-custom-payment-methods-2025]] — verbatim mobile CPM guide (638 lines, iOS+Android+React Native)
