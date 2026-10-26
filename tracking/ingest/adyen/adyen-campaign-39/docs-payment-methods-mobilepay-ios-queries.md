# MobilePay iOS chooser retrieval checks

Route: `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-mobilepay-ios]]`.

## Q1. What is its purpose and scope, and what cannot be inferred?

The canonical stem `source-adyen-docs-payment-methods-mobilepay-ios` is a 2026-09-15 iOS navigation page for MobilePay Drop-in versus Components (`raw/adyen/docs/payment-methods/mobilepay/ios/2026-09-15.md:15-27`). It also points to four base iOS Sessions/Advanced guides (`:29-36`). The chooser has no method-specific request, version, current enablement, payout, payment-result or live-eligibility rule; linked child guides are separate evidence (`:19-36`).

## Q2. What are the central capability, prerequisites, and warnings?

The page offers an all-in-one iOS Drop-in route and an `InstantPaymentComponent` route (`raw/adyen/docs/payment-methods/mobilepay/ios/2026-09-15.md:19-27`). It says to create the main integration before adding MobilePay, and lists iOS Drop-in Sessions, Components Sessions, Drop-in Advanced and Components Advanced guides (`:29-36`). These are navigation choices; they do not establish that setup or payment behavior is identical across routes or that a merchant is enabled (`:19-36`).
