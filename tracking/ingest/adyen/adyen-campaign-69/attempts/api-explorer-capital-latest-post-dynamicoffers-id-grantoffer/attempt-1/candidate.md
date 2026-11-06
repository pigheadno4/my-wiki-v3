---
title: "Adyen Capital static offer from dynamic selection"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/capital/latest/post/dynamicOffers/(id)/grantOffer"
raw_files:
  - "adyen/api-explorer/capital/latest/post/dynamicOffers/(id)/grantOffer/2026-11-07.md"
tags: [adyen, capital, grant-offers, api-explorer]
---

## Overview

Captured Capital API v1 `POST /dynamicOffers/{id}/grantOffer` reference for creating a static offer from a financing amount selected by a user within a dynamic offer. This creates an offer, not a grant request or disbursement. See [[adyen]] and [[adyen-capital]].

## Key takeaways

- Required path `id` identifies the source dynamic offer. The request-body schema marks `amount` required, with required three-character ISO `currency` and integer `value` in minor units. The page does not state a separate body-required flag, financing-range validation rule, idempotency behavior or operation-specific API role.
- Both TEST and live Capital v1 servers are listed. Each environment has a stated limit of 30 requests per minute.
- A `200` success response describes the static offer. `accountHolderId` is required; offer `id`, payout `amount`, `contractType` (`loan` or `cashAdvance`), validity times, `fee`, and `repayment` are optional top-level fields. Required members under optional objects apply when those objects are present. The fee APR and repayment percentage use basis points; estimated term is in days, and maximum term applies only to loans.
- `200` does not establish user acceptance, eligibility, grant creation, disbursement, settlement, bank receipt or repayment. The documented failure is `422` request validation; its error-body top-level fields are optional and `invalidFields` members are required only when an entry is present.

## Detail locators

- Purpose and rate limit: raw lines 5–13.
- TEST/live Capital v1 servers: raw lines 15–21.
- Dynamic-offer path ID and selected-amount schema: raw lines 23–36.
- Success offer/term schema: raw lines 38–65.
- Validation error schema: raw lines 68–84.

## Related

- [[adyen-capital]] — Capital offers and grant lifecycle.
- [[adyen]] — provider index.

## Raw Sources

- [[raw/adyen/api-explorer/capital/latest/post/dynamicOffers/(id)/grantOffer/2026-11-07|Static offer from dynamic selection, captured 2026-11-07]]
