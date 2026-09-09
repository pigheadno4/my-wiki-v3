---
title: "Metronome API Reference: List Credit Grants"
type: source
date_ingested: 2026-09-09
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/credit-grants/list-credit-grants"
raw_files:
  - "metronome/api-reference/credit-grants/list-credit-grants-2026-07-13.md"
tags: [metronome, api, credit-grants, plans, contracts]
---

## Overview

This OpenAPI page documents bearer-authenticated `POST /v1/credits/listGrants`, which lists credit grants on Metronome's deprecated Plans surface. Metronome directs new clients to Contracts, but this page does not identify an equivalent Contracts operation or a migration mapping.

## Query-critical facts

- The operation lists credit grants and explicitly excludes voided grants. It therefore cannot serve as a complete inventory or history of grants.
- The endpoint is part of the deprecated Plans API. The page's direction to new clients to use Contracts is a scope warning, not documentation of a replacement route.
- The raw OpenAPI exposes optional filtering categories for credit-grant, credit-type, and customer identifiers plus effective and expiration time bounds. Use the raw schema rather than this summary for exact filter interactions and timestamp semantics.

## Raw-detail coverage map

Use `OpenAPI -> post /credits/listGrants -> parameters`, `requestBody`, and `responses` for the exact query pagination parameters, filter example, and success envelope. Use `components.schemas.ListCreditGrantPayload` for filter definitions and exclusions; `components.schemas.CreditGrant`, `CreditLedgerEntry`, `CreditType`, and `CustomField` for returned-resource detail.

## Related

- Company: [[metronome]]
- Primary concept: [[metronome-credits-and-commits]]

## Raw Sources

- [[raw/metronome/api-reference/credit-grants/list-credit-grants-2026-07-13|2026-07-13 snapshot - deprecated Plans credit-grant listing, voided-grant exclusion, filters, pagination, and response schema]]