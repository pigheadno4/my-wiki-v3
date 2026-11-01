# C61 fixed-query answers — api-explorer-tokenization-webhooks-latest-post-recurring-token-created

Pinned raw: `raw/adyen/api-explorer/Tokenization-webhooks/latest/post/recurring.token.created/2026-09-15.md`. Canonical retrieval route: [[source-adyen-api-explorer-tokenization-webhooks-latest-post-recurring-token-created]]; URL: https://docs.adyen.com/api-explorer/Tokenization-webhooks/latest/post/recurring.token.created

## Q1

Adyen sends this incoming `recurring.token.created` webhook when a token is created (raw lines 5–7). Its required top-level fields are `createdAt`, `data`, `environment` (`test` or `live`), `eventId` (PSP reference of the triggering event), and outer `type` (webhook type); `version` is optional (14–24). Required nested `data` fields are `merchantAccount`, audit-description `operation`, `shopperReference`, `storedPaymentMethodId` (token ID), and nested `type` (payment-method type) (15–20). The sample shows `operation: "created"` and outer `type: "recurring.token.created"` (28–43), without defining an operation enum or token-use condition.

## Q2

The response section says HTTP 200 succeeds and any `2xx` status accepts the webhook; `notificationResponse` is optional and the table supplies no required literal value (raw lines 44–52). This receiver acceptance does not itself establish a later payment outcome, token usability, or deletion/propagation state. This 52-line page gives no delivery-order, retry, deduplication, signature or additional timing rule. It does not label an API version beyond the optional payload `version` field (raw lines 1–52). Retrieval route: [[source-adyen-api-explorer-tokenization-webhooks-latest-post-recurring-token-created]]; https://docs.adyen.com/api-explorer/Tokenization-webhooks/latest/post/recurring.token.created
