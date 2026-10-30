# Fixed query audit: POST /legalEntities

Source: `wiki/sources/adyen/source-adyen-api-explorer-legalentity-latest-post-legalentities.md` — https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities

## Q1

For `legalentity/latest/post/legalEntities`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

The captured LEM API v4 TEST endpoint creates a legal entity holding a platform user's verification data (raw lines 5–20). Request `type` is required; individual, organization, sole-proprietorship and trust objects are conditional on it (lines 41, 78, 142, 178, 210). `unincorporatedPartnership` is absent from the listed top-level enum but has a conditional object and example (lines 210–211, 471–504). The individual and organization branches require support information if there is a platform setup (lines 68–70, 123–125); the sole-proprietorship, trust and unincorporated-partnership branches in this table list no support field. Other nested fields and country conditions are in lines 30–240. The optional verification-code header is test-only, one suberror code at a time (lines 24–27). Limits: 700 live and 200 test requests per five seconds; five failed requests per ten seconds (lines 11–17). The page lists 401/403 but names no role (lines 803–826).

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

The 200 response identifies a created legal entity and may include capabilities, problems and deadlines; `requested` differs from `allowed`, which becomes true after successful verification (raw lines 513–535, 559, 664–676, 783–787). The example has `requested: true`, `allowed: false`, `verificationStatus: pending` (lines 1001–1025). Verification results can arrive by webhook or API response (line 9); creation does not prove approval, account-holder creation, payment or funds movement. Errors are 400/401/403/422/500 (lines 790–852). The displayed server is test `/lem/v4` (lines 19–20); `latest` is the captured URL label, not current-version or live-availability proof.
