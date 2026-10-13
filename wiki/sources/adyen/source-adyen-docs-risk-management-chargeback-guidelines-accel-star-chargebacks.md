---
title: "Adyen Docs: Accel and STAR chargebacks"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/chargeback-guidelines/accel-star-chargebacks"
raw_files:
  - "adyen/docs/risk-management/chargeback-guidelines/accel-star-chargebacks/2026-09-15.md"
tags: [adyen, risk-management, disputes, chargebacks, accel, star]
---

## Overview

This [[adyen]] guide describes the Accel and STAR chargeback process and defense requirements for fraud and non-fraud reason codes. Its 2026-09-15 snapshot gives reason-dependent initiation windows, a 30-day defense period measured from Notification of Chargeback (NoC), and different reversal and finality paths for the two flows. These are Accel/STAR rules in this captured guide, not a shared rule for other networks or proof of a particular dispute's current deadline. See [[adyen-risk-management]].

## Key takeaways

- The guide says an issuing bank's initiation window runs from the transaction date: **75 days** for Authorization reason codes, **90 days** for Processing error reason codes, and **120 days** for other reason codes. Once Accel or STAR opens a dispute, disputed funds are debited. NoC can arrive after a payment becomes Settled or Refunded; the chargeback debit usually occurs a few days after NoC.
- In either flow, the **30-day defense period starts at NoC**, and defense documents must be provided within 30 days after receiving it. The merchant may accept in Customer Area or through the Disputes API, closing defense, or upload reason-specific documents to defend. An order overview alone is insufficient. Once Adyen forwards the documents to the scheme at Information Supplied, they cannot be changed; the guide says there is no later opportunity to provide or update information.
- **Fraud reason codes:** after Information Supplied, Adyen automatically forwards a pre-arbitration case to the issuing bank, which has **30 days** to respond. If the bank accepts, `ChargebackReversed` is final and the disputed amount returns. If it declines, the status remains `Chargeback` and Adyen books `PreArbitrationLost`.
- **Non-fraud reason codes:** `ChargebackReversed` initially returns the amount **temporarily** while the bank reviews the defense. Bank acceptance makes that reversal final. If the cardholder challenges the evidence, the issuing bank can send pre-arbitration within **30 days of the ChargebackReversed date**. If Adyen accepts that pre-arbitration case, a `SecondChargeback` debits the returned amount again and is final.

## Detail locators

- **Opening, raw lines 19–30** — reason-code initiation windows, initial debit, 30-day defense period, and fraud/non-fraud split.
- **Fraud flow, raw lines 32–81** — NoC and first chargeback, accept/defend routes, document deadline and finality, automatic pre-arbitration, bank review, and final reversal or continuing chargeback.
- **Non-fraud flow, raw lines 83–137** — NoC and defense, temporary reversal, conditional pre-arbitration, and final second chargeback.
- **See also, raw lines 139–144** — reason-code, webhook, dispute-management, and Disputes API navigation.

## Related

- [[adyen-risk-management]]
- [[source-adyen-docs-risk-management-chargeback-guidelines]]
- [[source-adyen-docs-risk-management-understanding-disputes-dispute-process-and-flow]]

## Raw Sources

- [[raw/adyen/docs/risk-management/chargeback-guidelines/accel-star-chargebacks/2026-09-15|Adyen Accel and STAR chargebacks guide (2026-09-15 snapshot)]]
