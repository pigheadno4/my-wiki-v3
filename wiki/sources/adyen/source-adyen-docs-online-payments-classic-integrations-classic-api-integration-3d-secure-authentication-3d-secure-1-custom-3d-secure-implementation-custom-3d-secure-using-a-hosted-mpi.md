---
title: "Adyen Docs: Classic 3D Secure 1 with a hosted MPI"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/3d-secure-1/custom-3d-secure-implementation/custom-3d-secure-using-a-hosted-mpi"
raw_files:
  - "adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/3d-secure-1/custom-3d-secure-implementation/custom-3d-secure-using-a-hosted-mpi/2026-09-15.md"
tags: [adyen, classic-api, 3d-secure-1, hosted-mpi, historical]
---

## Overview

This [[adyen|Adyen]] guide describes a custom hosted-MPI 3D Secure 1 redirect within the Classic API `/authorise` integration. Its metadata says last modified 2020-05-01; the raw snapshot was fetched 2026-09-15. Adyen says it no longer develops the Classic API integration and no longer accepts new integrations with it, and recommends migrating to Checkout API's authorisation-only MPI-data flow. This is historical implementation evidence under [[adyen-3d-secure]], not a claim that the legacy route or a scheme's 3DS1 service remains available today.

## Key takeaways

- In the documented SOAP Classic flow, the merchant first calls `/authorise` with a `returnUrl`, shopper IP, and browser user-agent and accept-header data. The return URL is limited to 1024 characters; the guide warns against GET parameters on it. The SOAP request and response are explicitly examples to generate with a toolkit, not production credentials or current API acceptance proof.
- A `Refused` initial `resultCode`, such as a Risk refusal, is handled as an ordinary payment response. For `RedirectShopper`, the response supplies `issuerUrl`, `pspReference`, `md`, and MPI-prefixed redirect fields in `additionalData`. The merchant retains the returned `md` for `/authorise3d`; `RedirectShopper` is a redirect instruction, not successful authentication or authorization.
- The merchant POSTs all fields matching `mpiImplementationType` to `issuerUrl`, removing the prefix from their form-field names. The guide illustrates an auto-submitting form with a non-JavaScript submit fallback.
- Following issuer authentication, the shopper returns by POST to the original `returnUrl`. The merchant then calls `/authorise3d`, using the same merchant account as the initial call, browser and shopper-IP data, the saved `md`, and MPI-prefixed response data. The final SOAP response shown with `Authorised` is an example, not evidence of any actual payment outcome or a guarantee of authorization.
- The migration recommendation links to Checkout API authorisation-only MPI data, but this page does not provide its implementation contract. Do not combine these Classic SOAP steps with that newer flow.

## Detail locators

- **Classic status and migration warning** — raw lines 14–20.
- **Initial `/authorise` request, return URL and SOAP example** — raw lines 22–129.
- **Initial refusal/redirect fields and saved `md`** — raw lines 131–143.
- **MPI field selection and issuer redirect form** — raw lines 145–217.
- **Issuer POST return, `/authorise3d` inputs and example result** — raw lines 219–318.

## Related

- Company: [[adyen]]
- Main concept: [[adyen-3d-secure]]
- Related source: [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-3d-secure-authentication-3d-secure-1]]

## Raw Sources

- [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/3d-secure-1/custom-3d-secure-implementation/custom-3d-secure-using-a-hosted-mpi/2026-09-15|Adyen Docs — Classic custom 3D Secure with hosted MPI (2026-09-15)]]
