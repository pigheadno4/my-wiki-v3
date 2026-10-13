## 26.13.0 2026-10-05
### PaymentSheet
* [Fixed] Fixed a potential crash when using certain card brands in PaymentSheet.
* [Fixed] Fixed Apple Pay failing to open for fractional amounts in COP, HUF, IDR, LAK, LBP, PKR, and RSD.

### Payments
* [Fixed] Amounts in LBP are now displayed correctly.

### CryptoOnramp (Alpha)
* [Added] Added optional `email`, `phone`, and `rawPhone` fields to `KycInfo`, populated from Apple Pay billing or shipping contact information when requested. All values are for prefill only. `phone` is normalized to E.164 using the billing address's country when possible, and is otherwise `nil`; `rawPhone` always carries the wallet's original, unnormalized value. Names fall back to shipping contact values when billing values are missing or blank. Creating `KycInfo` from an Apple Pay payment still requires a usable name or billing address; email or phone alone is insufficient.
* [Changed] Apple Pay can now be presented via `CryptoOnrampCoordinator.collectPaymentMethod(type:from:)` before the user authenticates with Link. `createCryptoPaymentToken()` still requires an authenticated user.
* [Added] Added an optional `countryHint` parameter to `CryptoOnrampCoordinator.create(...)`, used to help select a merchant of record for a customer who does not yet have an established KYC region.
* [Added] Added `STPAPIClient.CryptoOnrampAPIError.missingLinkSessionKey` to report when a Link session key is unavailable.
* [Added] Added `CryptoOnrampCoordinator.fulfillKYCRequirement(from:)` to retrieve additional KYC requirements and present document collection when needed.

### PaymentSheet
* [Added] Added MoMo API bindings and PaymentSheet support for PaymentIntents.
* [Added] Added GoPay API bindings and PaymentSheet support for PaymentIntents.
* [Added] Added ShopeePay API bindings and PaymentSheet support for PaymentIntents.

