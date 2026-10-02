# C26 fixed query audit — Group C

- Analysis end (UTC): `2026-10-02T11:09:10Z`
- Final handoff (UTC): `2026-10-02T11:09:14Z`
- Verdict: **PASS (4/4 questions; 2/2 manifest hashes)**

## auth-branding-ios-v7

- Route: `wiki/index.md:11` → `wiki/braintree-index.md:284` → `wiki/concepts/braintree-auth.md:31` → `wiki/sources/braintree/source-braintree-auth-branding-ios-v7.md` → `raw/braintree/docs/guides/braintree-auth/branding/ios/v7-2026-09-16.md`. The source is not yet listed directly in the coordinator-owned Braintree/company source catalogs; the concept route is complete.
- Hash: `248c325b980c46ba4ec2f9ec96df4a9be25e8dd71ce34fba4a2d52da7eacd41e` = C26 manifest — **PASS**.
- Q1 — “Where is the iOS v7 Auth branding guide?”
  - Object/action match: iOS v7 Braintree Auth branding and asset guide / locate the guide — **MATCH**.
  - Direct answer: `https://developer.paypal.com/braintree/docs/guides/braintree-auth/branding/ios/v7`; pinned raw path above.
  - Exact locator: raw lines 1, 6-9, 14 — **PASS**.
- Q2 — “Which branding actions and required/optional conditions does this variant state?”
  - Object/action match: merchant-facing identity, dashboard/payment marks, explanatory copy and iOS Connect-button asset / state only the guide's actual modality and conditions — **MATCH**.
  - Direct answer: the snapshot labels Braintree Auth closed beta and says interested platforms should contact Braintree. It directs platforms to present the unified Braintree Auth/Connect experience as **PayPal powered by Braintree** and, when referencing that brand in a dashboard, use one of the supplied horizontal or vertical logos. It provides one mark for major cards plus PayPal and a cards-only mark. Copy beside **Connect with Braintree** is recommended, not required: transaction-creating platforms get the “start accepting” example, while platforms connecting merchants without running transactions need only the account-linking call to action; a generic FAQ link is supplied. The page links an iOS button-asset download and gives an optional resource choice—download partner assets to self-host or use the provided code. It does **not** state an iOS SDK integration, modal behavior, post-authorization button state, current support, payment acceptance for a specific merchant, or parity with Android/JavaScript.
  - Exact locator: closed-beta condition and brand direction lines 17-20; conditional dashboard logo use lines 23-37; cards+PayPal versus cards-only marks lines 38-51; recommended/relationship-dependent copy and FAQ lines 53-70; iOS asset link lines 74-76; self-host/provided-code choice lines 79-81 — **PASS**.

## auth-branding-android-v5

- Route: `wiki/index.md:11` → `wiki/braintree-index.md:284` → `wiki/concepts/braintree-auth.md:36` → `wiki/sources/braintree/source-braintree-auth-branding-android-v5.md` → `raw/braintree/docs/guides/braintree-auth/branding/android/v5-2026-09-16.md`. The source is not yet listed directly in the coordinator-owned Braintree/company source catalogs; the concept route is complete.
- Hash: `9bfe16f52e2eb69fafb52733a60866b04f43625829ed4b7e9e6f4c7abfc5fb8b` = C26 manifest — **PASS**.
- Q3 — “Where is the Android v5 Auth branding guide?”
  - Object/action match: Android v5 Braintree Auth branding and asset guide / locate the guide — **MATCH**.
  - Direct answer: `https://developer.paypal.com/braintree/docs/guides/braintree-auth/branding/android/v5`; pinned raw path above.
  - Exact locator: raw lines 1, 6-9, 14 — **PASS**.
- Q4 — “Which branding actions and required/optional conditions does this variant state?”
  - Object/action match: merchant-facing identity, dashboard/payment marks, explanatory copy and Android Connect-button asset / state only the guide's actual modality and conditions — **MATCH**.
  - Direct answer: the snapshot labels Braintree Auth closed beta and says interested platforms should contact Braintree. It directs platforms to present the unified Braintree Auth/Connect experience as **PayPal powered by Braintree** and, when referencing that brand in a dashboard, use one of the supplied horizontal or vertical logos. It provides one mark for major cards plus PayPal and a cards-only mark. Copy beside **Connect with Braintree** is recommended, not required: transaction-creating platforms get the “start accepting” example, while platforms connecting merchants without running transactions need only the account-linking call to action; a generic FAQ link is supplied. The page links an Android button-asset download and gives an optional resource choice—download partner assets to self-host or use the provided code. It does **not** state an Android SDK integration, modal behavior, post-authorization button state, current support, payment acceptance for a specific merchant, or parity with iOS/JavaScript.
  - Exact locator: closed-beta condition and brand direction lines 17-20; conditional dashboard logo use lines 23-35; cards+PayPal versus cards-only marks lines 38-55; recommended/relationship-dependent copy and FAQ lines 58-78; Android asset link lines 81-83; self-host/provided-code choice lines 86-88 — **PASS**.

## Shared bounded checks

- Raw gap sweep: a filename/content-bounded sweep under `raw/braintree/docs/guides/braintree-auth/branding/` found exactly the assigned iOS v7 and Android v5 raws plus the separate JavaScript v3 sibling; targeted brand/button phrases also surfaced adjacent Connect/reference pages, but no second snapshot or conflict for either selected canonical page.
- Extra read: the JavaScript v3 branding raw and its source page were read completely only to police variant boundaries. Its library, redirect and post-authorization button conditions are JavaScript-specific and were not imported into the mobile asset answers.
- Reciprocal checks: `wiki/index.md` routes to `wiki/braintree-index.md`; that index routes to `[[braintree-auth]]`; the concept links both assigned sources; each source links back to `[[braintree-auth]]`, names `[[braintree]]`, and links its exact raw. The Android source's additional Connect link is valid navigation; the iOS page's absence of that extra link does not break the required route.
- Remaining promotions overlap. Direct Braintree-index and company source-catalog additions/count reconciliation are deferred coordinator-owned aggregation and are not counted as Group C retrieval failures.
- Final verdict: **PASS**.
