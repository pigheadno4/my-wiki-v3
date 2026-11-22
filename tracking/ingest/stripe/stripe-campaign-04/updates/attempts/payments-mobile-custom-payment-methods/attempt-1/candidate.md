---
title: "Add Custom Payment Methods to Mobile Payment Element"
type: source
date_ingested: 2026-04-22
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/mobile/custom-payment-methods"
raw_files:
  - "stripe-inapp-custom-payment-methods-2025.md"
tags: [stripe, mobile, ios, android, react-native, custom-payment-methods, cpmt, payment-sheet, payment-records]
---

## Summary

The April 22, 2026 guide covers custom payment methods in PaymentSheet on iOS, Android and React Native, including the iOS and Android FlowController paths. The merchant completes the transaction outside Stripe and reports the external result to the mobile UI. Recording the transaction in Stripe is optional.

The separate embedded guide uses its own configuration and result types, including `EmbeddedPaymentElement.Configuration` and `EmbeddedPaymentElementResult` in its April Swift example. [[source-stripe-inapp-embedded-custom-payment-methods]]

## April Prerequisites and Shared Setup

- Start with a Stripe account and a working Payment Sheet payment integration for the relevant platform (April raw lines 18–25, 211–218 and 421–428).
- In Dashboard, open **Settings → Payments → Custom Payment Methods** and give the method a display name and logo. The April guide lists over 50 presets. Use the resulting `cpmt_` type ID in the mobile configuration (April raw lines 8–12, 23–54, 217–230 and 427–476).
- Custom methods follow Stripe-supported methods by default. Use `paymentMethodOrder` to position them, for example `["card", "cpmt_..."]`. Billing details are opt-in through `disableBillingDetailCollection = false`. The examples refer to platform-specific PaymentSheet billing configurations (April raw lines 129–145, 336–355 and 554–578).
- The client handler receives the selected custom method and any billing details that were collected. Merchant code processes and finalizes the payment with the external payment service provider, then relays completion, cancellation or failure to the relevant UI. The merchant is responsible for applicable laws and its payment service provider agreement (April raw lines 8–12, 60–124, 274–331 and 480–550).

## April iOS Example

```swift
// SPI import used in the April Swift sample
@_spi(CustomPaymentMethodsBeta) import StripePaymentSheet

// Handler signature
func handleCustomPaymentMethod(
    _ customPaymentMethodType: PaymentSheet.CustomPaymentMethodConfiguration.CustomPaymentMethod,
    _ billingDetails: STPPaymentMethodBillingDetails
) async -> PaymentSheetResult {
    // Return .completed, .canceled, or .failed(error:)
}
```

The April PaymentSheet and FlowController prose calls the error result `failure(error:)`. The Swift snippets use `.failed(error:)` and return `PaymentSheetResult`. The guide describes displaying Swift `errorDescription` or NSError `localizedDescription`. Its PaymentSheet example notes that `presentedViewController` can present UI over the sheet (April raw lines 60–128).

## April Android Example

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

The April PaymentSheet prose names `CustomPaymentMethodResultHandler.onCustomPaymentMethodResult()`. The Kotlin snippets and the FlowController prose use `handleCustomPaymentMethodResult()`. The Android FlowController guidance explicitly says to report a canceled result if the implementation exits without confirming payment. The guide says PaymentSheet displays the failure's `displayMessage` (April raw lines 274–335).

## April React Native Example

```javascript
const handleCustomPaymentMethod: ConfirmCustomPaymentMethodCallback = (
    customPaymentMethod, billingDetails, resultHandler
) => {
    resultHandler({ status: CustomPaymentMethodResultStatus.Completed });
    // or: { status: CustomPaymentMethodResultStatus.Failed, error: 'Message shown to user' }
    // or: { status: CustomPaymentMethodResultStatus.Canceled }
};
```

The April example passes a `resultHandler` into the callback and uses `CustomPaymentMethodResultStatus` to report completion, failure or cancellation. The demo alert illustrates result handling (April raw lines 438–550).

## Optional Server-Side Reporting

The April mobile examples initialize the server SDK with `2026-03-25.dahlia` and `invoice_partial_payments_beta=v3`. They create a separate `type: 'custom'` PaymentMethod keyed by the Dashboard `cpmt_` identifier, then call `paymentRecords.reportPayment()` with its ID and the external processor's payment reference. The sample uses `outcome: 'guaranteed'` after an externally successful payment (April raw lines 153–205, 363–415 and 586–638).

The separate November 7, 2026 API reference illustrates `POST /v1/payment_records/report_payment` with `2026-10-28.endive`, a version header without a beta suffix, and inline custom payment method details. These are dated request examples. The API reference leaves current mobile SDK compatibility and account availability unverified. The UI handler reports the external result, and the Payment Record stores the supplied account of that payment. Neither establishes Stripe processing, settlement or an independent guarantee of the external funds. [Report a payment API reference](https://docs.stripe.com/api/payment-record/report)

## Related Pages

- [[stripe]]
- [[stripe-custom-payment-methods]] — custom method identifiers, integration patterns and optional reporting
- [[stripe-inapp-payments]] — in-app payments concept page
- [[source-stripe-inapp-payments-overview]] — in-app payments overview

## Raw Sources

- [[raw/stripe-inapp-custom-payment-methods-2025|April 22, 2026 mobile custom payment methods guide]] — iOS, Android and React Native PaymentSheet guidance.

## Related raw API references

- [[raw/stripe-payments-mobile-custom-payment-methods-2026-11-07|November 7, 2026 mobile platform index]] — navigation for iOS, Android and React Native. The linked platform bodies were outside the capture.
