---
title: "Adyen Docs: PULSE chargebacks"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/chargeback-guidelines/pulse-chargebacks"
raw_files:
  - "adyen/docs/risk-management/chargeback-guidelines/pulse-chargebacks/2026-09-15.md"
tags: [adyen, pulse, disputes, chargebacks, pre-arbitration]
---

## Overview

This Adyen guide describes two PULSE dispute routes: the default route for reasons other than fraud reason code 4868, and a separate 4868 fraud route. Their pre-arbitration, reversal, and finality steps differ. This scheme-specific snapshot routes through [[adyen-risk-management]]; it does not establish current scheme rules or outcomes for a particular case.

## Key takeaways

- In both routes, an issuing bank initiates a Notification of Chargeback (NoC), which can follow a payment marked Settled or Refunded. Adyen says funds are charged back and the merchant has **30 days after NoC** to accept or defend. The NoC warns that money will be withdrawn, usually a few days later; the first-chargeback description records the chargeback debit, journals, and CHARGEBACK webhook. These descriptions should not be read as two separate chargeback debits.
- The merchant can accept through Customer Area or Disputes API, closing the case for defense, or upload relevant defense documents through either channel. The documents must address the dispute reason; an order overview alone is insufficient. Once Adyen forwards the documents and records Information Supplied, they cannot be changed, and there is no later opportunity to add evidence.
- In the **default route**, after documents are forwarded, the disputed amount is returned at Chargeback Reversed **for reasons other than card-not-present fraud**. That reversal is not necessarily final: for disputes other than card-not-present fraud, the issuing bank can initiate pre-arbitration within 30 days of the reversal date. If the issuer declines the defense or Adyen accepts that pre-arbitration case, a **second chargeback is final**, no further documents can be uploaded, and the previously returned amount is debited again.
- In the **4868 fraud route**, Adyen automatically creates and forwards a pre-arbitration case with the documents; the issuing bank has 30 days to review it. If the bank accepts, Adyen records PreArbitrationWon and ChargebackReversed, returns the amount, and **Chargeback Reversed is final**. If the bank declines, Adyen records PreArbitrationLost and the dispute status **remains Chargeback**. This route does not describe an earlier provisional reversal.

## Detail locators

- **Two routes and sequence, raw lines 19–42** — default versus fraud reason code 4868; both have a 30-day defense-or-accept window.
- **Default NoC, first chargeback, and defense, raw lines 55–74** — issuing-bank actor, Settled/Refunded timing, merchant debit, Customer Area or Disputes API response, and evidence deadline.
- **Default Information Supplied through second chargeback, raw lines 76–94** — immutable evidence, qualified reversal and pre-arbitration, final second chargeback and re-debit.
- **4868 NoC through Information Supplied, raw lines 110–135** — NoC start, debit, response channels, and fixed evidence deadline.
- **4868 pre-arbitration and reversal, raw lines 137–147** — Adyen-created case, bank review window, accepted versus declined outcome, returned funds, and finality.

## Related

- [[adyen]]
- [[adyen-risk-management]]

## Raw Sources

- [[raw/adyen/docs/risk-management/chargeback-guidelines/pulse-chargebacks/2026-09-15|Adyen Docs — PULSE chargebacks (2026-09-15)]]
