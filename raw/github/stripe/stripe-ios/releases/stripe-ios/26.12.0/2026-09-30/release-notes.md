## 26.12.0 2026-09-21
### CryptoOnramp (Alpha)
* [Removed] Removed public exposure of `StripeCryptoOnramp.Image`, including `Image.linkIconSquare`.
* [Added] Added `CryptoOnrampCoordinator.presentTermsAndConditionsIfNeeded(from:)` and `presentTermsOfServiceIfNeeded(from:)` to present and record acceptance of current partner terms when required. Both methods return `PartnerTermsResult`.

### StripeCore
* [Added] Added `additionalHeaders` support to the `STPAPIClient` GET, POST, and DELETE APIs exposed through the `STP` SPI.

### PaymentSheet
* [Fixed] Fixed card funding warnings not appearing after scanning a card.

