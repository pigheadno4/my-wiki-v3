## 26.6.0 2026-08-10
### PaymentSheet
* [Fixed] LinkController (private preview) now returns an error when no funding sources are available for a Link session, rather than silently falling back to card.

### CryptoOnramp (Alpha)
* [Added] Added `CryptoOnrampCoordinator.deleteWalletAddress(walletId:)` to delete a registered wallet address.

### PaymentSheet
* [Added] Added support for MB WAY payments.
* [Added] Added support for Bizum payments.

