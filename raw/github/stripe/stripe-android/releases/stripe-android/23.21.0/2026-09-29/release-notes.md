### Payments
* [FIXED][14625](https://github.com/stripe/stripe-android/pull/14625) Fixed an issue where PaymentSheet and `CardNumberEditText` rejected valid card numbers for BINs whose account ranges have different PAN lengths, such as some 16-digit UnionPay cards.

### PaymentSheet
* [ADDED] `EmbeddedPaymentElement.Configuration.apiConfiguration` to set publishable key and stripe account ID is now available in public preview.
* [ADDED] Added support for MB WAY payments.

### Financial Connections
* [FIXED] Preserved `no_eligible_accounts` in `onEvent` error callbacks instead of reporting it as `unexpected_error`.
* [FIXED] Prevented background authorization-session telemetry failures from triggering `onEvent` error callbacks.

See [the changelog for more details](https://github.com/stripe/stripe-android/blob/master/CHANGELOG.md).
