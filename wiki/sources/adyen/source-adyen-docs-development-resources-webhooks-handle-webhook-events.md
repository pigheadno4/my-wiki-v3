---
title: "Adyen Docs: Handle webhook events"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/webhooks/handle-webhook-events"
raw_files:
  - "adyen/docs/development-resources/webhooks/handle-webhook-events/2026-09-15.md"
tags: [adyen, webhooks, verification, acknowledgement, ordering, deduplication]
---

## Overview

This [[adyen]] documentation page is a 2026-09-15 snapshot of recommended receiver handling for Adyen webhook events. It separates authenticating and storing a message, acknowledging its delivery, and later applying business logic, then gives ordering and duplicate-handling guidance.

## Key takeaways

- Receiving starts with a webhook configured in Customer Area and a publicly accessible endpoint that does not redirect and is highly available. The documented handling sequence is to verify the message, store it in a database or queue, acknowledge it with a successful HTTP response such as `200` or `202`, and then process its data and apply business logic.
- The page says to verify that the message came from Adyen and was not modified in transit. It presents domain and IP allowlisting or basic authentication as security layers and HMAC signature verification as an additional strong measure; the HMAC signature must be verified before the payload is processed or used.
- Acknowledgement and business processing are separate. The receiver must return a successful HTTP status, such as `202`, within 10 seconds; the acknowledgement step says not to validate or process data there. If Adyen does not receive the response in time, it marks the webhook **Failing** and puts it in a retry queue. The page's earlier verify-before-accept sequence and its no-validation-at-acknowledgement wording should not be collapsed into an unsupported implementation ordering beyond the stated steps.
- Payloads contain headers and a JSON body. The body includes an `eventCode` or `type` and a timestamp; the receiver is told to check the timestamp for chronological processing, and some webhooks also provide identifiers such as `sequenceNumber` for ordering.
- Duplicate delivery is possible. The page characterizes duplicate events as sharing `eventCode` and `pspReference` while `eventDate` and other fields can differ, and directs the server to use details from the latest event. This is source-specific duplicate guidance, not a claim of globally unique keys, exactly-once delivery, or a complete idempotency design.
- Adyen server libraries are described as providing deserialization, verification, parsing, type-safety, and HMAC-validation tools. The snapshot names no exact library release and directs readers to each library's **Supported webhook versions**; it does not establish behavior for an unverified SDK or version.

> [!warning] Evidence boundary
> This documentation snapshot describes recommended webhook receiver behavior. It does not prove current endpoint availability, message authenticity before verification, ordered or exactly-once delivery, successful downstream business processing, account eligibility, or any payment or onboarding outcome. A successful acknowledgement is a delivery receipt, not proof that business logic completed.

## Detail locators

- Webhook purpose and secure/accept/process scope: `# Handle webhook events`, line 19.
- Customer Area configuration prerequisite and endpoint reachability, redirect, and availability requirements: `## How it works`, line 23.
- Verify, store, acknowledge, then process sequence and business-logic failure rationale: `## How it works`, lines 25-30.
- Authenticity and integrity verification, security layers, HMAC-before-processing requirement, and insecure-message warning: `## Verify webhooks`, lines 32-36.
- Successful-response acknowledgement, separation from validation or processing, 10-second deadline, **Failing** status, and retry-queue condition: `## Accept webhooks`, lines 38-40.
- Payload fields and timestamp or `sequenceNumber` ordering guidance: `### Webhook payload`, lines 46-48.
- Server-library parsing and verification capabilities plus supported-version route: `### Using an Adyen library to parse the payload`, lines 50-56.
- Duplicate possibility, identifying field comparison, differing dates or fields, and latest-event instruction: `### Handling duplicates`, lines 58-60.

## Related

- Company: [[adyen]]
- Concept: [[adyen-webhooks]]
- Configuration and endpoint setup: [[source-adyen-docs-development-resources-webhooks-configure-and-manage]]
- Retry-queue behavior and remediation: [[source-adyen-docs-development-resources-webhooks-troubleshoot]]
- HMAC verification: [[source-adyen-docs-development-resources-webhooks-secure-webhooks-verify-hmac-signatures]]

## Raw Sources

- [[raw/adyen/docs/development-resources/webhooks/handle-webhook-events/2026-09-15|Adyen Docs — Handle webhook events (2026-09-15)]]
