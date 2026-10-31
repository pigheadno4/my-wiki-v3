# C59 fixed-query answers: networkToken.created

Pinned raw: `raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.networkToken.created/2026-09-15.md` (SHA-256 `45c739d8fbc2f4c1914898e99a43dffe4acb89c1b29279105b2460b8a38a031b`). Canonical route: [Adyen API Explorer](https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.networkToken.created). Proposed source: [[source-adyen-api-explorer-balanceplatform-webhooks-latest-post-balanceplatform-networktoken-created]].

## Q1

The incoming event is labeled `balancePlatform.networkToken.created`, but the trigger states Adyen sends it when a provisioning request is initiated (raw lines 5–7). The envelope requires `data`, `environment` and `type`; `timestamp` is optional, and environment can be test or live (lines 11–48). All listed `data` properties are optional, including token and payment-instrument IDs, decision (`approved`, `declined`, `requiresAuthentication`), status, authentication and validation detail, risk results, token requestor and token type (`wallet` or `cof`) (lines 14–45). Validation reasons are conditional on invalid walletValidation; wallet detail is returned only for wallet type (lines 35–45).

## Q2

The event documents initiation of a token-provisioning request, not a guaranteed approved, authenticated or active token. Its decision enum explicitly includes decline and authentication-needed states (line 20). Optional risk scores and validation details are evidence fields, not payment or settlement results (lines 23, 29–45). Any HTTP `2xx` accepts the webhook (lines 50–58); this source states no event-specific delivery order, retry, deduplication or signature rule. The `latest` URL and fetched date denote a snapshot rather than a current fixed API version (lines 1–2).
