---
title: "Adyen Classic raw 3D Secure responses"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/raw-3d-secure-responses"
raw_files:
  - "adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/raw-3d-secure-responses/2026-09-15.md"
tags: [adyen, classic-api, 3d-secure, 3ds1, 3ds2, authentication-status]
---

## Overview

This Classic 3D Secure lookup page explains raw authentication responses shown in Adyen Customer Area. It separates **3DS requested** from **3DS challenged**, and maps 3DS1 `threeDOfferedResponse`/`threeDAuthenticatedResponse` separately from 3DS2 `threeDS2Result.transStatus`. The raw page was captured 2026-09-15 and says last modified 2021-01-27. See [[adyen]] and [[adyen-3d-secure]].

## Key takeaways

- For **3DS requested / 3DS1**, `threeDOfferedResponse` reports enrollment or whether 3DS was offered: `Y` means **Enrolled**, `U` authentication unavailable, `N` not enrolled, and `N/A` unable to verify. A requested-stage `Y` is **not** a completed-authentication result.
- For **3DS requested / 3DS2**, the page maps `threeDS2Result.transStatus` when `ChallengeShopper` was **not** returned. The table labels `Y` frictionless, `U` could not be performed, `N` not authenticated, `A` attempted, `C` challenge, `D` decoupled challenge, `R` rejected, and `I` data only. Read the full table at the raw locator; these labels do not by themselves establish final payment status.
- For **3DS challenged / 3DS1**, `threeDAuthenticatedResponse` reports authentication outcome: `Y` authenticated, `U` issuer unable to respond, `A` attempted, `N` failed, and `N/A` unable to verify. This is a different field and stage from the requested-stage enrollment result.
- For **3DS challenged / 3DS2**, `threeDS2Result.transStatus` is shown for cases where `ChallengeShopper` **was** returned. Here the table labels `Y` successful, `U` could not be performed, `N` not authenticated, `A` attempted and `R` rejected.
- These are dated raw **authentication** status descriptions in a Classic integration context. They do not establish payment authorization, capture, settlement, PSD2 compliance or transaction-specific liability shift. The page does not provide API request steps, lifecycle guarantees or evidence of current 3DS1 availability.

## Detail locators

- Lines 19–32: Customer Area route and requested-stage 3DS1 `threeDOfferedResponse` table.
- Lines 34–47: requested-stage 3DS2 `threeDS2Result.transStatus` table without `ChallengeShopper`.
- Lines 49–61: challenged-stage 3DS1 `threeDAuthenticatedResponse` table.
- Lines 63–73: challenged-stage 3DS2 `threeDS2Result.transStatus` table with `ChallengeShopper`.

## Related

- [[adyen-3d-secure]] — provider 3DS concept and reciprocal Classic source route.
- [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-3d-secure-authentication]] — inactive Classic 3DS navigation and migration context.

## Raw Sources

- [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/raw-3d-secure-responses/2026-09-15|Raw 3D Secure responses, captured 2026-09-15]]
