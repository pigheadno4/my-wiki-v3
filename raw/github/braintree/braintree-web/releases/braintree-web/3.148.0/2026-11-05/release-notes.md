## 3.148.0 (2026-11-02)

- Dependencies
  - update `credit-card-type` to 10.3.1
- PayPal Checkout v6
  - Fix `paypal-checkout-v6` teardown function not correctly removing iframes
  - `paypal-checkout-v6` now allows passing a `shopperSessionId` parameter, which will propagate to the PayPal SDK
- Instant Verification
  - Fix `startPayment` sending client tokens generated with a customer ID to the Instant Verification experience in an unexpected format