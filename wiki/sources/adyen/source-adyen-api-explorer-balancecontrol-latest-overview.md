---
title: "Adyen Balance Control API v2 overview"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/BalanceControl/latest/overview"
raw_files:
  - "adyen/api-explorer/BalanceControl/latest/overview/2026-09-15.md"
tags: [adyen, balance-control, api-explorer, balances, balance-transfers]
---

## Overview

This 2026-09-15 API Explorer snapshot identifies **Balance Control API v2** as an API to view and manage balances in Adyen company and merchant accounts. It lists company-level and merchant-level balance-view GET endpoints and a `POST /balanceTransfers` endpoint. This is an API family and account-balance scope distinct from Terminal API or Balance Platform resources. See [[adyen]] and [[adyen-account-structure]].

## Key takeaways

- Authentication guidance recommends an API key generated in Customer Area and instructs callers to send it in `X-API-Key`; the example also sends JSON `Content-Type`. The going-live text directs generation of a separate API key in live Customer Area. No role, permission, credential-to-account scope or response/error contract is specified here.
- Versioning is in the endpoint URL. The example test URL has `/balance-control/api/v2/balanceOverview/companies/{companyId}/balances`. The endpoint table instead names `{companyAccountCode}` for the company-balance GET path and `{merchantAccountCode}` for the merchant-balance GET path; do not silently equate these placeholder names.
- The Servers list gives test `https://balance-control-test.adyen.com/balance-control/api/v2` and live `https://balance-control-live.adyen.com/balance-control/api/v2`. The separate Going live paragraph instead gives `https://balance-control-live.adyen.com/api/v2`, omitting `/balance-control`. This snapshot does not resolve the live base-path conflict; verify the applicable endpoint before implementation.
- The endpoint table summarizes `GET /balanceOverview/companies/{companyAccountCode}/balances` as available balances for all merchant accounts under a company, `GET /balanceOverview/merchants/{merchantAccountCode}/balances` as balances for a merchant account, and `POST /balanceTransfers` as performing a balance transfer. The overview gives no POST request/response schema, required fields, limits, transfer eligibility, acceptance/state machine, timing, reversal or settlement/receipt rule. A listed endpoint is not evidence of an executed transfer or bank receipt.
- The page labels itself v2 but gives no v1 comparison, migration or deprecation rule. It supplies no device, terminal or session identity.

## Detail locators

- Identity/purpose and authentication: raw lines 5–20.
- Versioned test URL and divergent live URLs: raw lines 22–38.
- Listed endpoint methods, paths and summaries: raw lines 40–47.

## Related

- [[adyen]]
- [[adyen-account-structure]]

## Raw Sources

- [[raw/adyen/api-explorer/BalanceControl/latest/overview/2026-09-15|Adyen Balance Control API v2 overview snapshot, 2026-09-15]]
