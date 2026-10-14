---
title: "Standalone go-live checklist | Adyen Docs"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/standalone/standalone-build/go-live-standalone"
raw_files:
  - "adyen/docs/point-of-sale/standalone/standalone-build/go-live-standalone/2026-09-15.md"
tags: [adyen, point-of-sale, standalone, go-live, live-environment]
---

## Overview

This Adyen Docs checklist, captured 2026-09-15, lays out the transition from a **test** standalone terminal setup to a **live** standalone solution: live account and finance setup, live terminal ordering and configuration, then physical receipt, boarding and connectivity checks. Standalone payments start on a terminal without a merchant POS app. The checklist is a sequence of tasks, not evidence that an account was approved, a terminal was boarded, or any live payment or payout succeeded. See [[adyen]] and [[adyen-standalone-terminals]].

## Key takeaways

- Apply for a live account and sign the contract before setting up the live account; the page also points to separate live-application requirements. **Test account structure is not copied to live.** Request the needed live merchant accounts in the live Customer Area. Adding stores is described as optional in this checklist and follows confirmation that the live merchant accounts were created. Its four-business-day merchant-account and two-business-day store estimates are dated usual processing times, not commitments.
- Provide payout bank-account information and review reporting/reconciliation. The page offers a separate bank account per currency, optional payout-schedule change, Settlement details reporting for transaction-level reconciliation, and possible reporting automation. It says to **consider** a Reserve and auto-funding to cover refunds and other expenses if in-process funds are insufficient; these are not framed as universal standalone prerequisites.
- **Test terminals cannot process live payments.** Order separate live terminals from the live Customer Area; the page's roughly four-business-day arrival estimate is historical guidance. **Test terminal settings also do not copy to live**: configure the live standalone mode and payment/terminal features through Customer Area or the Management API at the company, merchant, store or terminal level. Pre-assigning a terminal to a store is optional here and intended to speed boarding, not proof that boarding is complete.
- On receipt, follow the specific model manual: inspect for tampering, insert receipt paper, power on, network-connect, board, and test the Adyen-platform connection. The checklist's “ready to process your first live payment” is an instruction-stage conclusion; it does not show a successful authorization, capture, settlement, reconciliation, or payout. The linked model and standalone-setup guides own their detailed conditions.

## Detail locators

- `Standalone go-live checklist`, lines 15–25: standalone solution identity, live-account application requirement route.
- `1. Set up your Adyen live account`, lines 27–42: application/contract, test/live account separation, merchant accounts and optional stores with dated estimates.
- `2. Review your finance settings`, lines 44–87: payout account and optional schedule, Settlement details reconciliation, optional Reserve/auto-funding consideration.
- `3. Order live payment terminals`, lines 89–99: test-terminal live-payment prohibition, live ordering and dated arrival estimate.
- `4. Prepare your terminals`, lines 101–121: test/live settings separation, configuration scopes, standalone feature setup and optional store pre-assignment.
- `5. Get your terminals up and running`, lines 123–138: physical inspection, paper, power, networking, boarding and point-in-time platform test.

## Related

- [[adyen-standalone-terminals]] — direct terminal operation and source routes.
- [[adyen-terminal-management]] — live terminal fleet ordering and configuration.
- [[adyen-pos-store-management]] — live account/store structure context.
- [[adyen-payment-terminals]] — model-specific inspection and boarding manuals.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/standalone/standalone-build/go-live-standalone/2026-09-15|Standalone go-live checklist (2026-09-15 snapshot)]]
