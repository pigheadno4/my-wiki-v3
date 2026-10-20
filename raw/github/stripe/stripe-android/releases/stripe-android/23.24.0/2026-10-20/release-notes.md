### Crypto Onramp
* [Changed] Google Pay and Samsung Pay card sublabels now include the funding type (Credit, Debit, or Prepaid), falling back to Card when unavailable, matching Link's formatting.

### Payments
* [Fixed] Address country dropdowns now support autofill from saved addresses.

### PaymentSheet
* [CHANGED][15002](https://github.com/stripe/stripe-android/pull/15002) Moved `ApiConfigurationPreview` from the `paymentsheet` module to `stripe-core`. Update preview opt-in imports to `com.stripe.android.core.ApiConfigurationPreview`.
* [ADDED][14586](https://github.com/stripe/stripe-android/pull/14586) Added Naira bank transfer API bindings and PaymentSheet support for PaymentIntents.
* [ADDED][14830](https://github.com/stripe/stripe-android/pull/14830) Added Naira USSD API bindings and PaymentSheet support for PaymentIntents.
* [ADDED][14831](https://github.com/stripe/stripe-android/pull/14831) Added Naira Wallet API bindings and PaymentSheet support for PaymentIntents.
* [ADDED][14832](https://github.com/stripe/stripe-android/pull/14832) Added Mondu API bindings and PaymentSheet support for PaymentIntents.

### Identity
* [ADDED] Added test mode support to Stripe Identity, uploading bundled test document and selfie images for test-mode verification sessions.

See [the changelog for more details](https://github.com/stripe/stripe-android/blob/master/CHANGELOG.md).
