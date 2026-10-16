
* PayPalPayments
  * **Breaking:** Rename the `PayPalWebPayments` module to `PayPalPayments` — update `import PayPalWebPayments` to `import PayPalPayments`
  * **Breaking:** Rename `PayPalWebCheckoutClient` to `PayPalClient`
  * **Breaking:** Rename `PayPalWebCheckoutResult` to `PayPalCheckoutResult`
  * **Breaking:** Rename `PayPalWebCheckoutFundingSource` to `PayPalCheckoutFundingSource`
  * Add `PayPalClient.createPayPalSession(sessionType, userIdentity, urlConfig, userAction)` — establishes a shopper session that must be created prior to calling `start()` or `vault()`
  * Add `PayPalSessionType` enum (`.checkout`, `.vaultWithoutPurchase`) — replaces `PayPalFlowType` and expresses the caller's intent, independent of the underlying token/query-parameter representation
  * Add `PayPalClient.start(orderId, completion)` method — requires a prior call to `createPayPalSession()`
  * Add `PayPalClient.vault(setupTokenId, completion)` method — requires a prior call to `createPayPalSession()`
  * Add `PayPalPhoneNumber` type and update `PayPalUserIdentity(email:phone:)` to accept a structured `PayPalPhoneNumber` (country code + national number) instead of a `String`
  * Fix `start()` and `vault()` silently ignoring `updateClientConfig` failures — errors are now surfaced to the completion handler and reported via analytics instead of proceeding with a stale client config
  * **Breaking:** Remove `PayPalClient.start(request, completion)` and `start(request)` — use `createPayPalSession()` followed by `start(orderId, completion)` instead
  * **Breaking:** Remove `PayPalClient.vault(request, completion)` and `vault(request)` — use `createPayPalSession()` followed by `vault(setupTokenID, completion)` instead
  * **Breaking:** Remove `PayPalWebCheckoutRequest` and `PayPalVaultRequest` types (used only by the removed APIs)
* CorePayments
  * **Breaking:** `CoreConfig` requires a `merchantID` parameter; optional `bnCode` parameter added. See the [v3 Migration Guide](v3_MIGRATION_GUIDE.md) for details.
  * **Breaking:** Remove `PatchCCOWithAppSwitchEligibility` (and its `AppSwitchEligibility` response type) and the `ExternalTokenKind` constants — the legacy PatchCCO app-switch-eligibility path is no longer used
  * **Breaking:** Rename `Environment` to `CoreEnvironment`
  * Improve error messages for non-JSON/unstructured error responses to include the HTTP status, request URL, and raw response body

