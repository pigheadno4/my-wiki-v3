---
title: "Manage devices registered for SCA | Adyen Business accounts"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/manage-sca-devices"
raw_files:
  - "adyen/docs/business-accounts/manage-sca-devices/2026-09-15.md"
tags: [adyen, business-accounts, sca, registered-devices, payment-instruments]
---

## Overview

This 2022-11-30-modified Business Accounts guide, captured 2026-09-15, explains how to list registered SCA devices, associate further payment instruments with a device, and deregister a device from a particular business account. It assumes prior device registration and requires the Bank SCA Webservice Role on the API credential. It describes Configuration API and Authentication SDK steps, not current eligibility or a completed authentication for any user. See [[adyen]], [[adyen-business-accounts]] and [[source-adyen-docs-business-accounts-manage-access]].

## Key takeaways

- **List:** GET /registeredDevices uses a required paymentInstrumentId to list SCA devices for the specified business account, with pageSize and zero-based pageNumber options. The response identifies the registered device, name, associated payment instrument ID and type; the table includes ios, android and browser, despite the page's mobile-device description.
- **Associate:** After registration, the server POSTs /registeredDevices/{deviceId}/associations with up to five payment instrument IDs in one request. A payment instrument can be linked to only one device. Pass the returned sdkInput to the client Authentication SDK; after a user challenge, send its sdkOutput to the server and PATCH the same device ID with the same instrument IDs and type PaymentInstrument. A successful PATCH returns instrument IDs; the guide directs a subsequent GET for each instrument to verify association.
- **Failures and lifecycle:** The documented 422 'Device limit reached' case means at least one requested payment instrument is already linked to a device; the guide says to inspect and deregister existing links before retrying. A 422 'Challenge not found' usually indicates a client-device/challenge versus PATCH device-ID mismatch or sdkOutput from the wrong device. Client authenticate() cancellation can yield NotAllowedError; the guide allows retry with the same sdkInput in the same session.
- **Deregister:** DELETE /registeredDevices/{id} takes the device ID and required paymentInstrumentId to remove that device's association with the specified business account. For a device associated with multiple business accounts, the guide requires a separate request per account; a 204 empty response indicates success. This is a consequential removal of an authentication association, so confirm the intended account/device pairing before invoking it.

## Detail locators

- Scope, prerequisite role and list parameters: pinned raw lines 15–45; list response fields and sample: lines 222–258. The GET section's language-specific SDK snippets at lines 58–220 instead invoke initiateRegistrationOfScaDevice, so use its GET prose/curl rather than those snippets for this operation.
- Association limit and POST initiation: pinned raw lines 260–287; sdkInput/client authentication and server PATCH: lines 474–579; PATCH success and verification: lines 817–833.
- Association errors and retry guidance: pinned raw lines 835–902.
- Deregistration purpose, account-by-account scope, required path/query parameters and 204 response: pinned raw lines 904–1075. The curl header at lines 930–932 appears malformed; it is not a safe copy/paste template.

## Related

- [[adyen-business-accounts]] — Business Accounts concept and reciprocal source route.
- [[source-adyen-docs-business-accounts-manage-access]] — API credential role context.

## Raw Sources

- [[raw/adyen/docs/business-accounts/manage-sca-devices/2026-09-15|Manage SCA devices guide, captured 2026-09-15]]
