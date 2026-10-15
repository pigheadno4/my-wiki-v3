# Fixed retrieval checks: Classic API authorization with third-party 3DS data

## Q1 — Purpose and scope

**Query:** How does this Adyen Classic guide use third-party 3D Secure authentication data, and is it a route for a new Classic API integration?

**Expected answer:** A merchant first obtains 3DS authentication data from another provider, then sends a separate Classic Payment API POST `/authorise` request containing the relevant values in `mpiData`. The page chiefly describes 3DS2 but includes 3DS1 tabs. Adyen says it no longer develops or accepts new Classic API integrations and recommends the Checkout API authorization-only route, which requires migration to Checkout API. This dated snapshot does not prove current eligibility, successful authentication, payment authorization or capture.

**Raw locators:** title and deprecation notice, lines 15–23; authentication and request sections, lines 33–103. **Canonical retrieval route:** [[adyen-3d-secure]] → [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-3d-secure-authentication-other-3ds-flows-authorize-mpidata]] → [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/other-3ds-flows/authorize-mpidata/2026-09-15|pinned raw]].

## Q2 — Field conditions, co-badged warning, and outcome

**Query:** What conditions apply to the 3DS2 data and request fields, how must a co-badged card be handled, and does an authentication result guarantee `Authorised` or liability shift?

**Expected answer:** Use the raw guide's separate authentication-result and `/authorise` request tables: common fields are listed for all issuers, while Cartes Bancaires has additional data and request fields, including `additionalData.acquirerCode` set to `AdyenCartesBancaires`. The 3DS2 request table labels `dsTransID` without the `mpiData.` prefix while linking to an `mpiData` property; sample payloads nest it inside `mpiData`, so verify the intended Classic API schema before implementation. For a co-badged card, `selectedBrand` must identify the scheme that authenticated the payment or authorization may be refused. `Authorised` is returned only if Adyen's payment authorization succeeds; other result codes have separate actions, and the illustrative `liabilityShift` response is not a guarantee.

**Raw locators:** 3DS2 authentication-result table, lines 48–67; request-field table, lines 83–103; co-badged rule, lines 105–107; 3DS2 sample request from line 517; sample response, lines 1027–1054. **Canonical retrieval route:** [[adyen-3d-secure]] → [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-3d-secure-authentication-other-3ds-flows-authorize-mpidata]] → [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/other-3ds-flows/authorize-mpidata/2026-09-15|pinned raw]].
