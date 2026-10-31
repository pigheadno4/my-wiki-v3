# C60 fixed-query answers: terminalAssignment.completed

Canonical retrieval route: `wiki/sources/adyen/source-adyen-api-explorer-managementnotification-latest-post-terminalassignment-completed.md`; canonical URL: `https://docs.adyen.com/api-explorer/ManagementNotification/latest/post/terminalAssignment.completed`.

## Q1

The captured `ManagementNotification/latest` POST reference is an incoming `terminalAssignment.completed` notification that a terminal reassignment request completed (raw lines 5–7). This is a terminal-management event, not the merchant's reassign operation. Required body fields are `assignedToAccount` (merchant/company account ID), `eventDate` (completion time), `pspReference` (originating request reference), and `uniqueTerminalId` (terminal ID) (lines 11–19). Optional `assignedToStore` is a store reference/code and `assignedToStoreId` is a unique store ID (lines 15–16). This page gives no event-code or success-flag field, amount, currency, payment identity, or additional transition timing beyond the completed reassignment and `eventDate` (lines 5–19).

## Q2

The notification reports completion of a terminal reassignment request, not physical boarding, configuration application, payment readiness, or a financial outcome (raw lines 5–19). The response section lists `200 Success`, says the request succeeded, and marks `notificationResponse` optional while instructing any `2xx` HTTP response to accept the webhook (lines 21–29). That receiver acceptance is distinct from the assignment event. The 29-line reference gives no delivery-order, retry, deduplication, signature-verification, or subsequent device-state guarantee. `latest` is a captured API Explorer path; the immutable raw was fetched 2026-09-15 (lines 1–3). Follow the canonical source route above for the evidence and raw link.
