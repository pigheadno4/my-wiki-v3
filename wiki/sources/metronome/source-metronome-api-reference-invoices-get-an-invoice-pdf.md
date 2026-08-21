---
title: "Metronome Get an Invoice PDF API"
type: source
date_ingested: 2026-08-21
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/invoices/get-an-invoice-pdf.md"
raw_files:
  - "metronome/api-reference/invoices/get-an-invoice-pdf-2026-07-13.md"
tags: [metronome, api, invoices, pdf, binary-response]
---

## Overview

This API reference documents the bearer-authenticated `GET /v1/customers/{customer_id}/invoices/{invoice_id}/pdf` endpoint on `https://api.metronome.com`. A successful request returns invoice content as `application/pdf`; both path identifiers are required UUID-formatted strings. The page documents one generic not-found response but does not define invoice-state eligibility, retention, generation guarantees, or the legal or compliance status of the returned document.

## Key takeaways

- The endpoint retrieves a PDF representation of a specified customer invoice. The descriptive prose presents it for customer sharing, accounting-team use, and record keeping, but those stated uses do not establish legal officiality, audit sufficiency, or compliance.
- `customer_id` and `invoice_id` are required path parameters, each represented as a UUID-formatted string. The guidance says the invoice identifier should correspond to an existing invoice for the specified customer, but the page does not define global invoice-ID uniqueness or mismatch handling beyond the generic `404`.
- HTTP `200` uses the `application/pdf` media type. The prose calls the response a binary PDF containing line items, totals, billing period, and customer details; the OpenAPI schema is only `type: object` and does not describe a byte stream, object properties, headers, filename, content length, or streaming behavior.
- HTTP `404` returns `application/json` using an error object whose required field is a string `message`. The generic description, `The specified resource was not found`, does not distinguish a missing customer, a missing invoice, or a customer-invoice mismatch.
- The operation is covered by the document's HTTP bearer security scheme. This page does not document `401`, `403`, other errors, authorization scope, rate limits, retry behavior, caching, timeout recovery, invoice lifecycle constraints, retention, PDF rendering stability, or availability guarantees.

## Request and authorization

Call `GET /v1/customers/{customer_id}/invoices/{invoice_id}/pdf` against the documented production server, `https://api.metronome.com`. The OpenAPI document applies `bearerAuth` globally and defines it as an HTTP bearer scheme. No request body or query parameter is documented.

Both path parameters are marked required and use string schemas with UUID format. The prose instructs callers to ensure that `invoice_id` corresponds to an existing invoice for the specified `customer_id`. It does not define whether invoice IDs are globally unique, whether the customer path component is an authorization boundary, or how a mismatch is distinguished from another missing resource.

## Success response and media boundary

The documented `200 Success` response has the `application/pdf` media type. The page describes it as a binary PDF representing the full invoice and says it includes standard invoice information such as line items, totals, billing period, and customer details. Applications are directed to use appropriate headers for the binary response, with `Content-Type: application/pdf` given as the example.

The OpenAPI media schema says only `type: object`; it does not define object properties and does not model the PDF bytes with a binary string schema. Accordingly, the media type and prose establish the intended binary PDF response, while the schema does not establish its byte encoding, disposition, filename, length, streaming behavior, or a JSON object contract. The page also does not promise identical rendering or byte stability across repeated retrievals.

## Not-found response

The only documented failure response is `404`. It uses `application/json` and references an `Error` object that requires `message`, a string. The response description is generic and does not identify which resource was absent or document a machine-readable error code.

No `401`, `403`, `429`, or `5xx` response schema is included. The absence of those entries is not evidence that those failures cannot occur, and the page gives no retry, timeout-recovery, or error-specific handling contract.

## Document-purpose and lifecycle boundaries

The descriptive text says the endpoint generates the PDF on demand and warns that frequent requests for the same invoice may affect performance. It gives no quantitative limit, latency target, caching rule, asynchronous state, or availability guarantee.

The page characterizes the PDF as professionally formatted and suitable for customer sharing, accounting, record keeping, audits, compliance, and official use. Those are stated purposes, not a contract that the PDF is legally official, compliant with a named standard, sufficient evidence for an audit, retained for a specified period, immutable, finalized, delivered, collectible, paid, or available in every invoice state. It also does not define the invoice data's calculation time, rendering time, locale, currency formatting, tax treatment, downstream-provider representation, or lifecycle propagation.

No contradiction was found with the existing Metronome invoicing concept. That concept documents broader calculation, lifecycle, delivery, and downstream-provider boundaries from other sources; this endpoint independently establishes only the retrieval path, required UUID identifiers, bearer authentication, PDF response media, generic not-found error, and the limitations described here.

## Related

- Company: [[metronome]]
- Concept: [[metronome-invoicing]]
- Related source: [[source-metronome-plans-shared-endpoints-invoices]]

## Raw Sources

- [[raw/metronome/api-reference/invoices/get-an-invoice-pdf-2026-07-13|2026-07-13 snapshot — invoice PDF retrieval path, binary media response, identifiers, authentication, and not-found schema]]
