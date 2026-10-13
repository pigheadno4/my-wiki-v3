---
title: "Adyen Docs: Cash App Pay chargebacks"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/chargeback-guidelines/cash-app-pay-chargebacks"
raw_files:
  - "adyen/docs/risk-management/chargeback-guidelines/cash-app-pay-chargebacks/2026-09-15.md"
tags: [adyen, cash-app-pay, disputes, chargebacks]
---

## Overview

This Adyen guide describes the **Cash App Pay** chargeback route: Notification of Chargeback (NoC), Chargeback, Information Supplied, and a successful-defense Chargeback Reversed. It routes through [[adyen-risk-management]]. Cash App Pay here is **distinct from Cash App Afterpay** and its separate chargeback guide; do not carry Afterpay's stage, decision, or fee terms into this Cash App Pay snapshot.

## Key takeaways

- **Shoppers** can initiate a Cash App Pay chargeback directly with Cash App Pay up to **120 days after the payment, order cancellation, or expected delivery** of goods or services. When Cash App Pay opens the dispute, funds are charged back. The merchant has **13 days to defend**, starting at the **NoC**. If the merchant does not respond within that window, the dispute is lost for the shopper; if it responds on time **and wins**, funds return to the merchant. A timely response alone is not a guaranteed win.
- Cash App Pay sends the NoC and Adyen books the NotificationOfChargeback journal. Cash App Pay then initiates the chargeback on behalf of the cardholder, usually **the same day as NoC**. Adyen assigns it in Customer Area or sends a webhook; the **liable account** is debited for the disputed amount and Adyen books the Chargeback journal.
- After review, the merchant can **accept in Customer Area**, which loses the dispute and ends defense, or **defend** by uploading relevant documents through Customer Area or the Disputes API. There is no later chance to provide information. At Information Supplied, Adyen forwards documents to Cash App Pay and they cannot be changed.
- **If Cash App Pay reviews and accepts the defense**, Chargeback Reversed is the **final status**: Adyen books the ChargebackReversed journal and returns the disputed amount to the merchant account. This page gives no chargeback fee or arbitration schedule; those terms should not be inferred from Cash App Afterpay or other methods.

## Detail locators

- **Opening and flow, raw lines 15–28** — Cash App Pay identity, 120-day initiation anchors, 13-day response condition, and four stages.
- **NoC and chargeback, raw lines 30–40** — NoC-based defense clock, Cash App Pay/cardholder actor, usually same-day chargeback, liable-account debit, and Adyen journal/webhook handling.
- **Merchant response and Information Supplied, raw lines 42–51** — accept channel, defense upload channels, no later information, and immutable forwarded documents.
- **Chargeback Reversed, raw lines 53–56** — Cash App Pay acceptance, final status, returned funds, and journal.

## Related

- [[adyen]]
- [[adyen-risk-management]]
- [[source-adyen-docs-risk-management-chargeback-guidelines-afterpay-chargebacks]]

## Raw Sources

- [[raw/adyen/docs/risk-management/chargeback-guidelines/cash-app-pay-chargebacks/2026-09-15|Adyen Docs — Cash App Pay chargebacks (2026-09-15)]]
