---
title: "PromptPay | Adyen Docs"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/promptpay"
raw_files:
  - "adyen/docs/payment-methods/promptpay/2026-09-15.md"
tags: [adyen, promptpay, thailand, online-banking, qr]
---

## Overview

This [[adyen]] method overview, last modified **2022-10-26** and captured **2026-09-15**, describes PromptPay as a Thailand online-banking method developed and regulated by the Bank of Thailand. For Adyen's described integration, the merchant shows a QR code; the shopper scans it or uploads a screenshot with an app from a participating bank. Adyen says it offers PromptPay only through QR-code payments. The page is a method overview and channel chooser, not evidence of current merchant eligibility or a completed payment. See [[adyen-online-payments]].

## Key takeaways

- **Method and scope:** The shopper uses a participating-bank app to pay from the displayed QR code. The page separately explains that interbank users can be identified by proxies such as mobile phone number, national ID, corporate registration number or digital-wallet number; those proxy examples are background to PromptPay, not fields this Adyen page tells a merchant to collect. See raw lines 21–25.
- **Dated capability matrix:** The single row labels the method **Real-time payments**, flow **Additional action**, country **TH**, and currency **THB**. It marks recurring, refunds and partial/multiple partial refunds, separate/partial/multiple partial captures, and chargebacks with x icons. These are the page's historical capability marks, not proof of current product support, account enablement, or any actual transaction outcome. See raw lines 27–29.
- **Integration navigation:** The page links to Web, iOS and Android prebuilt-UI routes. Those child guides must supply their own flow prerequisites, API/SDK versions, QR action/return behavior, TEST/LIVE setup and outcome evidence. This overview does not provide those implementation steps. See raw lines 31–49.

## Detail locators

- Original modification and snapshot provenance: raw lines 1–12.
- QR-only Adyen integration boundary, shopper scan/upload and proxy background: raw lines 21–25.
- TH/THB and historical capability marks: raw lines 27–29; Web/iOS/Android chooser: raw lines 31–49.

## Related

- [[adyen-online-payments]] — main Adyen online method and integration routes.

## Raw Sources

- [[raw/adyen/docs/payment-methods/promptpay/2026-09-15|PromptPay overview, 2026-09-15 snapshot]]
