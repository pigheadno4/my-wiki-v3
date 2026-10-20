---
title: "Adyen Enterprise Issuing: Fund cards with acquired payments"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/add-manage-funds/process-payments"
raw_files:
  - "adyen/docs/issuing/add-manage-funds/process-payments/2026-09-15.md"
tags: [adyen, issuing, enterprise-issuing, acquiring, settlement]
---

## Overview

This 2026-09-15-captured page describes **Enterprise Issuing** funding through payments the business acquires with Adyen. Customers pay the business online or in person; the acquired revenue can then fund Adyen-issued cards. The page sends Embedded Issuing readers to separate marketplace or platform guidance.

## Money flow and limits

- Payments first arrive **pending in the business's merchant account**. After its configured settlement delay (**T+2 by default in this snapshot**), Adyen deducts payment fees, aggregates remaining available funds into **net settlement batches**, and books each batch to the balance platform and the **balance account configured for that merchant account**. Hourly batches are the stated default; daily batching is an option through the Adyen contact. From the resulting balance account, funds can support issued cards or be paid out to a verified external-bank transfer instrument. See raw lines 23–30.
- Each settlement batch is treated as **one transfer** for Transfer webhooks: `balancePlatform.transfer.created` indicates an incoming transfer was initiated, and `balancePlatform.transfer.updated` carries status changes. The page does not make the created event proof of booked funds. See raw lines 74–81.
- In the Balance Platform Accounting Report, each entry represents **a settlement batch**, not a single acquired transaction. The page directs transaction-level reconciliation to a separate guide. See raw lines 83–87.

## Example discrepancy

The hotel example says its Stockholm guest pays **SEK 400** (raw line 47), but later says **EUR 400** becomes available in `HotelChain_SEK` (line 52). Subsequent fee and net-batch lines use **SEK 20** and **SEK 380** (lines 61–72). Treat the EUR label in line 52 as an unresolved example inconsistency, not a currency-conversion rule or a reliable reconciliation figure.

## Detail locators

- Enterprise-versus-Embedded scope and optional acquired-payment funding: [[raw/adyen/docs/issuing/add-manage-funds/process-payments/2026-09-15|raw lines 15–21]].
- Settlement sequence, hotel-branch example and currency discrepancy: [[raw/adyen/docs/issuing/add-manage-funds/process-payments/2026-09-15|raw lines 23–72]].
- Transfer webhooks and batch-level report boundary: [[raw/adyen/docs/issuing/add-manage-funds/process-payments/2026-09-15|raw lines 74–87]].

## Related

- [[adyen-issuing]] — Issuing balance-platform model and source catalog.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/issuing/add-manage-funds/process-payments/2026-09-15|Process payments (captured 2026-09-15)]]
