# C31 fixed query audit — Group B — 4/4 PASS

Analysis end (UTC): 2026-10-04T02:23:36Z

## 1. Android v5 exact route — PASS

- Object/action match: Local Payment Methods **configuration** prerequisite checklist; Android v5 website route, not exact-package/SHA implementation evidence.
- Route: `wiki/index.md:11` → `wiki/braintree-index.md:110` → `wiki/concepts/braintree-payment-methods.md:28` → `wiki/sources/braintree/source-braintree-local-payment-methods-configuration-android-v5.md:2-8` → `raw/braintree/docs/guides/local-payment-methods/configuration/android/v5-2026-09-16.md`.
- Exact route locator: raw `title`/`slug` at lines 6-9 and `# Configuration` at line 14. `raw_files` reverse lookup resolves to this one source owner; the only matching dated Android-v5 configuration raw is the selected file.
- Pin: SHA-256 `0d8e58ee1aaf0af5380bde57fc91aa4038eba27e6fdc6a5aba50d4ddddc58ad3`, matching the C31 manifest.

## 2. Android v5 configuration responsibility and warning — PASS

- Before acceptance, the checklist requires a valid PayPal business account created, verified and linked in the Braintree Control Panel (raw 24-27); server generation of a client token and its client-component initialization use (28-29); client integration (32-33); server-side Local Payment transaction creation, webhooks, and successful processing in **either** Sandbox **or** Production (36-38).
- Material warning: the captured notice gives a March 30, 2026 mobile-certificate expiry, Android floors `4.45.0+` or `5.0.0+`, and says 100% of traffic from affected app versions would fail unless those versions were decommissioned or force-upgraded (17-20). Because collection was 2026-09-16, this is historical snapshot evidence, not current certificate/support proof.
- Boundary preserved: “successful Sandbox or Production” is a prerequisite/checklist item, not evidence that account setup, environment configuration, or a transaction actually succeeded. The Android-v5 route separately says Local Payment Methods were introduced in Android SDK v2 (33); that does not make this exact-package evidence.

## 3. iOS v7 exact route — PASS

- Object/action match: Local Payment Methods **configuration** prerequisite checklist; iOS v7-routed website document, not exact-package/SHA implementation evidence.
- Route: `wiki/index.md:11` → `wiki/braintree-index.md:111` → `wiki/concepts/braintree-payment-methods.md:29` → `wiki/sources/braintree/source-braintree-local-payment-methods-configuration-ios-v7.md:2-8` → `raw/braintree/docs/guides/local-payment-methods/configuration/ios/v7-2026-09-16.md`.
- Exact route locator: raw `title`/`slug` at lines 6-9 and `# Configuration` at line 14. `raw_files` reverse lookup resolves to this one source owner; the only matching dated iOS-v7 configuration raw is the selected file.
- Pin: SHA-256 `1a98a2762b23986ff985108e69c7a08ecaeae1f9f5fb8628c2f8603712de5038`, matching the C31 manifest.

## 4. iOS v7 configuration responsibility and warning — PASS

- Before acceptance, the checklist requires a valid PayPal business account created, verified and linked in the Braintree Control Panel (raw 22-25); server generation of a client token and its client-component initialization use (26-27); client integration (30-31); server-side Local Payment transaction creation, webhooks, and successful processing in **either** Sandbox **or** Production (34-36).
- Material warning: the captured notice gives a March 30, 2026 mobile-certificate expiry, an iOS floor of `6.17.0+`, and says 100% of traffic from affected app versions would fail unless those versions were decommissioned or force-upgraded (17-20). It is historical snapshot evidence, not current certificate/support proof or the exact iOS-v7 package version.
- Boundary preserved: the final environment-success item is a requirement, not evidence of an initiated, authorized, completed, settled, or funded payment. The iOS-v7 route separately says Local Payment Methods were introduced in iOS SDK v4 (31); this is an introduction-history statement, not sibling-platform or exact-installed-version authority.

## Shared gap sweep

- No extra full raw read was needed. The selected full raws answer all four fixed questions; related client/server/webhook/testing links remain navigation-only.
- Bounded filename and `raw_files` reverse-lookup checks found one selected raw and one source owner per page. Both source pages link `[[braintree-payment-methods]]`; the iOS page additionally links `[[braintree-ios-sdk]]` without replacing the required provider-method route.
- No unresolved factual conflict blocks these answers. The only material scope tensions are route version versus historical introduction version, and the post-deadline certificate notice; both are explicitly preserved above.
