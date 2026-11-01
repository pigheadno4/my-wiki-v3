# Fixed retrieval answers — api-explorer-acs-webhook-latest-post-balanceplatform-authentication-relayed

Pinned raw: `raw/adyen/api-explorer/acs-webhook/latest/post/balancePlatform.authentication.relayed/2026-09-15.md`
Canonical source: [[source-adyen-api-explorer-acs-webhook-latest-post-balanceplatform-authentication-relayed]]
Canonical URL: https://docs.adyen.com/api-explorer/acs-webhook/latest/post/balancePlatform.authentication.relayed

## Q1 — purpose, identities, fields, limits and lifecycle

Adyen sends this ACS incoming webhook when an issued-card cardholder must perform out-of-band authentication (raw lines 5–7). The request table requires `environment`, challenge `id`, `paymentInstrumentId`, `purchase` with date/merchant/original amount and its currency/minor-unit value, and notification `type` (lines 15–29). Optional `threeDSRequestorAppURL` supports auto-switching; without it the 3DS Requestor App does not support auto-switching. Optional `timestamp` is queue time (lines 27–28). The request example omits required `environment` and `type` (lines 31–47). See [[source-adyen-api-explorer-acs-webhook-latest-post-balanceplatform-authentication-relayed]] and https://docs.adyen.com/api-explorer/acs-webhook/latest/post/balancePlatform.authentication.relayed.

## Q2 — response and outcome boundaries

The receiver must send **HTTP 200** with required `authenticationDecision.status` of `refused` or `proceed`; if Adyen does not receive the response within **two seconds**, the authentication process stops (raw lines 9–11, 48–57). The sample `proceed` response is illustrative (lines 124–135). This is the ACS authentication decision handoff, not final cardholder challenge completion, payment authorisation, capture or settlement; the separate Issuing OOB guide describes a later ACS challenge-finalization step. Generic error sections 400/401/403/422/500 list optional diagnostic fields (raw lines 60–122). This endpoint page states no general retry, fallback or signature policy. See [[source-adyen-api-explorer-acs-webhook-latest-post-balanceplatform-authentication-relayed]] and https://docs.adyen.com/api-explorer/acs-webhook/latest/post/balancePlatform.authentication.relayed.
