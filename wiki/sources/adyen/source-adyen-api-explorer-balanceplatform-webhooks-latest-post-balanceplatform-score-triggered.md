---
title: "Score signal triggered webhook | Adyen API Explorer"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.score.triggered"
raw_files:
  - "adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.score.triggered/2026-09-15.md"
tags: [adyen, balance-platform, webhooks, score, account-holder-risk]
---

## Overview

This captured Adyen Balance Platform webhook POST reference describes the incoming `balancePlatform.score.triggered` event: for merchants opted in to Score, Adyen sends it when a score signal is triggered against an account holder. The `latest` route does not resolve a numbered webhook API version in this capture. A signal is risk information, not a finding of fraud or proof of a financial action. [[adyen]] [[adyen-platforms]] [[adyen-webhooks]]

## Key takeaways

- The request-body table requires outer `data`, `environment`, and `type`; `timestamp` is optional. Every listed `data` child is optional: `accountHolder` (and its `description`, `id`, `reference`), `accountHolderStatus`, `automatedActions`, `balancePlatform`, `creationDate`, resource `id`, `riskScore`, `scoreSignalsTriggered`, and `signalSourceTypes`. The page therefore does not guarantee that a given payload contains a score, action, account-holder ID or signal list. [Raw: Request body, lines 11–29]
- `accountHolder.id` identifies the account-holder resource, while `data.id` is separately described only as an ID of the resource. The related [[source-adyen-docs-platforms-manage-account-holder-risk|Platforms Score guide]] identifies `data.id` in its example as a score calculation/recalculation ID; do not conflate it with the account-holder ID. The `automatedActions` field, if present, lists actions taken as a result of triggered signals; `riskScore` is a score resulting from those signals. [Raw: lines 15–26; related guide: Webhook setup and identity]
- The test example shows account-holder status `Active`, a `riskScore` of 67, signal names and source types, and `bumpKYCTier` as an automated action. Those sample values are not a universal threshold, current account state, confirmed fraud, verification result or payout outcome. `environment` may be `test` or `live`; any `2xx` response accepts the webhook, independently of later review or operational outcomes. [Raw: lines 27–75]

## Detail locators

- Opt-in scope and signal trigger: opening statement, lines 5–7.
- Payload optionality, identities, action/score/signal fields: Request body, lines 11–29.
- Illustrative account holder, score, signals and action: Request example, lines 31–66.
- Receiver `2xx` acknowledgement: Responses, lines 67–75.

## Related

- [[adyen-platforms]] — platform-user and Score context.
- [[adyen-webhooks]] — incoming event and acknowledgement context.
- [[source-adyen-docs-platforms-manage-account-holder-risk]] — product availability, Score cases and the example score-calculation versus account-holder identity distinction.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.score.triggered/2026-09-15|Adyen Balance Platform Score signal webhook — captured 2026-09-15]]
