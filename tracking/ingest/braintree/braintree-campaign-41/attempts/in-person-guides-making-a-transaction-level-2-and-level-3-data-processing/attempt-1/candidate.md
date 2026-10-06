---
title: "Braintree In-Person Level 2 and Level 3 Data Processing"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/in-person/guides/making-a-transaction/level-2-and-level-3-data-processing"
raw_files:
  - "braintree/in-person/guides/making-a-transaction/level-2-and-level-3-data-processing-2026-09-16.md"
tags: [braintree, in-person, card-present, graphql, level-2, level-3]
---

## Overview

This collected Braintree website guide covers passing Level 2 and Level 3 data in GraphQL transaction requests for Braintree in-person transactions. The page is an unversioned website snapshot with body metadata updated 2025-01-03 and raw fetched 2026-09-16; it is not GitHub, SDK-version, exact deployed-schema or current-support evidence.

## Key takeaways

- The page presents Level 2 data as primarily tax information and a purchase-order number, and Level 3 data as primarily line-item, discount and shipping information. Its examples put those inputs on an in-person reader charge request; use the raw locators for exact input names, query selections and sample values rather than treating the examples as a complete current field specification.
- Braintree says passing L2/L3 data can help lower interchange fee costs only for eligible MCC codes and eligible card types, and describes the use case as primarily relevant to B2B merchants. The page links to general L2/L3 documentation and tax-ID configuration instructions for a Braintree merchant account, but it does not enumerate the eligible MCCs or cards, identify processor/account applicability, prove merchant approval or enablement, or guarantee any interchange result.
- Merchants will typically send both levels in the same request; the page separates them only to illustrate each level.
- The documented flow has distinct stages: send the reader charge request, complete the card interaction on the reader, then have the POS poll the synchronously returned context ID. Request acceptance, a card prompt, reader completion, context status and transaction status are not interchangeable evidence of a successful processed or settled payment.
- Incorrectly formatted data may be accepted initially and prompt for card insertion, but the page says an error is thrown after the card is tapped, the transaction is not processed and the final context status is `FAILED`. L2/L3 fields are not supported for offline transactions and cause an API error there. They are also not supported on the Request Authorize mutation, although the page says they may be sent in the separate capture request.

> [!warning] Eligibility, support and outcome boundaries
> Supplying these fields does not establish merchant, merchant-account, MCC, processor or card eligibility; required approval or configuration; lower interchange; current GraphQL or reader support; or authorization, capture, settlement or funding of an individual transaction. Confirm the applicable account, processor, card, environment and current schema before implementation.

## Detail locators

- Purpose, qualified interchange-cost statement, B2B relevance and linked tax-ID configuration route: `## Feature Overview`, lines 19-24.
- Level 2 purpose, input names, reader-charge example and context-ID polling example: `## Level 2 Data Processing`, lines 27-33.
- Level 3 purpose, input names, reader-charge example and context-ID polling example: `## Level 3 Data Processing`, lines 34-40.
- Invalid-format timing and final `FAILED` context state: `## Important Tips for passing L2/L3 data`, line 44.
- Offline exclusion, Request Authorize exclusion, separate-capture allowance and GraphQL-format handoff: `## Important Tips for passing L2/L3 data`, lines 47-53.

## Related raw API references

The captured page links to the general L2/L3 required-fields and merchant-requirements pages; `TransactionTaxInput`, `TransactionShippingInput` and `TransactionLineItemInput`; the offline-transactions guide; and the card-present authorization/capture guide. Those targets are navigation only here and were not read as evidence for this entry.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- Processor-specific comparison route: [[source-braintree-articles-wells-ic-transactions-level-2-and-3-processing]]

## Raw Sources

- [[raw/braintree/in-person/guides/making-a-transaction/level-2-and-level-3-data-processing-2026-09-16|Braintree In-Person Level 2 and Level 3 Data Processing guide]] - complete collected page covering qualified purpose, reader-charge and context-polling examples, and action-specific limitations
