# Fixed retrieval answers — Forward API forwardApi.notification

## Q1

[[source-adyen-api-explorer-forward-api-webhooks-latest-post-forwardapi-notification]] routes to the 2026-09-15 Adyen Forward API webhooks `latest` incoming notification ([canonical source](https://docs.adyen.com/api-explorer/Forward-API-webhooks/latest/post/forwardApi.notification)). The title says the Forward API request completed and the description says Adyen forwarded a payment request to a third-party service (raw lines 5–7). Outer `createdAt` and `type` are required; `data`, `environment`, and `version` are optional (lines 14–35). Within `data`, eventDateTime, externalPsp, merchant account/country/reference, Adyen request pspReference, scheme, shopperReference, and storedPaymentMethodId are marked required (lines 18–32). The example has `type: forwardApi.notification`, version `1`, and external status `Authorised` (lines 42–59), but example values do not establish a universal result.

## Q2

[[source-adyen-api-explorer-forward-api-webhooks-latest-post-forwardapi-notification]] shows 200 Success, says the request succeeded, and says any `2xx` HTTP status accepts the webhook via optional `notificationResponse` (raw lines 63–71; [canonical source](https://docs.adyen.com/api-explorer/Forward-API-webhooks/latest/post/forwardApi.notification)). The optional `externalPspTransactionStatus` is returned by the third-party service, and the optional found/requested booleans refer to reference-path matching (lines 19–25); these do not turn receiver acceptance into authorization or settlement proof. This page supplies no delivery/order/retry/deduplication/signature/finality rule. `latest` is a captured route label; the example's `version: \"1\"` is not a pinned contract guarantee.
