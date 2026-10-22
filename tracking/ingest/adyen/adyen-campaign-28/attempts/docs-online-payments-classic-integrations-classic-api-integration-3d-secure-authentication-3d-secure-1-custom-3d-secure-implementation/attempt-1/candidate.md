---
title: "Adyen Docs: Classic custom 3D Secure 1 integration routes"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/3d-secure-1/custom-3d-secure-implementation"
raw_files:
  - "adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/3d-secure-1/custom-3d-secure-implementation/2026-09-15.md"
tags: [adyen, classic-api, 3d-secure-1, mpi, historical]
---

## Overview

This [[adyen|Adyen]] Classic API page is a route chooser for custom 3D Secure 1 payments using either an external merchant plug-in (MPI), owned by the merchant or another processor, or an acquirer-hosted/non-standard MPI. It describes authorization routes, not the issuer authentication steps or a completed payment. The page was last modified 2019-06-12 and captured 2026-09-15. It belongs under [[adyen-3d-secure]] as historical guidance.

## Key takeaways

- Adyen says it no longer develops the Classic API `/authorise` integration and no longer accepts new integrations with it. It recommends migration to Checkout API's authorisation-only MPI-data route, which has its own implementation contract.
- The page warns that, depending on the integration, processing 3D Secure payments through the Adyen API may not be possible. It routes readers to SOAP API guidance for either an external MPI or an acquirer using a hosted/non-standard MPI. These are distinct branches; this overview does not supply the request fields, redirect steps, or result semantics for either.
- The document says its guidance is provided for testing purposes and may change. Neither the route list nor its dated snapshot establishes current 3DS1 or scheme availability, successful authentication, authorization, capture, or settlement.

## Detail locators

- **Classic scope and migration** — raw lines 14–20.
- **Chooser purpose and testing caveat** — raw lines 22–28.
- **External and hosted/non-standard MPI routes** — raw lines 29–31.

## Related

- Company: [[adyen]]
- Main concept: [[adyen-3d-secure]]
- External MPI guide: [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-3d-secure-authentication-3d-secure-1-custom-3d-secure-implementation-custom-3d-secure-using-an-external-mpi]]
- Hosted MPI guide: [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-3d-secure-authentication-3d-secure-1-custom-3d-secure-implementation-custom-3d-secure-using-a-hosted-mpi]]

## Raw Sources

- [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/3d-secure-1/custom-3d-secure-implementation/2026-09-15|Adyen Docs — Classic custom 3D Secure implementation (2026-09-15)]]
