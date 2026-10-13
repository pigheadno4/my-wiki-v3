---
title: "Adyen Docs: Cartes Bancaires chargebacks"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/chargeback-guidelines/cartes-bancaires-chargebacks"
raw_files:
  - "adyen/docs/risk-management/chargeback-guidelines/cartes-bancaires-chargebacks/2026-09-15.md"
tags: [adyen, cartes-bancaires, chargebacks, disputes, risk-management]
---

## Overview

This [[adyen]] Cartes Bancaires chargeback page gives a narrow defense rule and three reasons for which Adyen says it automatically defends. In this 2026-09-15 snapshot, **reason code 45 (Fraud -Disputed transaction) is not defendable**. Adyen separately lists a past chargeback time limit, a credit issued before the chargeback, and a fully authenticated 3D Secure transaction as its automatic-defense reasons. The page does not describe a general merchant-submitted defense flow or a response deadline. See [[adyen-risk-management]].

## Key takeaways

- Cartes Bancaires can also be used to process on international networks, but these chargeback statements concern the Cartes Bancaires page and should not be applied to a different processing network.
- Adyen's listed automatic-defense grounds are **Past Chargeback Time Limit (> 400 days)**, **Credit previously issued** (the transaction must have been refunded before the chargeback was issued), and **3D Secure Fully Authenticated Transaction**. The >400-day criterion is presented as an automatic-defense reason, not a merchant defense window.
- The provider scope matters: the existing [[cartes-bancaires]] concept's unqualified “Cannot contest” line is based on a Stripe source, while this Adyen page describes limited automatic defense. Keep those provider-specific statements distinct.

## Detail locators

- **Cartes Bancaires context and reason-code limit, raw lines 14–18** — international-network context and non-defendable reason code 45.
- **Automatic-defense list, raw lines 20–24** — three specified reasons, including >400 days and a refund before the chargeback.
- **Reason-code navigation, raw lines 26–28** — link to the Cartes Bancaires dispute-reason list; detailed reason-code rules are outside this short page.

## Related

- [[adyen-risk-management]]
- [[source-adyen-docs-risk-management-chargeback-guidelines]]
- [[cartes-bancaires]]

## Raw Sources

- [[raw/adyen/docs/risk-management/chargeback-guidelines/cartes-bancaires-chargebacks/2026-09-15|Adyen Cartes Bancaires chargebacks page (2026-09-15 snapshot)]]
