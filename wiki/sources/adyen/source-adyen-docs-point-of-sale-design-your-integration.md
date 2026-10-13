---
title: "Adyen Docs: Design your in-person integration"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/design-your-integration"
raw_files:
  - "adyen/docs/point-of-sale/design-your-integration/2026-09-15.md"
tags: [adyen, point-of-sale, in-person-payments, terminal-api, integration-design]
---

## Overview

This Adyen Docs webpage is a brief decision guide for an in-person payment integration. It introduces account and store structure, terminal selection, POS-to-terminal communication, network setup, Terminal API messages, and transaction updates. Its topic-by-topic applicability labels matter: the page is an orientation route, not a full implementation procedure or evidence that a specific merchant, device, SDK, or environment is enabled. See [[adyen]] and [[adyen-terminal-api]].

## Key takeaways

- **Account structure — all solutions:** represent physical payment locations as stores in the Adyen account. The page presents stores under a merchant account or a merchant account per store as choices affecting payouts and reconciliation. [Raw: Account structure]
- **Terminal models — Terminal API integration and standalone terminals, excluding mobile solutions:** choose among portable, countertop/multimedia, and unattended models with differing connectivity. The selection details belong in the linked terminal guide. [Raw: Terminal models; Next steps → Terminals]
- **Local or cloud communication and network setup — Terminal API integration, excluding standalone and mobile solutions:** a POS can communicate with terminals over a local network or through the cloud. Cloud payment processing is unavailable during an internet outage unless a fallback has been implemented; network configuration and terminal IP addresses are also covered as preparation topics. [Raw: Local or cloud communications; Network and connectivity configuration]
- **Terminal API — Terminal API integration and mobile solutions, excluding standalone:** learn the general message structure and request structure for operations such as payments and refunds. This page does not define endpoint or request schema details. [Raw: Terminal API; Next steps → Terminal API]
- **Updates — webhooks for Terminal API integration and mobile solutions; terminal notifications for Terminal API integration with terminals; excluding standalone:** terminals and the Adyen platform generate transaction updates that can be sent to a POS endpoint. The page asks whether the architecture or use case requires receiving them. [Raw: Notifications and webhooks]

## Detail locators

- Raw headings `Account structure`, `Terminal models`, `Local or cloud communications`, `Network and connectivity configuration`, `Terminal API`, and `Notifications and webhooks` carry the solution-specific applicability and caveats.
- Raw `Next steps` links to separate account, hardware, architecture, local/cloud, network, Terminal API, and webhook instructions. Those linked pages are navigation targets, not evidence read for this entry.

## Related

- [[adyen-terminal-api]] — existing concept hub for terminal messages and related boundaries
- [[adyen]] — company page

## Raw Sources

- [[raw/adyen/docs/point-of-sale/design-your-integration/2026-09-15|Design your integration — Adyen Docs snapshot, 2026-09-15]]
