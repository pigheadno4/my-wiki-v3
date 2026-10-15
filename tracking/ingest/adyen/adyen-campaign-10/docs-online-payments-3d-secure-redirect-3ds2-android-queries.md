# Android redirect 3DS landing-page retrieval checks

## Q1 — Purpose, scope, and non-inference

**Query:** What does this Adyen Android redirect 3DS page establish, and can it answer SDK-version, challenge-return, or successful-payment questions?

**Expected route:** `[[adyen-index]]` → `[[adyen-3d-secure]]` → `[[source-adyen-docs-online-payments-3d-secure-redirect-3ds2-android]]`; pinned raw `# Redirect 3D Secure for Android` lines 15–17 and `### How do you want to integrate?` lines 19–27.

**Expected answer:** It is a short integration chooser for supporting 3D Secure authentication through redirect in an Android app. It offers Drop-in and Components links. It provides no SDK version, API workflow, app-return handling, authentication result, authorization, or payment outcome. Those claims require the chosen detailed guide and transaction-specific evidence.

## Q2 — Central capability, prerequisites, warnings

**Query:** Which two Android integration routes does the page name, and how should the reader use its labels?

**Expected route:** Same source; raw lines 19–27. The corresponding canonical wiki routes are `[[source-adyen-docs-online-payments-3d-secure-redirect-3ds2-android-drop-in]]` and `[[source-adyen-docs-online-payments-3d-secure-redirect-3ds2-android-component]]`.

**Expected answer:** The page calls Drop-in an all-in-one UI solution and Components a pre-built Component; each link points to its dedicated Android redirect 3DS guide. These labels are navigation, not prerequisites or a claim that the component is installed, the merchant is enabled, or a challenge has run. Use the selected detailed source for implementation conditions. The landing snapshot's 2019 last-modified date is not current SDK proof.
