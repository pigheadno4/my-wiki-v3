* BraintreeShopperInsights
  * Add `payPalCampaigns` to `BTCustomerSessionRequest` for customer session and recommendations requests so eligible PayPal campaign context can be recorded during the shopping journey.
  * Add `expiresAt` as an optional ISO-8601 `String` to `BTCustomerRecommendationsResult` to expose the recommendation expiration timestamp.
* BraintreePayPal
  * Add `campaigns` to `BTPayPalCheckoutRequest` so eligible campaign context can be persisted during order creation and surfaced in the PayPal checkout experience.
* BraintreeVenmo
  * Fix `BTVenmoAccountNonce.externalID` returning `nil` after vaulting a Venmo account with a client token

