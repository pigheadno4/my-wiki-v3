**Changes**

* Updated Stripe iOS SDK from 26.14.0 to 26.15.0.
* Updated Stripe Android SDK from 23.23.0 to 23.24.0.
* [Deprecated] `AddressSheet`'s Android-only `googlePlacesApiKey` prop. Autocomplete now does not require a Google Places API key.

**Fixes**

* [Fixed] Connect embedded components no longer hang without calling `onLoadError` when an init param contains a double quote, backslash, or backtick, such as a double-quoted family name in `appearance.variables.fontFamily`.