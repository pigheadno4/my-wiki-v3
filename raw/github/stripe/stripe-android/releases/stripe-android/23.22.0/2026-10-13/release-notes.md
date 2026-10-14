### Crypto Onramp
* [Added] Opt-in Samsung Pay contact collection for name, address, email, and phone prefill.
* [Changed] Crypto Onramp wallet collection returns contact-only `KycInfo` when available, including email, validated E.164 phone, and the original phone string.
* [Added] Optional `email`, `phone`, and `rawPhone` fields on Crypto Onramp `KycInfo` for contact prefill. These fields are not submitted with KYC.
* [Added] Crypto Onramp country hints and a recoverable `PlatformPayAccountChangedException` when wallet collection must be repeated after an account change.
* [Changed] Crypto Onramp supports Google Pay and Samsung Pay collection before Link authentication. Creating a crypto payment token still requires a crypto customer.

### Payments
* [FIXED] Stopped installing a process-wide HTTP response cache that could affect other network requests in the app.

### PaymentSheet
* [ADDED][14584](https://github.com/stripe/stripe-android/pull/14584) Added GoPay API bindings and PaymentSheet support for PaymentIntents.
* [ADDED][14619](https://github.com/stripe/stripe-android/pull/14619) Added MoMo API bindings and PaymentSheet support for PaymentIntents.
* [ADDED][14756](https://github.com/stripe/stripe-android/pull/14756) Added Pix support for PaymentIntents and SetupIntents in PaymentSheet.
* [FIXED][14759](https://github.com/stripe/stripe-android/pull/14759) Disabled the saved payment method View more and Edit actions during payment processing in the Embedded Payment Element.

See [the changelog for more details](https://github.com/stripe/stripe-android/blob/master/CHANGELOG.md).
