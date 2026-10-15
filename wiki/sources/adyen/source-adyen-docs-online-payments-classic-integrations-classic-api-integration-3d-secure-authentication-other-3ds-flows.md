---
title: "Adyen Classic API other 3D Secure flows"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/other-3ds-flows"
raw_files:
  - "adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/other-3ds-flows/2026-09-15.md"
tags: [adyen, online-payments, classic-api, 3d-secure, navigation]
---

## Overview

This 2026-09-15 snapshot is a short navigation page for alternative 3D Secure routes in an **existing Classic Payment API `/authorise` integration**. Adyen says it no longer accepts new Classic integrations and recommends moving both the payment integration and the other-3DS route to Checkout API. The page metadata says last modified in 2019. It identifies route purpose and a dated data-only scope; it is not an implementation specification or proof of current availability or payment outcome.

## Route distinctions

- **Full Adyen 3DS integration:** The page says Adyen performs authentication and proceeds with payment authorization. This is the contrast used to introduce the alternatives, not a transaction-success guarantee.
- **Authorize with 3DS MPI data:** The linked route uses a third-party 3D Secure provider and then submits the payment authorization request to Adyen. Third-party authentication data is distinct from an Adyen authorization response. The detailed field and result behavior belongs to [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-3d-secure-authentication-other-3ds-flows-authorize-mpidata]].
- **3DS2 data-only request:** The page labels a request made without requesting authentication, and says this Classic data-only flow is currently available only in Brazil for Mastercard. Its linked guide is needed for actual parameters and outcomes; this label does not establish card authentication or payment authorization.

## Evidence boundary

This page does not itself document an authentication-only implementation, payment-request fields, challenge or fingerprint steps, response codes, capture, liability shift, or success. Authentication-only is a separate Classic route described in [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-3d-secure-authentication-native-3ds2-authentication-only-integration]]. Do not infer its behavior from this landing page.

## Related

- [[adyen]]
- [[adyen-3d-secure]]
- [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-3d-secure-authentication-other-3ds-flows-authorize-mpidata]]
- [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-3d-secure-authentication-native-3ds2-authentication-only-integration]]

## Raw Sources

- [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/other-3ds-flows/2026-09-15|Adyen Classic other 3DS flows, 2026-09-15 snapshot]]
