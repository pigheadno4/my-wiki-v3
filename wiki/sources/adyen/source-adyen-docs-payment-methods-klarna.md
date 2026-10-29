---
title: "Klarna | Adyen Docs"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/klarna"
raw_files:
  - "adyen/docs/payment-methods/klarna/2026-09-15.md"
tags: [adyen, klarna, buy-now-pay-later, payment-methods]
---

## Overview

This 2026-09-15 Adyen Docs snapshot introduces Klarna for online payments and routes merchants to Web, iOS, Android, API-only and Pay by Link integration guides. It describes shopper choices of **Pay later** (after delivery), **Pay over time** (installments) and **Pay now** (online banking or direct debit), all shown as redirect flows. The availability matrix is specific to country/region, currency and product; it is not merchant approval or a successful payment. The page also has a separate **Billie (B2B)** row, which should not be treated as a fourth consumer Klarna choice. See [[adyen-online-payments]] and [[adyen]].

## Key takeaways

- Klarna checks shopper risk before approval. The page says that, if successful, Klarna takes the full fraud risk and pays the merchant up front; its chargeback note still allows chargebacks when the merchant does not follow Klarna scheme rules. Do not read approval, capture or settlement from this overview alone.
- Recurring is product- and country-specific in the feature matrix. The note says to contact Adyen Support to offer recurring payments; **Pay over time** is only for long-term subscriptions, not monthly subscriptions or one-off/on-demand tokenized purchases. Billie (B2B) is marked without recurring support.
- The matrix marks refunds, partial refunds and separate captures across the listed rows, but **multiple partial captures require Support enablement**. Klarna authorization adjustment is supported between authorization and capture; the linked adjustment guide owns its detailed eligibility and asynchronous outcome.
- Adding Klarna to a **live** Customer Area account sends a Merchant Portal activation link to the supplied dispute email. That email is the principal login credential and the page says it cannot later be changed. The Orders App can view order information and edit shipping and billing details; other portal apps manage users, branding and on-site messaging, but **disputes cannot be managed there**; use the linked Klarna chargeback process.

> [!warning] Contradiction
> This overview’s Billie (B2B) row lists Redirect only (raw line 36), while [[source-adyen-docs-payment-methods-klarna-billie|the Billie guide]] lists Redirect and Inline widget and describes the widget path (raw lines 27–29 and 815–843). The overview row is not a complete inventory of the child guide’s checkout paths; neither page proves current eligibility or a completed payment.

## Detail locators

- Product choices, redirect flow, recurring/capture/refund/chargeback feature matrix and three numbered qualifications: pinned raw lines 23–40.
- Authorization adjustment and linked procedural guides: `## Authorization adjustment`, lines 42–47.
- The 22-country/region `countryCode` and `amount.currency` matrix, with separate Pay now/later/over-time cells: `## Supported countries/regions`, lines 49–74. Read the exact row before making a country, currency or product claim.
- Live-account activation, immutable dispute email, portal apps and dispute-management boundary: `## Klarna Merchant Portal` and `## Chargebacks`, lines 76–91.
- Integration route chooser, including Web, iOS, Android, API only and Pay by Link: `## How do you want to integrate?`, lines 93–123. These links do not supply child-guide implementation requirements.

## Related

- [[adyen-online-payments]] — provider online-payment context.
- [[source-adyen-docs-online-payments-adjust-authorisation-adjust-with-preauth]] — detailed Klarna adjustment conditions and outcome.
- [[source-adyen-docs-risk-management-chargeback-guidelines-klarna-chargebacks]] — chargeback process and dated dispute changes.

## Raw Sources

- [[raw/adyen/docs/payment-methods/klarna/2026-09-15|2026-09-15 Klarna overview, feature and country matrices, portal and integration routes]]
