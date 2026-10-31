---
title: "Adyen relayed authorisation webhook: balancePlatform.authorisation.relayed"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/relayed-authorisation-webhooks/latest/post/balancePlatform.authorisation.relayed"
raw_files:
  - "adyen/api-explorer/relayed-authorisation-webhooks/latest/post/balancePlatform.authorisation.relayed/2026-09-15.md"
tags: [adyen, issuing, relayed-authorisation, webhooks]
---

## Overview

This 2026-09-15 Adyen API Explorer `relayed-authorisation-webhooks/latest` endpoint describes an incoming `balancePlatform.authorisation.relayed` request through which Adyen asks an Issuing platform for a transaction authorisation decision. To complete the relayed decision, the receiver must return HTTP 200 with `authorisationDecision` in the response body; if Adyen does not receive the response within two seconds, it applies configured fallback logic. This is a decision exchange, not an ordinary webhook receipt acknowledgement or proof of capture or settlement. See [[adyen]], [[adyen-issuing]], and [[adyen-webhooks]].

## Key takeaways

- The request table marks all top-level fields optional. It describes `accountHolder`, `balanceAccount`, `paymentInstrument`, and transfer `id` separately; `reference` is the payment reference, while scheme trace and unique transaction IDs are separate optional fields. `amount` and `originalAmount` are optional parents whose `currency` and minor-unit `value` children are marked required when present. `paymentInstrument` is optional but has required nested identifiers and type fields; the table's many conditional card and bank-account fields belong to that resource, not mandatory webhook envelope fields.
- The sample request carries a prefilled `authorisationDecision.status: Authorised`, a negative EUR amount, balance mutation, validation results, and `environment: test`; these are example request data, not the platform's response or evidence that the transaction was finally approved, captured, or settled. `type` is shown as `balancePlatform.authorisation.relayed` in the sample.
- The 200 response-body table marks `authorisationDecision` optional but its nested `status` required when that object is present, with `Authorised` and `Refused` values; optional `refusalReason`, `metadata`, and `reference` are also listed. The response example nests `status` inside `authorisationDecision`. The introductory prose nevertheless directs including `authorisationDecision` to complete the relayed authorisation, so the optional table parent must not be read as permission to omit a decision from a completed response.
- The endpoint lists 400, 401, 403, 422, and 500 error responses with optional error details. It expressly states two-second fallback on no response. The separate Issuing relayed-authorisation guide describes a prose `status` response shape that conflicts with its nested examples, while the validation-checks guide mentions a 1500 ms stand-in trigger; this endpoint's 200 nested response and two-second statement do not reconcile those separate guide claims. See their source pages before implementing.

## Detail locators

- Purpose, required decision response, and two-second fallback: raw lines 5–11.
- Full request schema, optional top-level versus required nested fields: raw lines 13–143.
- Illustrative incoming request, including identifiers, amounts, validation and type: raw lines 145–304.
- 200 response schema and error-status bodies: raw lines 305–382.
- Nested decision response example: raw lines 384–399.

## Related

- [[source-adyen-docs-issuing-authorisation-relayed-authorisation]] — Issuing decision guide with response-shape tension.
- [[source-adyen-docs-issuing-validation-checks]] — separate 1500 ms stand-in wording.
- [[adyen-issuing]] — product and authorisation context.

## Raw Sources

- [[raw/adyen/api-explorer/relayed-authorisation-webhooks/latest/post/balancePlatform.authorisation.relayed/2026-09-15|Adyen relayed authorisation endpoint reference, captured 2026-09-15]]
