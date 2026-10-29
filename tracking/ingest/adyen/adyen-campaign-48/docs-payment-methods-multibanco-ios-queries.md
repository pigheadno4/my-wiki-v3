# Retrieval checks: Multibanco for iOS

## Q1 — Purpose and scope
Query: What does the Multibanco iOS page do, and what does it not establish?
Expected: It is a 2026-09-15 captured iOS integration chooser, routing to method-specific Drop-in and Components guides and four main iOS base guides. It does not itself define voucher fields, payment finality, current eligibility, or a complete SDK recipe. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-multibanco-ios]] → [[raw/adyen/docs/payment-methods/multibanco/ios/2026-09-15|pinned raw]]. Verify canonical stem `/payment-methods/multibanco/ios`, raw lines 15–19 and **See also** lines 29–36.

## Q2 — Choice of child and base guide
Query: Which Multibanco iOS UI routes and base integration flows does this chooser list?
Expected: Drop-in links to `/payment-methods/multibanco/ios-drop-in` as all-in-one UI; Components links to `/payment-methods/multibanco/ios-component` and mentions `InstantPaymentComponent`. It says to create the main integration first, linking iOS Drop-in and Components guides for both Sessions and Advanced flows. These are navigation links, not behavioral evidence from unread child/base content. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-multibanco-ios]] → [[raw/adyen/docs/payment-methods/multibanco/ios/2026-09-15|pinned raw]]. Verify canonical stem and raw lines 19–36.
