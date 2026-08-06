---
title: "Metronome Audit Logs Guide"
type: source
date_ingested: 2026-08-01
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/platform-configuration/audit-logs"
raw_files:
  - "metronome/guides/platform-configuration/audit-logs-2026-07-13.md"
tags: [metronome, audit-logs, security-monitoring, operational-troubleshooting]
---

## Overview

This guide describes the metadata Metronome exposes for actions taken across its system, including activity initiated through the app or API. It presents audit logs as a way to attribute changes, inspect outcomes, and investigate potentially unauthorized activity, while leaving retention, completeness, access-control, export, and tamper-resistance guarantees unspecified.

## Key takeaways

- Metronome says its audit log tracks actions taken anywhere in its system, with the app and API given as examples of action sources.
- For each action, the guide lists a timestamp, the responsible user or API token, the affected resource, the action, and whether it succeeded.
- The guide directs users to the `/auditLogs` endpoint to access the log, but it does not define the HTTP method, authentication, permissions, filters, pagination, response schema, or error behavior.
- Example entries add a log-entry ID, actor details, `resource_type`, `resource_id`, `request_id`, and `status`; these examples illustrate token and human actors but do not establish a complete or required schema.
- Both example timestamps contain April 32 and an extra colon-delimited time component, so they cannot be treated as valid timestamp-format examples.

## Recorded action context

The guide frames one audit entry as metadata around an action: who performed it, when it occurred, what resource was affected, what operation was attempted, and whether the operation succeeded. The examples distinguish a named Developer API token from a human actor with a name and email, and they associate each action with a request ID. This supports operational attribution, but the guide does not say whether every actor field is always present, whether token names are unique or immutable, or whether a request ID is available for every action channel.

The two example actions affect the same customer resource and use `add_plan` and `change_name` as action labels. Both have `status` set to `success`; the guide does not enumerate other status values, failure metadata, before-and-after values, response bodies, or a stable action taxonomy. Its statement that the log records how the system responded is therefore narrower than a promise to preserve a complete API response.

## Access and evidence boundaries

The guide links to `/auditLogs` but does not specify the endpoint's method, versioned route, bearer-token scope, RBAC requirement, sorting, filtering, pagination, polling, rate limits, or error responses. Those mechanics require the dedicated API reference and should not be inferred from this page.

Audit visibility can support monitoring and investigation, but this source does not establish log retention, historical coverage, delivery latency, ordering, completeness, export format, alerting, access review, deletion behavior, immutability, cryptographic integrity, or tamper evidence. Actor attribution also does not prove that an action was authorized, and a successful status does not establish the business correctness of the resulting change.

The example timestamps are documentation defects rather than usable format evidence: `2023-04-32T18:31:55:00Z` and `2023-04-32T20:25:15:00Z` use an impossible calendar date and an extra colon-delimited component. This guide makes no explicit timestamp-format claim.

## Contradictions and unknowns

No direct contradiction with the existing Metronome security, authentication, or RBAC pages was found. The authentication source's statement that a token name can help track changes and requests in audit logs is consistent with this guide's token-actor example. The existing access-control sources define authorization and credential boundaries; this guide adds after-the-action visibility and must not be used as evidence that the recorded action was authorized or that the audit record is tamper-proof.

## Related

- Company: [[metronome]]
- Concept: [[metronome-security-principles]]
- Related sources: [[source-metronome-api-reference-authentication]], [[source-metronome-guides-platform-configuration-security-principles]], [[source-metronome-guides-platform-configuration-role-based-access-rbac]]

## Raw Sources

- [[raw/metronome/guides/platform-configuration/audit-logs-2026-07-13|2026-07-13 snapshot — audit action attribution, outcome visibility, example records, and documentation boundaries]]
