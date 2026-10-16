---
title: "Reconciliation and invoices | Adyen Mirakl connector"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/mirakl/reconciliation-and-invoices"
raw_files:
  - "adyen/docs/plugins/mirakl/reconciliation-and-invoices/2026-09-15.md"
tags: [adyen, mirakl, reconciliation, invoices, marketplace, payouts]
---

## Overview

This Adyen Mirakl connector guide describes how seller invoices, platform balance-account reporting, Mirakl invoice fields and Adyen transfer references support reconciliation. It covers seller payout and commission amounts in the connector flow, not the marketplace pay-in flow or independent proof that funds reached a seller bank account. [[adyen-mirakl]]

## Seller invoice and account flows

- Mirakl generates an invoice for each seller at the end of a billing cycle; the documented default is ten days, typically three invoices per month. The invoice shows the **net remaining amount** to pay the seller and the commission to transfer to the platform's liable balance account. This page gives no gross-to-net calculation, currency conversion, negative-payable treatment or calendar/time-zone rule.
- On invoice generation, the connector synchronizes invoice details through Mirakl IV01: the seller payout amount and commissions deducted from the seller. In Mirakl back office, the route is **Accounting → Billing and documents → Accounting documents**.
- **Only if Payment Confirmation is enabled**, the generated invoice is **Pending**; the commission is transferred from the seller's account to the platform account, and after payout completion the connector sets the invoice **Paid** through Mirakl IV07. The documented status sequence is conditional and is not, by itself, evidence of a bank statement credit or final settlement outside the described connector flow.

## Report and API reconciliation

- The Balance Platform Accounting Report is a daily record of balance changes across the platform's balance accounts, including the liable and user accounts. Customer Area can generate it on a schedule or manually for a chosen day. The page recommends using Mirakl invoices with this report; it does not define the report's row-level schema or establish a transaction-level gross/fee/net equation.
- In Mirakl IV07, `invoice.summary.amount_transferred_to_operator` identifies commission sent to the liable balance account, while `invoice.summary.amount_transferred` identifies the payout amount sent to the seller. Keep these account destinations and amounts separate.
- The connector makes Adyen `/transfers` requests for payouts and commissions. The response's `referenceForBeneficiary` is also supplied to the recipient and related transfer webhooks; its components are connector invoice `id`, attempt `count`, and transfer `type` (**P** payout, **C** commission, **S** subscription). The transfer `description` also includes type and invoice ID. These identifiers support matching and status tracking; a request or response alone does not establish completion or bank receipt.

## Detail locators

- **Invoice cadence, net seller amount, commission and IV01 synchronization:** raw lines 19–28.
- **Conditional Payment Confirmation invoice statuses and commission transfer:** raw line 30.
- **Daily Balance Platform Accounting Report and reconciliation use:** raw lines 32–38.
- **Mirakl IV07 amount fields:** raw lines 40–49.
- **Adyen transfer references, attempt count and type codes:** raw lines 51–67.

## Related

- [[adyen-mirakl]]
- [[adyen-payouts]]
- [[adyen-reporting]]

## Raw Sources

- [[raw/adyen/docs/plugins/mirakl/reconciliation-and-invoices/2026-09-15|Adyen Mirakl reconciliation — collected 2026-09-15]]
