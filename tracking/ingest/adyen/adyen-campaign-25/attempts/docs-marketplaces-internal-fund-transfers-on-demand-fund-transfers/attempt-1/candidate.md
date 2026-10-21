---
title: "Adyen Marketplaces: On-demand internal fund transfers"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/internal-fund-transfers/on-demand-fund-transfers"
raw_files:
  - "adyen/docs/marketplaces/internal-fund-transfers/on-demand-fund-transfers/2026-09-15.md"
tags: [adyen, marketplaces, platforms, internal-transfers, transfers-api]
---

## Overview

This 2020-modified, 2026-09-15-captured [[adyen]] Marketplaces guide describes initiating an on-demand **internal balance-account transfer**, including a push or internal direct debit, through Customer Area or the Transfers API. The source balance account is debited and the counterparty balance account is credited. This is distinct from a payout to an external bank transfer instrument; the EUR amounts and test requests are illustrations, not executed funds movement. [[adyen-platform-internal-transfers]] [[adyen-platforms]]

## Requirements and request route

- The stated gates are an Adyen for Platforms integration, Transfers API credential with **TransferService Webservice Initiate** role, Customer Area **Initiate internal transfers** and **Balance platform base** roles for the UI route, a server that receives/accepts subscribed Transfer webhooks, and Adyen Support enabling transfers on the **source** balance account. For transfers across **different account holders**, the sender needs `sendToBalanceAccount` and the receiver needs `receiveFromBalanceAccount`; the table makes this holder relationship conditional, not universal. See [[raw/adyen/docs/marketplaces/internal-fund-transfers/on-demand-fund-transfers/2026-09-15|raw lines 21–38]].
- In Customer Area, select the source balance account, counterparty type `balanceAccount`, destination balance-account ID, currency and amount; the guide's UI illustration sends **EUR 150** from liable to a user's balance account. The UI action **creates** a transfer request; booked status must be checked separately. For POST `/transfers`, the field table marks `amount` (currency/value), `balanceAccountId` (source), `counterparty.balanceAccountId` (destination), and `category=internal` required; description and references are optional. The test `/btl/v4/transfers` API illustration sends **EUR 100.00** (value 10000), a separate example. See [[raw/adyen/docs/marketplaces/internal-fund-transfers/on-demand-fund-transfers/2026-09-15|raw lines 44–125]].
- The sample API response provides a transfer `id` with `status=received` and `reason=pending`. The guide explicitly says to wait for transfer webhooks to confirm **booked**. For each request, separate webhook series cover the **outgoing/debited** and **incoming/credited** balance-account entries, progressing through `received`, `authorised`, and `booked` or reporting failure. HTTP 2XX, received or authorised status alone is not two-sided booked movement; none of this is external bank receipt. See [[raw/adyen/docs/marketplaces/internal-fund-transfers/on-demand-fund-transfers/2026-09-15|raw lines 419–463, 909–915]].

## Review, scheduling and failure boundary

- The optional `review.numberOfApprovalsRequired` value is **1** in this snapshot: one additional team review may be requested. A team member must approve before Adyen continues processing. A successful HTTP 2XX review response reports the number required, not approval or booking. See [[raw/adyen/docs/marketplaces/internal-fund-transfers/on-demand-fund-transfers/2026-09-15|raw lines 467–475, 830–836]].
- With `executionDate.date`, an accepted request remains `received/pending` until a future date within **30 days** in ISO `YYYY-MM-DD` format. On that date the guide describes a **00:00–03:00** window and checks for source funds and required team approval. It says Adyen attempts execution **only once**; an error such as insufficient funds ends `failed` and generates a webhook. A request can be cancelled **before** its execution date through POST `/transfers/cancel`. The narrative refers to the Balance Platform configured timezone by default, while the request-field table labels omitted `executionDate.timezone` default **Europe/Amsterdam**; do not assume the effective timezone from one sentence alone. See [[raw/adyen/docs/marketplaces/internal-fund-transfers/on-demand-fund-transfers/2026-09-15|raw lines 840–859, 890–892]].
- If an internal transfer fails, the guide directs reading the source balance account's **available** balance, then considering a user top-up or liable-to-user internal funding if insufficient, or Support if funds suffice. This is troubleshooting guidance, not authorization to submit another transfer or a promise of retry. See [[raw/adyen/docs/marketplaces/internal-fund-transfers/on-demand-fund-transfers/2026-09-15|raw lines 894–907]].

## Detail locators

- Scope, access, webhook, conditional cross-holder capabilities and source enablement: [[raw/adyen/docs/marketplaces/internal-fund-transfers/on-demand-fund-transfers/2026-09-15|raw lines 15–38]].
- UI/API required fields, examples, test endpoint and dated SDK snippets: [[raw/adyen/docs/marketplaces/internal-fund-transfers/on-demand-fund-transfers/2026-09-15|raw lines 40–417]].
- Response, review, future-date single-attempt execution and cancel window: [[raw/adyen/docs/marketplaces/internal-fund-transfers/on-demand-fund-transfers/2026-09-15|raw lines 419–892]].
- Troubleshooting and two-sided webhook/Customer Area status route: [[raw/adyen/docs/marketplaces/internal-fund-transfers/on-demand-fund-transfers/2026-09-15|raw lines 894–915]].

## Related

- [[adyen-platform-internal-transfers]] — main internal-transfer concept.
- [[source-adyen-docs-platforms-internal-fund-transfers-on-demand-fund-transfers]] — related Platforms-path guide; preserve path-specific text.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/marketplaces/internal-fund-transfers/on-demand-fund-transfers/2026-09-15|Marketplace on-demand internal fund transfers (captured 2026-09-15)]]
