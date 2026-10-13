---
title: "Adyen Afterpay and Clearpay Chargebacks"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/chargeback-guidelines/afterpay-chargebacks"
raw_files:
  - "adyen/docs/risk-management/chargeback-guidelines/afterpay-chargebacks/2026-09-15.md"
tags: [adyen, risk-management, disputes, chargebacks, afterpay, clearpay]
---

## Overview

This Adyen Docs snapshot describes the chargeback process for **Afterpay** in Australia, Canada, and New Zealand, **Cash App Afterpay** in the United States, and **Clearpay** in the United Kingdom. It calls them Afterpay/Clearpay collectively. See [[adyen]] and [[adyen-risk-management]]. Its regional and product scope must not be generalized to other payment methods or schemes.

For disputes opened on or after **August 25, 2025**, the described flow starts with a **Notification of Chargeback** (NoC), replacing a Request for Information. Disputes already open within their 13-day defense period on that date continue under the old flow until finalization.

## Key takeaways

- Shoppers can initiate these chargebacks with Afterpay/Clearpay up to 120 days after payment, cancellation, or expected receipt of goods or services. The merchant's 13-day window to accept or defend starts when Afterpay/Clearpay opens the dispute and sends the NoC. No response within that window, or accepting the dispute, loses it and leads to a chargeback debit. After a defense is submitted, Afterpay/Clearpay has 30 days to decide.
- At NoC, Adyen books `NotificationOfChargeback` and sends a matching webhook. Accepting through Customer Area or the Disputes API ends the right to defend. A defense must include relevant documents that address the dispute reason; an order overview alone is insufficient. The page says there is no later chance to add or update evidence. Once Adyen has forwarded the documents, `InformationSupplied` is booked and they cannot be changed.
- A refund of the disputed payment closes the dispute without a chargeback because the payment was already returned. If the defense wins, `DisputeDefensePeriodEnded` is a final status in that path. If it loses or no defense is made, `Chargeback` is booked, a webhook is sent, and the account is debited; that is final in this flow. `DisputeDefensePeriodEnded` also appears for acceptance and refund, so that journal name alone is not a win determination.
- Afterpay/Clearpay assumes fraud liability when its pre-approval shopper risk checks succeed; the page says unauthorized-payment disputes incur no dispute fee. There is no standard reason code identifying fraud at the outset, and a fraud determination can lead from an initial NoC to `DisputeWonWithoutChargeback`. All other disputes carry a dispute fee regardless of outcome, booked as `PaymentCost`; the page gives no universal numeric fee.
- The listed reason codes are `product_not_received`, `product_unacceptable`, and `credit_not_processed`, each shown as defendable with a 13-day NoC timeframe. Their evidence requirements remain at the raw table and linked reason-code guidance. This snapshot cannot establish a particular dispute's final outcome or the terms applicable to another scheme.

## Detail locators

- Opening scope and dated transition, raw lines 15–37 — product/region mapping, new versus grandfathered flow, shopper initiation window, merchant deadline, and provider decision period.
- `## Liability for fraud disputes`, raw lines 39–43 — conditional risk assumption and fraud-identification journal sequence.
- `## Notification of Chargeback (NoC)`, raw lines 45–61 — webhook, defense clock, accept/defend routes, evidence finality, and refund closure.
- `## Information Supplied` and `## Chargeback`, raw lines 63–74 — immutable forwarded evidence, provider review, final win/loss routes, and debit.
- `## Dispute reasons`, raw lines 76–84 — three reason codes, defendability, and linked defense requirements.
- `## Dispute fees`, raw lines 86–90 — unauthorized-payment exception, other-dispute fee, and `PaymentCost` reporting route.

## Related

- [[adyen]] — provider page.
- [[adyen-risk-management]] — provider dispute and risk concept.
- [[source-adyen-docs-risk-management-chargeback-guidelines]] — chargeback-guidelines directory for other schemes and methods.

## Raw Sources

- [[raw/adyen/docs/risk-management/chargeback-guidelines/afterpay-chargebacks/2026-09-15|Adyen Docs — Afterpay and Clearpay chargebacks (2026-09-15 snapshot)]]
