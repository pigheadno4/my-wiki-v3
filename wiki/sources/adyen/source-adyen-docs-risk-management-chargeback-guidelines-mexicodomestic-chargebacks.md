---
title: "Adyen Docs: Mexico domestic chargebacks"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/chargeback-guidelines/mexicodomestic-chargebacks"
raw_files:
  - "adyen/docs/risk-management/chargeback-guidelines/mexicodomestic-chargebacks/2026-09-15.md"
tags: [adyen, mexico-domestic, disputes, chargebacks, arbitration]
---

## Overview

This Adyen guide describes the **Mexico domestic** chargeback path, from an optional Request for Information (RFI) through first chargeback, defense, conditional reversal or second chargeback, and possible arbitration filing. It routes through [[adyen-risk-management]]. The pinned page does **not name Carnet**; its Mexico-domestic label should not be extended to every Carnet or Mexican card dispute without separate evidence. This dated snapshot does not establish current scheme rules or a specific dispute outcome.

## Key takeaways

- An **optional RFI** can arise when a cardholder does not recognize or agree to a charge, or in a fraud investigation. Adyen advises the merchant to upload information supporting recognition or validity. **Funds are not yet deducted** at RFI. After an RFI—or without one if the step is skipped—the **issuing bank** can initiate a Notification of Chargeback (NoC); without RFI, the page says NoC can occur after the payment is Settled or Refunded. Adyen sends the NoC webhook and warns of a withdrawal, with the debit usually a few days later.
- At **first chargeback**, the issuing bank acts on behalf of the cardholder. Adyen assigns the dispute for merchant review, books NotificationOfChargeback and Chargeback journals, sends a CHARGEBACK webhook, and debits the chargeback amount. The merchant can accept through Customer Area or Disputes API, closing defense, or upload relevant evidence through those channels. Evidence must address the reason; an order overview alone is insufficient. The defense documents are due **within 25 days after receiving NoC**. The guide says there is no later chance to add or update them; once Adyen forwards them to the scheme at Information Supplied, they cannot be changed.
- **If the issuer accepts the defense**, Adyen books ChargebackReversed, returns the disputed amount, and calls that outcome final. **If the issuer declines**, the issuing bank can initiate a second chargeback on behalf of the cardholder **within 30 days from the first chargeback defense date**. The SecondChargeback journal can take **up to 45 days** to be booked, and the page calls second chargeback a final status. It also separately describes a possible later arbitration filing route; do not read “final status” as removing that stated merchant decision.
- **After receiving a second chargeback**, the merchant decides whether to pursue the case. To pursue it, the merchant must contact the **Adyen Chargeback team** with supporting information **within 10 days of receiving the second chargeback**. A **USD 500 fine** applies **if arbitration is raised and lost**; the page does not present that fine as automatic for any earlier stage. Adyen says it is not responsible if the dispute is ruled in the cardholder's favor.

## Detail locators

- **Mexico domestic flow and optional RFI, raw lines 15–44** — named scope, stage sequence, RFI actor and no deduction, and immutable forwarded documents.
- **NoC and first chargeback, raw lines 46–65** — issuing-bank trigger, optional RFI, payment statuses, debit, merchant response channels, and 25-day clock starting at NoC receipt.
- **Information Supplied and outcomes, raw lines 67–81** — forwarded evidence, accepted-defense reversal, issuer-declined second chargeback within 30 days of defense, and up-to-45-day journal timing.
- **Arbitration filing, raw lines 83–87** — merchant decision and Adyen Chargeback-team contact within 10 days of second-chargeback receipt, plus conditional USD 500 fine.

## Related

- [[adyen]]
- [[adyen-risk-management]]

## Raw Sources

- [[raw/adyen/docs/risk-management/chargeback-guidelines/mexicodomestic-chargebacks/2026-09-15|Adyen Docs — Mexico domestic chargebacks (2026-09-15)]]
