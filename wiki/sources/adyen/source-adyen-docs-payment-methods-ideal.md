---
title: "iDEAL | Wero"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/ideal"
raw_files:
  - "adyen/docs/payment-methods/ideal/2026-09-15.md"
tags: [adyen, ideal, wero, online-banking, redirect, online-payments]
---

## Overview

This 2026-09-15 Adyen overview presents iDEAL | Wero for online payments and routes readers to platform-specific integration guides. It describes a Netherlands bank-selection redirect flow and a dated iDEAL-to-Wero co-branding step. It is a provider snapshot, not evidence of current merchant eligibility, present branding compliance or an executed payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The shopper selects an issuing bank from a list, then is redirected to the bank website or mobile app to complete payment (raw lines 23–25). The page says Adyen-integrated merchants do not need direct contracts with iDEAL | Wero acquiring banks (line 27). Bank completion is described at a high level; the page does not specify a particular Checkout API response, webhook or final settlement state.
- The page says iDEAL is evolving into Wero under the European Payments Initiative, with mandatory iDEAL–Wero co-branding as a first step. Its instruction specifically addresses merchants using iDEAL on **API-only**, giving a **January 29–March 31, 2026** window to change the displayed name to “iDEAL | Wero” and use the co-branded logo with `pm-type: ideal` for logo download (lines 29–34). Treat this as dated source guidance, not a statement that a new window is open or that the same steps apply to every integration.
- The overview's capability row labels the method Online Banking, redirect, NL and EUR. It marks recurring and refunds/partial refunds positively, and separate/partial/multiple-partial capture and chargebacks with X marks (lines 36–38). Recurring and chargebacks each say “See note,” but no corresponding note appears in this pinned page; do not treat those two cells as unconditional eligibility or complete limitation detail.
- The page links Web, iOS, Android, React Native, Flutter, API-only and Pay by Link routes (lines 40–82). Those child guides, not this overview, carry integration requirements and outcome handling. The NL/EUR row and route list do not prove a given merchant account has iDEAL | Wero enabled.

## Detail locators

- Identity, issuing-bank redirect, contract statement and co-branding instructions: raw lines 15–34.
- Country/currency, lifecycle capability table and unresolved “See note” references: raw lines 36–38.
- Platform and API-only integration navigation: raw lines 40–82; general related routes: lines 84–89.

## Related

- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/ideal/2026-09-15|iDEAL | Wero overview, fetched 2026-09-15]]
