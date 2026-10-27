---
title: "Adyen ACH Direct Debit iOS Drop-in"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/ach-direct-debit/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/ach-direct-debit/ios-drop-in/2026-09-15.md"
tags: [adyen, ach, direct-debit, ios, drop-in, sessions, advanced-flow]
---

## Overview

This 2026-09-15 Adyen guide adds ACH Direct Debit to an existing iOS Drop-in integration through Sessions or Advanced server-side flow. It is a method-specific add-on, not a complete native integration or evidence of current eligibility, bank-account validation, authorization or cleared funds. See [[adyen]], [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-ach-direct-debit]] for ACH eligibility, SEC-code, signed mandate, account-validation, refund and chargeback conditions.

## Key takeaways

- Sessions requires an existing iOS Drop-in Sessions integration, Checkout API v68 or later, ACH Direct Debit added in Customer Area and subscription to `DIRECT_DEBIT_NOTICE_OF_CHANGE_NOTIFICATION` for outdated banking details. Its ordinary `/sessions` request and Drop-in configuration need no additional ACH-specific parameters.
- Advanced requires an existing iOS Drop-in Advanced integration, ACH Customer Area setup and the same Notice of Change subscription. Its ordinary `/payments` request and Drop-in configuration need no additional ACH-specific parameters. These narrow integration statements do not remove the method overview's Nacha consumer-account validation, SEC-code or electronically signed mandate requirements; the overview says Drop-in handles the SEC code automatically, but the customer authorization remains necessary.
- The refund role in both prerequisite tables is conditional: issuing an ACH refund by API or Customer Area requires the **Merchant allow bank-refund** role for the relevant actor. The method overview says the payment must first settle and describes a three-day post-settlement delay; this child guide supplies no refund execution procedure.
- After Adyen receives the request, bank authorization may take up to five business days. The guide points to the Settlement details report if authorized and a `CHARGEBACK` webhook if not; an immediate response is not settled-funds proof. The ACH overview also warns of no real-time authorization and nondefendable chargebacks.
- The test section allows any correctly formatted account and routing number, and `ownerName` beginning `chargeback:` plus an ACH return code such as `R01` for test chargebacks. The guide merely links to giact validation, tokenization and ACH chargeback instructions; it does not itself show those flows or grant a general retry permission. Its `CHARGEBACK` links target a `#chargebacks` fragment not present in this child page; the method overview supplies the chargeback route.

## Detail locators

- Sessions iOS Drop-in/v68+, conditional refund role, Notice of Change webhook and Customer Area setup: pinned raw lines 25–37. No added `/sessions` or Drop-in fields: lines 39–49.
- Advanced integration, conditional refund role, Notice of Change webhook and setup: pinned raw lines 79–91. No added Drop-in or `/payments` fields: lines 93–103.
- Five-business-day bank outcome, Settlement details report and chargeback webhook: pinned raw lines 51–57 and 105–111. Test accounts/chargeback simulation: lines 59–77 and 113–131. Related links: lines 133–137.
- Method-level US-entity eligibility, consumer validation, SEC-code handling, signed mandate, settled-only delayed refund and nondefendable disputes: [[source-adyen-docs-payment-methods-ach-direct-debit]].

## Related

- [[adyen-online-payments]] — main provider integration concept
- [[source-adyen-docs-payment-methods-ach-direct-debit]] — method-level eligibility, mandate, account validation, refund and chargeback authority

## Raw Sources

- [[raw/adyen/docs/payment-methods/ach-direct-debit/ios-drop-in/2026-09-15|ACH Direct Debit iOS Drop-in, 2026-09-15]]
