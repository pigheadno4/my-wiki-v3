---
title: "Adyen Issuing overview"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing"
raw_files:
  - "adyen/docs/issuing/2026-09-15.md"
tags: [adyen, issuing, cards, balance-platform, webhooks]
---

## Overview

This 2023-modified page, captured 2026-09-15, introduces Adyen Issuing as a virtual and physical card program for a platform's users. It describes Mastercard and Visa cards, authorization requests that can be sent to the platform's servers for an approve/decline decision, optional automatic transaction rules, and a choice between a shared funding pool and balances per card. The platform manages account creation, card customization, funds and user contact; an Issuing integration uses a balance platform and the Balance Platform API. This is an integration overview, not proof of an active card program or completed card payment.

## Key takeaways

- The page distinguishes an `accountHolder` (the company or a customer, depending on account structure), a `balanceAccount` holding funds for that holder, and a `paymentInstrument` representing the card associated with a balance account. It says creating the payment instrument issues a card. Optional `transactionRules` can automatically approve or deny authorizations; the company's liable balance account contains funds for loading cards and balance transfers.
- Issuing events, including payments, captures and refunds, are asynchronous. The page says an integration is incomplete without accepting and handling webhooks. A resource setup or authorization decision alone does not establish capture, refund or settled funds.
- The captured supported-region list names the European Economic Area, United Kingdom and United States. This historical list does not establish current availability or a particular platform's or user's eligibility. PCI compliance scope depends on card type and use case; the page directs readers to an Adyen contact for applicability.

## Detail locators

- Opening and capabilities — card products, authorization routing, automatic rules, funding choices, platform responsibilities and API context (raw lines 15–34).
- `Supported countries/regions` and `Acquiring regions` — captured location lists and the page's acquiring-region definition (raw lines 36–48).
- `Core concepts and resources` — required resource identities, optional transaction rules and liable balance account (raw lines 50–66).
- `Example account structures` — illustrative 1-1-1 and 1-N structures, not required cardinalities (raw lines 68–75).
- `Webhooks` and `PCI compliance` — asynchronous event handling and conditional PCI scope (raw lines 77–85).
- `Next steps` — get-started and integration-checklist navigation (raw lines 87–99).

## Related

- Company: [[adyen]]
- Main concept: [[adyen-issuing]]
- Umbrella product family: [[adyen-financial-products]]

## Raw Sources

- [[raw/adyen/docs/issuing/2026-09-15|2026-09-15 Adyen Issuing overview]]
