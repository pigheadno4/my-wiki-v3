---
title: "Adyen A2A payments API v1 — issuer overview"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/a2aissuer-api/latest/overview"
raw_files:
  - "adyen/api-explorer/a2aissuer-api/latest/overview/2026-09-15.md"
tags: [adyen, business-accounts, a2a, issuer-api]
---

## Overview

This 2026-09-15 API Explorer snapshot describes Account-to-Account (A2A) payments API v1. It enables issuers to facilitate direct payments through Adyen for users with an Adyen Business account. The listed routes concern the issuer-side A2A flow, not a merchant checkout payment API or proof of a completed transfer. See [[adyen]] and [[adyen-business-accounts]].

## Key takeaways

- The overview says the API can retrieve payment transaction information, confirm payments with Strong Customer Authentication (SCA), and cancel pending transactions. Its endpoint catalog also lists iDEAL profile manage, authenticate and register POST routes. These are route summaries; request and response contracts belong to the individual endpoint pages.
- Each request uses an API key in `X-API-Key`. The API credential must have the `Role for A2A Issuer payments - API` role; the page directs readers to an Adyen contact to set up roles. For live use, it says to generate a key in the live Customer Area. The overview does not establish that a particular credential has the role or that a user has completed SCA.
- The page lists separate test and live `/a2aissuer-api/v1` server bases. Its live-use prose gives a `v{version}/payments` URL pattern, while the server section pins v1; consult the specific endpoint for exact path and operation behavior. Listing a confirm or cancel route does not establish an authorization decision, reversal or funds movement.

## Detail locators

- API identity, issuer and Business-account scope, and three payment capabilities: raw lines 5–15. API-key header, role and live-key instruction: raw lines 17–38.
- Test/live server bases and six POST route names: raw lines 40–58. This overview contains no endpoint request/response schema, error table or execution example beyond the API-key header snippet.

## Related

- [[adyen]] — provider context.
- [[adyen-business-accounts]] — Business-account context for the issuer flow.
- [[source-adyen-docs-business-accounts-send-funds-ideal-integration]] — separate issuer integration guide; this overview does not establish its flow details.

## Raw Sources

- [[raw/adyen/api-explorer/a2aissuer-api/latest/overview/2026-09-15|Adyen A2A payments API v1 overview, captured 2026-09-15]]
