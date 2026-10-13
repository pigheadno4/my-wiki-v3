---
title: "Adyen Docs: Elo chargebacks"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/chargeback-guidelines/elo-chargebacks"
raw_files:
  - "adyen/docs/risk-management/chargeback-guidelines/elo-chargebacks/2026-09-15.md"
tags: [adyen, elo, chargebacks, disputes]
---

## Overview

This [[adyen]] webpage snapshot describes the Elo-card chargeback flow and merchant defense guidance. It distinguishes optional Request for Information (RFI), Notification of Chargeback, first chargeback, conditional pre-arbitration, second chargeback, and arbitration case filing. Its 2026-09-15 capture has 2019-10-08 `last_modified` metadata; the stated timeframes and fee are historical document evidence, not verification of current Elo rules or a specific case. See [[adyen-risk-management]].

## Key takeaways

- At optional RFI, funds have not yet been deducted. For RFI codes other than 04, the guide says to upload recognition or validity evidence within **18 days**. Code 04 carries separate fraud-analysis recommendations. See raw **Optional: Request for Information (RFI)** and **RFI defense recommendations** for code-specific and physical/digital-goods examples.
- Notification of Chargeback (NoC) can follow RFI or occur without RFI after a payment is Settled or Refunded; it signals that money will be withdrawn, usually with the debit a few days later. At first chargeback, the issuer initiates the claim, Adyen assigns it for merchant review, books *NotificationOfChargeback* and *Chargeback*, sends a `CHARGEBACK` webhook, and debits the account for the disputed amount.
- The merchant can accept the first chargeback through Customer Area or the Disputes API, closing defense, or defend through either route. Evidence must address the dispute reason; an order overview alone is insufficient. The guide requires defense documents within **18 days** and says there is no later opportunity to add or update information. After Adyen receives and forwards documents to Elo, they cannot be changed; *InformationSupplied* is booked and an `INFORMATION_SUPPLIED` webhook is sent. See raw **1st Chargeback** and **Information Supplied**.
- For Elo Consumer disputes and Processing errors, the disputed amount is returned after defense material is uploaded and *Chargeback reversed* is booked. This return is not a final win: the cardholder can challenge the evidence, and their bank can send pre-arbitration within **30 days of the Information Supplied date**. The guide says bank-initiated pre-arbitration applies only to those Elo workflow categories. The Adyen Chargeback Team, rather than the merchant, reviews and accepts or declines those cases. If Adyen accepts, the merchant is debited and *SecondChargeback* is booked; if it declines, the bank may escalate to Elo arbitration. See raw **Chargeback Reversed** and **Pre-arbitration**.
- A second chargeback follows if the issuer declines defense or Adyen accepts pre-arbitration; no new defense documents can be uploaded and the guide calls this the final status. At arbitration case filing, Elo's committee rules on liability; the party that did not meet dispute requirements loses and owes a **USD 500 filing fee** on top of the disputed amount. See raw **2nd Chargeback** and **Arbitration case filing**.

## Detail locators

- Raw **Elo flow** and opening stage list show the described sequence; stages are conditional, and RFI is optional.
- Raw **Elo transaction receipt RFI reasons** lists codes 01, 03, 04, and 05; raw **Reason codes and guidelines** links to the Elo dispute-reason reference.
- Raw **Notification of Chargeback** and **1st Chargeback** identify event, journal, debit, and merchant action boundaries.

## Related

- [[source-adyen-docs-risk-management-understanding-disputes-dispute-process-and-flow]] — general scheme-dependent dispute stages.
- [[source-adyen-docs-risk-management-disputes-api]] — API handling route.

## Raw Sources

- [[raw/adyen/docs/risk-management/chargeback-guidelines/elo-chargebacks/2026-09-15|Elo chargebacks (2026-09-15 snapshot)]]
