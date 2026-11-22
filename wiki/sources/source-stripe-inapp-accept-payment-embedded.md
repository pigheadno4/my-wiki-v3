---
title: "Accept In-App Payments with the Embedded Payment Element"
type: source
date_ingested: 2026-04-22
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/mobile/accept-payment-embedded"
raw_files:
  - "stripe-inapp-accept-payment-embedded-2025.md"
tags: [stripe, mobile, ios, android, react-native, embedded-payment-element, embedded, scrollview, height-changes, mandate, formsheet]
---

## Summary

The April 22, 2026 guide describes embedding Stripe's Mobile Payment Element in native checkout. It renders a list of payment methods and opens detail sheets for methods that need them. The Swift examples below cover UIKit and SwiftUI. Use the April capture's platform and intent routes to find the Android and React Native examples.

## April 22, 2026 Platform and Intent Routes

These line ranges point into the April capture under Raw Sources.

| Platform | Accept a payment (`payment`) | Set up a payment method (`setup`) | Pay and save (`paymentsfu`) |
| --- | --- | --- | --- |
| iOS | 10–1188 | 1189–2379 | 2380–3788 |
| Android | 3789–4640 | 4641–5484 | 5485–6461 |
| React Native | 6462–7452 | 7453–8539 | 8540–9657 |

## Key Integration Requirements

- **SDK and server.** The April paths set up the platform SDK with a publishable key, enable payment methods and use merchant server endpoints that call Stripe.
- **iOS.** Place the changing-height Element in a scrollable container such as `UIScrollView` in UIKit or `ScrollView` in SwiftUI. Set `presentingViewController` and `delegate` after UIKit `create()`. The SwiftUI example loads `EmbeddedPaymentElementViewModel` as a `@StateObject` and renders `EmbeddedPaymentElementView` (lines 110–146 and 333–406).
- **Android.** Render Jetpack Compose `Content` inside a scrollable container. Classic Android views wrap the Element in `ComposeView` (lines 3870–4006).
- **React Native.** Use `useEmbeddedPaymentElement` and render `embeddedPaymentElementView`. Keep the native Android view mounted so initialization can finish. The example controls visibility with opacity (lines 6544–6650).

## iOS UIKit Pattern

```swift
// 1. Create async
let embeddedPaymentElement = try await EmbeddedPaymentElement.create(
  intentConfiguration: intentConfig, configuration: configuration
)
embeddedPaymentElement.presentingViewController = self
embeddedPaymentElement.delegate = self

// 2. Add to UIScrollView
scrollView.addSubview(embeddedPaymentElement.view)

// 3. Confirm
let result = await embeddedPaymentElement.confirm()
```

## Handle Height Changes (UIKit)

```swift
extension MyVC: EmbeddedPaymentElementDelegate {
  func embeddedPaymentElementDidUpdateHeight(embeddedPaymentElement: EmbeddedPaymentElement) {
    self.view.setNeedsLayout()
    self.view.layoutIfNeeded()
  }
}
```

Test: call `embeddedPaymentElement?.testHeightChange()` in DEBUG.

## `paymentOption` — Selected PM Details

- `.label`: e.g. "····4242"
- `.image`: e.g. Visa logo
- Billing details and `.mandateText`

Delegate: `embeddedPaymentElementDidUpdatePaymentOption` — fires when PM selection changes.

## Cart Changes

```swift
let result = await embeddedPaymentElement?.update(intentConfiguration: updatedIntentConfig)
// .succeeded | .failed | .canceled (when subsequent update cancels this one)
```

The Swift UIKit and SwiftUI examples use `update()`. React Native also uses `update()` and awaits it to sequence loading states. The Android cart example calls `configure()` again, which updates the content and selected option. Refresh the displayed total and selection after the change, and let the customer retry a failed Swift update (lines 264–292, 458–484, 4009–4036 and 6683–6690).

## Checkout Button and In-Sheet Confirmation

```swift
configuration.formSheetAction = .confirm(completion: { result in
  // .completed | .failed | .canceled
})
```

In the April iOS and Android guides, **Continue** normally dismisses the detail sheet so the customer can finish in the app checkout. The optional `formSheetAction` configuration confirms the selected flow when the customer taps the action in the sheet. In the Swift example above the result callback runs after dismissal, and the embedded UI cannot be reused after completion. In setup mode the action confirms setup without a charge. Android shows its own builder configuration (lines 100–106, 579–602, 1794–1815, 3861–3868, 4155–4179 and 5027–5049).

## Intent Creation, Confirmation and Payment Outcomes

- **Charge or save.** Use a server-created `PaymentIntent` for a charge, a `SetupIntent` to save without charging, or a `PaymentIntent` with the intended future-use setting for pay-and-save. The server determines the charge amount in a trusted environment and the client `IntentConfiguration` needs to match the intent's applicable properties, such as amount and currency for payment or `usage` for setup (lines 604–610, 1189–1199, 1817–1889 and 3035–3104).
- **Confirm the selected intent.** The documented deferred SDK flow calls the merchant backend from the confirmation callback and returns the matching intent's client secret or an error. The SDK confirms with that secret in the client-confirmed flow. The April iOS callback example also directs the integrator to pass the ConfirmationToken ID to the backend when using server-side confirmation (lines 293–330, 4067–4115 and 6822–6874).
- **Historical setup wording.** The iOS setup callbacks correctly ask the server for a `SetupIntent`, then call the object being confirmed a `PaymentIntent`. Follow the setup-mode configuration and server `SetupIntent` in that same variant. Android and React Native explicitly confirm the `SetupIntent`. The Android setup example's payment wording in the button label and completion comment still accompanies a setup flow (lines 1189–1199, 1336–1347, 1535–1537, 1724–1726, 1817–1889, 4939–4975 and 7833–7835).
- **Payment outcomes.** Delayed methods are hidden by default. `allowsDelayedPaymentMethods` lets the SDK show eligible enabled methods without activating them. The app can report completion while payment is pending. Use server-side payment events for fulfillment decisions. `payment_intent.processing` is pending and may later be followed by `payment_intent.succeeded` or `payment_intent.payment_failed`. Setup completion records payment-method setup. An authentication return or client result alone cannot establish payment success or funds availability (lines 747–759, 905–929, 4409–4422 and 7028–7040).

## iOS Authentication Returns

The April native iOS and React Native-on-iOS SDK guides use a custom URL scheme forwarded to Stripe for returns from Safari or a banking app. The native guide sets `returnURL` on the Element configuration. Universal Links belong to the separate app-to-web flows linked in [[stripe-inapp-payments]]. In the React Native iOS examples, enabled methods that require a return URL are unavailable without one (lines 680–745, 6890–6950, 7900–7910 and 8992–9002).

## Saving Payment Methods and Consent

- **Customer identity.** Attach the payment method for future payments to a customer-configured Accounts v2 `Account` (`customer_account`) or a Customers v1 `Customer` (`customer`). The April guide describes Accounts v2 as generally available for Connect users and in public preview with a preview API version for other Stripe users (lines 1277–1311, 1817–1889, 2489–2524 and 7537–7548).
- **CustomerSession.** The saved-card examples pass the customer ID and CustomerSession client secret separately from the intent's secret. `payment_method_save` enables the save checkbox in the documented path, and the examples show redisplay and removal controls (lines 794–902 and 4299–4408).
- **Merchant obligations.** The April pay-and-save guidance calls for use-specific terms, explicit consent and a record of the customer's written agreement. The merchant is responsible for compliance. `allow_redisplay` distinguishes attached methods that can be shown for future purchases. A later off-session charge uses a new server-side `PaymentIntent`, and an authentication request can still cause it to fail (lines 1958–2008, 2395–2405, 3198–3247 and 8554–8565).
- **Global future use and per-method preview.** In the standard April global pay-and-save example the server sets `setup_future_usage` on the `PaymentIntent` and matches the client `IntentConfiguration`. In the separate April Embedded Mobile Payment Element per-method SDK preview, leave both `setup_future_usage` and `payment_method_options[X][setup_future_usage]` unset on the server-created `PaymentIntent`. The SDK supplies them from `IntentConfiguration` (lines 3035–3104, 3320–3354, 6046–6084 and 9196–9258).

## Mandate Display

The April guide says the Element displays mandates by default. If you display the mandate yourself, keep the text close to the Buy button and make its links work. The Swift examples read mandate text from the selected payment option.

**April Swift example conflict.** The UIKit and SwiftUI manual-render snippets set `embeddedViewDisplaysMandateText = true` even though the accompanying prose says to disable built-in display. The Android builder example passes `false`. The April capture leaves the appropriate Swift flag setting unresolved (iOS lines 548–576, 1763–1792 and 2979–3008 and Android lines 4136–4154).

## `clearPaymentOption()` — Deselect PM

```swift
embeddedPaymentElement?.clearPaymentOption()
// or: embeddedViewModel.clearPaymentOption()
```

Useful when you have external payment options (e.g. Apple Pay button) and need to deselect.

## Additional April Examples

- iOS SDK installation and dated platform compatibility (lines 29–90). The Android Gradle sample uses Stripe Android SDK `23.5.0` and includes Financial Connections for US bank accounts (lines 3810–3853). React Native setup and test/live key guidance are at lines 6481–6536.
- Native Apple Pay merchant ID, certificate, Xcode capability, and one-time and recurring configuration (lines 930–1022). Native Android Google Pay manifest, environment and physical-device testing, including the supported-country and test-account prerequisites (lines 4423–4462).
- Payment testing, appearance and CVC recollection examples (iOS lines 761–788 and 1058–1187 and Android lines 4270–4297 and 4472–4640).

## Images

![iOS embedded example](../raw/assets/stripe-inapp-ios-embedded.png)
![Android embedded example](../raw/assets/stripe-inapp-android-embedded.png)
![Embedded pay immediately](../raw/assets/stripe-inapp-embedded-pay-immediate.png)

## Related Pages

- [[stripe]]
- [[stripe-inapp-payments]] — mobile UI and intent patterns
- [[source-stripe-inapp-payment-element]] — Payment Element overview

## Raw Sources

- [[raw/stripe-inapp-accept-payment-embedded-2025|Embedded Mobile Payment Element integration guide]] — captured 2026-04-22. Covers nine iOS, Android and React Native variants.

## Related raw API references

- [[raw/stripe-payments-mobile-accept-payment-embedded-2026-11-07|2026-11-07 platform and intent variant index]] — navigation for iOS, Android and React Native payment, setup and pay-and-save guides. The linked November variant bodies were outside the capture.
