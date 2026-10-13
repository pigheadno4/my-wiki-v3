---
title: "Adyen American Express chargebacks"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/chargeback-guidelines/american-express-chargebacks"
raw_files:
  - "adyen/docs/risk-management/chargeback-guidelines/american-express-chargebacks/2026-09-15.md"
tags: [adyen, risk-management, disputes, chargebacks, american-express]
---

## Overview

This [[adyen]] guide describes American Express dispute stages and merchant defense actions within [[adyen-risk-management]]. An RFI may precede a chargeback, but American Express can start directly with a Notification of Chargeback (NoC). The page is a 2026-09-15 documentation snapshot; it does not establish the current state or deadline of an individual case.

## Key takeaways

- If an RFI is sent, the merchant can upload supporting documents within 14 days. No funds have been deducted at that stage. If the merchant does not respond and then receives a chargeback for the transaction, this guide says the chargeback cannot be defended. American Express can omit the RFI and begin at NoC under certain circumstances.
- NoC is sent when the issuer initiates the chargeback. The merchant has 14 days from receiving NoC to submit defense documents through Customer Area or the Disputes API. NoC occurs before the funds are deducted, yet the guide says it always indicates an upcoming chargeback debit. Accepting the chargeback in Customer Area loses the dispute and ends the ability to defend.
- Adyen forwards submitted documents to the scheme at an `InformationSupplied` stage, after which they cannot be changed. The guide says there is no later opportunity to add documents or other information; it advises addressing the dispute reason rather than submitting only an order overview.
- At the first chargeback, the account is debited and the `Chargeback` journal is booked, usually a few days after NoC. The case remains open for defense until the defense window expires. If the issuer rejects the defense after submission, the dispute is lost. If accepted, `ChargebackReversed` is booked and the disputed amount is transferred back; that is normally final, but American Express can exceptionally reopen a case closed in the merchant's favor, book `SecondChargeback`, and debit the account again.
- This page names the relevant journals and financial movements but states no chargeback fee amount or fee rule. Do not infer that fees are zero or apply another scheme's fees.

## Detail locators

- `# American Express chargebacks`, raw lines 15–27 — stage list, with RFI marked optional.
- `## Request for Information (RFI)`, raw lines 33–43 — 14-day RFI response, no debit yet, inability to defend after an unanswered RFI followed by chargeback, and direct-NoC exception.
- First `## Information Supplied`, raw lines 45–47 — forwarding of RFI documents, no later change, journal, and webhook.
- `## Notification of Chargeback`, raw lines 49–68 — NoC start event, 14-day defense window, pre-debit notice, acceptance versus defense, document channel and completeness.
- `## 1st Chargeback` and second `## Information Supplied`, raw lines 70–80 — debit timing, defense while the window remains open, submitted-document lock, and rejected-defense finality.
- `## Chargeback Reversed` and `## 2nd Chargeback`, raw lines 82–90 — accepted-defense fund return, normal finality, exceptional reopening and final second debit.

## Related

- [[adyen]] — provider page.
- [[adyen-risk-management]] — provider risk and dispute source routes.

## Raw Sources

- [[raw/adyen/docs/risk-management/chargeback-guidelines/american-express-chargebacks/2026-09-15|American Express chargebacks (2026-09-15 snapshot)]]
