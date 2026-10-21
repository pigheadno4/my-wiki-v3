---
title: "Adyen Classic Platforms: reconcile accounts receivable"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/reconciliation-use-cases/reconcile-accounts-receivable"
raw_files:
  - "adyen/docs/classic-platforms/reconciliation-use-cases/reconcile-accounts-receivable/2026-09-15.md"
tags: [adyen, classic-platforms, reconciliation, accounts-receivable, settlement]
---

## Overview

This 2023-modified [[adyen-classic-platforms]] guide from [[adyen]], captured 2026-09-15, explains how to use the Settlement details report to reconcile the net batch amount Adyen settles to accounts in a Classic platform. It explicitly directs new implementations to the newer integration guide. Its example is report arithmetic, not proof of any actual merchant settlement, individual account allocation, bank receipt or present-day report state.

## Key takeaways

- The Classic flow described is buyer payment processing through the platform's Adyen merchant accounts, followed by Adyen's receipt of funds and settlement/credit to accounts in the platform. Adyen creates a Settlement details report for a settled transaction batch. The report lets the platform identify settled transactions, batch net debit/credit and related scheme/interchange or other fees. See raw lines 19–27.
- The worked table deliberately includes selected rows and columns only: two `Settled` payments, one `Refunded` item, a fee deduction and an `XASTransfer` row. Consult the complete Settlement details report for a full ledger. The shown net credits are EUR 297.60 and 147.00; the refund and fee net debits are EUR 54.00 and 0.32. Their net is EUR 390.28, represented by the `XASTransfer` debit row. Do not add the transfer row again when deriving that underlying net. See raw lines 29–52.
- The source defines `XASTransfer` as the cross-accounting-system-transfer row reflecting the net amount settled to platform accounts, with the stated calculation **total Net credit minus total Net debit**. For its illustrated batch, Adyen says EUR 390.28 was settled and credited to platform accounts. The separate transactional-ledger guide is the route for breaking that amount down into credits and debits for each platform account. See raw lines 46–54.

## Detail locators

- Classic-only scope, merchant-to-platform-account settlement direction and report purpose: raw lines 19–27.
- Selected Settlement details report rows and fields: raw lines 29–46.
- `XASTransfer` interpretation, stated net formula, EUR 390.28 example and per-account ledger route: raw lines 48–54.

## Related

- [[adyen]] — provider profile.
- [[adyen-classic-platforms]] — Classic account and settlement model.
- [[source-adyen-docs-classic-platforms-reconciliation-use-cases]] — Classic reconciliation hub.
- [[source-adyen-docs-classic-platforms-reconciliation-use-cases-understand-fees]] — separate fee breakdown route.
- [[adyen-reporting]] — report context; this Classic example does not establish current report generation or account-specific outcomes.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/reconciliation-use-cases/reconcile-accounts-receivable/2026-09-15|Reconcile accounts receivable — pinned 2026-09-15 raw snapshot]]
