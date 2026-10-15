# Fixed retrieval queries — docs-online-payments-classic-integrations-classic-api-integration-3d-secure-authentication-native-3ds2-authentication-only-integration

## Q1 — purpose, scope, and non-inference

**Query:** In the 2026-09-15 snapshot, what is the Adyen Classic API authentication-only 3DS2 guide for, and what cannot be inferred from it?

**Expected answer:** It documents a legacy Classic Payment API (`/authorise` and `/authorise3ds2`) route in which a merchant has Adyen perform 3DS2 authentication separately from later payment authorization, potentially with another PSP or acquirer. It covers browser, Android, and iOS paths. The page says Adyen no longer accepts new Classic integrations and points to Checkout API standalone authentication. Authentication success does not establish authorization, capture, charge, live merchant eligibility, or current support.

**Raw locators:** lines 17–27; headings **Web-based authentication only** (line 46), **Android 3D Secure 2 SDK authentication only** (line 217), **iOS 3D Secure 2 SDK authentication only** (line 773); **Optional: Authorise the payment with Adyen** (line 1702). Canonical route: https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/authentication-only-integration

## Q2 — central capability, prerequisites, and warnings

**Query:** How does the Classic authentication-only route initiate and complete 3DS2, what must be prepared, and which conditions or warnings matter before a later authorization?

**Expected answer:** The merchant prepares a test account, API key, library connection, and the applicable web or native 3DS2 guide. It sends a Classic `/authorise` request with the relevant 3DS2 data and `threeDSAuthenticationOnly: true`; issuer-directed results can require fingerprinting, challenge, or 3DS1 redirect. After successful authentication, the merchant obtains the authentication data needed for a separate authorization (`authenticationValue`, `dsTransID`, `eci`). `/getAuthenticationResult` needs additional Adyen configuration and the guide routes Cartes Bancaires to `/retrieve3ds2Result`. For another acquirer, Adyen strongly recommends matching enrolled acquirer data, as mismatches can cause refusals. Authentication data expires by scheme. Continuing with Adyen is a distinct server-side `/authorise3ds2` request using `threeDSAuthenticationOnly: false`; its `Authorised` outcome is conditional on successful payment.

**Raw locators:** **Before you begin** (line 33); **Submit a payment authentication request** (lines 50–58); **3D Secure 1 authentication-only fallback** (line 29); **Get the 3D Secure 2 authenticated data** (lines 1329–1346); **Optional: Provide additional acquirer-related data** (lines 1608–1636); **Optional: Authorise the payment with Adyen** (lines 1702–1715); **Authentication data expiry** (lines 1767–1776). Canonical route: https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/authentication-only-integration
