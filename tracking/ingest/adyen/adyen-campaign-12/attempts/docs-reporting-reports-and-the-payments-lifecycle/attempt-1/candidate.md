---
title: "Adyen reports and the payments lifecycle"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/reporting/reports-and-the-payments-lifecycle"
raw_files:
  - "adyen/docs/reporting/reports-and-the-payments-lifecycle/2026-09-15.md"
tags: [adyen, reporting, payments-lifecycle, reconciliation]
---

## Overview

This Adyen webpage snapshot maps named payment-lifecycle statuses to three financial-report families: Payment accounting, Settlement details, and Dispute transaction details. It is a guide to where status entries appear, not a transaction-level result, report schema, or proof of final cash movement. See [[adyen]] and [[adyen-reporting]].

## Key takeaways

- The **Payment accounting report** list spans attempted/validated, acquirer-authorised, modification, error/refusal, cancellation, expiry, and `Settled/Refunded` labels. For the exact status list and definitions, see pinned raw lines 26–36. In particular, `Received` describes validated payment details; `Authorised` is an authorised response from an acquirer. Neither should be collapsed into settlement.
- The **Settlement details report** list has `Settled`, `Chargeback`, `Refunded`, and `ChargebackReversed`. Here the page defines `Settled` as captured funds released to merchant payable and `Refunded` as funds deducted from merchant payable (raw lines 38–43). That report listing alone does not establish a bank deposit or final financial outcome for a particular payment.
- The **Dispute transaction details report** list includes `Notification of Chargeback` for a pending chargeback and `Request for information` (raw lines 45–48). The page notes webhooks for selected statuses across the lists; it does not say every listed report status has a webhook.
- The `Settled/Refunded` entry in the Payment accounting list is glossed as “Payment attempt with validated details” in this snapshot (raw line 30). Keep that wording as a source peculiarity; do not substitute a detailed settlement/refund meaning from this line.

## Detail locators

- `Payment statuses and corresponding reports`, raw lines 19–48: report-to-status mapping and short glosses. The embedded status chart is referenced on line 23, but the text snapshot does not expose its contents.
- `See also`, raw lines 50–54: navigation to the three specific report guides, which should be read for their own report fields, grain, timing, and reconciliation rules.

## Related

- [[adyen-reporting]] — reporting concept route.
- [[adyen-online-payments]] — payment acceptance context; separate from report status evidence.

## Raw Sources

- [[raw/adyen/docs/reporting/reports-and-the-payments-lifecycle/2026-09-15|Reports and the payments lifecycle, fetched 2026-09-15]]
