---
title: "Adyen NYCE chargebacks"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/chargeback-guidelines/nyce-chargebacks"
raw_files:
  - "adyen/docs/risk-management/chargeback-guidelines/nyce-chargebacks/2026-09-15.md"
tags: [adyen, risk-management, disputes, chargebacks, nyce]
---

## Overview

This Adyen documentation snapshot describes the NYCE chargeback sequence, the merchant's defense window, and what each subsequent state means. Its deadlines and defense rules apply to this NYCE flow.

## Key takeaways

- A NYCE Notification of Chargeback (NoC) may arrive immediately after a payment becomes Settled or Refunded. Adyen sends a `NOTIFICATION_OF_CHARGEBACK` webhook; the debit usually follows a few days later. The merchant's 30-day defense period starts at the NoC, not at the debit or first-chargeback notice.
- At the first chargeback, Adyen assigns the dispute in Customer Area, books `NotificationOfChargeback` and `Chargeback` journals, sends a `CHARGEBACK` webhook, and debits the chargeback amount. The merchant may accept via Customer Area or Disputes API, closing the case for defense, or upload relevant defense documents through either channel.
- The defense must address the dispute reason; an order overview alone is insufficient. Documents are due within 30 days after the NoC, with no later opportunity to provide or update them. After Adyen forwards submitted documents to the scheme, they cannot be changed; Adyen books `InformationSupplied` and sends its webhook.
- A Chargeback Reversed returns the disputed amount and triggers a journal and webhook, but the issuing bank is still reviewing the defense. The reversal becomes final only if the bank accepts the defense.
- If the merchant defended the first chargeback, the issuing bank may initiate a second chargeback within 30 days of Chargeback Reversed. The returned amount is debited again, with a `SecondChargeback` journal and webhook. NYCE does not permit second-chargeback defense documents. The page advises contacting the issuing bank directly if the merchant has enough information to challenge it; it does not promise a successful challenge.

## Detail locators

- NYCE flow and overall 30-day period: [[raw/adyen/docs/risk-management/chargeback-guidelines/nyce-chargebacks/2026-09-15|raw snapshot]], lines 19–27.
- NoC timing, webhook, debit timing, and defense-clock start: [[raw/adyen/docs/risk-management/chargeback-guidelines/nyce-chargebacks/2026-09-15|raw snapshot]], lines 31–37.
- First chargeback, merchant actions, evidence standard, and submission deadline: [[raw/adyen/docs/risk-management/chargeback-guidelines/nyce-chargebacks/2026-09-15|raw snapshot]], lines 39–52.
- Information Supplied and provisional Chargeback Reversed: [[raw/adyen/docs/risk-management/chargeback-guidelines/nyce-chargebacks/2026-09-15|raw snapshot]], lines 54–62.
- Second-chargeback timing, renewed debit, and defense limitation: [[raw/adyen/docs/risk-management/chargeback-guidelines/nyce-chargebacks/2026-09-15|raw snapshot]], lines 64–70.

## Related

- [[adyen]]
- [[adyen-risk-management]]

## Raw Sources

- [[raw/adyen/docs/risk-management/chargeback-guidelines/nyce-chargebacks/2026-09-15|Adyen Docs — NYCE chargebacks (2026-09-15 snapshot)]]
