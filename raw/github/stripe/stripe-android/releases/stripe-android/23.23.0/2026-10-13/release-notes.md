### Payments
* [Security] Restricted intent URLs in payment authentication to browsable activity resolution.
* [Fixed] Return helpful errors for invalid PaymentIntent and SetupIntent client secrets without including the supplied value.
* [Fixed] Return errors for invalid client secrets in legacy Stripe next-action APIs instead of throwing uncaught exceptions.

### PaymentSheet
* [Fixed] Address forms now recognize country and state codes and names case-insensitively when prefilling default values.
* [ADDED][14585](https://github.com/stripe/stripe-android/pull/14585) Added Naira card API bindings and PaymentSheet support for one-time payments.
* [REMOVED] Removed the test mode header from PaymentSheet, CustomerSheet, and the Embedded Payment Element.
* [ADDED][14620](https://github.com/stripe/stripe-android/pull/14620) Added GCash API bindings and PaymentSheet support.
* [ADDED][14829](https://github.com/stripe/stripe-android/pull/14829) Added QRIS API bindings and PaymentSheet support for PaymentIntents.
* [ADDED][14828](https://github.com/stripe/stripe-android/pull/14828) Added ShopeePay API bindings and PaymentSheet support for PaymentIntents.

### AddressElement
* [Fixed] Address Element now rejects incomplete optional phone numbers.

### Financial Connections
* [REMOVED] Removed the test mode indicator from the header.

See [the changelog for more details](https://github.com/stripe/stripe-android/blob/master/CHANGELOG.md).
