
* General
    * Remove `VisaCheckout` module. Visa Checkout is no longer supported.
    * Deprecate `Configuration#isVisaCheckoutEnabled`, `Configuration#visaCheckoutApiKey`,
      `Configuration#visaCheckoutExternalClientId`, and `Configuration#visaCheckoutSupportedNetworks`.
      These will be removed in the next major version.
* Build
  * Drop Gradle Toolchains usage
* AmericanExpress
    * Expose `getRewardsBalance` as a public suspend function
* Card
    * Expose `tokenize` as a public suspend function
* GooglePay
    * Expose `isReadyToPay` as a public suspend function
    * Expose `getTokenizationParameters` as a public suspend function
    * Expose `createPaymentAuthRequest` as a public suspend function
* LocalPayment
    * Expose `createPaymentAuthRequest` as a public suspend function
    * Expose `tokenize` as a public suspend function
* PayPal
    * Expose `createPaymentAuthRequest` as a public suspend function
    * Expose `tokenize` as a public suspend function
* SEPADirectDebit
    * Expose `createPaymentAuthRequest` as a public suspend function
    * Expose `tokenize` as a public suspend function
* ShopperInsights
    * Expose `createCustomerSession` as a public suspend function
    * Expose `updateCustomerSession` as a public suspend function
    * Expose `generateCustomerRecommendations` as a public suspend function
* ThreeDSecure
    * Expose `createPaymentAuthRequest` as a public suspend function
    * Expose `prepareLookup` as a public suspend function
    * Expose `initializeChallengeWithLookupResponse` as a public suspend function
    * Expose `tokenize` as a public suspend function
* Venmo
    * Expose `createPaymentAuthRequest` as a public suspend function
    * Expose `tokenize` as a public suspend function
* BraintreeCore
    * Update Android Gradle Plugin version to 8.13.2
    * Update compileSdkVersion and targetSdkVersion to 37
* UIComponents
    * `PayPalButton` and `VenmoButton` now honor an explicit `layout_width`/`layout_height` or `match_parent` but defaults to the standard size for `wrap_content`
        * Note: if your layout previously set an explicit size or `match_parent` on these buttons, the button will now render at that size
  
