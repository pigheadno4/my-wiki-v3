# 6.0.0 2026-10-07
* Built with Xcode 27.0, Swift version 6.4.
* The framework is built with `-Xfrontend -disable-module-selectors-in-module-interface`, so the public `.swiftinterface` uses the pre-6.3 dot-qualified spelling instead of the SE-0491 `Module::Type` selector syntax Swift 6.3+ emits by default. Minimum requirement for integrators: Xcode 16.0+, Swift 6.0+.
### New
* WisePad 3 now supports amount surcharge and confirm-time on-reader surcharge consent. Collect-time `surchargeNotice` remains unsupported on WisePad 3.
* Added `SCPErrorCanceledByReader`, returned when an operation is canceled on the reader: the physical cancel button on a mobile reader, or the customer canceling on a smart reader. Programmatic cancellations initiated through the SDK continue to return `SCPErrorCanceled`.
* Tap to Pay on iPhone now returns `SCPErrorCanceledByReader` when the customer dismisses the payment sheet or backs out of PIN entry. Cancellations the integration requests through `SCPCancelable` continue to return `SCPErrorCanceled`.
* Added [`SCPPaymentMethodCardPresentDetails`](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPPaymentMethodCardPresentDetails.html), which exposes the instrument fields returned by `payment_method.card_present` and `payment_method.interac_present`, including available and preferred card networks.
* Added `latestCharge` and `latestChargeId` to `SCPPaymentIntent`, exposing the PaymentIntent's most recent Charge from either `latest_charge` or the legacy `charges` list.
* Preview: Refunds - Added `confirmRefund`, which creates a Refund for a PaymentIntent without collecting a payment method or displaying reader UI.
  * Added `SCPConfirmRefundParameters` to configure full or partial refunds and optional Refund fields.
  * Added `SCPRefundStatusCanceled` and `SCPRefundStatusRequiresAction`.
  * Added `SCPRefundNextAction` to expose required follow-up details.
  * To request access to this feature, please contact [Stripe Support](https://support.stripe.com/).
* Preview: Added support for Mexico installments (meses sin intereses, or MSI) for eligible card-present transactions. Use `SCPInstallmentsParametersBuilder` to enable installments when creating a PaymentIntent. After payment method collection, `SCPInstallmentsParameters.availablePlans` contains the eligible installment plans. After confirmation, `SCPInstallmentsParameters.plan` contains the plan selected by the cardholder.
  * To request access to this feature, please contact [Stripe Support](https://support.stripe.com/).
* Preview: Swish — Added `SCPPaymentMethodTypeSwish` and `SCPSwishDetails`, and exposed Swish details through `SCPPaymentMethod.swish` and `SCPPaymentMethodDetails.swish`. 
  * To request access to this feature, please contact [Stripe Support](https://support.stripe.com/).


### Updates
* **Breaking:** `SCPRefund.stripeId` now returns a nullable string. In Swift, `Refund.stripeId` is now `String?`. Check for a value before using it.
* **Breaking:** Standardized the PaymentMethod properties on `SCPSetupIntent` to match `SCPPaymentIntent`. The expanded `SCPPaymentMethod` is now exposed as `paymentMethod`, and its ID is exposed as `paymentMethodId`. Replace uses of the previous ID-valued `paymentMethod` property with `paymentMethodId`, and replace `paymentMethodExpanded` with `paymentMethod`.
* **Breaking:** Removed `SCPPaymentIntent.charges`. Use `latestCharge` for the expanded most recent Charge and `latestChargeId` for its ID.
* **Breaking:** Removed `SCPPaymentIntent.invoice`. Retrieve the PaymentIntent's invoice relationship through the Stripe API from your server.
* **Breaking:** `SCPPaymentMethod.cardPresent` and `SCPPaymentMethod.interacPresent` now return `SCPPaymentMethodCardPresentDetails` instead of `SCPCardPresentDetails`. Transaction-only properties remain on `SCPPaymentMethodDetails.cardPresent` and `SCPPaymentMethodDetails.interacPresent`. `SCPCardPresentDetails.networks` has been removed; use the corresponding `SCPPaymentMethodCardPresentDetails.networks` property instead. Expiration month and year on the new model are nullable to preserve their absence in API responses.
* **Breaking:** Removed `SCPCardBrand` (`CardBrand`). The `brand` properties on
  `SCPCardDetails`, `SCPCardPresentDetails`, and `SCPOfflineCardPresentDetails`
  are now strings. `SCPCardPresentDetails.network` and the entries in
  `SCPNetworks.available` are also strings, and `SCPNetworks.preferred` now
  exposes the API's preferred network. Replace enum comparisons such as `.visa`
  with string comparisons such as `"visa"`.
* **Breaking:** Replaced `SCPErrorPrinterLowBattery` with the more general `SCPErrorReaderBatteryLow`, returned when a reader remains connected but cannot complete an operation, such as printing, because its battery is too low.
* **Breaking:** Removed `SCPCardFundingType` (`CardFundingType`). The `funding`
  properties on `SCPCardDetails` (`CardDetails`) and `SCPCardPresentDetails`
  (`CardPresentDetails`) are now nullable strings containing the value returned
  by the Stripe API. Replace enum comparisons such as `.credit` with string
  comparisons such as `"credit"`. Missing funding values are returned as `nil`,
  and values introduced after the installed SDK version are preserved.
* **Breaking:** Removed `SCPTerminal.stringFromCardBrand:` (`Terminal.stringFromCardBrand`).
  `brand` values are now strings directly, so no conversion is necessary.
* **Breaking:** Removed `SCPReadMethod` (`ReadMethod`). The `readMethod`
  properties on `SCPCardPresentDetails` (`CardPresentDetails`) and
  `SCPOfflineCardPresentDetails` (`OfflineCardPresentDetails`) are now strings
  containing canonical Stripe API values such as `"contact_emv"`. Values
  introduced after the installed SDK version are preserved, and missing values
  are returned as `"unknown"`.
* **Breaking:** Removed `SCPTerminal.stringFromReadMethod:`
  (`Terminal.stringFromReadMethod`). `readMethod` values are now strings
  directly, so no conversion is necessary.
* **Breaking:** Removed `SCPErrorSimulatedOfflineModeNotAvailableForAccount`.
  Simulated offline mode is now generally available and is no longer gated
  per-account, so this error is never returned.
  `setSimulatedOfflineModeConfiguration:error:` no longer fails when a reader is
  connected, and connecting a testmode reader no longer disconnects it for
  lacking access. Remove any handling for this error code. Connecting to a
  livemode reader still returns
  `SCPErrorSimulatedOfflineModeNotAvailableInLivemode`.
* **Breaking:** `SCPPaymentIntentParametersBuilder` now defaults `captureMethod` to `SCPCaptureMethodAutomaticAsync` instead of `SCPCaptureMethodManual`. Integrations that require separate capture, including those using on-receipt tipping, incremental authorization, or extended authorization, must explicitly set `SCPCaptureMethodManual`.
* **Breaking:** `allowRedisplay` is now required when initializing `CollectSetupIntentConfigurationBuilder`, and all SetupIntent collection and processing methods require a `CollectSetupIntentConfiguration`. In Swift, migrate from `CollectSetupIntentConfigurationBuilder()` to `CollectSetupIntentConfigurationBuilder(allowRedisplay: .always)` (or another appropriate value), then pass the built configuration as `setupConfig` to `collectSetupIntentPaymentMethod` or as `collectConfig` to `processSetupIntent`.
* **Breaking:** Renamed `SCPRefundParameters` (`RefundParameters`) and `SCPRefundParametersBuilder` (`RefundParametersBuilder`) to `SCPProcessRefundParameters` (`ProcessRefundParameters`) and `SCPProcessRefundParametersBuilder` (`ProcessRefundParametersBuilder`). Update integrations that call `processRefund` to use the new names. Refund behavior is unchanged.
* **Breaking:** Added `ReaderInteractionDelegate` as the shared base protocol for `MobileReaderDelegate` and `TapToPayReaderDelegate`. The five reader lifecycle and display callbacks shared by Mobile Reader and Tap to Pay now use the `reader` method prefix, allowing integrations that support both reader types to implement these callbacks once.
  * Rename the five required Swift callbacks from `tapToPayReader(_:didStartInstallingUpdate:cancelable:)`, `tapToPayReader(_:didReportReaderSoftwareUpdateProgress:)`, `tapToPayReader(_:didFinishInstallingUpdate:error:)`, `tapToPayReader(_:didRequestReaderInput:)`, and `tapToPayReader(_:didRequestReaderDisplayMessage:)` to their corresponding `reader(_:` forms. In Objective-C, rename the corresponding selectors from `tapToPayReader:didStartInstallingUpdate:cancelable:`, `tapToPayReader:didReportReaderSoftwareUpdateProgress:`, `tapToPayReader:didFinishInstallingUpdate:error:`, `tapToPayReader:didRequestReaderInput:`, and `tapToPayReader:didRequestReaderDisplayMessage:` to selectors beginning with `reader:`.
  * Payment callbacks are not part of `ReaderInteractionDelegate`. Mobile Reader and Tap to Pay connections use the separate `ReaderPaymentInteractionDelegate.reader(_:didRequestInteraction:)` callback and `PaymentInteraction` wrapper types for blocking payment UI. Set the delegate on the connection configuration with `setReaderPaymentInteractionDelegate(_:)`.
  * The update API split is intentional: `MobileReaderDelegate.reader(_:didReportAvailableUpdate:)` reports a deferred optional update whose installation is user-triggered for Mobile Readers, while the shared installation callbacks also report mandatory Tap to Pay configuration installation during connection. Tap to Pay doesn't report available optional updates.
* **Breaking:** Removed `allowCustomerCancel` and `setAllowCustomerCancel:` from [`SCPInternetConnectionConfiguration`](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPInternetConnectionConfiguration.html). Customer-initiated cancellation is controlled per-collection by [`customerCancellation`](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPCollectPaymentIntentConfiguration.html#/c:objc(cs)SCPCollectPaymentIntentConfiguration(py)customerCancellation) on the collect configuration, which is enabled by default on readers that support it.
* **Breaking:** Removed the deprecated collect-then-confirm refund APIs: all `collectRefundPaymentMethod` overloads and the parameterless `confirmRefund(completion:)` and `confirmRefund(reader:completion:)` overloads. Use `processRefund` instead.
* **Breaking:** Removed the deprecated `SCPSimulateReaderUpdate` enum and `SCPSimulatorConfiguration.availableReaderUpdate`. Use `testReaderUpdate` on the Bluetooth, USB, or Tap to Pay connection configuration instead.
* **Breaking:** Removed the deprecated `description` properties from `SCPPaymentIntentParameters` and `SCPSetupIntentParameters`. Use `stripeDescription` instead.
* **Breaking:** The minimum supported iOS version is now iOS 16.


### Fixes
* Fixed automatic reconnect to report [`SCPDisconnectReasonPeerRemovedPairingInformation`](https://stripe.dev/stripe-terminal-ios/docs/Enums/SCPDisconnectReason.html#/c:@E@SCPDisconnectReason@SCPDisconnectReasonPeerRemovedPairingInformation) when a peer-removal error refines an initially unknown disconnect reason.
