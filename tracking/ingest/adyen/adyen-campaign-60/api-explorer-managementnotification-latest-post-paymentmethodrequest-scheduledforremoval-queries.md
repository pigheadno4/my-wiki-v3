# api-explorer-managementnotification-latest-post-paymentmethodrequest-scheduledforremoval fixed queries

## Q1

The 2026-09-15 ManagementNotification `latest` POST paymentMethodRequest.scheduledForRemoval snapshot says an add-payment-method request will be removed in 30 days and directs provision of missing KYC information to make sure the method is added (raw lines 5–7; canonical source: https://docs.adyen.com/api-explorer/ManagementNotification/latest/post/paymentMethodRequest.scheduledForRemoval). It is an incoming ManagementNotification event, not a merchant removal operation. Required outer fields are `createdAt`, `data`, `environment` (test/live), and `type`; required nested `data` fields are `id`, `merchantId`, `status`, and `type` (payment-method variant) (lines 14–26). `data.status` can be success, failure, or capabilityPending; the last means `receivePayments` is not allowed. Optional allowed, enabled, and verificationStatus are separate permission, enablement, and verification states (lines 16–24). No request example or exact outer type value is shown.

## Q2

This event establishes scheduled removal of the add request after the stated 30-day horizon, not that removal has happened or that a payment method is enabled or payments can be received (raw lines 5–7, 16–24; canonical source: https://docs.adyen.com/api-explorer/ManagementNotification/latest/post/paymentMethodRequest.scheduledForRemoval). The response section accepts the webhook with any 2xx status and lists optional `notificationResponse`; receiver acceptance is separate from KYC, request success, capability approval, and payment processing (lines 28–36). The page gives no exact removal timestamp, subsequent removal event, delivery/order/retry/deduplication, signature, or reversal contract. `latest` is a captured label, not a fixed version.

Canonical source route: [[source-adyen-api-explorer-managementnotification-latest-post-paymentmethodrequest-scheduledforremoval]] — https://docs.adyen.com/api-explorer/ManagementNotification/latest/post/paymentMethodRequest.scheduledForRemoval.
