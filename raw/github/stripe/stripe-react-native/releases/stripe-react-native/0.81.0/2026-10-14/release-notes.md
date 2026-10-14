* [Added] Added `financialConnectionsSessionId` to Financial Connections `FinancialConnectionsEvent`. Events are now emitted once the session identifier is available.

**Changes**

* Updated Stripe iOS SDK from 26.12.1 to 26.13.0.
* Updated Stripe Android SDK from 23.21.0 to 23.22.0.

**Fixes**

* [Fixed] Android: Fixed PaymentSheet presentation failures after the host Activity changes. ([#2705](https://github.com/stripe/stripe-react-native/pull/2705))
* [Fixed] Fixed an issue where CustomerSheet could crash on iOS or remain stuck loading on Android when using CustomerSession.
* [Fixed] Android: ConfirmationToken `setupFutureUsage` now returns the `FutureUsage` values (`OffSession` / `OnSession` / `None`), matching iOS. ([#2697](https://github.com/stripe/stripe-react-native/pull/2697))