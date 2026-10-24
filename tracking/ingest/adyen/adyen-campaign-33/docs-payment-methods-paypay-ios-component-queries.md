# PayPay iOS Component retrieval checks

Q1. What must exist before adding PayPay to an iOS Components integration?

Use the matching existing Sessions or Advanced iOS Components flow, with redirect handling and PayPay added in Customer Area (raw lines 25–36 and 88–98). The Sessions tab additionally states Checkout API v68 or later (line 34). The page says no PayPay-specific `/sessions` or `/payments` additions or configuration (lines 40–48, 100–104, 130–134), while the main integration remains necessary. Forward route: [[index]] → [[adyen-index]] → [[adyen-ios-sdk]] → [[source-adyen-docs-payment-methods-paypay-ios-component]] → [[raw/adyen/docs/payment-methods/paypay/ios-component/2026-09-15]].

Q2. How should a reader interpret the TEST simulator, LIVE condition and example code?

The TEST tabs list DGFT acquirer accounts and a redirect to a simulator without the PayPay app (raw lines 75–84 and 136–145). LIVE requires an activated PayPay smartphone app accessed through a Japan local IP address (lines 86, 147). Neither proves payment authorization or settlement. The initializer calls the type `None` (lines 54–66, 110–121) and passes `payPayConfiguration` despite saying no PayPay-specific configuration is required (lines 46–48, 102–104); Advanced Components prose links to `integration=Drop-in` (line 96). Verify these against the chosen SDK and main flow before implementation. Forward route: [[index]] → [[adyen-index]] → [[adyen-ios-sdk]] → [[source-adyen-docs-payment-methods-paypay-ios-component]] → [[raw/adyen/docs/payment-methods/paypay/ios-component/2026-09-15]].
