---
title: "Metronome API Reference: Get a Threshold Notification"
type: source
date_ingested: 2026-08-27
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/alerts/get-a-threshold-notification.md"
raw_files:
  - "metronome/api-reference/alerts/get-a-threshold-notification-2026-07-13.md"
tags: [metronome, api, alerts, notifications]
---

## Overview

Metronome exposes `POST /v1/customer-alerts/get` to retrieve the current evaluation state and configuration for one threshold-notification/customer pair. It is an on-demand, targeted status read rather than a history or bulk-status API.

## Durable facts

- The lookup is identified by a Metronome customer UUID and threshold-notification UUID. The enclosing OpenAPI `requestBody` is not marked `required: true`, although `customer_id` and `alert_id` are required properties inside a supplied `GetCustomerAlertPayload`; omitted-body behavior is therefore not established.
- A successful response requires `data`, whose `CustomerAlert` object requires both `customer_status` and `alert`. `customer_status` is nullable and otherwise uses `ok`, `in_alarm`, or `evaluating`; an archived notification returns `null` while its notification configuration remains available.
- The nested alert configuration carries notification identity and operating configuration, including alert type and status, threshold, timestamp, and type-specific credit, grouping, seat, invoice, or custom-field filters. The full object and enum catalogs remain in the raw OpenAPI page.
- The endpoint reports current evaluation state only. Threshold-notification history belongs in webhook notifications or event logs, and the documentation positions this operation for on-demand or targeted monitoring rather than bulk checks.
- The page documents HTTP `404` when either locator does not exist or is inaccessible to the caller's organization; the OpenAPI response component itself gives only the generic boundary that the specified resource was not found.

## Material boundaries

Because this read uses POST, the API-wide [[metronome-api-idempotency|`Idempotency-Key` contract]] applies: an identical same-key retry can replay the original result rather than prove a fresh threshold evaluation. This endpoint adds no status-read-specific guarantee for caching, freshness, another or expired key, concurrent reads, or recovery after an ambiguous failure. [[source-metronome-api-reference-idempotency]]

The operation schema does not set `additionalProperties: false` on the request or returned objects, so unknown-field rejection and closed-schema behavior are not established. Optional request filters are notification-type specific; the raw page is authoritative for their applicability and nested required properties.

> [!warning] Documentation conflict
> The narrative presents `updated_at` as the time `customer_status` was last updated and lists it with the `CustomerAlert` fields, but the OpenAPI `CustomerAlert` schema does not define a top-level `updated_at`; the response example and `Alert` schema place it under `alert`. Do not assume a top-level JSON path without verifying the current contract or observed response.

## Raw-detail coverage map

- **Request schema:** exact UUID formats; Plans-versus-Contracts migration flag; group, seat, alert-specifier, custom-field, and webhook-notification filters; nested required properties and feature annotations.
- **Response schema:** the complete alert-type and alert-status enums, nullable fields, threshold and credit-type objects, group and invoice filters, alert specifiers, and their nested schemas.
- **Examples and errors:** sample request and `in_alarm` response, bearer authentication, and the generic `404` error object.
- **Documentation tension:** exact prose and schema locations for `updated_at`, request-wrapper requiredness, and schemas whose `additionalProperties` behavior is unspecified.

## Primary concepts

- [[metronome-alerts-and-notifications]] — threshold-state identity, lifecycle state, configuration, and targeted lookup semantics
- [[metronome-api-idempotency]] — API-wide POST replay behavior and the fresh-read boundary
- [[metronome-webhooks]] — historical notification routing versus this endpoint's current-state view

## Related

- Companies: [[metronome]]

## Raw Sources

- [[raw/metronome/api-reference/alerts/get-a-threshold-notification-2026-07-13|Get a threshold notification — 2026-07-13]] — complete narrative and OpenAPI evidence
