* Lower minimum deployment target from iOS 16.0 to iOS 15.0
* BraintreePayPal
    * Fix bug where the return tokenization request could fail to complete after the app was backgrounded during the PayPal app switch or browser flow, resulting in a network connection timeout error
    * Add `BTPayPalError.returnBackgroundTaskExpired` (code 15), returned if background execution time runs out before the request completes
