# Fixed retrieval answers — api-explorer-payment-webhooks-latest-overview

Pinned raw: `raw/adyen/api-explorer/payment-webhooks/latest/overview/2026-09-15.md`
Canonical source: [[source-adyen-api-explorer-payment-webhooks-latest-overview]]
Canonical URL: https://docs.adyen.com/api-explorer/payment-webhooks/latest/overview

## Q1 — purpose, identities, fields, limits and lifecycle

The captured `latest` overview displays **Payment webhooks (deprecated) v1** (raw line 5). It says Adyen sends these incoming platform notifications for payment-resource creation and money movements (line 9), and lists six POST paths: incoming/outgoing transfer created/updated and payment created/updated (lines 13–23). The payment-created summary covers initiated authorisation, refund or funds transfer; payment-updated covers authorisation expiry or cancellation (lines 22–23). It has no event request/response schema, ID contract, lifecycle timing or field requiredness. See [[source-adyen-api-explorer-payment-webhooks-latest-overview]] and https://docs.adyen.com/api-explorer/payment-webhooks/latest/overview.

## Q2 — deprecation and evidence boundaries

The page explicitly says Payment webhooks are deprecated and instructs readers to use “accounting webhooks,” linking the Transfer Webhooks overview (raw line 7). That is the source's wording and link; it does not itself describe Transfer or Transaction event behavior. Suggested dashboard/incoming-funds uses are illustrative (lines 9–11). The catalog gives no receiver acknowledgement, delivery/order/retry/deduplication/signature, transfer completion or financial-finality contract. See [[source-adyen-api-explorer-payment-webhooks-latest-overview]] and https://docs.adyen.com/api-explorer/payment-webhooks/latest/overview.
