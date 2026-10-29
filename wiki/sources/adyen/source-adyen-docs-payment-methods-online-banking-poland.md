---
title: "Online banking Poland payment method overview"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-poland"
raw_files:
  - "adyen/docs/payment-methods/online-banking-poland/2026-09-15.md"
tags: [adyen, online-banking-poland, poland, redirect, pln]
---

## Overview

This 2026-09-15-captured Adyen method overview describes **Online banking Poland through partner Przelewy24 (P24)**, a bank-selection and redirect flow. It gives a PL/PLN capability matrix and integration routes. It is a dated documentation snapshot, not evidence of current merchant entitlement, market ranking, or completed payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The page calls online banking “one of the most popular” payment methods in Poland and identifies **Przelewy24 (P24)** as Adyen's partner for this offering. The popularity statement is a dated source assertion, not a measured current market claim (raw line 23).
- The shopper sees a list of issuing banks, selects one, then is redirected to the bank's website or mobile app to complete payment (raw line 25). Redirect initiation is not itself payment completion.
- The matrix identifies **Online Banking / redirect / PL / PLN**. It marks **recurring**, **separate captures**, **partial captures**, **multiple partial captures**, and **chargebacks** unavailable, while marking **refunds**, **partial refunds**, and **multiple partial refunds** available (raw lines 27–29). Those marks do not imply that every ordinary capture operation is unavailable or prove a specific merchant account's current configuration.
- The chooser links pre-built UI paths for **Web, iOS, Android, React Native, and Flutter**, an **API-only** own-UI path for website/iOS/Android, and **Pay by Link** (raw lines 31–73). These are navigation routes, not implementation facts from unread child guides. The generic See also links to 3D Secure and Capture do not establish Poland-specific support (raw lines 75–80).

## Detail locators

- Partner, popularity statement and shopper redirect: raw `# Online banking Poland`, lines 23–25.
- PL/PLN flow and capability matrix: raw lines 27–29.
- Platform, API-only and Pay by Link routes: raw `## How do you want to integrate?`, lines 31–73.
- Generic See also links: raw lines 75–80.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-poland/2026-09-15|Online banking Poland overview, captured 2026-09-15]]
