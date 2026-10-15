# iOS v5 migration retrieval checks

## Q1 — Purpose, scope, and non-inference

**Query:** Who is the Adyen iOS v5.0.0 upgrade guide for, and does it require Checkout API v69 or prove an app/payment works after migration?

**Expected route and answer:** `wiki/sources/adyen/source-adyen-docs-online-payments-upgrade-your-integration-upgrade-to-ios-5-0-0.md` → pinned raw `raw/adyen/docs/online-payments/upgrade-your-integration/upgrade-to-ios-5-0-0/2026-09-15.md`, lines 15–23 and 25–39. It targets native online-checkout iOS integrations on v4.10.1 or earlier moving to v5.0.0. It **recommends** Checkout API v69 (line 23), rather than stating a hard requirement in this page. It documents migration edits, not build, device, live merchant/account, server API, authorization or settlement proof. The test-environment example at lines 41–49 should not be copied as live configuration.

## Q2 — Central migration steps and version qualifications

**Query:** Which callbacks/configuration objects change for iOS v5.0.0, and how do Drop-in, Apple Pay, cards and the v5.9.0 iDEAL note differ?

**Expected route and answer:** `wiki/sources/adyen/source-adyen-docs-online-payments-upgrade-your-integration-upgrade-to-ios-5-0-0.md` → raw lines 25–35 for exact method table, 37–50 for required `AdyenContext` and client-side test example, 52–73 for Component/payment-method configuration objects, 75–93 for later iDEAL note plus Apple Pay and CardType changes, and 95–106 for Drop-in-only Step 5 requirement. `finalizeIfNeeded` is unchanged in the method table (line 32). Step 5 is required if using Drop-in despite its general optional heading (lines 95–99); `allowsSkippingPaymentList` is an example optional value. The iDEAL `InstantPaymentComponent` note explicitly applies to v5.9.0 (line 75), not v5.0.0. The client key/`AdyenContext` shown here does not replace server credentials or specify server payment outcomes.
