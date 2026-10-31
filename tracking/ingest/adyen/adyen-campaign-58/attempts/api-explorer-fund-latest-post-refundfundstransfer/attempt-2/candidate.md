---
title: "Adyen Fund API v6: POST /refundFundsTransfer"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Fund/latest/post/refundFundsTransfer"
raw_files:
  - "adyen/api-explorer/Fund/latest/post/refundFundsTransfer/2026-09-15.md"
tags: [adyen, classic-platforms, fund-api, funds-transfer, refund]
---

## Overview

This 2026-09-15-captured Fund API v6 TEST reference documents `POST /refundFundsTransfer`, which requests a refund of funds previously transferred between two accounts. Both accounts must be on the same platform, though they may have different account holders. The required `originalReference` is the PSP reference of the **original fund transfer**, distinct from the `pspReference` returned for the refund request.

## Key takeaways

- The request table marks `amount` and `originalReference` required. Within `amount`, `currency` (three-character ISO code) and `value` (integer minor units) are required. Optional `merchantReference` links transactions at the executing user's discretion. The endpoint table does not separately specify request-body requiredness or state a minimum, maximum, cumulative-refund, currency-matching, or idempotency rule. The related, 2020-modified Classic guide explicitly permits a full or partial reversal regardless of account-holder status.
- A 200 says the request succeeded; a 202 says it was accepted for processing but has **not completed**. Optional response fields include `originalReference`, `pspReference` (the request identifier), `merchantReference`, `message`, `resultCode`, and `invalidFields`. The original-transfer reference must not be confused with the new request reference.
- Listed errors are 400 (request reading/understanding), 401 (authentication), 403 (insufficient permissions), 422 (validation), and 500 (server processing). The page does not name a specific permission role. These endpoint responses do not by themselves establish completed funds reversal, ledger posting, or recipient balance. The dated Classic guide says the initial refund response only acknowledges receipt; follow the `REFUND_FUNDS_TRANSFER` webhook for the result. It says a successful reversal appears as `FundTransferReversed` in the Marketplace Payment Accounting Report.
- The page shows a TEST server only. Its `latest` route and snapshot do not establish current live availability, account eligibility, or a performed refund.

## Classic guide context

The related [[source-adyen-docs-classic-platforms-fund-transfer|Classic fund-transfer guide]] (last modified 2020-05-26; captured 2026-09-15) says Adyen Support must enable fund transfers and define platform transfer codes before transfer or reversal use, and requires `TRANSFER_FUNDS` and `REFUND_FUNDS_TRANSFER` notification webhooks to track asynchronous outcomes. Its pinned raw lines 30–36 give those prerequisites; lines 111–120 permit full or partial reversal even when the account holder is no longer Active; lines 139–151 distinguish the initial receipt from the final `REFUND_FUNDS_TRANSFER` result and `FundTransferReversed` journal entry. These are guide-level workflow statements, separate from this endpoint's request schema and 200/202 labels.

## Detail locators

- Purpose, same-platform qualification and TEST server: pinned raw, lines 5–10.
- Request field requirements and example: `## Parameters > ### Request body` and `## Request examples > ### basic`, lines 12–35.
- 200/202 response descriptions, request versus original references, optional result fields: `## Responses`, lines 36–75. Error descriptions and optional fields: lines 78–140.

## Related

- [[adyen-classic-platforms]] — Classic account-holder/account and Fund API context.
- [[source-adyen-docs-classic-platforms-fund-transfer]] — dated Classic guide for enablement, full/partial reversal and asynchronous result tracking.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/api-explorer/Fund/latest/post/refundFundsTransfer/2026-09-15|Fund API v6 POST /refundFundsTransfer capture]]
