---
title: "Adyen Balance Platform API v2: Update an account holder"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/accountHolders/(id)"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/patch/accountHolders/(id)/2026-11-02.md"
tags: [adyen, platforms, balance-platform, account-holders, api-reference]
---

## Overview

Captured Balance Platform API v2 TEST-server reference for `PATCH /accountHolders/{id}`. It updates the account holder identified by the required path `id`; omitted request parameters ordinarily remain unchanged. This is an account-holder resource operation for [[adyen]] and [[adyen-platforms]], not a payment or payout operation.

## Key takeaways

- The listed server is `https://balanceplatform-api-test.adyen.com/bcl/v2`. The request body's `balancePlatform` is optional in the table but required when the API credential can access multiple balance platforms. The response identifies the account holder with `id` and its associated legal entity with `legalEntityId`; these are different resources.
- Optional update fields include `capabilities`, `contactDetails`, `description`, `metadata`, `primaryBalanceAccount`, `reference`, `status`, and `timeZone`. If `contactDetails` is supplied, its nested address, email and phone are marked required in the schema; US/Canada `stateOrProvince` is conditionally required in prose. `timeZone` defaults to the balance platform's time zone when unset.
- Metadata is an exception to the ordinary omission rule: when updating metadata, omitted existing key-value pairs are deleted. The first created balance account is the default `primaryBalanceAccount`; this PATCH can assign a different one.
- Capability `requested` is a request, not permission. Check returned `allowed`; `enabled: false` temporarily disables a capability, and returned `verificationStatus` can be pending, invalid, valid or rejected. A 200 response means the update request succeeded, not that requested capability verification completed or a payment occurred.
- `active` is the initial holder status; `suspended` temporarily disables the holder and blocks payouts; `closed` permanently disables the holder and its capabilities and cannot be changed. The raw response also describes verification deadlines that can disallow capabilities if errors remain unresolved.

## Detail locators

- Operation, TEST base URL, path and request fields: pinned raw lines 5–46. Capability levels and nested contact-field requirements: lines 24–40.
- Request examples: lines 48–68. Response fields and verification states: lines 69–133. The capability-request example returns `requested: true`, `allowed: false`, `verificationStatus: pending` (lines 239–257), illustrating their separation.
- Success and error schemas: lines 71–233; 400/401/403/422/500 examples: lines 271–335. The generic 422 and 500 examples refer to a payment instrument, so they do not establish account-holder-specific validation or recovery behavior.

## Related

- [[adyen-platforms]] — platform account-holder and resource context.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/patch/accountHolders/(id)/2026-11-02|Pinned 2026-11-02 API reference]]
