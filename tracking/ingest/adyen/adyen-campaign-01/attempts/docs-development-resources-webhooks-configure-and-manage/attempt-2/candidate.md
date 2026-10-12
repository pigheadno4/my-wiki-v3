---
title: "Adyen Docs: Configure and manage webhooks"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/webhooks/configure-and-manage"
raw_files:
  - "adyen/docs/development-resources/webhooks/configure-and-manage/2026-09-15.md"
tags: [adyen, webhooks, configuration, customer-area, retry]
---

## Overview

This [[adyen]] documentation page is a 2026-09-15 snapshot of the Customer Area workflow and server requirements for configuring, accepting, testing, updating, disabling, and deleting Adyen webhook subscriptions. It covers company, merchant, and merchant-group scope, while recommending company-level subscriptions with merchant inclusion or exclusion to reduce duplicate configurations.

## Key takeaways

- Processing requires a merchant server endpoint, Customer Area subscription setup, and successful acknowledgement of received events. The endpoint and environment requirements, supported methods, ports, authentication inputs, event selection, and optional additional settings are routed to the detailed sections below.
- The captured page broadly requires HTTPS endpoints with TLS 1.2 or 1.3, but its environment-specific list separately permits test HTTP on ports 80, 8080, or 8888, or test HTTPS on ports 443, 8443, or 8843; live permits only HTTPS on ports 443, 8443, or 8843. The endpoint URL configured in Customer Area must be public. OAuth 2.0 is documented only for Standard webhooks, and its access-token TTL must be at least 3599 seconds.
- Every webhook event must receive a successful HTTP response, such as `200` or `202`, within 10 seconds. Otherwise, the page says all webhook events to that endpoint enter the retry queue; acknowledgement is separate from the further handling steps linked by the page.
- Customer Area configuration testing and a recommended test-payment correlation exercise precede live setup. Test configuration does not prove production delivery, business outcome, or current account eligibility.
- Test webhook configurations are not copied into live. Live subscriptions must be configured and tested separately, and signature verification must use the live HMAC key rather than the different test key.

> [!warning] Disabling is not deletion
> Disabling a configuration queues events for that endpoint, and the captured page says queued events are delivered after reactivation. It also says configurations inactive for more than six months are automatically deleted. Plan maintenance and endpoint cutovers around both consequences rather than treating disablement as a durable pause.

## Detail locators

- Subscription scope, company-level recommendation, and duplicate/performance rationale: `# Configure and manage webhooks`, lines 17-23.
- Roles and prerequisite security guidance: `## Requirements`, lines 25-34.
- Three-step processing outline: `## How it works`, lines 36-42.
- Endpoint protocol, environment-specific ports, authentication preparation, and firewall navigation: `## 1. Expose an endpoint on your server`, lines 46-75.
- Customer Area scope and Payments-versus-Platforms level constraint: `## 2. Set up webhooks in your Customer Area`, lines 77-83.
- Configuration fields, security options, OAuth qualification and TTL, events, and additional settings: `## 2. Set up webhooks in your Customer Area`, lines 84-127.
- Response deadline and retry-queue consequence: `## 3. Accept webhooks`, lines 129-135.
- Customer Area configuration test and end-to-end test-payment correlation: `### Test your webhooks server`, lines 141-154, and `### End-to-end testing`, lines 156-158.
- Separate live setup, no-copy limitation, live testing, and environment-specific HMAC keys: `### Go live`, lines 160-165.
- Applying one company-level subscription to all, included, or excluded merchant accounts: `## Configure webhooks for multiple merchant accounts`, lines 167-183.
- Existing endpoint update and add-new-before-disable cutover route: `## Configure your existing webhook endpoint`, lines 185-215.
- Disablement, queued-event delivery after reactivation, six-month inactive deletion, and explicit deletion: `## Disable and delete webhook configurations`, lines 217-245.

The snapshot documents configuration behavior and recommendations, not current webhook availability for a particular account, successful delivery, successful downstream processing, or a payment outcome. Linked security, handling, troubleshooting, webhook-structure, and API pages are navigation unless separately retained and read.

## Related

- Company: [[adyen]]
- Concept: [[adyen-webhooks]]
- Event structure and type catalog: [[source-adyen-docs-development-resources-webhooks-webhook-types]]

## Raw Sources

- [[raw/adyen/docs/development-resources/webhooks/configure-and-manage/2026-09-15|Adyen Docs — Configure and manage webhooks (2026-09-15)]]
