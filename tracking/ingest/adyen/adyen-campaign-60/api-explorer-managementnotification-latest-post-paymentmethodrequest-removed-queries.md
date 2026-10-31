# Fixed retrieval answers — api-explorer-managementnotification-latest-post-paymentmethodrequest-removed

Canonical source: [[source-adyen-api-explorer-managementnotification-latest-post-paymentmethodrequest-removed]]; URL: https://docs.adyen.com/api-explorer/ManagementNotification/latest/post/paymentMethodRequest.removed. Pinned raw: `raw/adyen/api-explorer/ManagementNotification/latest/post/paymentMethodRequest.removed/2026-09-15.md`.

## Q1

The captured ManagementNotification `POST paymentMethodRequest.removed` event says an add-payment-method request was removed and another request must be made (raw lines 5–7). Required top-level body fields are `createdAt`, `data`, `environment` and notification `type`; required fields inside `data` are resource `id`, `merchantId`, request `status`, and payment-method-variant `type` (lines 11–26). The two `type` fields have different scopes. `status` lists success/failure/capabilityPending with descriptions (line 21), but no example establishes which status accompanies this removal event. Optional `allowed`, `enabled`, `reference`, `storeId`, and `verificationStatus` are described in lines 16–24. `createdAt` timestamps webhook creation; no removal timing is specified.

## Q2

The response says return any `2xx` HTTP status to accept the webhook, with optional `notificationResponse` (raw lines 28–36). This is receiver acceptance, not proof that a payment method is enabled, screening has allowed `receivePayments`, or a payment succeeded. The event says an add request was removed and must be remade (lines 5–7); it does not say an already-added method was removed. The page gives no delivery/order/retry/deduplication/signature rule, no financial outcome, and no deprecation statement. `latest` is the captured path label rather than evidence of later versions.
