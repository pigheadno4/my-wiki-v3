### PaymentSheet
* [DEPRECATED] Deprecated the `googlePlacesApiKey` builder methods and the `AddressLauncher.Configuration` constructor overloads that accept a Google Places API key. Address autocomplete is now available to all merchants without providing a Google Places API key. Existing integrations can remove the key without losing autocomplete, and integrations that did not provide one receive autocomplete automatically.

### Payments
* [ADDED][14089](https://github.com/stripe/stripe-android/pull/14089) Support for Alipay when using `SetupIntent` through the direct APIs.

### Identity
* [ADDED][13176](https://github.com/stripe/stripe-android/pull/13176) Added guided 3D selfie capture for supported verification sessions, including left and right pose collection.

See [the changelog for more details](https://github.com/stripe/stripe-android/blob/master/CHANGELOG.md).
