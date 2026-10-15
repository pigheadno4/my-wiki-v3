---
title: "Adyen Classic API 3D Secure authentication overview"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication"
raw_files:
  - "adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/2026-09-15.md"
tags: [adyen, classic-api, 3d-secure, 3ds2, authentication, legacy]
---

## Overview

This Adyen Classic integration page surveys historical 3D Secure authentication routes for card-not-present payments. The page labels its endpoint **inactive** and no longer supported for new integrations: it directs new online-payment builds to Checkout API and existing Classic integrations to contact Adyen and migrate. Its metadata says last modified 2019-08-28, although the raw snapshot was captured 2026-09-15. See [[adyen]], [[adyen-3d-secure]] and [[adyen-online-payments]].

## Key takeaways

- The historical Classic choices are redirect authentication for 3D Secure 1 or 2, and native 3DS2 through web helpers or iOS/Android SDKs with a 3DS1 redirect path. The page describes redirect as issuer-version-dependent and says a native 3DS2 route may still be sent to the 3DS1 flow based on issuer performance. These are navigation and migration context for existing integrations, not a present-day implementation recommendation or evidence of current 3DS1 availability.
- For existing 3DS1 integrations, the page says a returned redirect URL can carry a 3DS2 transaction to an Adyen-hosted authentication page. Its integration table also lists period-specific legacy SDK/plugin versions and “do nothing” redirect support. Those historical claims do not establish current support, compatibility or merchant eligibility.
- The source's 2020/2021 prediction that 3DS2 would replace 3DS1, and its interim advice to handle both, are dated statements. Do not infer the present status of 3DS1 from them.
- 3D Secure is shopper authentication, separate from a payment authorization or capture. The page offers no transaction result or proof of PSD2 compliance or liability shift for a particular payment; its broad liability wording must be read with scheme-, region- and outcome-specific rules in [[adyen-3d-secure]].

## Detail locators

- Lines 19–24: inactive endpoint warning and new/existing integration routes.
- `## Understanding 3D Secure versions` (lines 33–40): dated 3DS1/3DS2 description and 2020/2021 forecast.
- `## Your 3D Secure implementation options` (lines 42–58): historical redirect and native-plus-redirect option links.
- `## Implementing 3D Secure 2 with your existing Adyen integration` (lines 60–83): redirect guidance and legacy integration/version table; treat “do nothing” rows as dated, not current instructions.
- Lines 85–93: navigation to PSD2 SCA and Classic API native 3DS2 guides.

## Related

- [[adyen-3d-secure]] — provider 3DS concept and reciprocal Classic source route.
- [[adyen-online-payments]] — Checkout API online-payments context.
- [[source-adyen-docs-online-payments-classic-integrations]] — Classic Ecommerce navigation and inactive scope.

## Raw Sources

- [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/2026-09-15|Classic 3D Secure authentication overview, captured 2026-09-15]]
