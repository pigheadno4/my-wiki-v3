---
title: "Adyen Issuing: Create recurring top-ups"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/add-manage-funds/top-ups/create-recurring-top-ups"
raw_files:
  - "adyen/docs/issuing/add-manage-funds/top-ups/create-recurring-top-ups/2026-09-15.md"
tags: [adyen, issuing, balance-accounts, top-ups, direct-debit]
---

## Overview

This 2026-09-15-captured Adyen Issuing guide configures recurring top-ups for a balance account. A configured schedule triggers outgoing **direct debit requests to a bank-account source** according to amount, frequency and source settings; Adyen then books top-up funds to the balance account. The guide describes configuration and tracking, not evidence that a particular debit settled or a card payment succeeded.

## Key takeaways

- Scope and prerequisites: Issuing integration; a top-up source with enough balance; an account holder whose `receiveFromTransferInstrument` capability is active with a valid `verificationStatus`; and Configuration, Transfer and Transaction webhook subscriptions. API setup requires the **BankAPI Advanced Webservice role** and prior Terms of Service acceptance. Customer Area setup lists **Balance platform base role** plus **Configure scheduled payouts**; its wizard handles Terms of Service acceptance. See raw Requirements, lines 23–38.
- The captured page says recurring top-ups support **EUR and USD only** and **do not support on-demand top-ups**. API creation uses `POST /balanceAccounts/{balanceAccountId}/recurringTopUps`; the configuration selects one of `topUpAmount.fixed` or `topUpAmount.target`, with a threshold and optional schedule. Without a schedule, the page says balance is continuously monitored. See raw lines 35–36, 40–99.
- A triggered top-up creates a transfer record. The guide points to Customer Area transfer status, balance-account schedule/history and the Balance Platform Accounting Report; it gives USD and EUR processing and cut-off examples. A created schedule or transfer record alone does not establish final bank receipt. See raw lines 254–275.
- Creation can fail for invalid or mismatched currencies, missing capability or signed Terms of Service, inactive account status, invalid/inaccessible transfer instrument, unavailable route, direct-debit threshold, or duplicate configuration. See raw error table, lines 277–304.

## Source discrepancies

- The API `trigger.threshold` prose says a top-up triggers when available balance is **below** the threshold (raw line 99). The Customer Area instructions say **less than or equal to** (raw line 242). The snapshot does not reconcile equality behavior.
- The parameter table names `topUpAmount.fixed` (raw lines 78–83), while the optional placeholder payload uses `topUpAmount.fixedAmount` and an outer `currency` field (raw lines 203–225). Treat that payload as an example, not a resolved schema.
- The example request uses a `balanceplatform-api-beta.adyen.com` `/bcl/v2/` URL (raw line 122), while the page links the endpoint under the latest API Explorer (raw line 46). The snapshot does not establish which version or host to use now.

## Detail locators

- API field requiredness, `counterparty.transferInstrumentId` condition, fixed-versus-target selection, schedule values and threshold: [[raw/adyen/docs/issuing/add-manage-funds/top-ups/create-recurring-top-ups/2026-09-15|raw lines 44–99]].
- Example request/response, dynamic description placeholders and Customer Area wizard: [[raw/adyen/docs/issuing/add-manage-funds/top-ups/create-recurring-top-ups/2026-09-15|raw lines 103–252]].
- Tracking, timing and failure codes: [[raw/adyen/docs/issuing/add-manage-funds/top-ups/create-recurring-top-ups/2026-09-15|raw lines 254–304]].

## Related

- [[adyen-issuing]] — Issuing balance-platform model and source catalog.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/issuing/add-manage-funds/top-ups/create-recurring-top-ups/2026-09-15|Create recurring top-ups (captured 2026-09-15)]]
