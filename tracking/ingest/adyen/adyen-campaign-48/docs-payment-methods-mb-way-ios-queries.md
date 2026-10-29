# docs-payment-methods-mb-way-ios retrieval checks

## Q1 — purpose and limit
Query: What does the MB WAY iOS page itself document?
Expected: A captured router to iOS Drop-in and MBWayComponent child guides, not a method-specific implementation. It does not itself define phone entry, App2App, request fields, payment status or merchant eligibility. Route: [[wiki/index]] → [[wiki/adyen-index]] → [[wiki/concepts/adyen-online-payments]] → [[wiki/sources/adyen/source-adyen-docs-payment-methods-mb-way-ios]] → [[raw/adyen/docs/payment-methods/mb-way/ios/2026-09-15]]. Canonical stem: `/payment-methods/mb-way/ios`. Verify raw lines 15–27.

## Q2 — UI and base guide navigation
Query: Which MB WAY iOS UI choices and base flows does this router link?
Expected: Drop-in is all-in-one UI; Components names MBWayComponent. The page links each UI's Sessions and Advanced main integration guides and says to build the main integration before MB WAY. Follow the chosen child guide for flow-specific method behavior; the router does not make their requirements interchangeable. Route: [[wiki/index]] → [[wiki/adyen-index]] → [[wiki/concepts/adyen-online-payments]] → [[wiki/sources/adyen/source-adyen-docs-payment-methods-mb-way-ios]] → [[raw/adyen/docs/payment-methods/mb-way/ios/2026-09-15]]. Canonical stem: `/payment-methods/mb-way/ios`. Verify raw lines 19–36.
