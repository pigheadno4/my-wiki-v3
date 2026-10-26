---
title: "Trustly"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/trustly"
raw_files:
  - "adyen/docs/payment-methods/trustly/2026-09-15.md"
tags: [adyen, trustly, online-banking, redirect, chargebacks, online-payments]
---

## Overview

This Trustly overview (last modified 2025-07-31, captured 2026-09-15) describes online payments directly from bank accounts in Europe, especially popular in Nordic countries/regions. The shopper is redirected to a Trustly-hosted bank-selection page, authenticates with their bank, chooses an account, confirms with a one-time code, and returns to the merchant website or app. The page's most consequential qualification is that a successful `AUTHORISATION` webhook means checks passed and a bank transfer was initiated, **not that Adyen has received the funds**. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- The capability table labels Trustly **Online Banking** with **Redirect** flow, countries as **International**, and currencies DKK, EUR, NOK and SEK. Its snapshot marks recurring and separate/partial/multiple partial captures unavailable; refunds, partial and multiple partial refunds, and chargebacks are marked available. These marks do not establish current country, bank, merchant or currency eligibility. See raw lines 23–36.
- After selection, the shopper sees available banks in their country/region on Trustly's hosted page, logs into the bank, selects an account, confirms with a one-time code, and returns to the merchant. This is the described shopper path, not evidence of cleared funds. See raw lines 25–32.
- A successful `AUTHORISATION` webhook signals issuer/Trustly account verification and successful **initiation** of the transfer. The shopper may still cancel where a bank permits same-day cancellation, or a bank may process later without blocking funds; the transfer can fail. In these cases Adyen says it is not informed of failure and does not know if the bank might still process it. See raw lines 38–45.
- The Adyen-side status stays **SentForSettle** until funds arrive. If funds have not arrived after **8 calendar days**, the page says the status becomes **Settled**, then **Chargeback**, and a `CHARGEBACK` webhook is sent. Trustly chargebacks cannot be defended. If money arrives after that point, a `CHARGEBACK_REVERSED` webhook follows. The intermediate Settled label in this exceptional sequence is not proof that funds were received. See raw lines 47–53.
- The overview routes to Web, iOS, Android and API-only integration pages, and points to Pay by Link. Those links are navigation; this page does not define platform-specific API/SDK versions, request fields, customer setup, refund execution or current availability. See raw lines 55–85.

## Detail locators

- Purpose, geography, redirect and shopper bank flow: raw lines 15–32.
- Historical capability table, currencies and feature marks: raw lines 34–36.
- Authorized-but-unfunded risk, failure examples, chargeback and reversal sequence: raw lines 38–53.
- Platform and Pay by Link routes: raw lines 55–85.

## Related

- [[adyen-online-payments]] — online payment-method context.

## Raw Sources

- [[raw/adyen/docs/payment-methods/trustly/2026-09-15|Trustly overview, captured 2026-09-15]]
