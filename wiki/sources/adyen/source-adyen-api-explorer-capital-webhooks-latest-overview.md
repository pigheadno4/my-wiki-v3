---
title: "Adyen Capital webhooks v1 overview"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/capital-webhooks/latest/overview"
raw_files:
  - "adyen/api-explorer/capital-webhooks/latest/overview/2026-09-15.md"
tags: [adyen, capital, webhooks, financing]
---

## Overview

This 2026-09-15-captured API Explorer overview labels the family **Capital webhooks v1**. Adyen says these events notify a system when financing offers or grants are created or updated. The page catalogs four incoming POST event routes; it does not supply their payload schemas or prove a particular offer, grant or disbursement. The `latest` route is not independent current-version proof. See [[adyen]], [[adyen-capital]] and [[adyen-webhooks]].

## Key takeaways

- The catalog separates static-offer creation (`balancePlatform.balanceAccountHolder.capitalOffer.created`), dynamic-offer creation (`balancePlatform.capital.dynamicOffer.created`), grant creation (`balancePlatform.grants.created`) and grant update (`balancePlatform.grants.updated`). These are event names and summaries, not a single state transition or four claims about one financing case.
- The overview suggests using webhook data in a user-facing business-financing dashboard. It does not define field requirements, offer acceptance, grant status, funding-transfer stages, disbursement to a balance account or bank, repayment, or delivery mechanics. Offer and grant notifications are separate from fund-movement evidence.

## Detail locators

- Captured family/version, purpose and dashboard example: pinned raw lines 5–9.
- Four incoming event routes: `## Endpoints > ### General`, lines 11–19.

## Related

- [[source-adyen-docs-capital-webhook-types]] — separate Capital webhook taxonomy and transfer/transaction evidence routes.

## Related raw API references

- [[raw/adyen/api-explorer/capital-webhooks/latest/post/balancePlatform.balanceAccountHolder.capitalOffer.created/2026-09-15|Static-offer created reference]] — navigation only.
- [[raw/adyen/api-explorer/capital-webhooks/latest/post/balancePlatform.capital.dynamicOffer.created/2026-09-15|Dynamic-offer created reference]] — navigation only.
- [[raw/adyen/api-explorer/capital-webhooks/latest/post/balancePlatform.grants.created/2026-09-15|Grant-created reference]] — navigation only.
- [[raw/adyen/api-explorer/capital-webhooks/latest/post/balancePlatform.grants.updated/2026-09-15|Grant-updated reference]] — navigation only.

## Raw Sources

- [[raw/adyen/api-explorer/capital-webhooks/latest/overview/2026-09-15|Capital webhooks v1 overview snapshot]]
