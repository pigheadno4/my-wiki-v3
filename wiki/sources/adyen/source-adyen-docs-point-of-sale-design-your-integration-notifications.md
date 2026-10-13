---
title: "Adyen Docs: POS notifications and webhooks overview"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/design-your-integration/notifications"
raw_files:
  - "adyen/docs/point-of-sale/design-your-integration/notifications/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, notifications, webhooks]
---

## Overview

This Adyen Docs overview separates **terminal-generated notifications** from **platform-generated webhooks** in a POS integration. Terminal notifications are JSON-formatted callbacks to a POS-system endpoint for staff awareness; platform-generated webhooks originate on Adyen's platform and go by HTTP callback to a merchant server endpoint. The page names categories and routes to their own setup guides. See [[adyen-webhooks]], [[adyen-terminal-api]], and [[adyen]].

## Key takeaways

- **Display notifications:** terminal-generated updates about progress of a tender, including shopper-terminal interaction or a payment-result message. Their purpose here is to keep POS staff informed; the overview does not define their payload, delivery handling, or payment finality. [Raw: terminal-notification bullets]
- **Event notifications:** terminal-generated updates about terminal availability and state, such as maintenance or shutdown. For **asynchronous cloud communications**, the page says event notifications **must** be set up so Terminal API responses are sent to the endpoint. These should not be conflated with display-progress messages. [Raw: event-notification bullet and cloud condition]
- **Platform-generated webhooks:** Adyen's platform sends HTTP callbacks to a merchant server endpoint. Listed POS use cases include refunds, manual capture, omnichannel shopper recognition, and terminal-management updates. Their actor and endpoint differ from terminal-generated notifications; the linked detail guide is needed for exact event structure and handling. [Raw: platform-generated paragraph]
- Each selected notification/webhook category requires setup. This is a navigation overview, not evidence that a particular merchant has configured callbacks or received a response. [Raw: final setup sentence; Next steps]

## Detail locators

- Raw introductory paragraph and terminal-notification bullets identify the terminal sender, POS endpoint, display versus event purpose, and the asynchronous cloud response requirement.
- Raw platform-generated paragraph identifies the platform sender, server endpoint, and example use cases.
- Raw `Next steps` links to the three detail pages. Those links are navigation targets, not evidence read for this entry.

## Related

- [[adyen-webhooks]] — existing provider notification/webhook concept hub
- [[adyen-terminal-api]] — in-person message and cloud response context
- [[adyen]] — company and knowledge-status page

## Raw Sources

- [[raw/adyen/docs/point-of-sale/design-your-integration/notifications/2026-09-15|Notifications and webhooks — Adyen Docs snapshot, 2026-09-15]]
