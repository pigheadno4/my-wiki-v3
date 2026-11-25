### Payments
* [ADDED][15314](https://github.com/stripe/stripe-android/pull/15314) Klarna confirmation options for passing SDK-generated interoperability and partner confirmation tokens (private preview).

### PaymentSheet
* [ADDED][15326](https://github.com/stripe/stripe-android/pull/15326) Added `ApiConfiguration.betas` in public preview to configure beta API version headers for Payment Element.
* [ADDED][15327](https://github.com/stripe/stripe-android/pull/15327) Added `PaymentSheet.Configuration.Builder.apiConfiguration` in public preview to configure API credentials for PaymentSheet and FlowController.
* [FIXED][15315](https://github.com/stripe/stripe-android/pull/15315) Fixed an issue that caused the Bank payment method to be hidden unnecessarily.
* [FIXED][15317](https://github.com/stripe/stripe-android/pull/15317) Fixed a memory leak where PaymentSheet could retain its Activity when closed before passive CAPTCHA warm-up finished.

See [the changelog for more details](https://github.com/stripe/stripe-android/blob/master/CHANGELOG.md).
