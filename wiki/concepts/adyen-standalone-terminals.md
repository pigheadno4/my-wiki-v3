---
title: "Adyen standalone terminals"
type: concept
category: technology
tags: [adyen, point-of-sale, standalone-terminals, in-person-payments]
---

## Adyen standalone terminals

Adyen's standalone solution starts in-person transactions directly on a terminal, without a merchant POS app or POS-system integration. It is a separate solution choice from POS-app-to-terminal Terminal API integration. The dated overview also proposes it as a fallback when a POS app cannot communicate with integrated terminals, provided the standalone terminal has cellular connectivity or offline payments enabled. That condition does not establish a successful outcome for every outage or offline transaction.

## Scope and operating boundary

The 2026-09-15 source limits standalone use to terminals with a built-in printer because a customer must be able to receive a printed receipt. The listed models are S1F2, S1F2L, V210, V240m Plus (Brazil), V400c Plus and V400m; current model, region and merchant eligibility require separate confirmation. The overview lists payment, refund, tipping, cancellation, accessibility, surcharge, totals and receipt routes, but excludes shopper recognition and tax-free shopping and requires manual reconciliation with sales and returns. Feature procedures and account setup belong to the linked guides. This snapshot is neither security certification nor proof of a successful payment.

## Related

- [[adyen-terminal-api]] — integrated POS-app-to-terminal messages
- [[source-adyen-docs-point-of-sale-what-we-support-solutions]] — broader solution comparison

## Sources

- [[source-adyen-docs-point-of-sale-standalone-standalone-build]] — 2026-09-15 Adyen standalone-build navigation hub for test checklist, go-live checklist, and terminal setup required for both test and live integrations.


- [[source-adyen-docs-point-of-sale-standalone-standalone-build-go-live-standalone]] — 2026-09-15 standalone go-live checklist for live account/finance setup, separate live terminals and configuration, optional store pre-assignment, and receipt/boarding/connectivity steps.


- [[source-adyen-docs-point-of-sale-standalone-standalone-build-standalone-checklist]] — Adyen dated test-to-live standalone checklist (fetched 2026-09-15) for account structure, printer-equipped test devices, boarding, test transactions/reconciliation and separate live application/contract.


- [[source-adyen-docs-point-of-sale-standalone-standalone-use]] — 2026-09-15 Adyen terminal-operated standalone guide for payment variants, feature/passcode gates, in-progress cancellation, referenced and unreferenced refunds, stored value, Totals, and receipt reprints.


- [[source-adyen-docs-point-of-sale-standalone-standalone-build-set-up-standalone]] — 2026-09-15 standalone setup guide for Customer Area or Management API enablement, optional tipping, refund passcode and separate live-terminal setup.


- [[source-adyen-docs-point-of-sale-standalone]] — Adyen standalone-solution overview (2026-09-15 snapshot): direct terminal initiation, fallback conditions, built-in-printer/model scope, feature routes and manual-reconciliation limit.
