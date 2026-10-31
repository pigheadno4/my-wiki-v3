---
title: "Adyen Capital webhook: static offer created for account holder"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/capital-webhooks/latest/post/balancePlatform.balanceAccountHolder.capitalOffer.created"
raw_files:
  - "adyen/api-explorer/capital-webhooks/latest/post/balancePlatform.balanceAccountHolder.capitalOffer.created/2026-09-15.md"
tags: [adyen, capital, webhooks, static-offers]
---

## Overview

This captured Capital Webhooks API Explorer POST reference describes Adyen's incoming `balancePlatform.balanceAccountHolder.capitalOffer.created` event, which provides details of a newly created static offer for an account holder. It is an offer notification, not a grant request, acceptance, disbursement, or repayment event. The `latest` route label gives no numbered webhook API version. See [[adyen-capital]], [[adyen-webhooks]], and [[adyen]].

## Key takeaways

- The request-body table marks `accountHolderId` required and describes it as the holder to whom a grant is offered. The static offer `id`, offered `amount`, `contractType` (`loan` or `cashAdvance`), validity dates, `fee`, and `repayment` configuration are marked optional. This captured page does not show a `type` or `environment` envelope field or a request example; do not import fields from other Capital webhook references.
- The optional `amount` is what *would* be paid out for business financing, with required currency and minor-unit integer value if supplied. An optional `fee` contains a required amount object when present and may include APR basis points. Optional `repayment` has required `basisPoints` when present, optional term with required estimated days if present, and a loan-only maximum-days description. Its optional threshold has a required amount object when present; the captured table does not expand that nested amount into currency/value fields.
- Offer creation alone does not establish current holder eligibility, offer acceptance, signed terms, a grant or transfer, credited funds, bank receipt, or repayment. The response section says any HTTP `2xx` accepts the webhook and `notificationResponse` is optional. It gives no delivery order, retry, deduplication, signature, or downstream funding status rule.

## Detail locators

- Static-offer event purpose: pinned raw lines 5–7.
- Required holder identity, optional offer terms and nested conditional fields: pinned raw lines 11–33.
- Acknowledgment response: pinned raw lines 35–43.

## Related

- [[adyen-capital]] — Capital offer and grant context.
- [[adyen-webhooks]] — webhook event and receipt context.
- [[source-adyen-docs-capital-webhook-types-capital-webhooks]] — separate Capital event-family guidance.
- [[source-adyen-api-explorer-transfers-latest-post-grants]] — separate grant-request reference.

## Raw Sources

- [[raw/adyen/api-explorer/capital-webhooks/latest/post/balancePlatform.balanceAccountHolder.capitalOffer.created/2026-09-15|Static Capital offer created webhook reference, captured 2026-09-15]]
