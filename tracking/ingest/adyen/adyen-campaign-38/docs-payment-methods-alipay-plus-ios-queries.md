# Alipay+ iOS chooser — retrieval checks

Canonical source stem: `source-adyen-docs-payment-methods-alipay-plus-ios`

## Q1 — What purpose and scope does this page have, and what cannot be inferred?

It is a 2026-09-15-captured navigation chooser for adding Alipay+ to an iOS app (raw lines 15–19). It links child and base integration guides but gives no on-page merchant/wallet eligibility, SDK/API version, environment, redirect, or payment-outcome rule (the entire raw is lines 15–36). Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` (`## Sources`) → `wiki/sources/adyen/source-adyen-docs-payment-methods-alipay-plus-ios.md` → `raw/adyen/docs/payment-methods/alipay-plus/ios/2026-09-15.md`.

## Q2 — What are the central choices, prerequisite, and warning?

The two linked choices are iOS Drop-in, called an all-in-one UI solution, and iOS Components via `InstantPaymentComponent` (raw lines 19–27). The page directs readers to create the main integration first and lists iOS Drop-in and Components base routes for Sessions and Advanced flows (raw lines 29–36). Those are navigation and sequencing advice; child/base guides carry the actual requirements and result handling. Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` (`## Sources`) → `wiki/sources/adyen/source-adyen-docs-payment-methods-alipay-plus-ios.md` → pinned raw above.
