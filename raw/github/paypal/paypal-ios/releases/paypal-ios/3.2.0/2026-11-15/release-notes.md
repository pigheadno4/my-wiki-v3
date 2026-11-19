
* VenmoPayments (New Module)
  * Add `VenmoClient` with `start(orderID:completion:)` and `start(orderID:) async throws` for Venmo checkout; opens the Venmo app when installed, otherwise Safari
  * Add `handleReturnURL(_:)` for processing the return URL from Venmo
  * Add `VenmoCheckoutResult` with `orderID` and `payerID` properties
  * Add `VenmoError` with error codes for URL errors, malformed results, and cancellation
  * Add `VenmoError.isCheckoutCanceled(_:)` helper to distinguish user cancellation

