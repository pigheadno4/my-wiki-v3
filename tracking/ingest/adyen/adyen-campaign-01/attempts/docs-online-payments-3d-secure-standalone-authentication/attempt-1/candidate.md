---
title: "Adyen Docs: Standalone authentication"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/3d-secure/standalone-authentication"
raw_files:
  - "adyen/docs/online-payments/3d-secure/standalone-authentication/2026-09-15.md"
tags: [adyen, 3d-secure, 3ds2, authentication, advanced-flow]
---

## Overview

This Adyen guide explains standalone 3D Secure 2 authentication: authenticate a shopper separately from payment authorization, receive authentication data, and later use that data to seek authorization from Adyen or another PSP. The documented route uses Adyen's Advanced flow and does not support triggering standalone authentication through `/sessions` or Hosted Checkout.

The snapshot documents authentication and later authorization as separate operations. It does not prove current merchant eligibility, account configuration, issuer outcome, authorization success, or settlement.

## Key takeaways

- The merchant sends `/payments` with `authenticationData.authenticationOnly` set to `true`, handles the returned 3DS2 action through the existing native or redirect integration, and submits the authentication result through `/payments/details` with `authenticationOnly: true`.
- A completed authentication returns `AuthenticationFinished`; `threeDS2Result.transStatus` value `Y` indicates successful authentication. Redirect results are instead documented under `additionalData.threeDAuthenticatedResponse`. See **Perform the authentication** and **Get the 3D Secure 2 authentication data**.
- The setup requires an Advanced-flow online-payments integration, an API credential with the Checkout webservice role, Standard webhooks with the non-default `AUTHENTICATION` event enabled, 3DS2 Native or Redirect setup, and response/configuration settings that cause authentication to be attempted. See **Requirements** for the exact conditions.
- When authentication is performed with Adyen but authorization will use a different PSP or acquirer, the guide recommends providing the matching acquirer enrollment data because mismatches can cause refusals. See **Provide additional acquirer-related data**.
- Authentication data cannot be reused across PSPs and cannot be used after expiry. The snapshot lists different cryptogram-validity periods by scheme; consult **Authentication data expiry** rather than assuming one universal lifetime.
- `AuthenticationNotRequired` means the transaction does not require 3DS authentication and can proceed to a standard payment flow with Adyen or another PSP. The guide lists possible reasons under **Authentication not required reasons**.

## Material qualifications

- Standalone authentication is not available through `/sessions` or Hosted Checkout in this guide.
- Authentication success is not payment authorization. A later authorization request is still required, and its outcome is separate.
- Authentication data is time-limited and cannot be retried with a different PSP after it has been sent to one PSP and that authorization fails.
- Field availability varies by scheme; Cartes Bancaires has additional conditional fields, and redirect authentication exposes its result through a different response field.
- This is a documentation snapshot collected on 2026-09-15, not proof of current enablement, supported schemes, or a successful live transaction.

## Detail locators

- **Requirements** — Advanced-flow, credential role, webhook, unsupported `/sessions`/Hosted Checkout routes, 3DS2 setup, response-field enablement, and authentication-trigger configuration.
- **Make a payment request for authentication** — request fields by channel, web and mobile qualifications, result-code branching, and language-specific examples.
- **Provide additional acquirer-related data** — cross-PSP/acquirer enrollment data and mismatch warning.
- **Perform the authentication** — action handling, `/payments/details` submission, completion/refusal results, and redirect result location.
- **Get the 3D Secure 2 authentication data** — scheme-qualified `threeDS2Result` fields and `transStatusReason` values.
- **Authorize the payment** — non-reuse warning, Adyen `mpiData` mapping, co-badged-card brand handling, and Cartes Bancaires conditions.
- **Authentication data expiry** — scheme-specific cryptogram validity table.
- **Authentication not required reasons** — `AuthenticationNotRequired` handling and reason values.
- **Testing** — test-guide route and `AUTHENTICATION` webhook outcome notice.

## Related

- [[adyen]]
- [[adyen-3d-secure]]
- [[adyen-3ds2-android-sdk]]
- [[adyen-3ds2-ios-sdk]]

## Raw Sources

- [[raw/adyen/docs/online-payments/3d-secure/standalone-authentication/2026-09-15|Adyen Docs — Standalone authentication (2026-09-15)]]
