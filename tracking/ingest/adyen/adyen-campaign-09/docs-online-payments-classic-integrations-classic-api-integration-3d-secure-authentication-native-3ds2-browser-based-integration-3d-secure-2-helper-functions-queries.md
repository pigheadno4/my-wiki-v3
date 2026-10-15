# C09 fixed queries — docs-online-payments-classic-integrations-classic-api-integration-3d-secure-authentication-native-3ds2-browser-based-integration-3d-secure-2-helper-functions

## Q1 — Purpose, scope, and inference boundary

**Query:** What does the 3D Secure 2 helper-functions page cover, and may it be used as the Checkout API browser 3DS2 implementation contract for a new integration?

**Expected answer:** It documents helper functions for browser-based 3DS2 using Classic Payment API `/authorise`. Adyen says it no longer accepts new Classic integrations and recommends the newer Checkout API helper functions, which require migrating to Checkout API. The Classic instructions and dated examples must not be generalized into the modern Checkout contract.

**Evidence:** `raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/browser-based-integration/3d-secure-2-helper-functions/2026-09-15.md:19-33` and example Payment API v68 test URL at `raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/browser-based-integration/3d-secure-2-helper-functions/2026-09-15.md:105-109`.

**Canonical retrieval route:** `[[adyen-index]]` → `[[adyen-3d-secure]]` → `[[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-3d-secure-authentication-native-3ds2-browser-based-integration-3d-secure-2-helper-functions]]` → pinned raw.

## Q2 — Central capability, prerequisites, and warnings

**Query:** In the Classic browser 3DS2 helper flow, what do the helpers do, what setup is needed, and how do the fingerprint and challenge timeout branches affect the next server request?

**Expected answer:** Helpers collect browser info, encode/decode base64url data, make iframe/form posts for issuer fingerprint and challenge steps, and set challenge size. The guide calls for a test account, API key, library, helper import, and separate method and challenge notification URLs. After `IdentifyShopper`, the server submits `/authorise3ds2` with `threeDSCompInd=Y` for a method callback within 10 seconds or `N` otherwise. After `ChallengeShopper`, it submits the challenge `transStatus`; absent challenge callback after 10 minutes leads to `transStatus: U`. Neither intermediate result alone proves final payment authorization.

**Evidence:** `raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/browser-based-integration/3d-secure-2-helper-functions/2026-09-15.md:25-69`, `raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/browser-based-integration/3d-secure-2-helper-functions/2026-09-15.md:601-659`, `raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/browser-based-integration/3d-secure-2-helper-functions/2026-09-15.md:927-950`, and `raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/browser-based-integration/3d-secure-2-helper-functions/2026-09-15.md:996-1020`.

**Canonical retrieval route:** `[[adyen-index]]` → `[[adyen-3d-secure]]` → `[[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-3d-secure-authentication-native-3ds2-browser-based-integration-3d-secure-2-helper-functions]]` → pinned raw.
