---
title: "Allowlist the Metronome API"
type: source
date_ingested: 2026-08-01
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/platform-configuration/allowlist"
raw_files:
  - "metronome/guides/platform-configuration/allowlist-2026-07-13.md"
tags: [metronome, api-security, ip-allowlisting, service-registry, network-security]
---

## Overview

This guide describes the operational use of Metronome's service registry for IP allowlisting: poll `getServices`, apply the returned IPs through the organization's security tooling, and keep the rules current as addresses rotate. It treats IP allowlisting as an additional security layer and recommends automation, recurring tests, and an audit changelog, but it does not define a complete safe-update algorithm or network policy.

## Key takeaways

- Metronome says an allowlist restricts API access to a selected set of IP addresses, reducing potential unauthorized entry points.
- The implementation flow is to poll `getServices` for Metronome API IPs and apply the response through the organization's own security protocols and network tools.
- The guide warns that failing to poll regularly can cause loss of API access as IPs rotate in and out of service. This is a fail-closed availability risk from stale allowlist state, not a documented instruction to remove working entries when retrieval or rule updates fail.
- New IPs are said here to appear at least 30 days before first use. The existing endpoint reference uses the weaker wording that new IPs "typically" appear 30 or more days before use, so the statements must remain source-scoped rather than becoming a universal guaranteed notice period.
- IP allowlisting is only an extra layer; the guide also calls for measures such as SSO and scoped RBAC roles.

## Polling and update workflow

The guide requires customer action to keep allowlisting both available and secure. It recommends automating regular `getServices` polling and allowlist updates, testing the resulting configuration regularly, and retaining a changelog of rule changes for auditing. It provides no polling interval, freshness signal, change notification, cache lifetime, removal notice, overlap period, update ordering, rollback process, or response to a failed poll, malformed or partial response, or failed network-rule deployment. Consequently, "regularly" cannot be converted into a specific schedule, and the source does not authorize clearing or narrowing a last-known-good allowlist solely because a registry refresh fails.

## Service-registry and network boundary

This guide refers readers to `getServices` but does not restate its HTTP route, bearer-authentication requirement, response schema, or the registry's `makes_connections_from` and `accepts_connections_at` usage labels. It says to use response IPs, yet does not explain which named services or direction labels apply to a particular firewall or allowlist control. The dedicated API reference therefore owns the registry schema and direction-label facts; neither page defines actor perspective, protocols, ports, IP notation, environment mapping, or a complete inbound-versus-outbound rule design.

## Security and notice boundaries

IP membership limits network reachability but is not documented here as request authentication, authorization, message integrity, or a substitute for TLS, bearer-token controls, or webhook signature verification. The guide's recommendation to pair allowlisting with SSO and scoped RBAC reinforces the layered-control boundary.

The guide's "at least 30 days" statement and the service-registry reference's "typically 30+ days" statement concern the same update workflow but carry different guarantee strength. They do not prove that an observed update violates either source, but they are an operational wording tension: consumers should not infer an unconditional notice SLA, a removal lead time, or an overlap guarantee without further confirmation. No other direct contradiction with the existing service-registry source or Metronome security concept was found.

## Related

- Company: [[metronome]]
- Concept: [[metronome-security-principles]]
- Related source: [[source-metronome-api-reference-security-get-services]]

## Raw Sources

- [[raw/metronome/guides/platform-configuration/allowlist-2026-07-13|2026-07-13 snapshot — IP allowlisting workflow, polling obligation, rotation risk, and layered-security guidance]]
