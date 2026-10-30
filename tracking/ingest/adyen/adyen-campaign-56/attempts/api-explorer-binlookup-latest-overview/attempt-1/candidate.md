---
title: "Adyen BinLookup API v54 overview"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/BinLookup/latest/overview"
raw_files:
  - "adyen/api-explorer/BinLookup/latest/overview/2026-09-15.md"
tags: [adyen, binlookup, online-payments, api-reference]
---

## Overview

This 2026-09-15 **BinLookup API v54** overview routes to BIN-based information about 3D Secure supported version and fee cost estimates. It is an [[adyen]] API reference linked to [[adyen-online-payments]]. The `latest` URL is a captured v54 snapshot, not proof of a later current version.

## Key takeaways

- Authentication needs an API credential. The page shows **alternative** API-key `X-API-Key` and username/password Basic authentication examples (raw lines 9–25); it does not require both methods together.
- Endpoint URLs carry a `vXX` version suffix. The captured test server is `https://pal-test.adyen.com/pal/servlet/BinLookup/v54` (lines 27–33, 45–46). Live authentication requires a credential from the live Customer Area, and the live URL uses a company-specific `{PREFIX}` found under **Developers > API URLs > Prefix** (lines 35–43). These instructions do not prove live access for a particular account.
- The table lists `POST /get3dsAvailability` and `POST /getCostEstimate` (lines 48–54). This overview gives method/path/summary navigation, not request or response schemas, eligibility, a guaranteed 3DS result, final charged fees, payment authorization, or settlement. Read the individual endpoint reference for those details.

## Detail locators

- Purpose, authentication alternatives, versioning and live setup: raw lines 5–43.
- Test server and complete endpoint table: raw lines 45–54.

## Related

- [[adyen-online-payments]] — provider integration context.
- [[adyen-api-access]] — credential and account-scope context.
- [[adyen-3d-secure]] — authentication context; this overview supplies only a lookup route.

## Raw Sources

- [[raw/adyen/api-explorer/BinLookup/latest/overview/2026-09-15|BinLookup API v54 overview, captured 2026-09-15]]
