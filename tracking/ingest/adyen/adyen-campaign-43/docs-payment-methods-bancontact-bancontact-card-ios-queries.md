# Fixed retrieval checks: Bancontact Card iOS chooser

Canonical source stem: `source-adyen-docs-payment-methods-bancontact-bancontact-card-ios`
Pinned raw: `raw/adyen/docs/payment-methods/bancontact/bancontact-card/ios/2026-09-15.md` (SHA-256 `b3bfda5bd3e5805b570fd04475abb864dd39784057e0b327494e7b42d595ca0f`)
Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-bancontact-bancontact-card-ios.md`

## Q1 — What is this page for, and what should a reader not infer?

This page is a Bancontact **Card** iOS integration chooser (`raw/adyen/docs/payment-methods/bancontact/bancontact-card/ios/2026-09-15.md:15-17`). It links card-specific Drop-in and Components child guides (`:19-27`) and base iOS Sessions guides (`:29`). It is not the Bancontact Mobile app/QR path, and provides no request fields, SDK version, payment-result steps or proof that a merchant can accept live card payments. Those details require the linked child and base guides.

## Q2 — What choices and prerequisite route matter most?

Choose all-in-one iOS Drop-in or a prebuilt iOS Component for Bancontact Card (`:19-27`), then follow the relevant base iOS Sessions Drop-in/Components guide linked at line 29. This page provides no Advanced-flow link; that absence does not itself say Advanced is unsupported. Its role is navigation rather than a method-specific card/3DS implementation recipe.
