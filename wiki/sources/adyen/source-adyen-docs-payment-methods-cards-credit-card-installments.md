---
title: "Adyen credit card installments"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cards/credit-card-installments"
raw_files:
  - "adyen/docs/payment-methods/cards/credit-card-installments/2026-09-15.md"
tags: [adyen, cards, installments, online-payments]
---

## Overview

Adyen online credit-card installment guide for Brazil/BRL, Mexico/MXN and Japan/JPY, covering country and network plan options, Web checkout or custom-card setup, payment requests, and later reconciliation and funds timing. The page metadata says last modified 2022-12-21 and this copy was captured 2026-09-15. Its support tables and examples do not prove present merchant, bank, card, or regional eligibility.

## Key takeaways

- A successful installment purchase charges the first installment immediately and schedules following installments automatically; cards that support 3D Secure can also use it for authentication. The page lists refunds, partial refunds, separate/partial captures and chargebacks for its three country/currency rows, but those feature marks do not establish a particular transaction outcome (raw lines 19–31).
- Country counts differ: Brazil allows 1–99, Mexico names 3/6/9/12/18 monthly installments, and Japan regular plans allow 2–99. Japan additionally describes regular, revolving and bonus plans; revolving requires prior issuer approval and the network matrix differs by plan (raw lines 33–57).
- Prerequisite routes are Web Drop-in/Components v3.15.0+ or a custom card UI. For Web, `/sessions` installment options are documented from v5.21.0+, while the `/payments` path sets options in the Drop-in or Card Component configuration from v3.15.0+. Sessions offers all-card or brand-specific options with `values`, optional `preselectedValue` and `plans` listed as regular/revolving; the guide’s older table marks `values` required (raw lines 59–90, 458–929). The existing [[adyen-online-payments]] concept records newer exact Web SDK 6.47.0 code accepting plan-only configuration; retain the version difference rather than applying this older table universally.
- With a custom card UI, Brazil/Mexico send valid `installments.value` on the first `/payments` request; the guide says Brazilian merchant-charged installment interest is added to `amount.value`. Japan requires Checkout API v64+ and adds `installments.plan`: regular uses value 2–99, revolving/bonus value 1. The `/sessions` `plans` table lists only regular/revolving while the Japan `/payments` path also documents bonus; these are distinct surfaces, not an all-flow plan list (raw lines 930–945, 1316–1332). Encrypted-card payloads, test endpoints, library-version snippets and idempotency keys are illustrations, not proof of a safe or successful implementation.
- On a successful first payment the guide describes a `/payments` response and AUTHORISATION webhook; it says no webhook arrives for later installment charges, whose success is checked in Settlement details reporting. This does not equate the first authorization with later settlement or bank receipt (raw lines 1312–1314, 1709–1711).
- Payout timing depends on country: Brazil says each settled installment has a 30-day settlement delay, with fee-bearing advances offered; Mexico and Japan say funds are received in full on first-installment settlement, with stated Japan Visa/Mastercard exceptions. Mexico additionally gives a then-supported issuer-bank list and requires a direct legal agreement with other issuing banks, plus an additional scheme fee. These are historical provider statements, not current support or a guarantee of receipt (raw lines 1713–1736). Test with test card numbers before live installments (raw lines 1738–1742).

## Detail locators

- Country/currency feature matrix and plan/network choices: raw lines 19–57.
- Web prerequisites, Sessions options and all-card/brand-specific examples: raw lines 59–871.
- Web client configuration examples: raw lines 872–929.
- Brazil/Mexico and Japan custom-UI `/payments` examples and versioned library samples: raw lines 930–1711.
- Country settlement, issuer-bank and test notes: raw lines 1713–1742.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-3d-secure]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/cards/credit-card-installments/2026-09-15|Adyen credit card installments snapshot]]
