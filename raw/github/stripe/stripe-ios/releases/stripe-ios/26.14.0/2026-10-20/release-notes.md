## 26.14.0 2026-10-12
### General
* [Removed] Removed the "test mode" badge from all UI surfaces.

### PaymentSheet
* [Added] Added TrueMoney API bindings and PaymentSheet support for payments and setup.
* [Added] Added Touch 'n Go API bindings and PaymentSheet support for payments and setup.
* [Added] Added Mondu API bindings and PaymentSheet support for PaymentIntents.
* [Added] Added Naira Wallet API bindings and PaymentSheet support for PaymentIntents.
* [Added] Added Naira USSD API bindings and PaymentSheet support for PaymentIntents.
* [Added] Added Naira bank transfer API bindings and PaymentSheet support for PaymentIntents.
* [Fixed] Fixed a potential crash when canceling redirect payment methods such as Afterpay/Clearpay.
* [Added] Added QRIS API bindings and PaymentSheet support for PaymentIntents.
* [Added] Added GCash API bindings and PaymentSheet support for payments and setup.
* [Added] Added Naira card API bindings and PaymentSheet support for PaymentIntents.

### CryptoOnramp (Alpha)
* [Fixed] If the customer's KYC region changes after Apple Pay is collected before authentication, token creation now throws `PaymentMethodKYCRegionChangedError` (`payment_method_kyc_region_changed`). Collect Apple Pay again and retry token creation only after successful collection.

