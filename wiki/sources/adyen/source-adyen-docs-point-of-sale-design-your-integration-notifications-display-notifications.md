---
title: "Adyen Docs: Display notifications for POS apps"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/design-your-integration/notifications/display-notifications"
raw_files:
  - "adyen/docs/point-of-sale/design-your-integration/notifications/display-notifications/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, display-notifications, webhooks]
---

## Overview

This Adyen Docs webpage describes terminal-generated **display notifications** during a transaction or tender. A configured endpoint receives a webhook containing a Terminal API `DisplayRequest`; its `ReferenceID` carries an `event` about terminal–shopper interaction or a `Result` associated with transaction outcome. The intended use here is to show staff a progress message in a POS app. Treat this as the display-notification surface, distinct from the linked event-notification and platform-generated webhook pages; a display message by itself is not documented here as a complete payment state machine. See [[adyen-terminal-api]] and [[adyen]].

## Key takeaways

- Configure a JSON-capable HTTP callback endpoint and a display URL through either Customer Area device settings or Management API `/terminalSettings`. The API path requires the **Management API - Terminal settings Advanced read and write** role; its `nexo.displayUrls` settings distinguish local and public URLs. Configuration can be at company, merchant, store, or terminal level. Check higher-level inheritance before removing settings. [Raw: Set up display notifications in the Customer Area; Set up display notifications using API calls]
- The snapshot lists test callback ports for HTTP (80, 8080, 8888) or HTTPS (443, 8443, 8843) with TLSv1.2, while live lists HTTPS (443, 8443, 8843) with TLSv1.2. Customer Area also offers optional basic-auth credentials and encryption; the Management API example is illustrative, not a general schema guarantee. [Raw: setup headings, endpoint requirements and examples]
- On receipt, store the display notification, return a successful HTTP status (202 is an example), then apply business logic. Adyen says acknowledgement prevents repeated sends and warns that logic errors before acknowledgement can prevent important event notifications from reaching the system. [Raw: Accept display notifications]
- `ReferenceID` uses `event` for terminal–customer interaction or `Result` for the transaction outcome. The type table includes tender start/final, card/PIN/signature, DCC, gratuity, gift-card load and balance-query progress. `TENDER_FINAL` covers a completed **or abandoned** tender and includes `Result`, timestamp, and transaction ID; do not equate the event name alone with payment success. [Raw: Display notification types]

## Detail locators

- Raw `Set up display notifications in the Customer Area` and `Set up display notifications using API calls` give the two configuration paths, callback prerequisites, scope, URL choices, and illustrative request/response.
- Raw `Accept display notifications` gives the acknowledgement sequence and the warning about applying business logic first.
- Raw `Display notification types` gives the `ReferenceID` distinction and event table; raw `Examples` gives JSON and Java illustrations, including `MessageCategory: Display` and `CashierDisplay`. Example values are historical samples, not independently verified current SDK or terminal requirements.

## Related

- [[adyen-terminal-api]] — existing Terminal API concept hub
- [[adyen]] — company and knowledge-status page

## Raw Sources

- [[raw/adyen/docs/point-of-sale/design-your-integration/notifications/display-notifications/2026-09-15|Display notifications — Adyen Docs snapshot, 2026-09-15]]
