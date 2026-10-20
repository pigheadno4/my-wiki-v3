---
title: "Adyen Issuing: Top up accounts"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/add-manage-funds/top-ups"
raw_files:
  - "adyen/docs/issuing/add-manage-funds/top-ups/2026-09-15.md"
tags: [adyen, issuing, balance-accounts, recurring-top-ups, direct-debit]
---

## Overview

This 2020-modified, 2026-09-15-captured Adyen Issuing overview explains recurring top-ups as a way to increase a balance account apart from internal funds transfers or acquired payments. A configured trigger initiates an outgoing direct-debit request to a bank-account source and an incoming transfer to the linked balance account. This describes the intended funds direction, not proof that a particular bank debit, transfer or card payment completed. [[adyen]] [[adyen-issuing]]

## Key takeaways

- The stated use cases are liquidity for pre-funded card programs and sufficient funds for active Adyen-issued cards. The top-up amount can be a fixed value or a target available balance; the latter is described as increasing available balance to the configured target when triggered. See raw lines 19-31.
- The guide describes a balance threshold and a checking schedule: weekdays at 07:00, weekly Monday at 07:00, monthly on the first at 07:00, each in the balance account's time zone; `null`/omitted schedule is described as continuous checking. A top-up is triggered when available balance falls **below** the threshold, and Adyen creates an outgoing direct-debit request to pull funds into the balance account. See raw lines 33-44 and 60-66.
- The text says trigger criteria use **both** schedule and threshold, yet also says omitted schedule defaults to `null`; read this as a described default rather than proof that the API requires an explicit schedule field. The companion [[source-adyen-docs-issuing-add-manage-funds-top-ups-create-recurring-top-ups]] has a separate Customer Area `less than or equal to` threshold statement, while this overview says `below`; equality behavior is unresolved across the captured guides. See this raw lines 35-44 and companion source's raw lines 99 and 242.
- The source is a transfer instrument, represented in API requests by `counterparty.transferInstrumentId`. The guide provides Customer Area steps for finding its ID and says to contact Adyen if none is listed. It does not establish that a listed instrument is currently eligible or that a direct debit will settle. See raw lines 46-58.
- The page routes to separate Terms of Service acceptance, recurring top-up creation/management and webhook guides. Follow those guides for setup and event details; this overview alone does not establish acceptance, an active schedule or completed funds movement. See raw lines 68-84.

## Detail locators

- Funding alternatives and use cases: raw lines 19-24. Fixed versus target amount: raw lines 26-31.
- Schedule values, balance-account time zone, null default and threshold language: raw lines 33-44. Transfer-instrument ID lookup: raw lines 46-58.
- Three-step check, trigger and transfer description: raw lines 60-66. Child-guide navigation: raw lines 68-84.

## Related

- [[adyen-issuing]] — main Issuing concept and reciprocal source route.
- [[source-adyen-docs-issuing-add-manage-funds-top-ups-sign-terms-of-service]] — top-up contract acceptance.
- [[source-adyen-docs-issuing-add-manage-funds-top-ups-create-recurring-top-ups]] — creation requirements and configuration.

## Raw Sources

- [[raw/adyen/docs/issuing/add-manage-funds/top-ups/2026-09-15|Adyen Issuing top-up overview, captured 2026-09-15]]
