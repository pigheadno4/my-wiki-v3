
* All Modules
  * **Breaking:** Bump minimum iOS version from 14 to 16.
* PayPalPayments
  * Fix `createPayPalSession()` sending a hardcoded `PAY` payment type in the shopper session experimentation context regardless of the caller's `userAction` — now correctly passes `CONTINUE`, `PAY`, or `COMMIT` based on `userAction`
* FraudProtection
  * Migrate SDK to use new PPRiskMagnes Swift Package
  * Remove PPRiskManges.xcframework from project
* CorePayments
  * **Deprecated:** `UIApplication.isPayPalAppInstalled()` has been removed

