# Fixed queries — Pix Android chooser

## Q1 — page purpose and limits

**Query:** What does the captured Pix Android page provide, and what should not be inferred from it?

**Expected answer:** https://docs.adyen.com/payment-methods/pix/android is a 2026-09-15-captured Android chooser for Drop-in and Components with Sessions/Advanced base-guide links. It is not a request-field, SDK-version, QR-expiration or payment-status recipe and does not prove current merchant enablement or successful payment (full pinned raw/adyen/docs/payment-methods/pix/android/2026-09-15.md, # Pix for Android lines 15–17; chooser lines 19–27; ## See also lines 29–36). Method-level Brazil/BRL context is at wiki/sources/adyen/source-adyen-docs-payment-methods-pix.md. Route: wiki/index.md → wiki/adyen-index.md → wiki/concepts/adyen-online-payments.md → wiki/sources/adyen/source-adyen-docs-payment-methods-pix-android.md.

## Q2 — child routes and redirect-teaser caveat

**Query:** Which Pix Android UI paths and base guides are linked, and should the Components teaser define the required action?

**Expected answer:** The chooser links Drop-in as an all-in-one Android UI at /payment-methods/pix/android-drop-in and Components as InstantPaymentComponent at /payment-methods/pix/android-component (pinned raw/adyen/docs/payment-methods/pix/android/2026-09-15.md, ### How do you want to integrate? lines 19–27). It says to establish the main integration first and links Android Drop-in and Components under both Sessions and Advanced (## See also lines 29–36). The Components teaser says “handle the redirect to Pix” (line 27), but the approved child source wiki/sources/adyen/source-adyen-docs-payment-methods-pix-android-component.md describes a qrCode Advanced action. Treat the teaser as navigation, not a redirect-only implementation instruction; QR action and asynchronous payment behavior belong to the child guide. Route: wiki/index.md → wiki/adyen-index.md → wiki/concepts/adyen-online-payments.md → wiki/sources/adyen/source-adyen-docs-payment-methods-pix-android.md.
