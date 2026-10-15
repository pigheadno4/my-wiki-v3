---
title: "Adyen Classic API authorization with third-party 3D Secure data"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/other-3ds-flows/authorize-mpidata"
raw_files:
  - "adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/other-3ds-flows/authorize-mpidata/2026-09-15.md"
tags: [adyen, 3d-secure, 3ds2, classic-api, mpi-data, authorization]
---

## Overview

This Adyen Classic Payment API guide describes submitting a payment authorization to Adyen using 3D Secure authentication data obtained from a third-party provider. The merchant obtains the authentication result first, maps it to the documented fields, then sends a separate Classic `/authorise` request carrying `mpiData`. The page covers 3D Secure 2 and also includes 3D Secure 1 field and request tabs. A third-party authentication result is input to authorization; it does not establish that Adyen authorized or captured the payment.

Adyen says it no longer develops or accepts new Classic API (`/authorise`) integrations and recommends a Checkout API authorization-only route. The raw page reports `last_modified: 2024-06-19` and was captured 2026-09-15. Its API and library examples are dated snapshot evidence, not current schema or successful live-payment proof.

## Key takeaways

- Before using this route, the page directs the merchant to create an Adyen test account, obtain an API key, and install a library for connecting to Adyen APIs. See **Before you begin**.
- The merchant must have authentication data from the external 3DS provider. The guide points to Adyen-to-EMVCo mapping for non-Adyen authentication and separates the 3DS1 and 3DS2 fields; its **Applies to** tables distinguish common 3DS2 fields from Cartes Bancaires additions. See **Get authentication data**.
- The merchant sends POST `/authorise` with the relevant 3DS authentication values in the documented request fields, including `mpiData`. The 3DS2 table includes common issuer fields and additional Cartes Bancaires request data; use the exact table and intended Classic API version when implementing. See **Send a payment authorisation request with 3D Secure authentication data**.
- For a co-badged card, `selectedBrand` must name the scheme that performed authentication; a mismatch can cause refusal. See **Co-badged cards**.
- `Authorised` is the response only if Adyen's later payment authorization succeeds. Other result codes require their own follow-up; the illustrated response, including `liabilityShift`, is not a guarantee for another transaction. See **Sample response**.

## Detail locators

- **Get authentication data** — 3DS1 and 3DS2 result-field tables, all-issuer versus Cartes Bancaires applicability, and external-provider parameter mapping route.
- **Send a payment authorisation request with 3D Secure authentication data** — Classic `/authorise` field tables. The 3DS2 table labels `dsTransID` without the `mpiData.` prefix while linking to an `mpiData` parameter; the examples place it inside `mpiData`. Verify the intended Classic API schema rather than treating the table label alone as a top-level field.
- **Co-badged cards** — `selectedBrand` must match the authenticating scheme, or authorization may be refused.
- **Sample request** — 3DS1 and 3DS2 curl and language examples, including scheme-specific Cartes Bancaires illustration; the example values do not define universal request obligations.
- **Sample response** — conditional `Authorised` result and route to other result codes.

## Related

- [[adyen]]
- [[adyen-3d-secure]]
- [[source-adyen-docs-online-payments-3d-secure-authorize-mpidata]] — Checkout API third-party authentication and authorization guide.
- [[co-badged-cards]]

## Raw Sources

- [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/other-3ds-flows/authorize-mpidata/2026-09-15|Classic API authorization with third-party 3DS data (2026-09-15 snapshot)]]
