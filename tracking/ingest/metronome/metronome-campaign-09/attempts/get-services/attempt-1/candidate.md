---
title: "Metronome Security Service Registry API"
type: source
date_ingested: 2026-08-01
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/security/get-services"
raw_files:
  - "metronome/api-reference/security/get-services-2026-07-13.md"
tags: [metronome, api-security, ip-allowlisting, firewall-configuration, service-registry]
---

## Overview

This API reference documents the bearer-authenticated `GET /v1/services` endpoint on Metronome's production API. The endpoint returns named services and IP strings intended for security allowlisting and firewall configuration, with a direction label indicating how each service uses those IPs. The page defines the successful response schema but does not publish current registry values, error responses, refresh mechanics, or a complete network-security policy.

## Key takeaways

- `GET https://api.metronome.com/v1/services` inherits the document-level HTTP bearer requirement and has no documented parameters or request body.
- A 200 response is an object with a required `services` array. Every service item requires `name`, `usage`, and `ips`.
- `name` is a string; `usage` is restricted to `makes_connections_from` or `accepts_connections_at`; and `ips` is an array of strings. The schema does not define whether an IP string is a host address, CIDR range, or another notation.
- Metronome says new IPs typically appear in the registry 30 days or more before first use. The word "typically" does not establish a guaranteed notice period.
- The page documents no non-200 responses, token-scope requirement, rate limit, cache lifetime, polling cadence, change notification, removal lead time, or fallback behavior.

## Endpoint and authentication boundary

The production server is `https://api.metronome.com`, the route is `GET /v1/services`, and the operation ID is `getServices-v1` under the Security tag. The OpenAPI document declares HTTP bearer authentication at the document level. The operation defines no path or query parameters and no request body.

Bearer authentication governs access to this API call, but this page does not identify the permission or endpoint scope a token needs. It also does not define token creation, rotation, expiry, archival, or invalid-token responses; the dedicated authentication reference owns those controls.

## Service registry schema

The only documented response is 200 Success with `application/json`. Its top-level object requires `services`, an array whose items reference the `Service` schema. Each `Service` object requires all three documented properties: string `name`, enum `usage`, and string-array `ips`.

The two permitted `usage` values are `makes_connections_from` and `accepts_connections_at`. Their labels express opposite connection directions, but the page supplies no field descriptions or examples that define the actor perspective, protocol, port, environment, or whether one service can appear in multiple records. Although the narrative calls the values IP ranges, the schema gives each `ips` item only `type: string`; it supplies no IP or CIDR format, validation pattern, uniqueness rule, minimum array size, or address-family indication.

The OpenAPI schema requires the `services` property and each item's three fields, but it sets no `minItems` on either array and no `minLength` on `name` or an `ips` string. It also provides no registry version, generation timestamp, effective-from time, retirement time, pagination, ordering, or stable-identifier field.

## Operational security boundaries

Metronome presents the registry as an input to allowlists and firewall rules and says new IPs typically appear 30 days or more before first use. This does not define how often a consumer must poll, how quickly changes become visible, how removals are announced, how long old IPs remain valid, or what to do when retrieval fails. The page also does not state that registry membership proves a request's authenticity or replaces TLS, bearer authentication, or webhook signature verification.

Related webhook documentation makes a narrower statement that changes to its published webhook IP list receive at least 30 days' notice. This generic registry page instead says new IPs "typically" appear 30 days or more before first use. Those statements are not a direct contradiction because their scopes and wording differ, but they should not be collapsed into one universal guarantee.

## Errors, unknowns, and contradictions

- Only the 200 response is defined; there are no 401, 403, 404, 429, or 5xx schemas and no documented error object.
- Current service names, IP values, environments, protocols, ports, address families, and directional interpretation are absent because the page includes no example response.
- Completeness, ordering, pagination, caching, freshness, polling, versioning, update notification, IP addition and removal timelines, and failure recovery are unspecified.
- No direct contradiction with the existing Metronome security material was found. The 30-day wording difference above remains a source-scoped operational boundary rather than a contradiction.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-security-principles]], [[metronome-webhooks]]
- Related sources: [[source-metronome-api-reference-authentication]], [[source-metronome-guides-platform-configuration-security-principles]], [[source-metronome-guides-platform-configuration-setup-webhooks]]

## Raw Sources

- [[raw/metronome/api-reference/security/get-services-2026-07-13|2026-07-13 snapshot — bearer-authenticated service registry and IP allowlisting schema]]
