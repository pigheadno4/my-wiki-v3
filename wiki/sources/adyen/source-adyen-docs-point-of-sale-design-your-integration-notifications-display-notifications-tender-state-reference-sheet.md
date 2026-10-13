---
title: "Adyen Docs: POS tender states reference"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/design-your-integration/notifications/display-notifications/tender-state-reference-sheet"
raw_files:
  - "adyen/docs/point-of-sale/design-your-integration/notifications/display-notifications/tender-state-reference-sheet/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, display-notifications, tender-states]
---

## Overview

This Adyen Docs reference sheet explains **tender** states for a Terminal API integration with payment terminals. A tender spans the POS app starting a transaction, card or payment-method interaction, possible amount change, authorization wait, receipt handling, and final status. During it, terminal-generated display notifications can inform **staff in the POS app** about progress. The page distinguishes an ongoing tender state from a completed **tender result** and sends readers elsewhere for payment lifecycle statuses such as Received, Authorised, or Settled. See [[adyen-terminal-api]] and [[adyen]].

## Key takeaways

- **Scope:** Terminal API integration with payment terminals. The reference is a state glossary for POS tender/display-notification handling, not a guide to configuring callbacks or a statement that every state occurs for every payment method. [Raw: Requirements; introduction]
- **In progress:** the table includes shopper card, application, PIN, signature, DCC, donation, and gratuity interactions; balance/load/refund-related progress; receipt steps; and terminal processing. `ACKNOWLEDGED` specifically means the transaction is acknowledged but has not yet been approved, declined, cancelled, or failed. `PROCESSING_TENDER` means processing is under way. [Raw: In-progress tender states]
- **Completion:** the separate tender-result table defines `APPROVED`, `CANCELLED`, `DECLINED`, and `ERROR`. The in-progress table also lists `TENDER_FINAL` as tender completed; that label alone should not be read as `APPROVED` or as later payment settlement. [Raw: In-progress tender states; Tender result; Looking for payment statuses?]
- **Status boundary:** this page directs payment-status questions to a separate Payments lifecycle page. Its tender terms concern a terminal/POS interaction; do not substitute them for the platform lifecycle's Received, Authorised, or Settled status. The linked lifecycle page is navigation, not a source read here. [Raw: Looking for payment statuses?]

## Detail locators

- Raw `In-progress tender states` holds the full state-to-description table, including the exact card, payment-method, shopper, staff, and terminal actions.
- Raw `Tender result` lists four final tender outcomes and their meanings.
- Raw introductory paragraphs and `Requirements` delimit Terminal API with payment terminals and the staff-facing display-notification use.

## Related

- [[adyen-terminal-api]] — existing in-person API concept hub
- [[adyen]] — company and knowledge-status page

## Raw Sources

- [[raw/adyen/docs/point-of-sale/design-your-integration/notifications/display-notifications/tender-state-reference-sheet/2026-09-15|Tender states — Adyen Docs snapshot, 2026-09-15]]
