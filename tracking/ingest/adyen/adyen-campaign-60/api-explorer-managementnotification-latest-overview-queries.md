# C60 ManagementNotification overview fixed retrieval queries

Canonical retrieval route: `wiki/sources/adyen/source-adyen-api-explorer-managementnotification-latest-overview.md` — https://docs.adyen.com/api-explorer/ManagementNotification/latest/overview. Pinned raw: `raw/adyen/api-explorer/ManagementNotification/latest/overview/2026-09-15.md`.

## Q1

The captured overview is labeled **Management Webhooks v3** (raw line 5). Adyen describes incoming notifications about company and merchant accounts, stores, payment terminals and payment methods in the Management API context, sent as HTTP POST requests with event details in the body to a merchant-server URL (lines 7–9). The General table lists eight POST routes: `merchant.created`, `merchant.updated`, `paymentMethod.created`, `paymentMethodRequest.removed`, `paymentMethodRequest.scheduledForRemoval`, `terminalAssignment.completed`, `terminalBoarding.triggered`, and `terminalSettings.modified` (lines 13–25). The short summaries identify creation, capability update, removal/scheduled removal, assignment completion, boarding result and settings update. This overview does not provide event-specific resource identifiers, required fields, example payloads, response bodies, state-transition detail or timing rules; use an individual reference for those.

## Q2

The overview establishes event notification direction and catalog scope, not receipt acceptance or a completed business action beyond each route's one-line description (raw lines 7–25). It has no response/acknowledgement section and no delivery, ordering, retry, deduplication, signature, failure/reversal or finality guarantee. The `latest` URL is a captured path label while the page names Management Webhooks v3 (lines 1–5). A listed terminal or merchant-capability event does not establish a specific resource's current state or payment readiness.
