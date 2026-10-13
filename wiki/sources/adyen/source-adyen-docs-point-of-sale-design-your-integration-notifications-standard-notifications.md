---
title: "Adyen POS platform-generated webhooks"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/design-your-integration/notifications/standard-notifications"
raw_files:
  - "adyen/docs/point-of-sale/design-your-integration/notifications/standard-notifications/2026-09-15.md"
tags: [adyen, point-of-sale, webhooks, standard-webhooks, terminal-management]
---

## Overview

This Adyen Docs page describes **platform-generated** webhooks relevant to in-person payments: Standard webhooks about payment activity and terminal-management webhooks about terminal orders, assignment, boarding, and settings. They arrive at a merchant backend from Adyen's payments platform. They are distinct from terminal-generated EventNotification or DisplayRequest messages and from a Terminal API payment response.

## Key takeaways

- Standard webhooks support asynchronous POS-related outcomes, including refunds, authorization adjustment, manual capture, and cancellation of uncaptured authorization; the page also lists offline-payment PSP-reference reconciliation, cross-channel insights, and recurring online payments after POS token creation. Terminal approval/decline feedback is immediate, and a missing Terminal API transaction response can be checked with a transaction-status request; a Standard webhook is a separate platform event, not the immediate terminal response.
- For Standard webhooks, configure event codes and optional additional-data settings for identifiers needed by the use case. The page's table maps fields such as alias, funding source, issuer country, BIN, POIID, store, and tender reference to settings. Some identifiers, including Payment Account Reference and recurring detail reference, require **Developers > Additional data** rather than or in addition to webhook settings; enabling them there also adds them to API responses. The JSON example is illustrative (`live: false`, `AUTHORISATION`, `success: true`), not a guarantee of delivered fields or finality for another event/environment.
- Terminal-management webhooks have a **different structure** from Standard webhooks. They cover completed terminal assignment, successful boarding, terminal-order updates, and terminal-settings updates. The guide says they need no further setup beyond Customer Area server and security configuration; do not apply the Standard event-code or `additionalData` table to these payloads.
- The setup section directs receivers to verify webhook HMAC signatures and acknowledge with a successful HTTP status such as `202`. Its linked general webhook docs carry the detailed verification and delivery rules; this POS page alone does not define a complete security or retry contract.

## Detail locators

- Platform origin, two webhook categories, HMAC and acknowledgment pointers: `# Platform-generated webhooks` and `## Set up webhooks`, raw lines 15–34.
- Standard POS use cases, terminal-result distinction, event-code/additional-data settings, and illustrative `AUTHORISATION` payload: `## Standard webhook`, raw lines 36–129. The exact identifier/settings mapping is at lines 55–78.
- Terminal-management payload distinction, setup boundary, event types, and examples: `## Terminal management webhooks`, raw lines 131–235. Example environment values belong to their individual samples.

## Related

- [[adyen]] — provider context.
- [[adyen-webhooks]] — platform-generated webhook concept, verification, and backend handling.
- [[adyen-terminal-api]] — separate POS-to-terminal messages and transaction-status recovery.
- [[source-adyen-docs-point-of-sale-design-your-integration-notifications-event-notifications]] — terminal-generated event messages and cloud response delivery.
- [[source-adyen-docs-point-of-sale-design-your-integration-notifications-display-notifications]] — terminal-generated display messages.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/design-your-integration/notifications/standard-notifications/2026-09-15|Adyen Docs: Platform-generated webhooks (2026-09-15 snapshot)]]
