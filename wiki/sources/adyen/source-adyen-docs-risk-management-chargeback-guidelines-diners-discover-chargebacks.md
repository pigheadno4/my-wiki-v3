---
title: "Adyen Docs: Diners/Discover chargebacks"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/chargeback-guidelines/diners-discover-chargebacks"
raw_files:
  - "adyen/docs/risk-management/chargeback-guidelines/diners-discover-chargebacks/2026-09-15.md"
tags: [adyen, diners, discover, disputes, chargebacks, arbitration]
---

## Overview

This Adyen Diners/Discover guide describes an optional Request for Information (RFI), chargeback defense, conditional reversal, pre-arbitration, second chargeback, and possible arbitration case filing. It routes through [[adyen-risk-management]]. The captured page is a dated documentation snapshot, not proof of current scheme rules, fees, or a particular dispute result.

## Key takeaways

- An **optional RFI** can arise when a cardholder does not recognize or agree to a charge, or during a fraud investigation. At RFI, funds are **not yet deducted**. Adyen advises uploading information that helps identify the charge or supports its validity and gives an **18-day** upload window. Its warning is conditional: if the merchant does not respond before the issuer sends a chargeback, the merchant **might** be unable to defend it. The raw wording for the 18-day start is “Request for Information's data”; check the raw page rather than assuming a clearer start date.
- The issuing bank can send a Notification of Chargeback (NoC) after an RFI, or skip RFI and send it after a payment is marked Settled or Refunded. Adyen warns of a withdrawal, usually a few days after NoC. At first chargeback, Adyen assigns the dispute for merchant review, books NotificationOfChargeback and Chargeback journals, sends a CHARGEBACK webhook, and debits the disputed amount. These are descriptions of the chargeback debit, not two independent debits.
- The merchant can **accept** through Customer Area or Disputes API, closing defense, or **defend** by uploading relevant documents through either channel. Evidence must address the dispute reason; an order overview alone is insufficient. The guide says to submit within **40 days** and says there is no later opportunity to add or update evidence; the captured text does **not specify the starting event** for that 40-day window. Once forwarded to the scheme at Information Supplied, documents cannot be changed.
- **Chargeback Reversed** returns the disputed amount while the issuer is still reviewing the defense; the guide calls it final **if the issuer accepts**. A cardholder can instead challenge the evidence. The bank can send pre-arbitration to Adyen within **30–32 days of the Information Supplied upload date**. Adyen's Chargeback Team accepts or declines that case. If Adyen accepts, the merchant is debited and a SecondChargeback journal is booked; the second chargeback description calls that status final and bars more defense documents.
- If Adyen **declines pre-arbitration**, the bank **can** escalate to Diners/Discover arbitration case filing. The scheme's committee then rules against the party that failed the dispute conditions and requirements; that losing party is liable for a **USD 500 filing fee on top of the disputed amount**. The fee is conditional on that arbitration ruling, not an automatic fee for an RFI, first chargeback, or every pre-arbitration.

## Detail locators

- **Flow and optional RFI, raw lines 19–57** — stage sequence, RFI actors, no initial deduction, 18-day wording, conditional missed-RFI warning, and example documents.
- **Information Supplied, NoC, and first chargeback, raw lines 59–82** — document forwarding, RFI versus direct NoC, debit/journals/webhooks, acceptance or defense, and 40-day wording.
- **Reversal and pre-arbitration, raw lines 84–102** — immutable evidence, conditional reversal finality, 30–32-day period from upload, Adyen Chargeback Team response, and possible escalation.
- **Second chargeback and arbitration, raw lines 104–112** — no additional defense, stated final second-chargeback status, scheme ruling, and conditional USD 500 filing fee.

## Related

- [[adyen]]
- [[adyen-risk-management]]

## Raw Sources

- [[raw/adyen/docs/risk-management/chargeback-guidelines/diners-discover-chargebacks/2026-09-15|Adyen Docs — Diners/Discover chargebacks (2026-09-15)]]
