---
title: "Adyen A2A Issuer API v1: authenticate iDEAL profile"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/a2aissuer-api/latest/post/ideal/profile/authenticate"
raw_files:
  - "adyen/api-explorer/a2aissuer-api/latest/post/ideal/profile/authenticate/2026-09-15.md"
tags: [adyen, business-accounts, a2a-issuer, ideal, authentication]
---

## Overview

This 2026-09-15-captured A2A Issuer API v1 reference documents `POST /ideal/profile/authenticate` on test and live balance-platform API servers. It generates a redirect URL to finish iDEAL-requested profile authentication. The caller must first ensure the user has completed multi-factor authentication. This issuer-side profile flow is separate from a merchant iDEAL payment authorization or final payment result.

## Key takeaways

- The request requires `accountHolderId` and the `payload` supplied by iDEAL for authentication. The sample payload is a URL string, but the schema calls it a string and does not define a general URL-format requirement.
- A 200 response lists an optional `redirectUrl` object described as short-lived; if that object is present, its `href` child is required and contains the full URL to redirect the user to the iDEAL authentication page. The page gives no duration for this URL. Generating it does not itself prove that the user completed profile authentication.
- The page defines 400 malformed-request, 422 validation and 500 server-error schemas. Illustrative 422 errors include no registered iDEAL profile (`1069_008`), an expired authentication payload (`1069_009`) and missing account holder (`30_012`). The 400 example is a body-mapping error; the 500 examples include an internal error and a payment-method error. Error examples do not establish the complete set of failure conditions.

## Detail locators

- Purpose, MFA prerequisite, and API v1 test/live servers: raw lines 5–15.
- Required request body and illustrative payload: raw lines 17–33.
- 200 redirect object and 400/422/500 response schemas: raw lines 34–100.
- Success and error examples: raw lines 102–186.

## Related

- [[adyen]] — provider.
- [[adyen-business-accounts]] — platform Business Accounts and A2A issuer context.
- [[source-adyen-docs-business-accounts-send-funds-ideal-integration]] — separate integration guide for platform redirects and iDEAL payment flow.

## Raw Sources

- [[raw/adyen/api-explorer/a2aissuer-api/latest/post/ideal/profile/authenticate/2026-09-15|A2A Issuer API v1 POST /ideal/profile/authenticate (captured 2026-09-15)]]
