---
title: "Balance-account sweep created webhook | Adyen API Explorer"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountSweep.created"
raw_files:
  - "adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountSweep.created/2026-09-15.md"
tags: [adyen, balance-platform, webhooks, sweeps]
---

## Overview

This captured Adyen Balance Platform webhook POST reference describes the incoming `balancePlatform.balanceAccountSweep.created` event sent when a sweep is successfully created. The event concerns a sweep configuration, not execution of a sweep transfer or booking of funds. The `latest` route in this capture does not establish a numbered webhook API version. [[adyen]] [[adyen-webhooks]] [[adyen-platforms]]

## Key takeaways

- At the outer request-body level, `data`, `environment`, and `type` are marked required; `timestamp` is optional. Within `data`, `accountId`, `balancePlatform`, and `sweep` are all marked optional. If the `sweep` object is present, its field rows mark `counterparty`, `currency`, `id`, and `schedule` required. The table says the counterparty needs one of `balanceAccountId`, `transferInstrumentId`, or `merchantAccount`, according to sweep direction; it does not make the optional parent `sweep` mandatory. [Raw: Request body, lines 11–36]
- The schema describes `push` as moving funds out and `pull` as moving funds in; omitted sweep `type` defaults to `push`. Omitted `status` defaults to `active`; `inactive` cannot be triggered. The schedule governs threshold evaluation. For `pull`, a balance at or below `triggerAmount` triggers pulling in; for `push`, a balance at or above it triggers pushing out. The trigger defaults to zero if absent. `sweepAmount` and `targetAmount` are alternatives. These describe configuration and potential trigger behavior, not a completed transfer. [Raw: Request body, lines 28–33]
- `category` may be `bank` or `internal` and is described as required when setting optional `priorities`; the listed priority options apply to bank-transfer routing. The example is a test-environment, active, weekly `push` to another balance account in EUR with zero target and trigger amounts. Those example values do not constrain every sweep or prove funds moved. Any `2xx` HTTP status accepts the webhook; acknowledgement is separate from later transfer outcomes. [Raw: lines 18–23, 38–80]

## Detail locators

- Creation event purpose: opening statement, lines 5–7.
- Full payload table and nested requiredness: Request body, lines 11–36.
- Direction, schedule, status, amount and priority semantics: Request body, lines 18–33.
- Illustrative envelope and receiver response: Request examples and Responses, lines 38–80.

## Related

- [[adyen-webhooks]] — incoming event and receiver acknowledgement context.
- [[adyen-platforms]] — platform sweep and balance-account context.
- [[source-adyen-docs-platforms-top-up-balance-account-scheduled-top-ups]] — a pull-sweep creation guide that distinguishes the configuration event from later top-up transfer outcomes.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountSweep.created/2026-09-15|Adyen Balance Platform sweep created webhook — captured 2026-09-15]]
