---
title: "Adyen Docs: POS penalty box"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/error-scenarios/penalty-box"
raw_files:
  - "adyen/docs/point-of-sale/error-scenarios/penalty-box/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, payment-network, aid-routing, error-handling]
---

## Overview

Adyen's POS “Penalty box” page, fetched 2026-09-15 with raw metadata last modified 2022-12-26, describes temporary handling of a **card application/payment-network route** when the connection to that payment network is unavailable. Adyen's platform marks the affected application; a terminal learns this when it tries to authorize through it and then temporarily avoids it where another route or eligible offline processing exists. This is not a generic local POS-to-terminal network circuit breaker, a payment time-out rule, or proof of an individual transaction's authorization. [[adyen]] · [[adyen-terminal-api]]

## Key takeaways

- Co-badged, combo, and US debit cards may have multiple applications, including a local payment method. A failed connection to one payment network can make that routed application unusable. The guide says Adyen's platform puts that application in a penalty box and routes through other connections until the network problem is resolved.
- The terminal is informed when it attempts authorization with the affected application and then puts that application in its own penalty box for the next couple of hours. While there, it checks for offline processing, trying offline EMV and then Store and Forward; these are conditional possibilities, not guaranteed approvals. If offline processing is unavailable, it skips the penalized application and uses another application on a multi-application card.
- With a **single-branded** card, the terminal still attempts authorization in case the outage has resolved, then tries offline processing if that fails. If no other application is available and offline processing is not possible, the transaction is declined. The raw's Cartes Bancaires/Visa example illustrates alternative routing, not a universal scheme or merchant entitlement.
- The page describes future live terminal updates about penalty-box additions/removals as a planned feature. Do not treat this future-tense statement as deployed current behavior or infer an exact production TTL from the test fixture.
- For a **test terminal and Adyen test card**, an amount ending in **158** simulates no offline route and no alternative application: the first transaction declines and the selected application is skipped by the test terminal for **four hours**. The sample `PaymentResponse` shows `Result=Failure`, `ErrorCondition=Refusal`, `refusalReason=235 AID banned`, and `message=ERROR`. Adyen says POS code may use `ErrorCondition` but should not key logic to the explanatory `refusalReason` or `message`. Optional test checks include Customer Area acquirer response and an `AUTHORISATION` webhook with `success=false` and reason `Application banned`.
- The guide applies to a Terminal API integration with payment terminals or a Mobile solution, and lists standard-webhook subscription for checking the test. It does not give a local-link repair procedure, a generic request retry policy, or permission to repeat an unresolved payment. Use transaction-status/error-handling guidance separately for missing responses.

## Detail locators

- **Network/application cause and scope:** raw lines 19–30. The unavailable link is to a **payment network** for a card application, not necessarily merchant internet, LAN, Wi-Fi, terminal cloud WebSocket, or account credentials.
- **Platform and terminal states:** “Preventing declined payments,” lines 32–48. Offline EMV precedes Store and Forward; alternative card application and single-brand fallback paths have distinct conditions. The live-update sentence is future-tense.
- **Test scenario:** “Testing,” lines 50–57 and 91–143. Suffix 158, test terminal/card, first decline, four-hour test penalty, response fields, Customer Area and webhook checks are all fixture-specific. The example `ProtocolVersion=3.0`, `ServiceID`, `POIID`, EUR amount, and timestamp are sample values, not account or software eligibility proof.
- **Codeable versus explanatory fields:** lines 94–101. `ErrorCondition` may drive the POS response handling; `refusalReason` and `message` are additional insight rather than stable logic keys.

## Related

- [[adyen-terminal-api]] — POS response and transaction-status boundary
- [[source-adyen-docs-point-of-sale-error-scenarios]] — separate missing-result and error-handling guide

## Related raw API references

Linked card-application selection, offline-payment, standard-webhook, test-card v2, and payment pages are navigation only; they were not read to extend this entry's behavior.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/error-scenarios/penalty-box/2026-09-15|Adyen POS Penalty box, fetched 2026-09-15]]
