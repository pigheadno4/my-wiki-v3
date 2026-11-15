
* Venmo
  * Add `VenmoClient.start(activity: Activity, orderId: String)` suspend function to initiate Venmo checkout
  * Add `VenmoClient.start(activity: Activity, orderId: String, callback: VenmoStartCallback)` callback-based method for Java compatibility
  * Add `VenmoClient.finishStart(intent: Intent)` to return type-safe results:
    * `VenmoFinishStartResult.Success` for successful payments
    * `VenmoFinishStartResult.Canceled` when user cancels payment
    * `VenmoFinishStartResult.NoResult` when intent is unrelated to Venmo flow
    * `VenmoFinishStartResult.Failure` for errors

