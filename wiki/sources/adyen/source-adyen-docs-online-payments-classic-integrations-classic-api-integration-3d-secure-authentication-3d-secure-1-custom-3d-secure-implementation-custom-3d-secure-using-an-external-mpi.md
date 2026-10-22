---
title: "Adyen Docs: Classic 3D Secure 1 with an external MPI"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/3d-secure-1/custom-3d-secure-implementation/custom-3d-secure-using-an-external-mpi"
raw_files:
  - "adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/3d-secure-1/custom-3d-secure-implementation/custom-3d-secure-using-an-external-mpi/2026-09-15.md"
tags: [adyen, classic-api, 3d-secure-1, external-mpi, historical]
---

## Overview

This 2026-09-15 [[adyen|Adyen]] page describes using data retrieved from an external merchant plug-in (MPI) in a Classic API SOAP `/authorise` request for a custom 3D Secure 1 integration. It is an authorization request carrying external MPI data, rather than a guide to perform issuer authentication through Adyen. Adyen says it no longer develops Classic API integrations or accepts new ones and recommends migrating to Checkout API's authorisation-only MPI-data flow. Under [[adyen-3d-secure]], this page is historical Classic-route evidence, not proof of current 3DS1 availability.

## Key takeaways

- The merchant sends a Classic SOAP `/authorise` request using the normal payment service URL, WSDL, username and password. The custom 3DS fields are `shopperIP`, `browserInfo.userAgent`, `browserInfo.acceptHeader`, and `mpiData` retrieved from the external MPI. The example `mpiData` contains directory and authentication responses, CAVV, XID, ECI and CAVV algorithm; those sample values are not evidence of a real authentication result.
- The page says `acquirerCode` and `authorisationMid` are supplied by support and must be passed in `additionalData`. Their purpose is to keep authorization on the same acquirer and merchant ID that the external MPI used, instead of allowing Adyen's default dynamic acquirer routing to choose a different one. This is a material matching condition, not an optional example embellishment.
- The page's SOAP request and `Authorised` response are examples. They show where the external authentication data and routing identifiers go, but do not establish that any merchant's external authentication is valid, that authorization will succeed, or that a card payment was captured or settled.
- The linked Checkout API authorisation-only flow is a migration route, not the contract for this Classic SOAP request. This page states no current scheme support, Classic endpoint version, or universal 3DS1 eligibility; verify any present-day implementation against its own current route.

## Detail locators

- **Classic status and migration warning** — raw lines 14–20.
- **SOAP authorization, external MPI data and acquirer/MID match** — raw lines 22–35.
- **Illustrative request payload and MPI fields** — raw lines 37–86.
- **Illustrative response, including `Authorised`** — raw lines 88–136.

## Related

- Company: [[adyen]]
- Main concept: [[adyen-3d-secure]]
- Related source: [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-3d-secure-authentication-other-3ds-flows-authorize-mpidata]]

## Raw Sources

- [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/3d-secure-1/custom-3d-secure-implementation/custom-3d-secure-using-an-external-mpi/2026-09-15|Adyen Docs — Classic external-MPI 3D Secure 1 (2026-09-15)]]
