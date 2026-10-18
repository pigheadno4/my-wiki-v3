---
title: "Register a device for SCA | Adyen Business Accounts"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/register-sca-devices"
raw_files:
  - "adyen/docs/business-accounts/register-sca-devices/2026-09-15.md"
tags: [adyen, business-accounts, sca, authentication-sdk, registered-devices]
---

## Overview

This [[adyen]] Business Accounts guide, last modified 2022-11-30 and captured 2026-09-15, describes registering a user's device for Strong Customer Authentication against a business-account payment instrument. It combines client Authentication SDK eligibility/registration with server Balance Platform `registeredDevices` initiation and finalization. The opening description names iOS and Android, while the procedure also includes a WebAuthn browser tab. See [[adyen-business-accounts]].

## Key takeaways

- Before registration, confirm the user's OS or browser supports SCA, install the Authentication SDK, give the API credential **Bank SCA Webservice Role**, and obtain the additional configuration from Adyen Support. The client eligibility check yields `sdkOutput`; the Web tab says unsupported browsers throw `SCA_UNAVAILABLE`. This dated guide does not establish current device or account eligibility. [Raw: lines 30–39, 41–129]
- Registration is a one-off procedure per device. The server POSTs `/registeredDevices` with the business account's `paymentInstrumentId` and client eligibility `strongCustomerAuthentication.sdkOutput`; the response supplies `sdkInput` and a device `id` beginning `BSDR` or `RD`. The optional device name is an identifying label. The page's sample API calls use TEST and are examples, not proof of registration. [Raw: lines 131–145, 147–162, 374–390]
- The platform performs two-factor authentication of the user, then the client SDK registers using the returned `sdkInput` and sends its resulting `sdkOutput` to the server. Android shows cancellation/error branches; iOS calls out Touch ID, Face ID or device passcode and the Face ID plist description; Web uses WebAuthn. The page does not define a separate consent or permission artifact. [Raw: lines 392–449]
- The server PATCHes `/registeredDevices/{id}` with the device ID, the same business-account `paymentInstrumentId` and SDK output, then checks for response `success: true`. Only after that response does the guide say registration is complete and the device ID connected to the payment instrument; the user can then authenticate for future operations involving it. The guide says a device cannot be registered more than once, but additional payment instruments can later be associated through the separate management flow. [Raw: lines 451–461, 690–694]

## Detail locators

- Purpose, sequence and requirements: pinned raw lines 15–39. Android, iOS and Web eligibility checks: lines 41–129.
- POST input and `sdkInput`/device-ID response: lines 131–145 and 374–390. Language-specific TEST examples: lines 147–372.
- 2FA and client SDK registration including cancellation/error branches: lines 392–449. Server PATCH and final success check: lines 451–461 and 690–694.
- Linked device management, transfer SCA and transaction-history SCA routes: lines 696–716.

## Related

- [[adyen-business-accounts]] — product and evidence boundary.
- [[source-adyen-docs-business-accounts-manage-sca-devices]] — subsequent device listing, payment-instrument association and deregistration.
- [[source-adyen-docs-business-accounts-sca-for-funds-transfers]] — separate operation authentication; registering a device does not authorize or settle a transfer.

## Raw Sources

- [[raw/adyen/docs/business-accounts/register-sca-devices/2026-09-15|Register a device for SCA — collected 2026-09-15]]
