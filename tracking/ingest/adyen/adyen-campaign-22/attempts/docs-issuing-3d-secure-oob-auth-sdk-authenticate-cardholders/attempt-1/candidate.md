---
title: "Adyen Issuing: Authenticate cardholders with the OOB Authentication SDK"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/3d-secure/oob-auth-sdk/authenticate-cardholders"
raw_files:
  - "adyen/docs/issuing/3d-secure/oob-auth-sdk/authenticate-cardholders/2026-09-15.md"
tags: [adyen, issuing, 3d-secure, authentication, mobile-sdk]
---

## Overview

Adyen Issuing guide last modified 2023-07-12 and captured 2026-09-15 for issuer-side out-of-band authentication of a cardholder when an Adyen-issued-card transaction requires 3D Secure. It describes a relayed authentication webhook, a mobile Authentication SDK step, server-side challenge finalization and an authentication outcome webhook. The guide's ten-minute challenge window and two-second webhook response deadline are separate. A completed authentication lets the transaction continue; it does not itself prove payment authorisation, capture or settlement. [[adyen]] [[adyen-issuing]]

## Key takeaways

- The platform must set up an HTTPS server endpoint to receive/process relayed authentication webhooks, with JSON, basic authentication and port 443, 8443 or 8843, then supply the endpoint URL to its Adyen contact. Adyen enrolls the balance platform in ACS if needed, subscribes it to the webhook, sets OOB/OTP priority based on preference and shares ACS basic-auth credentials. The server must respond to an authentication webhook within **2 seconds** or the authentication fails. See raw **Set up and accept relayed authentication webhooks**, lines 29–49.
- The relayed webhook provides `sdkInput` as a Base64-encoded blob in the `www-authenticate` header, challenge `id`, `paymentInstrumentId` to route the request to the correct cardholder, and purchase details. Acknowledge with HTTP 200 and `authenticationDecision.status: proceed`; a late response or `refused` stops the authentication process. See raw **Get data from the authentication webhooks**, lines 53–111.
- Present transaction details to the cardholder in the app; the guide recommends push notification. Pass `sdkInput` to the iOS/Android Authentication SDK, then send its Base64-encoded `sdkOutput` to the server if authentication succeeds. The Kotlin and Swift snippets are examples, not SDK release guarantees. See raw **Authenticate cardholder**, lines 115–175.
- Finalize within **10 minutes of receiving the request**: the server PATCHes the ACS `/challenges/{id}` route using the Adyen-provided basic auth, challenge ID, `www-authenticate` header carrying `sdkOutput`, and `completed: true`. Check that the response has the challenge ID and `challengeCompleted: true`; the guide says this indicates cardholder authentication and continuation of the transaction. See raw **Finalize authentication**, lines 177–220.
- The guide says `balancePlatform.authentication.created` is sent **regardless of authentication outcome**, and shows frictionless authenticated, OOB challenge authenticated, and OTP retry-exceeded rejected examples. This is an authentication event, separate from later payment authorisation. **Cross-source warning:** [[source-adyen-docs-issuing-3d-secure-troubleshooting]] broadly says a failed 3D Secure attempt has “no webhook”; that wording must not be used to rule out this authentication-specific event, and neither source establishes a later authorisation/transfer event for every attempt. See raw **Get updates**, lines 222–360, and the linked troubleshooting source.

## Detail locators

- Webhook header/body field definitions and example: raw lines 63–96.
- Kotlin/Swift SDK examples and success/error branches: raw lines 123–169.
- ACS PATCH request/response examples, including a live-host example URL: raw lines 181–220. These are sample payloads, not evidence of a live challenge.
- Authentication outcome example fields and `environment: test`: raw lines 230–360.
- The guide's next-step links point to separate payment stages and authorisation topics: raw lines 362–374.

## Related

- [[adyen-issuing]] — Issuing concept and reciprocal source route.
- [[source-adyen-docs-issuing-3d-secure-oob-auth-sdk]] — OOB SDK overview and issuer-side scope.
- [[source-adyen-docs-issuing-3d-secure-troubleshooting]] — conflicting broad webhook statement for failures.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/issuing/3d-secure/oob-auth-sdk/authenticate-cardholders/2026-09-15|Authenticate cardholders using the Authentication SDK — 2026-09-15 capture]]
