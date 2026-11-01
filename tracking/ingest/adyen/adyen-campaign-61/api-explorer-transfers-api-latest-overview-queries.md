# Fixed retrieval answers — api-explorer-transfers-api-latest-overview

Pinned raw: `raw/adyen/api-explorer/transfers-api/latest/overview/2026-09-15.md`
Canonical source: [[source-adyen-api-explorer-transfers-api-latest-overview]]
Canonical URL: https://docs.adyen.com/api-explorer/transfers-api/latest/overview

## Q1 — actual family, version, purpose and routes

Despite its `transfers-api` URL, this captured overview is headed **Raise disputes API v4** and identifies an Issuing Disputes API for issued-card transactions and fraud reports (raw lines 5–7). It describes raising disputes, adding attachments, updating information, chargeback submission and closure in prose, while its eight listed endpoints cover dispute list/create, attachment list/add/get/delete and dispute get/PATCH only (lines 49–61). It says `X-API-Key` or basic authentication, an additional unspecified credential role, a `vXX` URL suffix, and separate TEST/LIVE v4 bases (lines 9–47). The catalog has no individual request or response schemas. See [[source-adyen-api-explorer-transfers-api-latest-overview]] and https://docs.adyen.com/api-explorer/transfers-api/latest/overview.

## Q2 — result and family boundaries

A catalog entry does not show a dispute submission, closure, attachment deletion outcome, chargeback result, funds movement or financial finality. The introduction mentions submit/close, but the visible endpoint table has no separate submit/close route (raw lines 7, 54–61). The URL-family mismatch should remain explicit; the distinct `transfers/latest/overview` Transfers API v4 source governs funds movement and must not be imported into this dispute catalog. This page gives no delivery/acknowledgement contract because it documents API routes, not incoming webhooks. See [[source-adyen-api-explorer-transfers-api-latest-overview]] and https://docs.adyen.com/api-explorer/transfers-api/latest/overview.
