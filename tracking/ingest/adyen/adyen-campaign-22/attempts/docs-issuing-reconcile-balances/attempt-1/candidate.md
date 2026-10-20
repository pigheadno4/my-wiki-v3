---
title: "Adyen Issuing: Reconcile balances"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/reconcile-balances"
raw_files:
  - "adyen/docs/issuing/reconcile-balances/2026-09-15.md"
tags: [adyen, issuing, reconciliation, balance-platform, settlement-reports]
---

## Overview

Adyen's 2026-09-15-captured Issuing-path guide reconciles payment-processing merchant-account settlement with funds moved by internal transfer into the balance platform. It pairs Standard Capture and balance-platform transfer webhooks with merchant-side and balance-platform reports, then gives daily, monthly and final-balance methods. The guide describes matching evidence, not bank receipt or proof that a particular transfer completed. [[adyen]] [[adyen-reporting]] [[adyen-issuing]]

## Key takeaways

- The guide says funds processed through Adyen move from the merchant account to the balance platform through internal transfers. Standard Capture webhooks on the payment-processing side carry `settlementReference` and `expectedValueDate`; balance-platform transfer created/updated webhooks track a settlement batch as one internal transfer and its status. A created-transfer example is initiation evidence, not a received/settled guarantee. See raw lines 19-26 and 62-129.
- For daily reconciliation, compare merchant-side Settlement Details Report (SDR) `MerchantPayout` entries with balance-side Balance Platform Statement Report (BPSR) `InternalTransfer` entries by settlement batch, amounts, description and date. The guide says a merchant account has 1-24 payable batches/day, each settled to the balance platform in one internal transfer; generate SDR for each BPSR batch or cover the corresponding dates. BPSR Value Date must match SDR Creation Date or conditional Booking Date (AMS). See raw lines 144-164.
- Merchant-account and balance-platform report time zones can differ. Configure Booking Date (AMS) in SDR or Aggregate Settlement Details Report (ASDR) when the merchant account is outside CET, and align the relevant sales dates; the guide describes balance-platform reporting as CET/CE(S)T and notes that one sales day can cross two CET dates. See raw lines 135-142, 154-162 and 184-194.
- For monthly reconciliation, sum booked `InternalTransfer` entries in the Balance Platform Interactive Accounting Report (BPIAR) whose Value Date falls in the month, then compare with `MerchantPayout` totals in ASDR for every relevant merchant account. Where multiple merchant accounts settle into one balance account, BPIAR Description identifies the source merchant account. See raw lines 176-194.
- The Liable account summary dashboard method is explicitly limited to a balance platform with one account holder; otherwise use reports. Its steps first request ASDR but then name SDR in the count/amount comparisons, a report-label conflict in the captured text. Do not treat that wording as a settled report contract. See raw lines 205-223.
- BPSR is offered as a final ledger with starting balance, positive/negative adjustments, other movements and ending balance; its abbreviated equation lists incoming settlement minus outgoing movements. This report view does not independently establish external-bank receipt or accounting finality. See raw lines 226-241.

## Detail locators

- Standard Capture example and reconciliation fields: raw lines 25-60. The displayed JSON lacks a comma after `hmacSignature` at line 50, so treat it as an illustrative payload, not directly parseable JSON.
- Balance-platform `transfer.created` example includes `environment: test`, `direction: incoming`, `status: received` and embedded batch/reference fields: raw lines 62-129. These example values do not establish a live outcome.
- SDR, ASDR, BPSR and BPIAR report grains and generation dates: raw lines 131-142. Daily worked CSV links: raw lines 166-174; monthly worked CSV links: raw lines 196-203. The linked CSV contents were not part of this pinned raw.

## Related

- [[adyen-reporting]] — main reporting and reconciliation route.
- [[adyen-issuing]] — Issuing balance-platform context.

## Raw Sources

- [[raw/adyen/docs/issuing/reconcile-balances/2026-09-15|Adyen Issuing reconcile balances, captured 2026-09-15]]
