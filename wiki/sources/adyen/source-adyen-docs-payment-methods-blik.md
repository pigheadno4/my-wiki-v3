---
title: "Adyen BLIK payment-method overview"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/blik"
raw_files:
  - "adyen/docs/payment-methods/blik/2026-09-15.md"
tags: [adyen, blik, poland, online-banking, oneclick]
---

## Overview

This Adyen BLIK overview was captured on 2026-09-15 and carries 2025-02-04 last-modified metadata. It describes a Poland mobile-banking payment method with a six-digit-code and banking-app authorization path, plus BLIK OneClick for a shopper who has saved the merchant as a trusted shop in the issuer app. It gives PL/PLN capability marks and routes to platform-specific integration guides. This dated overview does not prove current merchant eligibility, a configured integration or a completed payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- In the code flow, the shopper uses a six-digit BLIK code in the merchant payment form; the page says the code expires after 120 seconds. BLIK then sends a banking-app push notification, and the shopper must authorize there within 45 seconds. This is shopper confirmation timing, not a guarantee of subsequent authorization, capture or settlement.
- The introduction says OneClick lets a shopper pay without the six-digit code after first saving the merchant as a trusted shop in the issuer app. The section labeled "BLIK OneClick" nevertheless repeats all code-entry steps, then says the shopper can choose to save the shop after a successful payment. Treat that section as conflicting with the introductory no-code/prior-trust description; it does not establish a coherent no-code OneClick payment or enrollment sequence. Saving a trusted shop is not evidence of Adyen recurring/tokenization support.
- The capability table classifies BLIK as Online Banking with an additional-action flow in Poland and PLN. It marks recurring, separate/partial/multiple partial captures and chargebacks unsupported, while refunds, partial refunds and multiple partial refunds are marked supported. These are historical overview marks, not a present merchant-account enablement or refund-success guarantee; follow the linked operational guides for conditions.
- The page routes to Web, API-only, iOS and Android integrations. Its API-only tile says a merchant can build a UI for website, iOS or Android. Pay by Link and in-person payment tiles are also navigation. This overview does not give channel-specific API/SDK versions, request fields, OneClick registration API, callback handling or outcome sequence.

## Detail locators

- BLIK identity, bank-app six-digit code and OneClick prior-trust claim: pinned raw lines 15–23.
- Code flow and expiry/authorization timing: pinned raw lines 25–36.
- OneClick-labeled repeated code flow and post-payment trusted-shop option: pinned raw lines 38–48.
- PL/PLN additional-action and capability marks: pinned raw lines 50–52.
- Web, API-only, iOS, Android, Pay by Link and in-person navigation: pinned raw lines 54–90.

## Related

- [[adyen-online-payments]] — main provider online-payment concept

## Raw Sources

- [[raw/adyen/docs/payment-methods/blik/2026-09-15|BLIK overview, 2026-09-15]]
