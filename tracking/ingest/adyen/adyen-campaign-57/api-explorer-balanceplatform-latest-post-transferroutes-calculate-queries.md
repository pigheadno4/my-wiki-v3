# C57 fixed query answers: transfer route calculation

Canonical source route: [[source-adyen-api-explorer-balanceplatform-latest-post-transferroutes-calculate]] — https://docs.adyen.com/api-explorer/balanceplatform/latest/post/transferRoutes/calculate
Pinned raw: [[raw/adyen/api-explorer/balanceplatform/latest/post/transferRoutes/calculate/2026-09-15]] (captured 2026-09-15).

## Q1

This Configuration API v2 `POST /transferRoutes/calculate` returns candidate transfer routes from country, currency, counterparty and priorities before a separate transfer request (raw lines 5–10). The request-body **properties** `balancePlatform`, `category` (documented `bank` value) and `currency` are marked required; either `counterparty` or `country` must be present. The optional counterparty denotes a bank account or transfer instrument. `balanceAccountId` becomes required with `transferInstrumentId`; `bankAccount.accountIdentification` is marked required and its inner fields depend on country and currency (lines 14–26). The page does not separately state whole-body requiredness. Optional priorities specify speed/fee categories, including region- or recipient-qualified `instant`, `crossBorder` and `internal` descriptions (line 26). It lists a TEST `/bcl/v2` server (lines 9–10); 401/403 errors identify authentication/permission boundaries but no named role (lines 62–99).

## Q2

A 200 means the calculation request succeeded; optional `transferRoutes` may list country/currency/priority and requirements for a later request (raw lines 46–59). The NL/USD crossBorder and wire response is an example, including amount/address/identification/instrument rules, not general limits or current eligibility (lines 141–221). Error sections cover 401, 403, 422 and 500 with common problem details (lines 62–139). The 422 and 500 examples instead describe payment-instrument update/creation, so cannot establish route-specific validation or failure behavior (lines 249–275). Nothing here verifies a counterparty, approves a transfer, initiates the separate Transfers API request, books funds, or proves bank receipt. The `latest` URL captures a `/bcl/v2` TEST reference; no live execution or current availability is shown (lines 5–10).
