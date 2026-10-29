# Fixed retrieval checks: Bancontact mobile iOS chooser

Canonical source stem: `source-adyen-docs-payment-methods-bancontact-bancontact-mobile-ios`
Pinned raw: `raw/adyen/docs/payment-methods/bancontact/bancontact-mobile/ios/2026-09-15.md` (SHA-256 `b29e5583e3da74ea8117fa103baf9834a3a3438a196c62a6cabc0869027cda9a`)
Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-bancontact-bancontact-mobile-ios.md`; iOS cross-route: `wiki/concepts/adyen-ios-sdk.md`.

## Q1 — What is this page for, and what should a reader not infer?

It is a Bancontact mobile iOS integration chooser, captured 2026-09-15 with 2019-09-30 last-modified metadata (`raw/adyen/docs/payment-methods/bancontact/bancontact-mobile/ios/2026-09-15.md:5-17`). It links to iOS Drop-in and Components child guides (`:19-27`) and base Sessions integration routes (`:29`). It does not itself define app handoff, QR behavior, request fields, outcome handling, test availability, current account eligibility or live success. It is not the Bancontact card or Android mobile implementation.

## Q2 — What capabilities, prerequisites and warnings matter most?

The reader chooses the all-in-one iOS Drop-in or prebuilt iOS Component guide (`:21-27`); those child guides hold the actual implementation. The last sentence labels a base-guide link 'Android Drop-in', but the URL sets `platform=iOS&integration=Drop-in`; the other link also targets iOS Components (`:29`). This is a navigation label mismatch, not evidence that Android guidance applies to the iOS route. No payment prerequisites or lifecycle guarantees are established by this chooser beyond those navigation options.
