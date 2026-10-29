# docs-payment-methods-paypo-ios retrieval checks

## Q1 — page purpose
Query: What does the PayPo iOS page itself document?
Expected: A captured iOS router to PayPo Drop-in and Components child guides, not a payment implementation recipe. It does not itself define request fields, redirect handling or capture. Route: [[wiki/index]] → [[wiki/adyen-index]] → [[wiki/concepts/adyen-online-payments]] → [[wiki/sources/adyen/source-adyen-docs-payment-methods-paypo-ios]] → [[raw/adyen/docs/payment-methods/paypo/ios/2026-09-15]]. Canonical stem: `/payment-methods/paypo/ios`. Verify raw lines 15–27.

## Q2 — route choices and warning
Query: Which PayPo iOS integration choices and main guides are linked, and what is wrong with the Components description?
Expected: Drop-in is the all-in-one UI; Components is the other child-guide route. The raw says “Use the None” for Components, a placeholder/invalid component label to flag rather than implement. The page links both UI choices to Sessions and Advanced main integration guides and says to build the main integration first. Child guides own method-specific details. Route: [[wiki/index]] → [[wiki/adyen-index]] → [[wiki/concepts/adyen-online-payments]] → [[wiki/sources/adyen/source-adyen-docs-payment-methods-paypo-ios]] → [[raw/adyen/docs/payment-methods/paypo/ios/2026-09-15]]. Canonical stem: `/payment-methods/paypo/ios`. Verify raw lines 19–36.
