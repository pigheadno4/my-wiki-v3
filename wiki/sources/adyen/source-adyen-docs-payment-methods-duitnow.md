---
title: "Adyen DuitNow payment-method overview"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/duitnow"
raw_files:
  - "adyen/docs/payment-methods/duitnow/2026-09-15.md"
tags: [adyen, duitnow, malaysia, qr, real-time-payments]
---

## Overview

This Adyen DuitNow overview was captured on 2026-09-15 and carries 2025-01-28 last-modified metadata. It describes DuitNow as a Malaysian real-time payments network managed by PayNet, then narrows Adyen's offering to QR-code payments. It gives MY/MYR capability marks and routes to Web, iOS and Android child guides. The overview and those marks do not establish present merchant eligibility, pricing, settlement terms or an executed payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The page describes network-level transfers among online banks and digital wallets using a mobile number, national ID or business registration number. That background should not be treated as an Adyen alias-transfer integration: the page explicitly says Adyen only offers DuitNow integration for QR-code payments.
- Its table characterizes Adyen's DuitNow row as real-time payments with an additional-action flow, MY country and MYR currency. It marks recurring, separate capture, partial capture, multiple partial capture and chargebacks unsupported, while refunds, partial refunds and multiple partial refunds are marked supported. These are overview capability marks, not a merchant-account enablement, runtime outcome or refund-success guarantee. Use the linked refund/capture guidance and child guides for conditions and flow detail.
- Web, iOS and Android routes are described as prebuilt-UI options. This overview does not specify their SDK/API versions, request fields, QR lifetime, return handling or outcome sequence. The adyen.com pricing/settlement link is navigation; no fee or settlement term is given here.

## Detail locators

- Network description versus Adyen QR-only scope: pinned raw lines 19–25.
- Country/currency, additional-action and feature marks: pinned raw lines 27–29.
- Web, iOS and Android child routes: pinned raw lines 31–49; external pricing/settlement route: line 21.

## Related

- [[adyen-online-payments]] — main provider concept and payment-state context

## Raw Sources

- [[raw/adyen/docs/payment-methods/duitnow/2026-09-15|DuitNow overview, 2026-09-15]]
