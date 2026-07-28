---
title: "Metronome's Security Principles"
type: source
date_ingested: 2026-07-28
canonical_url: "https://docs.metronome.com/guides/platform-configuration/security-principles.md"
original_format: webpage
raw_files:
  - "metronome/guides/platform-configuration/security-principles-2026-07-13.md"
tags: [metronome, security, platform-configuration]
---

## Overview

This Metronome documentation page describes the security principles that govern access and communication within its systems. It identifies least privilege, zero-trust architecture, and the avoidance of long-lived credentials or configuration as its three core principles.

## Key takeaways

- Metronome states that access is explicitly granted and controlled down to the field level.
- Its zero-trust architecture requires communication between systems or between an actor and a system to be authenticated.
- Security tokens are passed through underlying service calls so each service can verify and grant the relevant access.
- Metronome states that engineers mint credentials daily and that those credentials last 12 hours.

## Details

Under least privilege, the page says an actor has no data access or ability to take action until access has been explicitly granted. For zero trust, it describes a security token being passed through underlying service calls so each service can verify and grant relevant access; it says this works with least privilege to limit human and system actors to the minimal data needed for their task.

The page also says that almost no part of Metronome's system depends on long-lived API keys or other static security tokens, and that its AWS organization has no long-lived AWS credentials on developers' machines. It directs readers to Metronome's company security page for current details and to a representative for its SOC 2 report.

## Related

- Companies: [[metronome]]
- Concepts: [[metronome-security-principles]]

## Raw Sources

- [[raw/metronome/guides/platform-configuration/security-principles-2026-07-13|2026-07-13 snapshot — Metronome security principles]]
