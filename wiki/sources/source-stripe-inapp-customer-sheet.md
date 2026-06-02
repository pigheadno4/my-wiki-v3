---
title: "Payment Method Settings Sheet (CustomerSheet) — Mobile"
type: source
date_ingested: 2026-04-22
original_format: webpage
raw_files:
  - "stripe-inapp-customer-sheet-2025.md"
tags: [stripe, mobile, ios, android, react-native, customer-sheet, payment-method-settings, saved-payment-methods, customer-session, setup-intent]
---

## Summary

Integration guide for `CustomerSheet` (Payment Method Settings Sheet) — a prebuilt UI for managing saved payment methods in an app settings page (NOT checkout). Covers iOS UIKit, iOS SwiftUI, Android (Compose), and React Native.

> `CustomerSheet` is the code name for "Payment Method Settings Sheet" for historical reasons.
> For checkout, use In-app Payments (Payment Sheet / EmbeddedPaymentElement) which supports more PMs.

## Supported Payment Methods

| Platform | Supported |
| --- | --- |
| iOS | Cards, US bank accounts, SEPA Direct Debit |
| Android | Cards, US bank accounts |
| React Native | Cards, US bank accounts |

## Two Required Server Endpoints

```javascript
// 1. CustomerSession client secret
app.post('/customer', async (req, res) => {
  const customer = await stripe.customers.create();
  const customerSession = await stripe.customerSessions.create({
    customer: customer.id,
    components: {
      customer_sheet: {
        enabled: true,
        features: { payment_method_remove: 'enabled' }
      },
    },
  });
  res.json({ customer: customer.id, customerSessionClientSecret: customerSession.client_secret });
});

// 2. SetupIntent client secret
app.post('/create-setup-intent', async (req, res) => {
  const setupIntent = await stripe.setupIntents.create({ customer: customer.id });
  res.json({ setupIntent: setupIntent.client_secret });
});
```

**Legacy ephemeral keys**: if migrating from legacy, set `payment_method_allow_redisplay_filters: ["unspecified", "always"]` to show older saved PMs.

## Platform APIs

### iOS UIKit

```swift
let customerSheet = CustomerSheet(
    configuration: configuration,
    intentConfiguration: CustomerSheet.IntentConfiguration(setupIntentClientSecretProvider: { ... }),
    customerSessionClientSecretProvider: { ... }
)

customerSheet.present(from: self, completion: { result in
    switch result {
    case .canceled(let paymentOption), .selected(let paymentOption):
        // paymentOption is PaymentOptionSelection? (nil if user deleted previously selected PM)
    case .error(let error): ...
    }
})
```

### iOS SwiftUI

```swift
.customerSheet(
    isPresented: $showingCustomerSheet,
    customerSheet: model.customerSheet,
    onCompletion: model.onCompletion
)
// result: .selected(PaymentOptionSelection?) / .canceled / .error
```

### Android (Kotlin/Compose)

```kotlin
// @OptIn(ExperimentalCustomerSheetApi::class) required
class MyCustomerSessionProvider : CustomerSheet.CustomerSessionProvider() {
    override suspend fun providesCustomerSessionClientSecret(): Result<CustomerSheet.CustomerSessionClientSecret>
    override suspend fun provideSetupIntentClientSecret(customerId: String): Result<String>
}

val customerSheet = rememberCustomerSheet(
    customerSessionProvider = viewModel.customerSessionProvider,
    callback = viewModel::handleResult
)
LaunchedEffect(customerSheet) { customerSheet.configure(configuration) }

// Results: CustomerSheetResult.Selected / .Canceled / .Failed
// Both Selected and Canceled return selection?.paymentOption
```

**Google Pay**: add `googlePayEnabled(true)` to Configuration.Builder + AndroidManifest `com.google.android.gms.wallet.api.enabled` meta-data.

### React Native

```javascript
const clientSecretProvider: ClientSecretProvider = {
    async provideCustomerSessionClientSecret(): Promise<CustomerSessionClientSecret>,
    async provideSetupIntentClientSecret(): Promise<string>
};

await CustomerSheet.initialize({ intentConfiguration, clientSecretProvider });
const { error, paymentOption, paymentMethod } = await CustomerSheet.present();
// error.code === CustomerSheetError.Canceled → dismissed without change
```

## Fetch Without Presenting

`customerSheet.retrievePaymentOptionSelection()` — all platforms, returns current selected PM without showing the sheet.

## ACH

- iOS: add `StripeFinancialConnections` dependency
- Android: add `com.stripe:financial-connections:23.5.0` dependency

## Related Pages

- [[stripe-inapp-payments]] — in-app payments concept page
- [[stripe-saved-payment-methods]] — saved payment methods concept page

## Raw Sources

- [[stripe-inapp-customer-sheet-2025]] — verbatim guide (~1213 lines, iOS UIKit + SwiftUI + Android + React Native, 1 image × 3)
