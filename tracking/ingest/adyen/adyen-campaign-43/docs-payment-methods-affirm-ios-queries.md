# Fixed retrieval checks: Affirm iOS chooser

Canonical source stem: `source-adyen-docs-payment-methods-affirm-ios`
Pinned raw: `raw/adyen/docs/payment-methods/affirm/ios/2026-09-15.md` (SHA-256 `6a8f5ea5eb4301d0d64a8202af16f689c7f85dc50ce6f7b98a083ba3201965bb`)
Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-affirm-ios.md`; iOS cross-route: `wiki/concepts/adyen-ios-sdk.md`.

## Q1 — What is this page for, and what should a reader not infer?

It is an Affirm iOS integration chooser (`raw/adyen/docs/payment-methods/affirm/ios/2026-09-15.md:15-19`) linking to iOS Drop-in and Components child guides (`:21-27`) and iOS Sessions base guides (`:29`). It is not an end-to-end Affirm integration and does not supply request fields, financing eligibility, payment outcome, capture/refund duties, credentials or live readiness. The page's Sessions links do not mean Advanced flow is unsupported; the child guides define their own flow scope.

## Q2 — What capabilities, prerequisites and warnings matter most?

The Drop-in link offers an all-in-one iOS UI (`:21-23`); the Components link names the Redirect Component to handle the Affirm redirect (`:25-27`). Its more-information links target iOS Sessions Drop-in and Components (`:29`). These are route choices, not operational payment proof or complete setup requirements. Follow the corresponding child guide for request, redirect, capture and go-live specifics; the overview owns method-level financing context.
