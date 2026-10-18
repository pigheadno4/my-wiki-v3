---
title: "Adyen Platforms on-demand internal fund transfers"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/internal-fund-transfers/on-demand-fund-transfers"
raw_files:
  - "adyen/docs/platforms/internal-fund-transfers/on-demand-fund-transfers/2026-09-15.md"
tags: [adyen, platforms, internal-transfers, transfers-api, balance-accounts]
---

## Overview

This Adyen for Platforms guide (last modified 2020-09-11; captured 2026-09-15) describes initiating an on-demand push or internal direct debit between balance accounts by Customer Area or Transfers API. The source balance account is debited and a counterparty balance account is credited; this is distinct from a payout to an external bank-account transfer instrument. The guide covers prerequisites, optional review and future execution, failure checks, and two-sided status evidence. See [[adyen]], [[adyen-platforms]] and [[adyen-platform-internal-transfers]].

## Key takeaways

- **Access and account gates:** The page requires an Adyen for Platforms integration and source-account transfer enablement via Adyen Support. It lists the TransferService Webservice Initiate API role, and Customer Area Initiate internal transfers plus Balance platform base roles. Configure a server to accept Transfer webhooks and subscribe to them. Where source and target balance accounts belong to different account holders, the sending account holder needs sendToBalanceAccount and the receiving account holder needs receiveFromBalanceAccount. A missing capability or failed required review can fail the request; role possession or a request alone does not show account eligibility or booking. The page does not list a reserve-account route or a universal supported-currency set.
- **Request identity and response:** Customer Area selects a source balance account, counterparty type balanceAccount, target balance-account ID, currency and amount. For POST /transfers, the body table marks amount (currency/value), balanceAccountId (source), counterparty.balanceAccountId (target) and category internal as required; description, reference and referenceForBeneficiary are optional. The examples call the test /btl/v4/transfers endpoint and show EUR 100 as value 10000; the Customer Area illustration separately uses EUR 150. A sample API response is status received, reason pending with transfer ID: it establishes a created request, not a booked debit/credit. See raw for reference character limits and dated SDK examples.
- **Review and future execution:** Adyen's own checks precede approval. The optional review object permits one additional team approval; when requested, a team member must approve before processing. A future executionDate.date must be ISO YYYY-MM-DD within 30 days; the request stays received/pending until that date. The guide describes a 00:00–03:00 execution window and then checks available source funds and required team approval. It says Adyen attempts the future transfer only once; an error such as insufficient funds ends failed and produces a webhook. A transfer can be cancelled before its execution date using /transfers/cancel. The narrative refers to the Balance Platform time zone by default, while the request-field table gives Europe/Amsterdam as the omitted timezone default; verify the configured and request timezone for an actual schedule.
- **Movement evidence and raw conflict:** For each internal request, Adyen describes separate outgoing and incoming webhook series, with received, authorised, booked or failed states; Customer Area shows a debit-side and a credit-side entry. Check both sides and booked status for the balance-account movement. A flow sentence at raw line 63 says a booked transfer goes to the user's transfer instrument, conflicting with this page's balance-account target instructions and its stated internal-transfer purpose. Do not reinterpret this route as an external payout from that sentence. HTTP 2XX, received or authorised status is not booked movement; none of these states proves a bank payout. For a failure, the guide directs checking the source account's available balance and then support if funds are sufficient; it does not promise an automatic retry or return outcome.

## Detail locators

- Scope, requirements, cross-account-holder capabilities, source enablement and review stages: pinned raw lines 15-65.
- Customer Area source/target/amount steps, reference limits and EUR 150 illustration: pinned raw lines 67-115.
- API body field table, EUR 100 test request and SDK examples: pinned raw lines 117-445; response ID/status/reason and received/pending example: 446-488.
- Additional review field, one-approval limit and team action: pinned raw lines 492-500, 855-861; SDK examples: 502-853.
- Future-date constraints, one attempt/failure/cancel and conflicting timezone descriptions: pinned raw lines 865-917.
- Insufficient-funds troubleshooting and two-sided webhook/Customer Area evidence: pinned raw lines 919-946.

## Related

- [[adyen-platform-internal-transfers]] — main internal-transfer concept and reciprocal source route.
- [[source-adyen-docs-platforms-internal-fund-transfers]] — internal-versus-external overview.
- [[source-adyen-docs-platforms-manage-access-webservice-roles]] — related credential-role route.

## Related raw API references

- [[raw/adyen/docs/platforms/internal-fund-transfers/approve-cancel-transfers/2026-09-15|Approve or cancel transfers]] — separate procedure; not evidence for this entry.
- [[raw/adyen/docs/platforms/internal-fund-transfers/internal-transfer-webhooks/2026-09-15|Internal-transfer webhooks]] — separate event detail; not evidence for this entry.

## Raw Sources

- [[raw/adyen/docs/platforms/internal-fund-transfers/on-demand-fund-transfers/2026-09-15|Adyen Initiate on-demand internal funds transfers, captured 2026-09-15]]
