---
title: "Webhook event logs | Adyen Docs"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/logs-resources/webhook-event-logs"
raw_files:
  - "adyen/docs/development-resources/logs-resources/webhook-event-logs/2026-09-15.md"
tags: [adyen, webhooks, event-logs, troubleshooting, test-environment]
---

## Overview

This 2026-09-15 Adyen Docs snapshot describes **test-environment Customer Area webhook event logs** for testing and troubleshooting webhook delivery. The list shows events sent to the merchant server and their request/response details. It is a delivery-diagnostics view, not proof that the merchant processed an event or that a payment reached a financial final state. See [[adyen]] and [[adyen-webhooks]].

## Key takeaways

- Viewing logs requires the **Merchant admin** or **Merchant technical integrator** Customer Area role. In the test Customer Area, a user can stay on the company account or select a merchant account; balance-platform integration webhook logs are available on the company account.
- The **Developers > Webhook event logs** view lists test-environment events from the past **30 days**. Each event exposes relevant timestamps and merchant response time, event code/identifier, PSP reference or resource ID, and request/response bodies. Selecting a row also shows the endpoint URL and full request/response details.
- A user can search by PSP reference, resource ID, or order reference, and filter by endpoint URL, status, or date. Those are UI diagnostic routes, not an API endpoint or an archive beyond the stated test window.
- The existence of a sent event or an endpoint response in the log does not alone establish that the merchant verified, persisted, or processed the event, or that the event reports a final successful payment. The event type and payload must be interpreted in its own lifecycle context. This page does not state equivalent live-environment log availability or retention.

## Detail locators

- Test-environment purpose and sent-event diagnostic fields: lines 15–28.
- Required Customer Area user roles: `Viewing your webhook event log`, lines 30–36.
- Company/merchant/balance-platform account location and 30-day test list: lines 37–41.
- Search and filter choices: lines 43–46.
- Separate webhook, notification, and API-log routes: `See also`, lines 48–52.

## Related

- [[adyen-webhooks]] — webhook delivery, acknowledgment, and business-processing boundaries.
- [[source-adyen-docs-development-resources-webhooks-troubleshoot]] — separate webhook troubleshooting and retry-queue guide.

## Raw Sources

- [[raw/adyen/docs/development-resources/logs-resources/webhook-event-logs/2026-09-15|Webhook event logs (2026-09-15)]]
