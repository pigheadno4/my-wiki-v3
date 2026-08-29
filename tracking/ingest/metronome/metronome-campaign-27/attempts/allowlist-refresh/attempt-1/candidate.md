---
title: "Allowlist the Metronome API"
type: source
date_ingested: 2026-08-29
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/platform-configuration/allowlist"
raw_files:
  - "metronome/guides/platform-configuration/allowlist-2026-08-28.md"
  - "metronome/guides/platform-configuration/allowlist-2026-07-13.md"
tags: [metronome, api-security, ip-allowlisting, service-registry, network-security]
---

## Overview

This guide describes the customer-operated workflow for restricting access to Metronome APIs by IP address: poll `getServices`, apply the returned IPs through the organization's security tooling, and keep the resulting allowlist current as addresses rotate. Its scope is operational allowlist maintenance, not the service-registry schema or a complete network-security policy.

## Query-critical facts

- Metronome presents IP allowlisting as restricting API access to a selected set of IP addresses to reduce potential unauthorized entry points.
- The documented responsibility split is that the customer polls `getServices` for Metronome API IPs and configures its own allowlist using its security protocols and network tools.
- The guide says IPs can change, new IPs appear in the list at least 30 days before first use, and failing to poll regularly may cause loss of API access as IPs rotate in and out of service.
- Metronome recommends automating registry polling and allowlist updates, testing the configuration regularly, and maintaining an allowlist-change log for audit purposes. It describes allowlisting as an additional layer to combine with controls such as SSO and scoped RBAC.

## Material boundaries

- The guide defines neither a polling interval nor a freshness signal, removal notice, overlap period, update ordering, rollback process, or handling for failed retrieval, parsing, or network-rule deployment. Its stale-rule warning establishes an availability risk, but does not authorize clearing or narrowing a last-known-good allowlist solely because a refresh fails.
- This page does not restate the `getServices` route, authentication requirement, response schema, service names, or the meaning and actor perspective of registry direction labels. The dedicated service-registry source remains authoritative for those details; neither source supplies protocols, ports, environment mapping, IP notation, or a complete inbound-versus-outbound rule design.
- This guide says new IPs appear at least 30 days before first use, while the existing endpoint reference says they typically appear 30 or more days before use. Preserve the statements as source-scoped wording with different guarantee strength; they do not establish a universal notice SLA, removal lead time, or overlap guarantee. IP membership is also not documented as request authentication, authorization, message integrity, or a substitute for other security controls.

## Raw-detail coverage map

Use the latest raw page for the exact two-step implementation instruction, address-change and stale-poll warning, layered-security recommendation, automation and testing checklist, audit-changelog guidance, and current support-portal escalation path. Use the related service-registry source and its raw evidence for the HTTP route, bearer-authentication boundary, response schema, usage-label vocabulary, and registry-specific unknowns.

## Related

- Company: [[metronome]]
- Primary concept: [[metronome-security-principles]]
- Related source: [[source-metronome-api-reference-security-get-services]]

## Raw Sources

- [[raw/metronome/guides/platform-configuration/allowlist-2026-08-28|2026-08-28 snapshot - IP allowlisting workflow, rotation risk, layered controls, operational checklist, and support route]]
- [[raw/metronome/guides/platform-configuration/allowlist-2026-07-13|2026-07-13 snapshot - prior wording of the support escalation path]]
