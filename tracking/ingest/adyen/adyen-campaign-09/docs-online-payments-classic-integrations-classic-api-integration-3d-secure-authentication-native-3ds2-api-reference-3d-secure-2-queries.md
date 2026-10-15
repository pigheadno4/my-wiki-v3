# Fixed retrieval checks: Classic API 3D Secure 2 API reference

## Q1 — Purpose and scope

**Query:** What does this Adyen 3DS2 API reference cover, and should a new merchant integration use its Classic API endpoints?

**Expected answer:** It is a parameter and authentication-result reference for legacy Classic API `/authorise` 3DS2, listing `/authorise`, `/authorise3ds2`, and `get3dsAvailability` at v40 or later. Adyen says it no longer accepts new Classic API integrations and recommends moving to the Checkout API 3DS2 route. Do not infer current endpoint availability, account eligibility, a supported new integration, SDK version, or successful authentication/payment from the snapshot.

**Raw locators:** `# API reference`, lines 15–29. **Canonical retrieval route:** [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-3d-secure-authentication-native-3ds2-api-reference-3d-secure-2]] → [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/api-reference-3d-secure-2/2026-09-15|pinned raw]].

## Q2 — Central capability, prerequisites, and warnings

**Query:** Which 3DS2 request and result data does the Classic reference describe, what conditions apply to browser, app and external authentication, and does authentication-only authorize a payment?

**Expected answer:** The reference gives additional request objects, channel-conditional browser and app fields, third-party `mpiData` mapping and scheme-specific response combinations, challenge/result status data, and `additionalData` returned for authentication-only `/authorise3ds2`. Issuer or scheme conditions can make objects mandatory; browser needs full `browserInfo`, and app fallback to 3DS1 needs `userAgent` and `acceptHeader`. It says `billingAddress` and `shopperEmail` are card-scheme requirements for browser/app. `authenticationData.authenticationOnly=true` does only 3DS2 authentication, not payment authorization. MPI combinations and authentication statuses do not guarantee a financial outcome. Keep the Classic deprecation and exact API/version qualifiers.

**Raw locators:** `## 3D Secure 2 additional parameters`, lines 31–51; `## billingAddress`, lines 117–130; `## browserInfo`, lines 132–148; `## mpiData` and combinations, lines 230–347; `## threeDS2RequestData`, lines 382–430; `## additionalData.threeDS2Result`, lines 444–505; `## authenticationData.authenticationOnly`, lines 506–510. **Canonical retrieval route:** [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-3d-secure-authentication-native-3ds2-api-reference-3d-secure-2]] → [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/api-reference-3d-secure-2/2026-09-15|pinned raw]].
