# C09 fixed queries — docs-online-payments-classic-integrations-classic-api-integration-3d-secure-authentication-other-3ds-flows-data-only

## Q1 — Purpose, scope, and inference boundary

**Query:** Is the Classic data-only flow a shopper-authenticated 3DS2 payment with liability shift, and does its Mastercard-only statement govern modern Checkout API?

**Expected answer:** This is a dated Classic `/authorise` data-only guide. It sends 3DS2 data through a scheme path and says the shopper gets no challenge or strong customer authentication; chargeback liability stays with the merchant. Data sharing does not prove authentication or authorization. Its 2019-modified page says Mastercard-only, whereas the separately retained Checkout-era guide covers Visa and Mastercard. Neither source should silently override the other's scoped route or time.

**Evidence:** `raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/other-3ds-flows/data-only/2026-09-15.md:19-37`; separate source `[[source-adyen-docs-online-payments-3d-secure-data-only]]`.

**Canonical retrieval route:** `[[adyen-index]]` → `[[adyen-3d-secure]]` → `[[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-3d-secure-authentication-other-3ds-flows-data-only]]` → pinned raw.

## Q2 — Central capability, prerequisites, and warnings

**Query:** What does the Classic merchant send to request data-only, what setup and market qualifications appear, and what response or payment result can be assumed?

**Expected answer:** In Classic Payment API `/authorise`, set `additionalData.threeDS2DataOnly: true`; remaining required fields and response depend on the regular 3DS2 integration. The guide lists a test account, API key, and API library, and warns that use in SCA-mandated markets such as its EEA example can increase authentication rejections. It presents a Payment API v50 test request, not a Checkout API `/payments` contract. No challenge or liability shift is described, and the guide does not guarantee authorization success or current merchant/scheme eligibility.

**Evidence:** `raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/other-3ds-flows/data-only/2026-09-15.md:25-27`, `raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/other-3ds-flows/data-only/2026-09-15.md:35-53`, `raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/other-3ds-flows/data-only/2026-09-15.md:57-70`.

**Canonical retrieval route:** `[[adyen-index]]` → `[[adyen-3d-secure]]` → `[[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-3d-secure-authentication-other-3ds-flows-data-only]]` → pinned raw.
