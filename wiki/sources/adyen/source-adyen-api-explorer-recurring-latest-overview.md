---
title: "Adyen Recurring API overview (captured v68)"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Recurring/latest/overview"
raw_files:
  - "adyen/api-explorer/Recurring/latest/overview/2026-09-15.md"
tags: [adyen, recurring-api, tokenization, api-reference]
---

## Overview

This captured [[adyen]] Recurring API v68 overview calls the API a legacy route for managing and removing stored payment details or tokens, recommends Checkout API recurring endpoints when possible, and says tokens should be created with validation during a payment request. This is an API directory and authentication/versioning overview, not an individual endpoint contract. See [[adyen-tokenization]].

## Key takeaways

- The overview requires an API credential, illustrating `X-API-Key` and basic authentication alternatives. It shows version suffixes such as `v68`, a test server at `https://pal-test.adyen.com/pal/servlet/Recurring/v68`, and a separate live URL pattern with a company-specific prefix and live Customer Area credential. The `latest` URL is not proof of a newer/current API version or account access.
- Its endpoint directory lists `POST /createPermit`, `/disable`, `/disablePermit`, `/listRecurringDetails`, `/notifyShopper`, and `/scheduleAccountUpdater`. Those labels are navigation only: this overview contains no individual request/response schemas or outcome guarantees. Do not transfer Checkout token-creation or payment contract fields to these legacy Recurring endpoints.
- The page does not describe a payment authorisation, capture, settlement, token disable propagation, or error response. Consult each endpoint's own pinned reference for its actual contract.

## Detail locators

- Legacy purpose and Checkout preference: raw lines 5–11. Authentication and versioning: lines 13–37.
- Live URL pattern, server and endpoint directory: raw lines 67–90.

## Related raw API references

- `Recurring/latest/post/createPermit`, `/disable`, `/disablePermit`, `/listRecurringDetails`, `/notifyShopper`, and `/scheduleAccountUpdater` are directory entries here; use their own source captures for behavior.

## Raw Sources

- [[raw/adyen/api-explorer/Recurring/latest/overview/2026-09-15|Recurring API Explorer overview capture]]
