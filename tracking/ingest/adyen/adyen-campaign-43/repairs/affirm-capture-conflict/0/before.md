---
title: "Adyen Affirm payment-method overview"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/affirm"
raw_files:
  - "adyen/docs/payment-methods/affirm/2026-09-15.md"
tags: [adyen, affirm, bnpl, installments, redirect, financing]
---

## Overview

This Adyen Affirm method overview was captured on 2026-09-15 and carries a 2022-12-05 last-modified marker. It describes a shopper redirect to Affirm for BNPL eligibility and installment choice, followed by merchant capture if approved. Its geography, cart-size, APR, conversion and audience figures are historical page claims, not evidence of current merchant eligibility, shopper approval, financing offers or payment execution. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The page presents Affirm for shoppers in Canada, the UK and the US, with a redirect payment flow and CAD, GBP and USD in its capability table. It states US cart sizes USD 35–30,000 and Canada CAD 50–30,000, with terms up to 24 months; it does not give a UK cart-size range. The table marks recurring unsupported, refunds and separate/partial/multiple-partial captures supported, and chargebacks unsupported with an unresolved 'See note' marker. These marks do not establish current account-level features or a definitive chargeback process.
- Three financing packages are described: Core offers interest-bearing monthly installments from three to 24 months; Standard adds interest-free biweekly Pay in 4 to interest-bearing monthly plans; Signature adds stated 0% APR three- and six-month terms alongside Pay in 4 and interest-bearing options. The table shows 10%–36% APR for interest-bearing installments. If `pricePlan` is not selected, the page says the MID defaults to Core. The package table's generic '35-30K' cart-size cells must be read with the explicit US/Canada currency ranges, not generalized to the UK.
- The stated flow is shopper selects Affirm, is redirected to the Affirm portal, undergoes a real-time eligibility check said not to affect credit score, and, if approved, the merchant can capture the full amount minus fees upfront. Affirm then manages the shopper's future repayments and the page says it bears credit risk. Approval and capture are conditional; the description does not prove that all shoppers qualify or that funds were actually captured/settled.
- The page routes to Web, iOS and API-only integration guides. It gives no method-specific request fields, SDK versions, action payloads, capture timing or refund implementation. Marketing claims about AOV, conversion and network size appear on this historical page but are not independently verified outcomes for any merchant.

## Detail locators

- Scope, coverage, cart sizes, term claim, credit-risk positioning and feature matrix: pinned raw lines 15–29. The matrix's chargeback 'See note' has no explanatory note in this 80-line capture.
- Historical marketing claims: pinned raw lines 31–35. Financing packages, APR/term descriptions and `pricePlan` Core default: lines 37–53.
- Redirect, eligibility, conditional capture and repayment handoff: pinned raw lines 55–60. Web/iOS/API-only navigation: lines 62–80.

## Related

- [[adyen-online-payments]] — main provider payment integration concept

## Raw Sources

- [[raw/adyen/docs/payment-methods/affirm/2026-09-15|Affirm overview, captured 2026-09-15]]
