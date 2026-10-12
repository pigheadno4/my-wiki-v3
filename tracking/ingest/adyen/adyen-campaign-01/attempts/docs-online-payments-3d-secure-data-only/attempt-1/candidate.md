---
title: "Adyen Docs: Data-only flow"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/3d-secure/data-only"
raw_files:
  - "adyen/docs/online-payments/3d-secure/data-only/2026-09-15.md"
tags: [adyen, 3d-secure, 3ds2, data-only, visa, mastercard, dcap]
---

## Overview

This [[adyen]] webpage snapshot describes a [[adyen-3d-secure|3D Secure 2]] data-only flow for Visa and Mastercard. Instead of sending an ordinary merchant authentication request, Adyen sends shopper data to the card scheme; the scheme handles the authentication request with the issuer and includes its risk evaluation in the authorization message for the issuer's decision. The guide positions the flow outside PSD2 SCA-regulated markets.

The flow does not present the shopper with a 3DS2 challenge and does not provide liability shift. The snapshot is implementation guidance, not proof of current merchant, market, scheme, transaction or issuer eligibility, successful authentication or authorization, interchange qualification, or production enablement.

## Key takeaways

- The documented prerequisite is a 3D Secure 2 integration for Web, Android, or iOS; Adyen recommends native 3DS2. For Authentication Engine routing, the guide says to configure native or redirect 3DS2 and set the default dynamic 3D Secure rule to **Prefer not**.
- For native or redirect integrations, the guide says the Authentication Engine decides whether to trigger data-only based on issuer readiness and performance uplift. This describes routing logic, not a guarantee that any transaction will use data-only or be authorized.
- An API-only integration, or a merchant intentionally forcing the flow, sends `additionalData.threeDS2DataOnly: true` in `/payments`; the guide limits that effect to transactions where data-only is possible. It recommends `allow3DS2: true` through Checkout API v68 and `nativeThreeDS: preferred` from v69.
- The general optimization list recommends shopper, address, holder-name and phone data. Visa DCAP has a stricter documented qualification list: `shopperIP`, `shopperEmail`, every billing-address field, and `deviceFingerprint`; empty, placeholder, missing or repeatedly incomplete data can lose the discount or lead to program removal.
- The DCAP section limits incentives to customer-initiated card-not-present Visa transactions and excludes merchant-initiated and in-person transactions. Adyen warns against applying data-only to every transaction because it can lower authorization rates with some issuers.

> [!warning] DCAP geography and snapshot timing
> The requirements table says DCAP applies to US and Canadian merchants, but the dedicated eligibility section says it was US-only and planned to expand to Canada in October 2026. Treat Canadian availability as unresolved within this 2026-09-15 snapshot and verify current eligibility rather than inferring that the planned expansion occurred.

## Detail locators

- **Purpose and scheme/issuer roles:** raw lines 17-19.
- **Integration, market and Authentication Engine setup requirements:** raw lines 21-28.
- **Scheme routing, authorization-message risk data, no challenge, and no liability shift:** raw lines 30-34.
- **Authentication Engine selection and recommended risk-assessment fields:** raw lines 36-55.
- **Forced data-only request and Checkout API-version settings:** raw lines 57-64.
- **Example request and response:** raw lines 66-120; examples do not establish a universal request contract or outcome.
- **Visa DCAP eligibility, exclusions, purpose, routing warning, required data and consequences:** raw lines 122-140.
- **Mastercard-only test availability and test card:** raw lines 142-148.

## Related

- [[adyen]]
- [[adyen-3d-secure]]
- [[source-adyen-docs-online-payments-3d-secure]] — high-level 3DS2 purpose, integration routes and flow shapes

## Raw Sources

- [[raw/adyen/docs/online-payments/3d-secure/data-only/2026-09-15|Adyen Docs — Data-only flow (2026-09-15)]]
