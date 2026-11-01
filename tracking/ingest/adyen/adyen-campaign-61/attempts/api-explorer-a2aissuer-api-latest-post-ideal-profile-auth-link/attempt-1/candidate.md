---
title: "Adyen A2A Issuer API: iDEAL profile management link"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/a2aissuer-api/latest/post/ideal/profile/auth-link"
raw_files:
  - "adyen/api-explorer/a2aissuer-api/latest/post/ideal/profile/auth-link/2026-09-15.md"
tags: [adyen, business-accounts, ideal, a2a-issuer, api]
---

## Overview

A2A Issuer API v1 `POST /ideal/profile/auth-link` generates a redirect URL for managing an already registered iDEAL profile linked to the supplied account holder. It is a profile-management link operation, not an iDEAL payment authorization or payment result. The captured reference lists test and live balance-platform A2A Issuer API hosts. [[adyen]] [[adyen-business-accounts]]

## Key takeaways

- The request body requires `accountHolderId`. A 200 response marks `redirectUrl` optional, with `href` required within that object if it appears; the URL is described as short-lived. The reference states no validity duration. See raw lines 5–41.
- The 422 examples include `1069_008` for no registered iDEAL profile, `29_001` for missing or invalid data, and `30_012` for an account holder not found. These are examples, not an exhaustive error list. See raw lines 127–167.
- The 400 malformed-request and 500 server-error schemas use optional problem fields; `invalidFields` is optional but its item fields are required when present. The 500 examples include `1069_001` unexpected internal error and `1069_002` payment-method error. See raw lines 44–99 and 169–191.
- A returned management link or 200 response does not establish profile-management completion, iDEAL authentication, payment authorization, or funds movement.

## Detail locators

- Purpose, hosts and request body: raw lines 5–31.
- 200 response and optional-parent requiredness: raw lines 32–41; example raw lines 100–111.
- Error schemas: raw lines 44–99; examples raw lines 113–191.

## Related

- [[adyen-business-accounts]]

## Raw Sources

- [[raw/adyen/api-explorer/a2aissuer-api/latest/post/ideal/profile/auth-link/2026-09-15|A2A issuer profile auth-link snapshot]]
