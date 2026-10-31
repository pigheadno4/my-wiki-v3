# C60 fixed-query answers: Forward API webhooks overview

Canonical retrieval route: [[source-adyen-api-explorer-forward-api-webhooks-latest-overview]] (`wiki/sources/adyen/source-adyen-api-explorer-forward-api-webhooks-latest-overview.md`); canonical URL: `https://docs.adyen.com/api-explorer/Forward-API-webhooks/latest/overview`. Pinned raw: `raw/adyen/api-explorer/Forward-API-webhooks/latest/overview/2026-09-15.md`.

## Q1

The captured API Explorer page is titled “Forward API webhook v1” (raw line 5). It says the Forward API sends payment requests to third-party services on the merchant's behalf and Adyen uses webhooks to notify the merchant of the result (lines 7–9). Its only endpoint row is `POST forwardApi.notification`, summarized as “Forward API request completed” (lines 11–16). This is a catalog, not an event-schema or relayed decision contract. It provides no event payload, required/conditional fields, type value, resource or request reference, response contract, trigger beyond the endpoint summary, state transition, or timing rule. The child `forwardApi.notification` reference must be read for those details; this overview alone cannot supply them.

## Q2

The overview establishes result-notification purpose and a “request completed” endpoint label (raw lines 7–9, 16). It does not define whether the third party accepted the forwarded request, whether a payment was authorized, captured, settled or final, or what an acknowledgement or response means. It has no delivery-order, retry, deduplication, signature, failure/reversal, or acceptance rules in its 16 lines. The page identifies the webhook family as v1 while the URL uses `latest`; both are 2026-09-15 snapshot evidence (lines 1–5), not proof of current version or availability. See [[source-adyen-api-explorer-forward-api-webhooks-latest-overview]] for the pinned raw and the child-reference navigation route.
