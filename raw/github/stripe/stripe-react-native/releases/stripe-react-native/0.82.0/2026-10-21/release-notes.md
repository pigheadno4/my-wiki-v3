**Changes**

* Updated Stripe iOS SDK from 26.13.0 to 26.14.0.
* Updated Stripe Android SDK from 23.22.0 to 23.23.0.

**Fixes**

* [Fixed] Android: Fixed custom font validation rejecting font resource names containing underscores in PaymentSheet and PaymentMethodMessagingElement. ([#2573](https://github.com/stripe/stripe-react-native/pull/2573))
* [Fixed] Fixed an issue where PaymentSheet could close immediately on Android after a JavaScript reload and Activity recreation.
* [Fixed] Android: Fixed R8 build failures when the optional push provisioning dependency is not included. ([#2715](https://github.com/stripe/stripe-react-native/pull/2715))