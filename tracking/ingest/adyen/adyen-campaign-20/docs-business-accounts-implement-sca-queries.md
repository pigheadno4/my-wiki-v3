# Business Accounts implement SCA retrieval checks

## Q1 — What is this page's SCA purpose and implementation route?

**Answer:** In its dated PSD2 framing, the page says SCA identity verification applies to some Business Accounts actions, giving third-party bank transfers, transaction-history consultation and transfer-limit creation as examples. It explains two factors from knowledge, possession and inherence. The client-side Authentication SDK combines possession with knowledge or inherence; the route is install for iOS/Android/web, register a device, then use action-specific guides for transfers and history. This overview is not evidence that a particular user authenticated or a transfer was booked.

**Evidence:** `raw/adyen/docs/business-accounts/implement-sca/2026-09-15.md:19-46`. **Forward route:** `[[index]]` → `[[adyen-index]]` → `[[adyen-business-accounts]]` → `[[source-adyen-docs-business-accounts-implement-sca]]` → `[[raw/adyen/docs/business-accounts/implement-sca/2026-09-15]]`.

## Q2 — Does the overview settle UK applicability or require SCA for every Business Accounts action?

**Answer:** No. Its opening names EEA or UK, while the bottom install link says the linked guide applies only to EEA. The body says “some procedures” and presents examples. The capture is marked modified in 2022, so use current, action-specific guidance before deciding UK scope or a particular SCA requirement. SDK installation and device registration are setup steps, not proof of a completed authentication or financial operation.

**Evidence:** `raw/adyen/docs/business-accounts/implement-sca/2026-09-15.md:11,19-25,35-46,48-60`. **Forward route:** `[[index]]` → `[[adyen-index]]` → `[[adyen-business-accounts]]` → `[[source-adyen-docs-business-accounts-implement-sca]]` → `[[raw/adyen/docs/business-accounts/implement-sca/2026-09-15]]`.
