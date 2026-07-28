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

## Sources

- [[source-metronome-guides-platform-configuration-security-principles]] — least privilege, zero trust, and short-lived credential principles

## Related

- [[metronome]]
- [[metronome-webhooks]]
