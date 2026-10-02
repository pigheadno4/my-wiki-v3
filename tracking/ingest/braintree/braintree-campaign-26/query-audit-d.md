# C26 fixed query audit — Group D

- Analysis end (UTC): `2026-10-02T11:10:36Z`
- Final handoff (UTC): `2026-10-02T11:10:51Z`
- Verdict: **PASS (4/4 questions; 2/2 manifest hashes)**

## sdk-deprecation-ios-v7

- Route: `wiki/index.md` → `wiki/braintree-index.md` → `wiki/concepts/braintree-ios-sdk.md` → `wiki/sources/braintree/source-braintree-client-sdk-deprecation-policy-ios-v7.md` → `raw/braintree/docs/guides/client-sdk/deprecation-policy/ios/v7-2026-09-16.md`.
- Hash: `3f0cd58baa8f18ec48725539748a0f6ffb60a6907a4c3f4bfe87154b55e82dd3` = C26 manifest — **PASS**.
- Q1 — “Where is the iOS v7 client-SDK deprecation policy?”
  - Object/action match: iOS v7-routed Braintree client-SDK deprecation policy / locate the guide — **MATCH**.
  - Direct answer: `https://developer.paypal.com/braintree/docs/guides/client-sdk/deprecation-policy/ios/v7`; pinned raw path above.
  - Exact locator: raw lines 1, 6-9, 14 — **PASS**.
- Q2 — “Which lifecycle distinctions and consequences does this historical snapshot state?”
  - Object/action match: historical iOS-routed client-SDK lifecycle policy / distinguish status categories and consequences without asserting current v7 support — **MATCH**.
  - Direct answer: the snapshot recommends at least annual client-SDK updates and says a major-version increase signals that existing integrations will likely need code changes; adding/dropping OS or browser support and security changes are examples, although Braintree says it tries to avoid a new major unless the change is large enough to break compatibility. For the **active major**, the iOS platform rule is relative: at minimum the newest iOS release plus the prior two; iOS 14/13/12 is only the page's example. `Active` is the single current fully supported major and receives new features. `Inactive` starts when a deprecation date is assigned and receives only security updates. `Deprecated` receives no updates; processing **will** continue for one year after the deprecation date, but the page says to upgrade immediately to avoid disruption. `Unsupported` has neither developer nor Braintree Support support, and processing **can** be suspended at any time. Per-major status and deprecation dates belong in each SDK README; exceptions may occur and Braintree says it will try to communicate them. This 2026-09-16 capture, whose embedded update time is 2025-11-21, does not assign v7 a status or date and is not current support evidence.
  - Exact locator: annual update lines 17-18; semantic-version signal/examples/qualification lines 23-35; relative iOS rule lines 38-42; category definitions and consequences lines 45-54; README/status-change route and exception qualification lines 56-60; monitoring/contact guidance lines 65-69 — **PASS**.

## sdk-deprecation-android-v5

- Route: `wiki/index.md` → `wiki/braintree-index.md` → `wiki/concepts/braintree-android-sdk.md` → `wiki/sources/braintree/source-braintree-client-sdk-deprecation-policy-android-v5.md` → `raw/braintree/docs/guides/client-sdk/deprecation-policy/android/v5-2026-09-16.md`.
- Hash: `634fb5e81795cce40eba68d443221c9836daa723e311a28d1bf0d9662bfe3c25` = C26 manifest — **PASS**.
- Q3 — “Where is the Android v5 client-SDK deprecation policy?”
  - Object/action match: Android v5-routed Braintree client-SDK deprecation policy / locate the guide — **MATCH**.
  - Direct answer: `https://developer.paypal.com/braintree/docs/guides/client-sdk/deprecation-policy/android/v5`; pinned raw path above.
  - Exact locator: raw lines 1, 6-9, 14 — **PASS**.
- Q4 — “Which lifecycle distinctions and consequences does this historical snapshot state?”
  - Object/action match: historical Android-routed client-SDK lifecycle policy / report only captured distinctions and explicitly retain the missing category definitions — **MATCH**.
  - Direct answer: the snapshot recommends at least annual SDK updates and says a major-version increase signals that an existing integration will likely need code changes; OS/browser support and security changes are examples, qualified by Braintree's stated effort to avoid a new major unless the required change is large enough to be breaking. Android platform support is release-relative: the active major supports the Android versions most widely used **at the time of its release**; API 21+ is only the page's example. The capture says client SDKs can have statuses, shows an external lifecycle diagram, and directs readers to each SDK README for major-version status and deprecation dates, updated as new majors release; unforeseen exceptions may occur. **The captured Android body contains no status-category names, definitions, or category-specific processing/update consequences.** None are imported from iOS or JavaScript. This 2026-09-16 capture has embedded update time 2025-04-02 and does not establish current Android support, current v5 status, or a deprecation deadline.
  - Exact locator: annual update lines 17-18; semantic-version signal/examples/qualification lines 21-33; release-time Android rule and example lines 36-40; category-section omission, diagram, README/date lookup, and exception qualification lines 43-56; monitoring/contact routes lines 59-73 — **PASS**.

## Shared bounded checks

- Raw gap sweep: one filename-bounded sweep of `raw/braintree/docs/guides/client-sdk/deprecation-policy/` found the assigned iOS v7 and Android v5 raws plus the separate JavaScript v3 sibling. No missing same-platform deprecation-policy raw was found.
- Extra reads: none. Both assigned raws directly answer the fixed questions. The JavaScript sibling and external lifecycle diagram remained outside Group D; Android's absent category definitions were not backfilled from iOS, JavaScript, GitHub, or inference.
- Reciprocal checks: `wiki/index.md` routes to `wiki/braintree-index.md`; that index lists both platform concepts and both source pages; each concept links its platform source; each source links back to its platform concept and to its exact pinned raw. Each raw is owned by exactly one source summary. Canonical URLs and both raw hashes match the C26 manifest.
- Final verdict: **PASS; 4/4 questions, no repair proposed**.
