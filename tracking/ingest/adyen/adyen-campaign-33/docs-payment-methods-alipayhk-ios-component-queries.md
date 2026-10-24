# AlipayHK iOS Component retrieval checks

Q1. What existing integration and setup does this page require for AlipayHK on iOS?

It adds method-specific steps to an existing iOS Components integration. Choose the already-used server-side Sessions or Advanced flow; both branches call for redirect handling (`action.type: redirect`) and Alipay HK added in Customer Area. Only the Sessions requirement table states Checkout API v68 or later. The guide says no extra Alipay HK `/sessions` or `/payments` parameters or Component configuration parameters are needed on top of the main integration. Raw lines 19–48 and 87–133. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-alipayhk-ios-component]] → [[raw/adyen/docs/payment-methods/alipayhk/ios-component/2026-09-15]].

Q2. What snippet conflicts and live/outcome boundaries matter before using these examples?

Both initialization examples literally use a `None` class and pass undefined `alipayHKConfiguration` despite the no-extra-configuration prose; the Advanced integration-type link points to Drop-in while the branch is labeled Components and its redirect link points to Components (raw lines 46–73 and 91–127). The test credentials and payment-list lookup do not prove a payment result. The page calls for a live Customer Area request before live AlipayHK acceptance, and supplies no final webhook, capture or settlement evidence (raw lines 75–85 and 135–145). Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-alipayhk-ios-component]] → [[raw/adyen/docs/payment-methods/alipayhk/ios-component/2026-09-15]].
