# iOS redirect 3D Secure route checks

## Q1 — Purpose, scope, and non-inference

**Query:** What does Adyen's iOS redirect 3D Secure page establish, and can it answer an iOS SDK or payment-outcome question?

**Expected route and answer:** `wiki/sources/adyen/source-adyen-docs-online-payments-3d-secure-redirect-3ds2-ios.md` → pinned raw `raw/adyen/docs/online-payments/3d-secure/redirect-3ds2/ios/2026-09-15.md`, lines 15–27. The page introduces redirect 3D Secure support in an iOS app and offers Drop-in versus Components navigation. It provides no SDK version, callbacks, Checkout API version, server operation, authentication result, authorization, capture or settlement evidence. The metadata last-modified date is 2019-10-08 (raw line 11), while the snapshot was collected 2026-09-15 (line 2).

## Q2 — Central routes and where details belong

**Query:** Which iOS redirect 3DS guide should a merchant open for Drop-in versus Components, and where do prerequisites and flow details come from?

**Expected route and answer:** `wiki/sources/adyen/source-adyen-docs-online-payments-3d-secure-redirect-3ds2-ios.md` → raw lines 19–27. The Drop-in link at lines 21–23 describes an all-in-one UI route; the Components link at lines 25–27 describes a pre-built Component route. The separate canonical sources `source-adyen-docs-online-payments-3d-secure-redirect-3ds2-ios-drop-in` and `source-adyen-docs-online-payments-3d-secure-redirect-3ds2-ios-component` own their detailed prerequisites, app/server handoffs and outcome qualifications. This landing page alone gives no implementation or runtime instructions.
