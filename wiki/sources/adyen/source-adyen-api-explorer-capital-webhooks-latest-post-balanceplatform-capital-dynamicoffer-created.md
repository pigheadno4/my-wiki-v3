---
title: "Capital dynamic offer created webhook | Adyen API Explorer"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/capital-webhooks/latest/post/balancePlatform.capital.dynamicOffer.created"
raw_files:
  - "adyen/api-explorer/capital-webhooks/latest/post/balancePlatform.capital.dynamicOffer.created/2026-09-15.md"
tags: [adyen, capital, webhooks, dynamic-offers, business-financing]
---

## Overview

This captured Adyen Capital webhook POST reference says Adyen sends `balancePlatform.capital.dynamicOffer.created` to provide details of a dynamic offer created for an account holder. It is an offer event, not a grant request, accepted financing agreement, disbursement or booked funding. The `latest` route does not resolve a numbered webhook API version in this capture. [[adyen]] [[adyen-capital]] [[adyen-webhooks]]

## Key takeaways

- The request-body table places required fields directly at its top level: `accountHolderId`, `contractType` (`loan` or `cashAdvance`), `expiresAt`, `financingType` (listed as `businessFinancing`), dynamic-offer `id`, `maximumAmount`, `minimumAmount`, `repayment`, and `startsAt`. Each amount object requires `currency` and integer `value` in minor units. The page does not show an enclosing `data` object, `type`, `environment`, or example payload; do not import an envelope from another Capital webhook page. [Raw: Request body, lines 11–29]
- `accountHolderId` identifies the intended holder and `id` the dynamic offer. `startsAt` and `expiresAt` bound the offer validity period. `repayment.term.estimatedDays` is required; `maximumDays` is optional and applies only when `contractType` is `loan`. The `repayment` description calls it a configuration “of the grant,” but this event's stated subject remains a dynamic offer; that wording alone does not establish a grant. [Raw: lines 14–29]
- The response section says any `2xx` HTTP status accepts the webhook. Receipt or acceptance of this event does not establish current account-holder eligibility, completed terms acceptance, creation of a static/formal offer, grant approval, money movement or repayment. The related [[source-adyen-docs-capital-get-grant-offers-dynamic-offers|dynamic-offer guide]] routes selected amounts to later calculation and formal-offer steps. [Raw: lines 5–7, 31–39]

## Detail locators

- Dynamic-offer event purpose: opening statement, lines 5–7.
- Required account-holder/offer IDs, amount range and validity dates: Request body, lines 11–24 and 29.
- Repayment term and loan-only maximum duration: Request body, lines 25–28.
- Receiver `2xx` acknowledgement: Responses, lines 31–39.

## Related

- [[adyen-capital]] — financing offer and grant lifecycle context.
- [[adyen-webhooks]] — incoming event and acknowledgement context.
- [[source-adyen-docs-capital-get-grant-offers-dynamic-offers]] — dynamic range, later calculation and formal-offer route.
- [[source-adyen-docs-capital-webhook-types-capital-webhooks]] — Capital offer and grant event-family distinctions.

## Raw Sources

- [[raw/adyen/api-explorer/capital-webhooks/latest/post/balancePlatform.capital.dynamicOffer.created/2026-09-15|Adyen Capital dynamic offer created webhook — captured 2026-09-15]]
