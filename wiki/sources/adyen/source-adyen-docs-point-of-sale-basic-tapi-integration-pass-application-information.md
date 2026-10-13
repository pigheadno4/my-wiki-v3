---
title: "Pass POS application information | Adyen Docs"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/basic-tapi-integration/pass-application-information"
raw_files:
  - "adyen/docs/point-of-sale/basic-tapi-integration/pass-application-information/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, application-info, metadata]
---

## Overview

This Adyen guide describes adding platform, POS application, and merchant-device OS details to Terminal API payment requests so Adyen can analyze and troubleshoot them. The 2026-09-15 snapshot documents request metadata, not a credential, a Checkout API request, a terminal hardware inventory, an SDK release contract, or proof that a payment was processed successfully.

## Key takeaways

- In the `applicationInfo` object, the guide marks `externalPlatform.name`, `externalPlatform.integrator`, `merchantApplication.name`, `merchantDevice.os`, and `merchantDevice.osVersion` required. `externalPlatform.version` and `merchantApplication.version` are required only if the relevant platform or app has versions. The integrator identifies the company that built the POS application or service partner that built the integration. These are merchant-supplied names/version labels, not authoritative runtime attestation.
- Field values may be up to 40 characters, start with a letter or number, and contain letters, digits, dashes, underscores or spaces. The page requires consistent formatting across requests. Its example platform, app, OS, and version strings are illustrative, not a prescribed merchant configuration.
- Put the metadata in `PaymentRequest.SaleData.SaleToAcquirerData` as either Base64-encoded JSON containing `applicationInfo` or form-encoded `applicationInfo.*` key-value pairs separated with `&`. The same `SaleToAcquirerData` field can carry other data elements. The payment-request examples also have `SaleID`, `ServiceID`, `POIID` and `SaleTransactionID`; those identify POS component, attempt, terminal and transaction, and are not `applicationInfo` fields.
- The chosen `SaleToAcquirerData` format determines whether the example payment response's `AdditionalResponse` is Base64 JSON or key-value pairs. The guide says to contact Adyen Support to always receive `AdditionalResponse` in one of those formats. The illustrated successful `PaymentResponse` is an example, not runtime, authorization, capture or settlement proof for a merchant.
- The page says a built Terminal API integration has no additional requirements, limitations or preparations for this metadata. It does not define a new API key, Management API configuration, Checkout API `/payments` field, terminal hardware model field, or account-specific permission.

## Detail locators

- `Requirements` — Terminal API integration scope and absence of additional preparations.
- `Application information fields` and `Field value requirements` — exact required versus conditional fields, meanings, length/character rules, and consistency.
- `Add application info to your request` > `Option 1: Base64-encoded JSON` — object shape, encoding, `SaleToAcquirerData` placement, and sample `AdditionalResponse`.
- `Add application info to your request` > `Option 2: Key-value pairs` — flattened field names, ampersand separation, request placement and response format.
- `Combining application info and other data elements` — coexistence with other `SaleToAcquirerData` payload elements.

## Related

- Company: [[adyen]]
- Concept: [[adyen-terminal-api]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/basic-tapi-integration/pass-application-information/2026-09-15|2026-09-15 Adyen application-information guide]]
