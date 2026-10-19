# Retrieval checks — docs-issuing-test-verification-errors

## Q1 — Main purpose and prerequisites

How can an Adyen Issuing/Platforms integration test a failed KYC verification, and what must be prepared? The 2026-09-15 guide says required data normally passes test checks, while a single requested suberror code in the `x-requested-verification-code` header on the stated Legal Entity Management POST endpoint forces a failure in **test only**; the integration and credentials, account holder for the relevant legal entity, and webhook/GET result route are described at raw lines 21, 25-47, 1162-1173. Follow [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-test-verification-errors]] → [[raw/adyen/docs/issuing/test-verification-errors/2026-09-15]].

## Q2 — Material boundary and failure check

Can this header be used with hosted onboarding or prove live remediation? No. The guide excludes hosted onboarding and restricts requested verification codes to the test environment (raw lines 39, 47, 1511). `0_0001` on the corresponding PATCH simulates resolution, conditional on successful error handling (raw lines 1507-1519); inspect the GET or account-holder webhook verification errors and actions (raw lines 1168-1505). Several SDK call snippets omit the header despite the prose/curl requirement (compare raw lines 35-47, 62-67, 146-149); a sample account-holder capability may be `enabled: true` but `allowed: false` (raw lines 1226-1231). Follow [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-test-verification-errors]] → [[raw/adyen/docs/issuing/test-verification-errors/2026-09-15]].
