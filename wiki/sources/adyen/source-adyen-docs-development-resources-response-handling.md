---
title: "Adyen HTTP Response Handling"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/response-handling"
raw_files:
  - "adyen/docs/development-resources/response-handling/2026-09-15.md"
tags: [adyen, online-payments, http, error-handling]
---

## Overview

This Adyen development-resources page explains how an online-payments integration should interpret HTTP responses to API calls and where to look for payment outcomes and error diagnostics. It distinguishes request receipt and processing from successful payment execution. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The page is scoped to an Adyen online-payments integration. It maps common HTTP response codes to request-level meanings and handling guidance; the exact response message still depends on the request method and requested data.
- A `202 Accepted` response means the request was accepted but has not yet been processed and does not guarantee completion. A `200 OK` confirms correct submission and successful processing by Adyen, but does not necessarily mean the payment or modification itself succeeded. For the capture example, the corresponding webhook reports the later operation outcome.
- Retry behavior is condition-specific: do not repeat a `400` without correcting the request, do not repeat a `403`, a `408` can be retried, and a `409` should be retried only when the API returns the transient-error header as `true`. For `429`, the page calls for exponential backoff with jitter.
- Do not interpret every `500` as proof of a provider-side transient failure: the page says an incorrect request, including a missing or empty mandatory field, can also produce `500`. The status table also sets a 10 MB maximum request size for `413`.
- In the listed validation, security, configuration, and internal-error scenarios, Adyen says the payments platform does not accept or store the request; the response includes an error code and problem description and should generally be handled as an exception. The page says rejected payment requests accompanied by an error message are not charged.
- Error response fields include `status`, `errorCode`, `message`, and `errorType`; `pspReference` may be absent from the body and then should be checked in the response headers. That request-specific reference can be provided to Adyen Support for debugging.

> [!warning] Outcome boundary
> An HTTP `200` is request-level evidence, not proof of payment or modification success. This unversioned documentation snapshot also does not establish current endpoint behavior, merchant eligibility, successful retries, or webhook delivery.

## Detail locators

- Purpose and response-dependent handling: `# HTTP status codes`, paragraph beginning "After submitting an API call", line 19.
- Integration scope: `## Requirements`, lines 21–25.
- Status meanings and handling instructions, including conditional retry guidance and the 10 MB request-size limit: `## HTTP responses`, lines 27–49.
- Request processing versus payment or modification outcome, refusal fields, and the capture/webhook example: `## Handle 200 responses`, lines 51–71.
- Rejected-request scenarios, exception handling, and charge statement: `## Handle 4xx and 5xx responses`, lines 73–85.
- Support correlation through the response-header `pspReference`: `## Debugging APIs`, lines 87–91.
- Error-object fields, allowed error types, body-versus-header `pspReference`, example, and complete-error-code route: `## Error response fields`, lines 93–119.

## Related

- [[adyen]] — provider page.
- [[adyen-online-payments]] — provider-level online-payments architecture and source route.
- [[adyen-webhooks]] — asynchronous event and payment-status route referenced by the capture example.

## Related raw API references

- [[raw/adyen/docs/development-resources/refusal-reasons/2026-09-15|Adyen refusal reason messages]]
- [[raw/adyen/docs/development-resources/error-codes/2026-09-15|Adyen error codes and messages]]

## Raw Sources

- [[raw/adyen/docs/development-resources/response-handling/2026-09-15|Adyen HTTP status codes and response handling (2026-09-15)]]
