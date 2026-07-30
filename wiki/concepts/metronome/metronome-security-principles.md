---
title: "Metronome Security Principles"
type: concept
category: framework
tags: [metronome, security, zero-trust, least-privilege]
---

## Definition

Metronome describes its security practices through three platform principles: least privilege, zero-trust architecture, and avoiding access based on long-lived credentials or static configuration.

## Access model

Access is denied until explicitly granted and can be controlled at field level. Metronome says this applies to both human and system actors so they receive only the data and capabilities required for their task.

## Authenticated service communication

Communication between systems, or between an actor and a system, is authenticated. The documentation describes forwarding the same security token through downstream service calls so that each service can independently verify the request and grant the relevant access.

## Credential lifetime

Metronome says almost no part of its system depends on long-lived API keys or static security tokens. Its engineers mint credentials daily, those credentials last 12 hours, and long-lived AWS credentials are not stored on developer machines.

## Customer API tokens

Metronome's public API uses bearer tokens created and archived through the dashboard. Tokens inherit the creating user's permissions by default and can be restricted by access level, environment, or endpoint through a Metronome representative. The full token is visible only at creation, the SDKs default to `METRONOME_BEARER_TOKEN`, and archiving a token cannot be undone.

The API quickstart corroborates the creation boundary: give the token a descriptive name and copy it to a secure location before completing the flow. Its setup examples accept a bearer token directly or use `METRONOME_BEARER_TOKEN`, but the quickstart adds no expiry, recovery, rotation, scope, or revocation policy.

> [!info] Credential-scope boundary
> The 12-hour lifetime above describes credentials minted by Metronome engineers. The API-authentication page does not state a lifetime or expiry policy for customer-created bearer tokens, so the two credential classes should not be treated as having the same lifecycle.

## Sources

- [[source-metronome-guides-platform-configuration-security-principles]] — least privilege, zero trust, and short-lived credential principles
- [[source-metronome-api-reference-authentication]] — customer bearer-token creation, use, scoping, and archival
- [[source-metronome-api-reference-api-quickstart]] — first-connection token handling and SDK environment-variable setup

## Related

- [[metronome]]
- [[metronome-webhooks]]
