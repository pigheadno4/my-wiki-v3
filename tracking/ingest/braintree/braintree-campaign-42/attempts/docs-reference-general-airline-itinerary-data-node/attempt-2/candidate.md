---
title: "Braintree Airline-Itinerary Data Reference (Node.js)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/general/airline-itinerary-data/node"
raw_files:
  - "braintree/docs/reference/general/airline-itinerary-data/node-2026-09-16.md"
tags: [braintree, node-js, airline-industry-data, transactions, interchange]
---

## Overview

This collected, unversioned Braintree website reference describes the Node.js request shape for sending Airline Industry Data (AID) with a transaction sale or capture. The page presents AID as additional information passed to card networks for interchange-rate assessment and covers Pay with PayPal, card, and Apple Pay/Google Pay transactions while naming Visa, Mastercard, and Discover. It is snapshot documentation, not proof of current availability, merchant eligibility, a particular SDK package version, a lower assessed fee, or successful authorization, settlement or funding.

## Key takeaways

- The page limits the merchant route to merchants recognized as airline merchants by card schemes. It states that AID is available globally for PayPal and in the US for card and Apple Pay/Google Pay, and that those merchants can pass it on sale or submit-for-settlement transactions for those payment-method categories.
- The field table labels the discriminator `industry_type` and lists `travel_flight` as its only value option; the displayed Node examples instead place camelCase `industryType` under `industry` and set it to `Transaction.IndustryData.TravelAndFlight`. The page says only one industry type can be sent per transaction and labels the generic table field as required for PayPal and card transactions, including Apple Pay or Google Pay.
- Field requiredness and length or value conditions vary by PayPal, card and Discover. The complete table is retained at `## Required Fields`, raw lines 25-141; do not treat one method's or network's conditions as universal.
- For the page's AS1 two-step case, its prose uses the generic labels `Transaction:Sale` and `Transaction:SubmitForPartialSettlement` for the instruction to pass lead-passenger data on sale when available and otherwise pass passenger data on partial settlement for each passenger. The displayed Node calls are `gateway.transaction.sale()` and `gateway.transaction.submitForPartialSettlement()`. The callback and Promise blocks are request-construction examples with empty result handlers; they do not establish that input was consumed or that authorization, capture, settlement or payment succeeded.
- The validation catalog says PayPal transactions with `travel_flight` industry data require `submit_for_settlement` to be true. It also documents a maximum of 12 legs and routes the remaining field-, format-, value- and type-specific errors to the raw tables.

## Detail locators

- Purpose, transaction stage and interchange-assessment description: `## Overview`, raw lines 17-21.
- Airline-merchant, geography, payment-method and operation qualifications: `## Merchant requirements`, raw lines 22-24.
- `industry_type`, payment-method/network-specific required fields, limits and full field inventory: `## Required Fields`, raw lines 25-141.
- Node.js callback and Promise sale examples: `## Examples` > `### Sale`, raw lines 144-296.
- AS1 lead-passenger instruction and Node.js partial-settlement examples: `### AS1 (2 Step Transaction)`, raw lines 301-448.
- PayPal settlement-submission condition and airline-data validation errors, including the 12-leg maximum: `## Validation errors`, raw lines 450-488.
- Per-leg validation codes and explanations: `### Airline-itinerary data legs`, raw lines 490-565.

## Related

- Company: [[braintree]]
- Server integration boundary: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/general/airline-itinerary-data/node-2026-09-16|Braintree Airline-Itinerary Data reference for Node.js]] - complete collected Node.js website variant covering AID purpose, merchant and payment-method qualifications, request fields, sale and AS1 examples, and validation errors
