# C60 relayed authorisation overview fixed-query answers

## Q1

The 2026-09-15 snapshot is titled “Authorization webhooks v4” and says Adyen sends webhooks about transaction authorization events (raw lines 5–7; [[source-adyen-api-explorer-relayed-authorisation-webhooks-latest-overview]]; https://docs.adyen.com/api-explorer/relayed-authorisation-webhooks/latest/overview). Its only listed general route is POST `balancePlatform.authorisation.relayed`, summarized as “Relayed authorization requested” (raw lines 9–14). This overview does not provide request or response fields, resource/reference identities, decision values, trigger timing, or a response deadline; those require the separately pinned [[raw/adyen/api-explorer/relayed-authorisation-webhooks/latest/post/balancePlatform.authorisation.relayed/2026-09-15|endpoint reference]] (unread here).

## Q2

This overview is a route catalog, so it does not establish what HTTP response or response body decides a relayed authorization, nor any capture, settlement or bank-receipt outcome (raw lines 5–14; [[source-adyen-api-explorer-relayed-authorisation-webhooks-latest-overview]]; https://docs.adyen.com/api-explorer/relayed-authorisation-webhooks/latest/overview). It gives no delivery, ordering, retry, deduplication or signature rules. The heading says v4 while the URL uses `latest`; both are properties of the captured 2026-09-15 page, not proof of current semantics (raw lines 1–5).
