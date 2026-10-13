---
title: "Networking issues | Adyen Docs"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/design-your-integration/network-and-connectivity/networking-issues"
raw_files:
  - "adyen/docs/point-of-sale/design-your-integration/network-and-connectivity/networking-issues/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-networking, mtu, mss]
---

## Overview

Adyen's POS "Networking issues" page describes one failure mode: payment packets may be dropped because path overhead exceeds the effective Maximum Transmission Unit (MTU), even while internet connectivity appears available. The pinned 2026-09-15 snapshot reports `last_modified` 2020-10-07. It offers a diagnostic hypothesis and a network-team escalation, not proof of a specific terminal's network condition or payment outcome. [[adyen]] [[adyen-terminal-api]]

## Key takeaways

- The cited symptoms are many `AuthorisedPending` or unauthorized payments, terminals failing to come online or switching to Store and Forward, and intermittent terminal-app loading. These symptoms can point to packet loss; the page says MTU exceedance **can** be the cause. Availability of an internet connection does not rule it out.
- The terminal's MTU is shown in the linked Endpoints connection test. Adyen says the terminal default MTU is 1500 bytes and TCP/IP headers leave a 1460-byte Maximum Segment Size (MSS). Additional PPPoE, VPN, or MPLS overhead along the path can exceed that budget. The page says payment packets are marked "Do not fragment," so a store or data-center router can drop oversized packets rather than fragment them.
- Lowering MSS through TCP MSS clamping/ceiling/adjustment is presented as a technique to avoid fragmentation or drops. Because changing MSS affects **all** network traffic, the page instructs contacting the network support team or network-vendor support before lowering it. The page names Path MTU Discovery as the standard technique and notes practical ICMP restrictions; it specifies no universal new MSS value.
- This source does not diagnose DNS, Wi-Fi, IP addressing, terminal assignment, encryption, or certificate faults. Its terminal/network symptoms do not establish that an authorization succeeded, failed, duplicated, or was safely retried. Use the separate Terminal API response and transaction-status authority for payment outcome investigation.

## Detail locators

- Symptoms and possible MTU cause: pinned raw, `## Dropped network packets when the internet connection is available`, `#### Symptom` and `#### Cause` (lines 18–36).
- Endpoints test, default MTU/MSS and path-overhead mechanism: pinned raw, `#### Cause` (lines 30–36).
- MSS adjustment, network-team warning, and PMTUD/ICMP qualification: pinned raw, `#### Solution` (lines 38–48).

## Related

- [[adyen-terminal-api]] — provider concept for POS message and response boundaries.
- [[source-adyen-docs-point-of-sale-design-your-integration-network-and-connectivity-network-configuration]] — broader terminal network configuration; separate source.
- [[source-adyen-docs-point-of-sale-error-scenarios]] — Terminal API response and transaction-status handling; separate source.
- [[adyen]] — provider hub.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/design-your-integration/network-and-connectivity/networking-issues/2026-09-15|Networking issues — 2026-09-15 snapshot]]
