---
title: "Braintree Allowlisting"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/risk-and-security/allowlisting"
raw_files:
  - "braintree/articles/risk-and-security/allowlisting-2026-09-16.md"
tags: [braintree, control-panel, allowlisting, ip-addresses, hostnames, api-security]
---

## Overview

This collected Braintree article documents merchant-configured IP-address and hostname allowlisting for access to the Braintree Gateway Control Panel and for server-to-server API calls. It distinguishes those restrictions from the separate developer reference for allowlisting Braintree IP addresses and domains.

## Key takeaways

- Once these restrictions are enabled, the article says access is denied unless the user's IP address or hostname is on the allowlist. It also says Braintree does not offer denylisting of selected IP addresses or hostnames.
- The allowlist applies only to Control Panel access and server-to-server API calls. Encrypted calls made directly from a customer's browser, including client-SDK requests for payment method nonces, are not subject to it and continue to be passed to Braintree regardless of the user's IP address.
- A user needs the **Edit IP Restrictions** role permission to configure the list. The documented Control Panel settings let that user grant Control Panel access, API access or both for each address or hostname; granting only one type blocks the other.
- The article recommends testing allowlisted addresses or hostnames in the sandbox before implementing them in production. It also documents wildcard logic for hostname ranges and IP subnet ranges, plus CIDR notation support.

## Evidence boundary

> [!warning] Restriction scope and rollout safety
> This page concerns merchant-configured access to the Braintree Gateway, not the separate task of allowing Braintree's own IP addresses or domains through merchant infrastructure. Browser-originated encrypted client-SDK calls are explicitly outside this allowlist. A Control Panel-only or API-only entry blocks the other access type, and the page recommends sandbox testing before production use. The 2026-09-16 collection establishes snapshot provenance, not current account eligibility, configuration state or successful enforcement.

## Detail locators

- Purpose and distinction from the Braintree IP-address/domain developer reference: `# Allowlisting > NOTE`, lines 17-18.
- Definition, default-deny behavior after enablement and unsupported denylisting: `# Allowlisting`, lines 22-26.
- Control Panel/server-to-server scope and browser-originated encrypted-call exclusion: `# Allowlisting`, line 30.
- Required role permission and Control Panel configuration procedure: `## Enabling IP and hostname restrictions`, lines 33-48.
- One-sided-access blocking consequence and sandbox-before-production recommendation: `## Enabling IP and hostname restrictions > IMPORTANT`, lines 51-52.
- Wildcard and CIDR support: `## Wildcards and CIDR notation`, lines 57-59.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]
- Role-permission reference: [[source-braintree-control-panel-users-roles-role-permissions]]

## Related raw API references

- [[raw/braintree/docs/reference/general/braintree-ip-addresses-2026-09-16|Braintree IP Addresses and Domains]] - unread navigation-only route linked by this article for the distinct task of allowlisting Braintree infrastructure

## Raw Sources

- [[raw/braintree/articles/risk-and-security/allowlisting-2026-09-16|Braintree Allowlisting]] - complete collected article covering merchant-configured IP/hostname restrictions, affected access paths, permission and configuration routes, rollout warnings, wildcards and CIDR support
