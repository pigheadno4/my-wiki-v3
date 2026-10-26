---
title: "Bizum | Adyen Docs"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bizum"
raw_files:
  - "adyen/docs/payment-methods/bizum/2026-09-15.md"
tags: [adyen, bizum, online-payments, online-banking, spain]
---

## Overview

This 2026-09-15 Adyen webpage snapshot introduces Bizum as a Spain online-banking payment method for online payments: customers pay directly from a bank account without a credit or debit card. It is a redirect method in the page's ES/EUR capability table. This overview routes to Web pre-built UI and API-only guides; it does not establish a merchant's current enablement or completed payment behavior. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- Activation starts with a contract with a locally supported acquiring bank, obtaining a MID (also called FUC) and Terminal ID, and telling the acquirer Adyen will process the payments so the MID can be connected to Adyen as gateway. The page gives Adyen's e-commerce/Bizum IPSP number as `31710` (raw lines 29–42).
- In the snapshot's capability table, Bizum is marked for refunds, partial refunds, and multiple partial refunds; recurring payments, separate/partial/multiple partial captures, and chargebacks are marked unavailable (raw lines 25–27). These are dated documentation marks, not proof of present account-level eligibility.
- The Web route offers pre-built UI for websites; the API-only route describes a custom UI for a website, iOS app, or Android app (raw lines 44–56). Follow the child guides for integration steps and payment outcomes.

## Detail locators

- Definition and ES/EUR redirect capability matrix: raw lines 15–27.
- Acquirer contract, MID/FUC, Terminal ID, gateway connection and IPSP number: raw lines 29–42.
- Web and API-only integration chooser: raw lines 44–56.
- General related topics: raw lines 58–63.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Related raw API references

- [[raw/adyen/docs/payment-methods/bizum/web/2026-09-15|Bizum Web chooser]]
- [[raw/adyen/docs/payment-methods/bizum/web-drop-in/2026-09-15|Bizum Web Drop-in guide]]
- [[raw/adyen/docs/payment-methods/bizum/web-component/2026-09-15|Bizum Web Component guide]]
- [[raw/adyen/docs/payment-methods/bizum/api-only/2026-09-15|Bizum API-only guide]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/bizum/2026-09-15|Bizum overview, 2026-09-15 snapshot]]
