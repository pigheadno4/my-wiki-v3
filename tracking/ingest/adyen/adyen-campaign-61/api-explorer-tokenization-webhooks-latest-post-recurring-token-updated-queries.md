# Fixed retrieval answers — api-explorer-tokenization-webhooks-latest-post-recurring-token-updated

Pinned raw: `raw/adyen/api-explorer/Tokenization-webhooks/latest/post/recurring.token.updated/2026-09-15.md`
Canonical source: [[source-adyen-api-explorer-tokenization-webhooks-latest-post-recurring-token-updated]]
Canonical URL: https://docs.adyen.com/api-explorer/Tokenization-webhooks/latest/post/recurring.token.updated

## Q1 — purpose, identities, fields, limits and lifecycle

Adyen sends this incoming tokenization webhook when a stored token is updated, including a merchant stored-details update or a card-network update (raw lines 5–7). The table requires top-level `createdAt`, `data`, `environment`, `eventId` and `type`, and nested `merchantAccount`, `operation`, `shopperReference`, `storedPaymentMethodId` and payment-method `type` (lines 12–24). `storedPaymentMethodId` names the token; `eventId` is the triggering event PSP reference (lines 19, 22). `operation` is audit text, not a listed enum; the example happens to say `updated` (lines 17, 38). `version` is optional and described as the entity version (line 24). See [[source-adyen-api-explorer-tokenization-webhooks-latest-post-recurring-token-updated]] and https://docs.adyen.com/api-explorer/Tokenization-webhooks/latest/post/recurring.token.updated.

## Q2 — acceptance and evidence boundaries

The receiver accepts this webhook with any `2xx` HTTP status (raw lines 44–52). The acknowledgement does not establish payment authorization, token use, or a financial outcome. The page does not state delivery order, retry, deduplication or signature mechanics; the example is a test-environment payload, not evidence of a particular live delivery (lines 28–43). See [[source-adyen-api-explorer-tokenization-webhooks-latest-post-recurring-token-updated]] and https://docs.adyen.com/api-explorer/Tokenization-webhooks/latest/post/recurring.token.updated.
