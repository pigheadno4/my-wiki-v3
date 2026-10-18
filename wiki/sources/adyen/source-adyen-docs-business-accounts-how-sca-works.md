---
title: "Adyen Business Accounts: How API SCA works"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/how-sca-works"
raw_files:
  - "adyen/docs/business-accounts/how-sca-works/2026-09-15.md"
tags: [adyen, business-accounts, sca, authentication, api]
---

## Overview

This 2022-modified overview, captured 2026-09-15, describes an Authentication SDK challenge around Business Accounts API procedures that require strong customer authentication (SCA). It names third-party funds transfers, transaction-history consultation and transfer-limit creation as examples, while expressly saying it is not a use-case-specific procedure guide. For a qualifying request, the client SDK supplies `sdkOutput`, the server exchanges it with Adyen, the user completes a challenge, and the server submits a new `sdkOutput`. A successful endpoint response is an API result, not proof that a transfer settled or a beneficiary received funds.

## Key takeaways

- The stated setup is an Adyen for Platforms integration including Business Accounts, a web-service API credential with roles depending on the requested endpoint, an installed Authentication SDK, and extra Adyen configuration for the eligibility-check functionality. The app must check device eligibility before a procedure requiring SCA. The captured SDK tabs cover Android/Kotlin, iOS/Swift and web/JavaScript; web availability may throw `SCA_UNAVAILABLE`.
- On initiation, the server places the eligibility `sdkOutput` in a `WWW-Authenticate` header, with an `SCA realm` identifying the procedure and base64 `auth-param1`. The guide treats a successful initiation as HTTP 401 containing a new blob, passed to the SDK as `sdkInput`. After challenge completion, the server sends a second `WWW-Authenticate` header with the same realm and new `sdkOutput`; successful finalization returns endpoint-dependent HTTP 2xx.
- The `Authenticate your user` section says to authenticate the user with two factors, then illustrates SDK `register(...)` calls for device registration. That wording blends a procedure challenge with device registration. Treat device eligibility/registration and authentication of a specific later API action as distinct evidence; this overview alone does not specify a complete repeat-authentication implementation or prove that a user completed a challenge.
- These are historical product-integration instructions, not current legal advice on when SCA is mandatory or evidence of live permissions, account opening, authorization, transfer booking or bank receipt. The next-step registration and device-management guides are navigation from this page.

## Detail locators

- Opening, examples and `Requirements` — overview-only scope, SCA-dependent procedures, SDK output, Platforms/Business Accounts integration, role and installation conditions (raw lines 15–39).
- `How it works` — eligibility, first server request, HTTP 401 challenge, second request and endpoint-dependent HTTP 2xx (raw lines 41–75).
- `Check SCA eligibility` — extra Adyen configuration and Android/iOS/web SDK examples, including web unsupported error (raw lines 77–173).
- `Initiate the procedure` — `WWW-Authenticate` realm and `auth-param1`, HTTP 401 and `sdkInput` handoff (raw lines 175–199).
- `Authenticate your user` — 2FA statement and registration examples whose terminology needs care (raw lines 201–256).
- `Finalize the procedure` — second header and endpoint-specific HTTP 2xx (raw lines 258–270).
- `Next steps` — device-registration and management navigation (raw lines 272–282).

## Related

- Company: [[adyen]]
- Main concept: [[adyen-business-accounts]]
- Platform context: [[adyen-platforms]]

## Raw Sources

- [[raw/adyen/docs/business-accounts/how-sca-works/2026-09-15|2026-09-15 Business Accounts API SCA overview]]
