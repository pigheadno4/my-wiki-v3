---
title: "Adyen payment response layers overview"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/overview-response-handling"
raw_files:
  - "adyen/docs/development-resources/overview-response-handling/2026-09-15.md"
tags: [adyen, online-payments, response-handling, result-codes, refusal-reasons]
---

## Overview

This [[adyen]] development-resources overview separates API request status, raw acquirer response, refusal reason, and payment result code at different stages of an online payment. HTTP status describes whether Adyen processed the API request; it does not by itself establish that the financial institution approved the transaction. Adyen maps raw acquirer responses to refusal reasons and result codes in the API response. See [[adyen-online-payments]] for the provider flow and [[source-adyen-docs-development-resources-response-handling|the HTTP handling guide]] for request-level status and retry detail.

## Key takeaways

- The response's type and details depend on the payment lifecycle stage and the responding entity. An HTTP `200/OK` can accompany a payment described in the API response as refused or cancelled; it only shows successful request processing at the transport/API layer.
- For a submitted payment, the raw acquirer response indicates whether the financial institution authorized or rejected it and can give a rejection reason. Adyen maps the raw response to a refusal reason and result code. A refusal reason or `resultCode=Refused` identifies a payment-level refusal; the page notes that Adyen can also refuse when its risk score exceeds 99.
- This overview lists `Authorised`, `Refused`, `Error`, and `Cancelled` result codes and their meanings. These are API-response summaries, not HTTP status codes. It describes `Authorised` as approved by the financial institution, `Error` as a communication error after payment receipt, and `Cancelled` as an approved submitted cancellation request.
- The overview stops at API responses and routes to more detailed HTTP, error-code, raw-acquirer, and refusal-reason pages. It does not document later webhook delivery or prove a particular final payment, capture, or settlement outcome; consult the relevant payment lifecycle and [[adyen-webhooks]] sources for asynchronous state.

## Detail locators

- **Response-stage and responding-entity scope:** raw lines 15–25, under `# Response handling` and `## Types of responses`.
- **HTTP request status and non-200 error diagnostics:** raw lines 27–37, under `### HTTP status codes` and `### Error codes and messages`.
- **Raw acquirer response versus successful HTTP processing:** raw lines 39–45, under `### Raw acquirer responses`.
- **Adyen's refusal-reason mapping and result-code table:** raw lines 47–72, under `## How Adyen handles responses`, `### Refusal reasons`, and `### Result codes`.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-webhooks]]
- [[source-adyen-docs-development-resources-response-handling]]

## Raw Sources

- [[raw/adyen/docs/development-resources/overview-response-handling/2026-09-15|Adyen response handling overview — collected 2026-09-15]]
