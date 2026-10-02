### PaymentSheet
* [FIXED] LinkController (private preview) now returns an error when no funding sources are available for a Link session, rather than silently falling back to card.
* [ADDED] Added support for the Agrobank, MBSB Bank, and Bank of China FPX banks, and the FPX bank list is now displayed in alphabetical order.

### CryptoOnramp
* [ADDED][13623](https://github.com/stripe/stripe-android/pull/13623) Added optional Samsung Pay support to Crypto Onramp, including availability checks, payment credential collection, and developer-facing error details. Integrators must provide the Samsung Pay SDK in their application.

See [the changelog for more details](https://github.com/stripe/stripe-android/blob/master/CHANGELOG.md).
