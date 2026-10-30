---
title: "Adyen Disputes API v30 overview"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Disputes/latest/overview"
raw_files:
  - "adyen/api-explorer/Disputes/latest/overview/2026-09-15.md"
tags: [adyen, disputes-api, disputes, api-reference]
---

## Overview

This 2026-09-15 **Disputes API v30** overview describes automating dispute and chargeback handling with routes to retrieve applicable defense reasons, supply or delete defense documents, and accept or defend a dispute. It is an API directory within [[adyen]]'s [[adyen-risk-management]] documentation. The `latest` URL is a captured v30 snapshot, not proof of a later current version.

## Key takeaways

- Each Disputes API request needs an API key in `X-API-Key`. The page separately says live access needs newly generated web service user credentials (raw lines 9–18). The version suffix is `vXX`; the shown test server is `https://ca-test.adyen.com/ca/services/DisputeService/v30` (lines 20–29).
- The endpoint table lists five `POST` routes: `/acceptDispute`, `/defendDispute`, `/deleteDisputeDefenseDocument`, `/retrieveApplicableDefenseReasons`, and `/supplyDefenseDocument` (lines 31–40). These are operation names and navigation only: this overview gives no request/response schemas, case-state eligibility, document/deletion propagation, or dispute outcome. The individual endpoint references and workflow guide own those details.

## Detail locators

- Purpose, API-key and live-credential statements: raw lines 5–18.
- Versioning, test server, complete endpoint table: raw lines 20–40.

## Related

- [[adyen-risk-management]] — provider dispute context and linked workflow sources.

## Raw Sources

- [[raw/adyen/api-explorer/Disputes/latest/overview/2026-09-15|Disputes API v30 overview, captured 2026-09-15]]
