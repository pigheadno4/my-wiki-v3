---
title: "Braintree Transaction Declines and Retry Guidance"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/control-panel/transactions/declines"
raw_files:
  - "braintree/articles/control-panel/transactions/declines-2026-09-16.md"
tags: [braintree, control-panel, transactions, processor-declines, retry-guidance, response-codes]
---

## Overview

This collected Braintree Control Panel article explains how to interpret and handle processor declines. The page metadata says it was updated on 2026-06-19, and the raw was collected on 2026-09-16. It distinguishes an issuer refusal from a gateway-setting rejection, separates authorization from settlement declines, and routes detailed handling to hard/soft classifications, response-code tables, card-network retry guidance, and processor-response fields.

## Key takeaways

- A processor decline means the customer's bank refused the request; the response code may indicate why, but the page says only that bank can confirm the specific reason. This differs from a gateway rejection caused by Braintree gateway settings. Response code `3000`, `Processor Network Unavailable - Try Again`, is separately described as a possible back-end processing-network problem rather than necessarily a payment-method problem.
- Authorization declines occur when the bank refuses an authorization request. Settlement declines occur after a successful authorization when the bank denies settlement; the page describes them as much rarer.
- A hard decline requires resolution, such as contacting support or the customer's bank, before retrying. A soft decline reflects a temporary issue for which retrying the supplied payment-method information may succeed; that possibility is not a blanket permission to ignore the response-code and network-specific rules below.
- In the collected Visa table, Category 1 says `Do not retry`; Category 2 says `Reattempt Allowed` but limits retries to 15 over a rolling 30-day period; Categories 3 and 4 also specify a 15-retry rolling-30-day limit. The table associates fees with attempts beyond thresholds, and the article says each Category 1 retry is fined. The table itself must be consulted for the exact Braintree-response-code mapping.
- For Mastercard, the article says retry decisions should use only `merchant_advice_code` and `merchant_advice_code_text`; it states a $0.10 fee for every reattempt beyond 10 retries in 24 hours for MAC 03 and MAC 21, and routes the specific rules to the separate Merchant Advice Codes page.
- Additional processor responses are an optional, default-disabled Control Panel display. When enabled and the processor declines a transaction, the raw processor response appears in transaction details. The article says the API returns the additional processor response in the transaction object regardless of that display setting.

> [!warning] Dated guidance with unresolved internal retry conflicts
> Treat the network fees, thresholds, mappings, Smart Retries migration statement, and Control Panel/API behavior as claims in the 2026-09-16 snapshot, not proof of present rules, merchant eligibility, configuration, or successful execution. The Visa table lists response code `2007` in both Category 1 (`Do not retry`) and Category 3 (`Limit retries to 15`), and the code `2044` row tells the customer to try again while also labeling it Category 1 (`do not retry`); the page does not resolve those conflicts.

## Detail locators

- Source title and update timestamp: frontmatter, lines 5-10.
- Processor decline identity, gateway-rejection boundary, and reason-confirmation limit: `# Declines`, lines 17-30.
- Decline-ratio context and repeated-attempt inflation: `## Decline ratios`, lines 33-42.
- Authorization versus settlement declines: `## Authorization declines` and `## Settlement declines`, lines 45-56.
- Hard and soft decline handling: `## Handling declines`, lines 59-65.
- Visa retry categories, response-code mappings, fees, and Category 1 warning: `## Retrying declined transactions > Visa`, lines 68-94.
- Mastercard Merchant Advice Code condition and stated fee threshold: `## Retrying declined transactions > Mastercard`, lines 98-102.
- Braintree Retry, Smart Retries, and migration wording: `## Retrying declined transactions > Braintree Smart Retries`, lines 104-114.
- Optional Control Panel display and API-return statement for additional processor responses: `## Additional Processor Responses`, lines 117-128.
- Response-specific authorization implications, hard/soft labels, payment-method or account qualifications, and retry guidance: `## Authorization decline codes`, lines 131-575.
- Network-unavailable response `3000`: `## Authorization decline codes > code-3000`, lines 569-575.
- Settlement response table, including processor, PayPal-risk, capture/refund, account, dispute, and attempt-limit cases: `## Settlement decline codes`, lines 578-595.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]

## Raw Sources

- [[raw/braintree/articles/control-panel/transactions/declines-2026-09-16|Braintree Control Panel transaction declines article]] - complete collected page covering decline identity and handling, network retry guidance, additional processor responses, and authorization and settlement response tables
