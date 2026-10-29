# Fixed queries — Pix iOS chooser

## Q1 — page purpose and limits

**Query:** What does the captured Pix iOS page provide, and what should not be inferred from it?

**Expected answer:** https://docs.adyen.com/payment-methods/pix/ios is a 2026-09-15-captured iOS chooser for Drop-in and Components with main Sessions/Advanced base-guide links. It has no request-field, SDK-version, QR-expiration or payment-status recipe; it does not prove current merchant enablement or successful payment (full pinned raw/adyen/docs/payment-methods/pix/ios/2026-09-15.md, # Pix for iOS lines 15–17; chooser lines 19–27; ## See also lines 29–36). Brazil/BRL Pix context is at wiki/sources/adyen/source-adyen-docs-payment-methods-pix.md. Route: wiki/index.md → wiki/adyen-index.md → wiki/concepts/adyen-online-payments.md → wiki/sources/adyen/source-adyen-docs-payment-methods-pix-ios.md.

## Q2 — child and base routes

**Query:** Which Pix iOS UI paths and base integration guides does the chooser route to?

**Expected answer:** It links Drop-in as an all-in-one iOS UI at /payment-methods/pix/ios-drop-in and Components as InstantPaymentComponent at /payment-methods/pix/ios-component (pinned raw/adyen/docs/payment-methods/pix/ios/2026-09-15.md, ### How do you want to integrate? lines 19–27). It says to establish the main integration before adding Pix and links iOS Drop-in and Components base guides under both Sessions and Advanced (## See also lines 29–36). Flow-specific QR action, payment expiry, asynchronous finality and test/live requirements belong to child guides, not this chooser. Route: wiki/index.md → wiki/adyen-index.md → wiki/concepts/adyen-online-payments.md → wiki/sources/adyen/source-adyen-docs-payment-methods-pix-ios.md.
