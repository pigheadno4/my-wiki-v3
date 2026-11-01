# Fixed-query check: recurring.token.disabled

## Q1

This captured Tokenization webhooks `latest` event reference says Adyen sends `recurring.token.disabled` when a stored-payment-method token is disabled, such as after merchant deletion of stored details or third-party disablement. The related family overview identifies v1; this event page's `version` entity field is optional. Required event fields are `createdAt`, `data` (with `merchantAccount`, `shopperReference`, `storedPaymentMethodId`, payment-method `type`), `environment`, `eventId` and outer `type`. `eventId` is the triggering event PSP reference, while `storedPaymentMethodId` identifies the token. See [[source-adyen-api-explorer-tokenization-webhooks-latest-post-recurring-token-disabled]], [[raw/adyen/api-explorer/Tokenization-webhooks/latest/post/recurring.token.disabled/2026-09-15|raw lines 5–23]], and [Adyen API Explorer](https://docs.adyen.com/api-explorer/Tokenization-webhooks/latest/post/recurring.token.disabled).

## Q2

The receiver accepts this webhook with any 2xx HTTP status, per its response table. That receipt acknowledgement is separate from token disablement and from any later payment authorization. The pinned page gives no propagation timing, retry, ordering, deduplication, signature, or payment outcome rule; the example is illustrative. See [[source-adyen-api-explorer-tokenization-webhooks-latest-post-recurring-token-disabled]], [[raw/adyen/api-explorer/Tokenization-webhooks/latest/post/recurring.token.disabled/2026-09-15|raw lines 25–50]], and [Adyen API Explorer](https://docs.adyen.com/api-explorer/Tokenization-webhooks/latest/post/recurring.token.disabled).
