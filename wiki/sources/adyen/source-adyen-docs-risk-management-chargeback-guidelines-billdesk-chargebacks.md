---
title: "India domestic chargebacks with BillDesk | Adyen Docs"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/chargeback-guidelines/billdesk-chargebacks"
raw_files:
  - "adyen/docs/risk-management/chargeback-guidelines/billdesk-chargebacks/2026-09-15.md"
tags: [adyen, risk-management, disputes, chargebacks, billdesk, india]
---

## Overview

Adyen's India domestic BillDesk chargeback guide covers disputed BillDesk-processed payments and routes merchants to the live India Customer Area or Disputes API for supported card and UPI transactions. Online banking India and wallets India disputes cannot be managed through either route; Adyen Support helps by email. This is a 2026-09-15 documentation snapshot, with source metadata last modified 2024-03-20, rather than evidence of a particular account's access or a current scheme deadline. See [[adyen]] and [[adyen-risk-management]].

## Key takeaways

- BillDesk initiates a Notification of Chargeback (NoC). Adyen books the `NotificationOfChargeback` journal and assigns the dispute in the live India Customer Area or sends a dispute webhook. Funds have not yet been deducted at this stage; the merchant has **7 days to respond to the chargeback notification**. The merchant may accept, which loses the dispute and closes defense, or defend by uploading documents through the live India Customer Area or Disputes API.
- When Adyen receives defense documents, it forwards them to the scheme, books `InformationSupplied`, and sends the `INFORMATION_SUPPLIED` webhook. The documents cannot then be changed. If BillDesk accepts the defense, no further journals are booked and that outcome is final; if it rejects the defense, a chargeback follows. The page says that if the `Chargeback` journal is not booked after BillDesk's 60-day period to determine final status, the merchant can consider the dispute won.
- If the shopper or issuer rejects the supporting document, or the merchant misses the defense deadline, Adyen books `Chargeback`, sends a `CHARGEBACK` webhook, and debits the account. This first chargeback cannot be defended and is described as final/lost. However, the same guide says the issuer can initiate pre-arbitration even after a win and after more than 60 days without a chargeback on Adyen's settlement report; therefore, the 60-day considered-won state should not be treated as an unconditional bar on a later issuer action.
- Pre-arbitration cannot be managed through the Disputes API or Customer Area. The issuer emails Adyen Support, which contacts the merchant for next steps.

## Detail locators

- Supported card schemes and UPI, excluded online banking and wallet methods: [[raw/adyen/docs/risk-management/chargeback-guidelines/billdesk-chargebacks/2026-09-15|BillDesk raw]], lines 16–23.
- NoC journal, live India Customer Area and webhook route, 7-day response, acceptance and defense-document paths: same raw, lines 36–49.
- `InformationSupplied`, immutability, BillDesk's decision and 60-day condition: same raw, lines 51–59.
- First-chargeback debit, loss/finality, and later issuer pre-arbitration/support path: same raw, lines 61–71.
- Customer Area/API management routes and reason-code reference: same raw, lines 73–89.

## Related

- [[adyen-risk-management]] — Adyen risk management and dispute-source routing.
- [[source-adyen-docs-risk-management-understanding-disputes-dispute-timeframes]] — scheme and payment-method dispute timing reference; use the BillDesk guide's exact stage and condition when applying its stated windows.

## Raw Sources

- [[raw/adyen/docs/risk-management/chargeback-guidelines/billdesk-chargebacks/2026-09-15|India domestic chargebacks with BillDesk (Adyen Docs, fetched 2026-09-15)]]
