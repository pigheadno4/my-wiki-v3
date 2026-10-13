---
title: "Adyen JCB Chargebacks"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/chargeback-guidelines/jcb-chargebacks"
raw_files:
  - "adyen/docs/risk-management/chargeback-guidelines/jcb-chargebacks/2026-09-15.md"
tags: [adyen, jcb, chargebacks, disputes, defense, arbitration]
---

## Overview

This Adyen guide describes the JCB-specific chargeback path from optional Request for Information (RFI) through first chargeback, merchant defense, conditional reversal, possible second chargeback, and arbitration-case filing. Its scheme-specific deadlines and outcome states are a 2026-09-15 snapshot of a page whose embedded metadata was last modified in 2019, not verification of currently applicable deadlines for a live case.

## Key takeaways

- An optional RFI may arise when the cardholder disputes or does not recognize a charge, or during a fraud investigation. The guide says funds are not yet deducted at RFI. Once Adyen forwards supplied information to the scheme and records `INFORMATION_SUPPLIED`, those documents cannot be changed.
- A Notification of Chargeback (NoC) may follow RFI or occur without it. Adyen sends `NOTIFICATION_OF_CHARGEBACK` and says the debit usually follows a few days later. At first chargeback, Adyen assigns the case in Customer Area, books the chargeback journals, sends `CHARGEBACK`, and debits the merchant account. The merchant may accept, closing defense, or submit reason-specific documents through Customer Area or Disputes API. The guide gives **40 days** to provide defense documents and says there is no later chance to provide or update them. The separate [[source-adyen-docs-risk-management-understanding-disputes-dispute-timeframes|dispute-timeframes table]] identifies the JCB response window as **40 calendar days from the NoC date**.
- `Chargeback Reversed` transfers the disputed amount back while the issuer still reviews the defense; it is final only if the issuer accepts. The issuing bank can initiate a second chargeback within **35 days from the first chargeback defense date**, taking funds again. JCB does not allow document upload at that second stage; a merchant with enough information to challenge it must contact Adyen's Disputes Team.
- To pursue arbitration after a second chargeback, the merchant must contact Adyen's Chargeback team with supporting information within **40 days of receiving the second chargeback**. The guide states that Adyen is not responsible if JCB rules for the cardholder. Do not treat document submission or a provisional reversal as a guaranteed win.

## Detail locators

- Opening and `## Optional: Request for Information (RFI)` (raw lines 15–40): stage map, RFI triggers, response purpose, and no-debit boundary.
- `## Information Supplied`, `## Notification of Chargeback`, and `## 1st Chargeback` (raw lines 42–65): immutable forwarded evidence, NoC versus chargeback webhook/debit timing, acceptance or defense paths, and 40-day document deadline.
- Second `## Information Supplied` through `## Arbitration Case Filing` (raw lines 67–87): conditional reversal, 35-day second-chargeback period, no new document upload, team routes, and 40-day arbitration contact limit.

## Related

- Company: [[adyen]]
- Concept: [[adyen-risk-management]]
- Cross-scheme timing table: [[source-adyen-docs-risk-management-understanding-disputes-dispute-timeframes]]

## Raw Sources

- [[raw/adyen/docs/risk-management/chargeback-guidelines/jcb-chargebacks/2026-09-15|2026-09-15 Adyen JCB chargeback guide]]
