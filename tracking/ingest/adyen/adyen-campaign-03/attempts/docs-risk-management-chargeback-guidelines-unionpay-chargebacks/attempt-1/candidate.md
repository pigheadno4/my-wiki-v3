---
title: "Adyen Docs: UnionPay chargebacks"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/chargeback-guidelines/unionpay-chargebacks"
raw_files:
  - "adyen/docs/risk-management/chargeback-guidelines/unionpay-chargebacks/2026-09-15.md"
tags: [adyen, unionpay, chargebacks, disputes, risk-management]
---

## Overview

This [[adyen]] guide describes UnionPay (CUP) chargeback handling through an optional Request for Information (RFI), Notification of Chargeback (NoC), defense, automatic pre-arbitration, and a possible final reversal. Its described flow applies to UnionPay chargebacks **received on or after 13 April 2020**; the guide says earlier chargebacks are not defendable through Adyen. This is the 2026-09-15 snapshot of a UnionPay-specific route, not a general chargeback rule or a determination of a current case outcome. See [[adyen-risk-management]].

## Key takeaways

- An RFI can precede the chargeback. Funds are not deducted at RFI, and the merchant can upload information through Customer Area or the Disputes API. **If the merchant does not respond to the RFI and later receives a chargeback for that transaction, that chargeback is undefendable.** After Adyen forwards RFI documents, they cannot be changed; Information Supplied ends the RFI, although a chargeback can still follow.
- A NoC may follow an RFI or arise directly after a payment becomes Settled or Refunded. The merchant has **30 days from receiving the NoC** to submit defense documents. NoC has not yet deducted the funds, but signals that the account will be debited; the first chargeback books that debit, usually a few days after NoC. Accepting in Customer Area loses and closes defense; defending requires reason-specific documents via Customer Area or the Disputes API. An order overview alone is insufficient, and there is no later opportunity to add information.
- After Adyen forwards chargeback defense documents to UnionPay at Information Supplied, the documents cannot change and funds are **not immediately returned**. Adyen automatically sends a pre-arbitration case to the scheme; the issuer has **20 days** to accept or decline it. Acceptance books `PreArbitrationWon`, returns the funds, and leads to final `ChargebackReversed`. Decline books `PreArbitrationLost`; the cardholder retains the funds, and the guide calls this final with no further journals.
- Despite that stated lost-case finality, the guide instructs a merchant who wants to challenge the issuer's rejection to contact the Adyen Disputes Team **within five days of receiving the PreArbitrationLost journal**. It does not promise a changed outcome.

## Detail locators

- **Scope and stages, raw lines 15–29** — 13 April 2020 receipt cutoff and sequence with optional RFI.
- **RFI and RFI Information Supplied, raw lines 35–49** — no initial debit, response route, undefendable later chargeback if unanswered, and immutable forwarded documents.
- **NoC and first chargeback, raw lines 51–76** — 30-day defense clock, no debit yet at NoC, accept/defend routes, evidence cutoff, and later debit.
- **Defense Information Supplied and pre-arbitration, raw lines 78–94** — no immediate return, automatic case, issuer's 20-day review, win/loss effects and five-day contact instruction.
- **Chargeback Reversed, raw lines 96–98** — returned funds and final reversal after accepted pre-arbitration.

## Related

- [[adyen-risk-management]]
- [[source-adyen-docs-risk-management-chargeback-guidelines]]
- [[source-adyen-docs-risk-management-understanding-disputes-dispute-process-and-flow]]

## Raw Sources

- [[raw/adyen/docs/risk-management/chargeback-guidelines/unionpay-chargebacks/2026-09-15|Adyen UnionPay chargebacks guide (2026-09-15 snapshot)]]
