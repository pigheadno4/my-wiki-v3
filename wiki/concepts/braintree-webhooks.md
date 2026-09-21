---
title: "Braintree Webhooks"
type: concept
category: technology
tags: [braintree, webhooks, notifications, gateway-events]
---

## Braintree Webhooks

Braintree Webhooks are the gateway's push-notification mechanism for important events. For merchant-selected triggers, Braintree sends an HTTPS POST to a merchant server; each notification contains a notification kind and the Braintree object being reported, allowing the merchant to update internal state or start a business process.

## Configuration and operating boundaries

The destination must be a valid HTTPS path, and the Control Panel user who configures it needs webhook permission on their role. The overview covers event families including ACH Direct Debit transaction statuses, subscription, payment-method, account, dispute, fraud, OAuth, local-payment, disbursement, and test notifications; dedicated references own the trigger and notification-kind details.

Braintree states that it strives to send notifications as quickly as events occur, but the overview does not establish a delivery-time guarantee. Simultaneous subscription billing can produce a flood of notifications in a short period, so integrations should be designed for burst volume. That overview itself does not define retry, ordering, duplicate-delivery, signature-verification, or parsing semantics. [[source-braintree-webhooks-overview]]

The dedicated Node.js parsing guide documents parsing the `bt_signature` parameter together with the signed `bt_payload` parameter, an invalid-signature exception, non-sequential arrival, and hourly retries when the handler does not return a successful HTTPS `2xx` response within 30 seconds; the retry window is up to 3 hours in sandbox and 24 hours in production. These guide-specific conditions do not establish a general delivery-time or sequential-delivery guarantee. [[source-braintree-webhooks-parse-node]]

## Sources

- [[source-braintree-webhooks-local-payment-methods-node]] - Node.js instant local-payment completion and reversal versus non-instant funding and expiry events, with the completion event's separate nonce-based Transaction Sale route

- [[source-braintree-webhooks-oauth-node]] - Node.js OAuth access-revocation notification for connected merchants, with production closed-beta and sandbox open-beta qualifications plus payload and parsing routes

- [[source-braintree-webhooks-grant-api-node]] - Node.js Grant API notifications for updates to previously granted payment instruments and grantor revocation, with side-qualified update kinds and broad payload-category routes

- [[source-braintree-webhooks-fraud-protection-node]] - Node.js `transaction_reviewed` notification for an accepted or rejected Fraud Protection Dashboard review, with requested-not-completed void/refund scope and review payload categories

- [[source-braintree-webhooks-account-updater-node]] - feature-restricted Account Updater daily-report webhook, including its 24-hour updated-method scope, no-updates suppression, payload-category route, and one-week report-link expiry

- [[source-braintree-webhooks-transaction-node]] - Node.js ACH and SEPA Direct Debit transaction settlement notification kinds, qualified post-settled decline wording, and damaged availability/attribute-rendering boundaries

- [[source-braintree-webhooks-dispute-node]] - Node.js dispute notification kinds, event-condition catalog, PayPal-qualified internal-review trigger, and notification-attribute/deprecation route

- [[source-braintree-webhooks-subscription-node]] - Node.js subscription notification kinds with event-specific charge, activation, past-due and skipped-billing trigger qualifications, plus the 20-most-recent-transactions payload limit

- [[source-braintree-webhooks-payment-method-node]] - Node.js payment-method webhook notification kinds and payload routes, with currently documented PayPal billing-agreement cancellation and Venmo revocation or enabled Enriched Customer Data update triggers

- [[source-braintree-webhooks-testing-go-live-node]] — Node.js routes for merchant-posted sample payloads and Control Panel-delivered test notifications, with dummy-object and notification-kind handling cautions

- [[source-braintree-webhooks-create-node]] — Control Panel webhook creation, exact **Manage Webhooks** permission, public HTTPS destination, minimum notification selection, and multiple-endpoint routing

- [[source-braintree-webhooks-parse-node]] — Node.js `bt_signature` plus signed-`bt_payload` parsing, invalid-signature failure, non-sequential arrival, and response-conditioned retry timing

- [[source-braintree-webhooks-overview]] — notification purpose, HTTPS delivery, event-family routing, permissions, and burst-volume warning
