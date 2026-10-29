---
title: "Adyen Bancontact Mobile overview"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bancontact/bancontact-mobile"
raw_files:
  - "adyen/docs/payment-methods/bancontact/bancontact-mobile/2026-09-15.md"
tags: [adyen, bancontact, mobile, wallet, belgium, redirect, qr]
---

## Overview

This Bancontact Mobile overview, last marked modified 2023-04-11 and captured 2026-09-15, describes a BE/EUR wallet payment completed in the Payconiq by Bancontact app or another supporting bank app. It distinguishes the mobile route from Bancontact card and links Web, iOS, Android, API-only and Pay by Link integration choices. It is a historical method description, not proof of current merchant eligibility, bank-app support or a successful payment. See [[adyen]], [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-bancontact|the broader Bancontact overview]].

## Key takeaways

- The shopper completes the payment in the Payconiq by Bancontact mobile app or another bank app supporting Bancontact Mobile. The source says the shopper is sent directly to the app on a mobile device or reaches it by scanning a QR code on desktop. Bancontact card is a separate acceptance route.
- The captured capability matrix calls Bancontact Mobile a wallet with a 'Redirect or Additional action' flow, Belgium as country and EUR as currency. It marks recurring, refunds and partial refunds supported, and separate captures, partial captures and chargebacks unsupported. The recurring footnote narrows recurring to the Bancontact Wallet Initiated Program (WIP); the matrix alone does not establish any merchant's WIP access or operational refund/recurring configuration.
- The page routes to prebuilt Web, iOS and Android UI integrations; API-only for building a website or app UI; and Pay by Link. It does not provide request fields, SDK versions, action payloads, token consent/setup, test behavior or outcome handling. Use the linked integration-specific guides for those details. The page's 'most popular' market claim is a historical publisher assertion without a dated market study here.

## Detail locators

- Page identity, capture metadata and market statement: pinned raw lines 1–23. Mobile/bank-app, direct-app/desktop-QR and card distinction: lines 25–27. BE/EUR wallet capability matrix and WIP recurring footnote: lines 29–33.
- Web, iOS and Android prebuilt routes: pinned raw lines 35–53. API-only website/app route and Pay by Link route: lines 55–65. These are navigation links, not implementation evidence.

## Related

- [[adyen-online-payments]] — main provider payment integration concept
- [[source-adyen-docs-payment-methods-bancontact]] — broader card/mobile overview

## Raw Sources

- [[raw/adyen/docs/payment-methods/bancontact/bancontact-mobile/2026-09-15|Bancontact Mobile overview, captured 2026-09-15]]
