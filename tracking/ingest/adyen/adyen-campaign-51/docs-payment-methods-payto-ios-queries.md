# Fixed queries — PayTo iOS chooser

## Q1 — page purpose and limits

**Query:** What does the captured PayTo iOS page provide, and what should not be inferred from it?

**Expected answer:** https://docs.adyen.com/payment-methods/payto/ios is a 2026-09-15-captured iOS chooser for Drop-in and Components, with main Sessions/Advanced base-guide links. It has no mandate, request-field, SDK-version or payment-status recipe; it does not prove account enablement, agreement approval or payment success (full pinned raw/adyen/docs/payment-methods/payto/ios/2026-09-15.md, # PayTo for iOS lines 15–17; chooser lines 19–27; ## See also lines 29–36). Method-level Australian PayTo context is at wiki/sources/adyen/source-adyen-docs-payment-methods-payto.md. Route: wiki/index.md → wiki/adyen-index.md → wiki/concepts/adyen-online-payments.md → wiki/sources/adyen/source-adyen-docs-payment-methods-payto-ios.md.

## Q2 — child and base routes

**Query:** Which PayTo iOS UI paths and base integration guides does the chooser route to?

**Expected answer:** It links Drop-in as the all-in-one iOS UI at /payment-methods/payto/ios-drop-in and Components as PayToComponent at /payment-methods/payto/ios-component (pinned raw/adyen/docs/payment-methods/payto/ios/2026-09-15.md, ### How do you want to integrate? lines 19–27). It instructs the reader to establish the main integration before adding PayTo and links iOS Drop-in and Components base guides under both Sessions and Advanced (## See also lines 29–36). Flow-specific one-time/subscription agreement, later-payment and asynchronous outcome details belong to the child guides, not this chooser. Route: wiki/index.md → wiki/adyen-index.md → wiki/concepts/adyen-online-payments.md → wiki/sources/adyen/source-adyen-docs-payment-methods-payto-ios.md.
