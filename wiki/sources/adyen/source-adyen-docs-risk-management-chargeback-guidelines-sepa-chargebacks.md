---
title: "Adyen Docs: SEPA chargebacks"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/chargeback-guidelines/sepa-chargebacks"
raw_files:
  - "adyen/docs/risk-management/chargeback-guidelines/sepa-chargebacks/2026-09-15.md"
tags: [adyen, sepa, direct-debit, disputes, chargebacks]
---

## Overview

This Adyen guide describes chargebacks on **SEPA Direct Debit**, a bank-account-based payment method used for ecommerce and recurring payments, and gives notification and prevention guidance. It routes through [[adyen-risk-management]]. The page says **no dispute management process is available for SEPA**; it does not offer a card-style defense workflow. The separate [[source-adyen-docs-online-payments-auto-rescue-sepa]] covers qualified Auto Rescue behavior; this chargeback guide itself does not establish a general right or ability to retry every SEPA chargeback.

## Key takeaways

- Unlike cards, the guide says SEPA has no extra CVC or 3D Secure authentication layer. It says a **shopper** can initiate a chargeback online **up to eight weeks after the SEPA purchase** with no questions asked, or dispute an **unauthorized or incorrect** SEPA payment within **thirteen months** when the shopper provides evidence to the bank. These are distinct triggers and windows; neither is a merchant defense period.
- A SEPA payment can be **charged back even after a refund** if the issuing bank does not take that refund into account. Adyen warns that refunding amid an ongoing customer dispute is risky and **recommends** contacting the shopper directly when a SEPA chargeback arrives. This warning does not assert that a refund itself prevents or resolves a chargeback.
- Adyen sends a **CHARGEBACK webhook** when a SEPA chargeback occurs. The page lists `pspReference`, `eventCode: CHARGEBACK`, `paymentMethod: sepadirectdebit`, reason, and `success: true`; its example is explicitly a **test** payload for reason AC01 and includes `defendable: false` and `disputeStatus: Lost`. Do not generalize every example field or example value into a required live schema or infer a merchant defense option from a `defensePeriodEndsAt` field in that example.
- With no SEPA dispute-management route in this guide, Adyen lists **precautions**: for retailers it recommends holding shipment for seven days to avoid loss if payment is unsuccessful; depending on business model, consider a maximum SEPA transaction value; and state refund timing clearly. These are advice, not mandatory controls or guaranteed prevention. The reason-code table, including AM04 and MS03, is at the raw locator; any Auto Rescue eligibility and attempt limits belong to its separate qualified source.

## Detail locators

- **Introduction, raw lines 14–22** — SEPA scope, absent card authentication and defense process, eight-week and thirteen-month shopper windows, and refund overlap.
- **Common reasons, raw lines 24–40** — reason-code descriptions, including insufficient funds, no mandate, customer refund request, and data-protection substitution.
- **Webhook fields and example, raw lines 42–87** — listed notification fields and a `live: false` AC01 example with reason, status, and `defendable` value.
- **Precautions, raw lines 89–95** — recommendation to hold retail shipment, consider value cap, and explain refund timing.

## Related

- [[adyen]]
- [[adyen-risk-management]]
- [[source-adyen-docs-online-payments-auto-rescue-sepa]]

## Raw Sources

- [[raw/adyen/docs/risk-management/chargeback-guidelines/sepa-chargebacks/2026-09-15|Adyen Docs — SEPA chargebacks (2026-09-15)]]
