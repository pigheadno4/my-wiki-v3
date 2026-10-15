# Adyen Android v5 migration retrieval probes

## Q1 — Purpose and scope

**Query:** What does Adyen's Android v5 migration guide cover, and which starting versions does it address?

**Expected route:** [[source-adyen-docs-online-payments-upgrade-your-integration-upgrade-to-android-5-0-0]] via [[adyen-android-sdk]].

**Answer boundary:** The guide is for Android integrations using v4.13.3 or earlier and upgrading to v5.0.0. It covers Drop-in and Components migration changes. Do not infer that every v5.x release has identical steps, that Checkout API v70 is mandatory, or that the documentation proves an SDK upgrade or successful payment. Raw lines 15–24 and 114–257.

## Q2 — Central transition, prerequisites and warnings

**Query:** What must change for Android Drop-in and Components when moving to v5, and what version or server-role caveats matter?

**Expected route:** [[source-adyen-docs-online-payments-upgrade-your-integration-upgrade-to-android-5-0-0]], then its pinned raw at [[raw/adyen/docs/online-payments/upgrade-your-integration/upgrade-to-android-5-0-0/2026-09-15]].

**Answer boundary:** Raw lines 25–47 give SDK/build dependency versions; lines 49–112 distinguish required configuration from conditional amount and TEST/live environments; lines 114–179 give method, callback, merchant-server and Component-view changes; lines 181–242 give launch changes and the removed result intent; lines 244–257 give import/internal-API and optional action handling. Keep the page's v5.0.0 title separate from the v5.3.0 configuration and launch links at lines 62, 89, 185, and 215. The `onSubmit`/`onAdditionalDetails` example assigns `/payments` and `/payments/details` calls to the merchant server at lines 146–161; it is an advanced-flow example, not a universal Sessions-flow requirement.
