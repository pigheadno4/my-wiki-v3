
* CardPayments
  * Removed deprecated `CardClient.finishApproveOrder(intent, authState)` — use `CardClient.finishApproveOrder(intent)` instead
  * Removed deprecated `CardClient.finishVault(intent, authState)` — use `CardClient.finishVault(intent)` instead
  * Removed `authState` from public API of `CardPresentAuthChallengeResult.Success`
* CorePayments
  * Renamed `Environment` to `CoreEnvironment` and `CoreConfig.environment` to `CoreConfig.coreEnvironment`
* PayPalPayments
  * Renamed the `PayPalWebPayments` module to `PayPalPayments` (Maven artifact `com.paypal.android:paypal-payments`, package `com.paypal.android.paypalpayments`)
  * Renamed `PayPalWebCheckoutClient` to `PayPalClient`, `PayPalWebLauncher` to `PayPalLauncher`, `PayPalWebCheckoutError(Code)` to `PayPalError(Code)`, `PayPalWebCheckoutSessionStore` to `PayPalSessionStore`, `PayPalWebCheckoutFinishStartResult` to `PayPalFinishStartResult`, `PayPalWebCheckoutFinishVaultResult` to `PayPalFinishVaultResult`, and `PayPalWebCheckoutFundingSource` to `PayPalCheckoutFundingSource`
  * Merged `PayPalWebStartCallback` and `PayPalWebVaultCallback` into a single `PayPalResultCallback` interface with one `onPayPalResult(result)` method, since both callbacks were identical aside from their name
  * Removed deprecated `PayPalClient(context, configuration, urlScheme)` constructor — use `PayPalClient(context, configuration)` and set `returnToAppStrategy` on requests instead
  * Removed deprecated `PayPalClient.start(activity, request)` — use `PayPalClient.start(activity, request, callback)` or `startAsync()` instead
  * Removed deprecated `PayPalClient.vault(activity, request)` — use `PayPalClient.vault(activity, request, callback)` or `vaultAsync()` instead
  * Removed deprecated `PayPalClient.finishStart(intent, authState)` — use `PayPalClient.finishStart(intent)` instead
  * Removed deprecated `PayPalClient.finishVault(intent, authState)` — use `PayPalClient.finishVault(intent)` instead
  * Removed `authState` from public API of `PayPalPresentAuthChallengeResult.Success`
  * Add `PayPalClient.createPayPalSession(tokenType, userIdentity, urlConfig, userAction)` — establishes a shopper session that must be created prior to calling `start()` or `vault()`; `urlConfig.fallbackSchemeUrl` is a mandatory field
  * Add `PayPalPhoneNumber(countryCode, nationalNumber)` and change `PayPalUserIdentity.phone` from `String?` to `PayPalPhoneNumber?` — the shopper's phone number is now sent to the `createShopperSessionWithAppSwitchEligibility` GraphQL mutation
  * Add `PayPalClient.start(activity, orderId, callback)` method (v3) — requires a prior call to `createPayPalSession()`
  * Add `PayPalClient.vault(activity, setupTokenId, callback)` method (v3) — requires a prior call to `createPayPalSession()`
  * Removed deprecated `PayPalClient.start(activity, request, callback)` and `PayPalWebCheckoutRequest` — use `createPayPalSession()` followed by `start(activity, orderId, callback)` instead
  * Removed deprecated `PayPalClient.vault(activity, request, callback)` and `PayPalWebVaultRequest` — use `createPayPalSession()` followed by `vault(activity, setupTokenId, callback)` instead
* FraudProtection
  * Removed deprecated `PayPalDataCollector.collectDeviceData(context, clientMetadataId)` and `collectDeviceData(context, clientMetadataId, additionalData)` overloads — use `collectDeviceData(context, PayPalDataCollectorRequest)` instead
  * Removed deprecated `PayPalDataCollector.setLogging(Boolean)`

