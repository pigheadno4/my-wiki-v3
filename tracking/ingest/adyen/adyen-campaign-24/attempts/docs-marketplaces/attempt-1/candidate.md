---
title: "Adyen Marketplaces integration overview"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces"
raw_files:
  - "adyen/docs/marketplaces/2026-09-15.md"
tags: [adyen, marketplaces, platforms, onboarding, split-payments, payouts]
---

## Overview

This 2026-09-15 Adyen **Marketplaces** guide describes the marketplace route of **Adyen for Platforms**: a marketplace onboards and verifies sellers, service providers or contractors, processes online payments on their behalf, splits payment funds, and pays out or transfers funds. It points businesses with a different model to the separate [[adyen-platforms|platforms integration guide]]. The page describes a proposed integration, not a particular user’s verification, payment, settlement or bank-received payout.

## Marketplace model and flow

- The page defines a marketplace here as processing **online payments only**, with its brand known to users and their customers and recognized by customers as the business they are dealing with. These criteria distinguish this Marketplace guide from the broader Platforms guide; the text does not establish legal seller, merchant of record or fund ownership for a particular transaction. See [[raw/adyen/docs/marketplaces/2026-09-15|raw lines 19–29]].
- Adyen describes onboarding and verification before payout, payment acceptance **on behalf of users**, payment splitting among users with cost deductions and funds held until payout, managed or custom payouts, internal debits/credits, risk controls, and reports/reconciliation. These are capability routes, with detailed conditions in their linked guides. See [[raw/adyen/docs/marketplaces/2026-09-15|raw lines 31–41]].
- The API Explorer examples for legal-entity creation, split `/payments`, and payout transfers are navigation examples, not evidence of a completed API call or financial outcome. See [[raw/adyen/docs/marketplaces/2026-09-15|raw lines 33–35]].

## Scope and availability

- The country/region and acquiring-region lists are a **2026-09-15 snapshot**, not live eligibility. The supported-country list includes a footnote that in-person payments and store creation are unavailable in the Channel Islands and Isle of Man (raw line 99), even though this Marketplace model says **online payments only** (raw line 27). Do not read that footnote as Marketplace POS support. See [[raw/adyen/docs/marketplaces/2026-09-15|raw lines 43–114]].
- Issuing, business accounts and Capital are presented as **optional financial products**. The page describes cards, business fund transfers and financing, then directs readers to separate availability and additional verification requirements; it does not establish a product grant, account opening, card issuance or financing offer for a user. See [[raw/adyen/docs/marketplaces/2026-09-15|raw lines 116–143]].

## Detail locators

- Marketplace model, online-only condition, actors and feature routes: [[raw/adyen/docs/marketplaces/2026-09-15|raw lines 15–41]].
- Dated supported-country and acquiring-region lists, including the in-person footnote: [[raw/adyen/docs/marketplaces/2026-09-15|raw lines 43–114]].
- Optional financial products and next-step guide links: [[raw/adyen/docs/marketplaces/2026-09-15|raw lines 116–163]].

## Related

- [[adyen-platforms]] — common Adyen for Platforms product and separate broader integration route.
- [[adyen-classic-platforms]] — older Classic integration, with distinct API/resource guidance.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/marketplaces/2026-09-15|Marketplaces overview (captured 2026-09-15)]]
