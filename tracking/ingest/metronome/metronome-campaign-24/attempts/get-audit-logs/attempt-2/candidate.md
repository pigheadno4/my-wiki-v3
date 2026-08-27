---
title: "Metronome Get Audit Logs API"
type: source
date_ingested: 2026-08-27
canonical_url: "https://docs.metronome.com/api-reference/security/get-audit-logs.md"
original_format: webpage
raw_files:
  - "metronome/api-reference/security/get-audit-logs-2026-07-13.md"
tags: [metronome, api, audit-logs, security-monitoring, compliance-reporting, pagination]
---

## Overview

This reference documents bearer-authenticated `GET /v1/auditLogs`, an account-wide retrieval surface for operations initiated through Metronome's API, web interface, or automated processes. It is intended for compliance reporting, security monitoring, and operational troubleshooting, with time and resource filters plus cursor-based continuous polling.

## Query-critical facts

- Optional `starting_on` is an inclusive RFC 3339 lower bound and `ending_before` is an exclusive RFC 3339 upper bound; neither can be combined with `next_page`. Optional `resource_type` and `resource_id` must be supplied together.
- Optional `sort` orders by timestamp as `date_asc` or `date_desc` and defaults to ascending. Optional `limit` accepts 1 through 100 results, while `next_page` identifies where the next page starts.
- The OpenAPI-defined HTTP `200` shape is a top-level object requiring an AuditLog array under `data` and a nullable string `next_page` beside `data`. The endpoint describes saving each returned cursor for later polling and says an empty array is a temporary absence of new logs rather than proof that future polls will remain empty.
- Each AuditLog requires only `id`, RFC 3339 `timestamp`, and a `request` object whose own only required field is request `id`. `actor`, `resource_type`, `resource_id`, `action`, `status`, and `description` are optional; when an actor is present it requires `id` and `name`, while `email` is optional.
- Optional `status` is one of `success`, `failure`, or `pending`; optional request context can include IP address and user agent. The page defines labels and fields but not a stable action or resource-type taxonomy.

## Material boundaries and documentation tensions

> [!warning] Narrative-versus-OpenAPI response shape
> The narrative introduces a list of fields as being contained by each AuditLog object and includes `next_page` in that list. The OpenAPI schema instead places `next_page` beside `data` in the required top-level HTTP `200` envelope; it is not an AuditLog property. Preserve the OpenAPI placement as the schema-defined integration shape while retaining this documentation contradiction.

> [!warning] Narrative-versus-schema attribution boundary
> The narrative calls this a comprehensive trail of all account operations and describes logs of who did what and when, but the AuditLog schema requires neither actor, resource identity, action, status, nor description. Only entry identity, timestamp, and request identity are required. Do not treat every returned entry as guaranteed to contain complete actor, resource, operation, or outcome attribution.

The page says saving cursors supports uninterrupted retrieval and helps ensure no logs are missed, but it does not define retention, earliest historical coverage, ingestion or visibility latency, backfill, cursor lifetime, invalid-cursor recovery, snapshot consistency, duplicate or skip behavior during concurrent activity, exactly-once delivery, immutability, deletion, export, or tamper evidence. Those omissions prevent the endpoint alone from proving an audit population is compliance-complete.

The API-wide pagination guide treats nullable `next_page` as the completion signal for a finite list, while this endpoint instructs callers to keep polling after an empty `data` array and to reuse the cursor. The page does not resolve how continuous polling should proceed if an empty response carries `next_page: null`; preserve this endpoint-specific ambiguity rather than assuming a terminal or nonterminal null. Only HTTP `200` is documented, and the page supplies no authorization-scope, rate-limit, timeout, cache, or error contract. None of its object schemas declares `additionalProperties: false`, so unknown-property handling and closed-schema guarantees remain undocumented.

## Raw-detail coverage map

Use the raw snapshot for the complete time, resource, sort, limit, and cursor parameter definitions; incompatibility and pairing constraints; bearer security declaration; the narrative placement of `next_page` inside its AuditLog field list versus the OpenAPI-defined top-level sibling placement beside `data`; the required success envelope; continuous-polling description; AuditLog, request, and Actor requiredness; optional attribution and request-context fields; status enum; RFC 3339 formats; and the absence of documented non-200 responses and closed-object declarations.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-security-principles]], [[metronome-reporting-and-analytics]]
- Related sources: [[source-metronome-guides-platform-configuration-audit-logs]], [[source-metronome-api-reference-pagination]], [[source-metronome-api-reference-authentication]]

## Raw Sources

- [[raw/metronome/api-reference/security/get-audit-logs-2026-07-13|2026-07-13 snapshot - account-wide audit-log retrieval, filters, continuous cursor polling, response-shape contradiction, attribution schema, and completeness boundaries]]