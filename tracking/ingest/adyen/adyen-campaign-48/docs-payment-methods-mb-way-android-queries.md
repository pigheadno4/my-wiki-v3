# MB WAY Android router retrieval checks

## Q1 — What does the captured MB WAY Android page directly cover?
Expected route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-mb-way-android.md` → `raw/adyen/docs/payment-methods/mb-way/android/2026-09-15.md`.
Expected answer: it routes to an Android Drop-in child guide and an Android Components child guide; the latter link text says `MBWayComponent` handles redirect to MB WAY. It instructs the reader to build the main integration first. This page is a navigation router, not an implementation recipe. Raw locators: lines 15–31.

## Q2 — Which server-side integration guides does it link, and what must not be inferred?
Expected route: same root/provider/concept/source/raw chain.
Expected answer: links to Android Drop-in and Components main guides for Sessions and Advanced flows. It does not state a version minimum, request fields, redirect sequence, test/live gate, payment finality, or merchant eligibility. Route such claims to fully read child guides or, for method-level context only, the approved `wiki/sources/adyen/source-adyen-docs-payment-methods-mb-way.md` overview. Raw locators: lines 29–36.
