---
title: "Adyen payments documentation entry"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/payments"
raw_files:
  - "adyen/docs/payments/2026-09-15.md"
tags: [adyen, payments, online-payments, point-of-sale, omnichannel]
---

## Overview

This 2026-09-15-captured Adyen **Payments** landing page orients readers to online, in-person and omnichannel documentation. It describes Adyen's shared-platform proposition and links to payment methods, risk, tokenization, reporting and Uplift, then to channel-specific guides and a setup checklist. Its “one integration” and “more than 200 payment methods” language is a high-level provider claim, not a specification for a merchant's architecture, eligible methods or deployed configuration. See [[adyen]], [[adyen-online-payments]], [[adyen-payment-terminals]] and [[adyen-unified-commerce]].

## Key takeaways

- **Channel choice:** The page says a business may integrate online, in-person or both. It routes online websites/mobile apps to pre-built UI or API documentation, in-person payments to POS terminals, and connected cross-channel customer/payment-data scenarios to Unified Commerce. It does not define a shared API contract, terminal protocol, customer-identity matching rule or financial flow across these routes.
- **Capability directory:** Payment methods, risk/SCA, tokenization/recurring, transaction/reporting reconciliation and Uplift are linked product areas. Their mechanics, prerequisites, version requirements, pricing, account eligibility, consent/privacy duties and outcomes belong to the respective child pages. This landing page does not establish that all advertised methods or features are enabled for a given merchant or region.
- **Setup route and outcome boundary:** The linked payment-setup checklist is the entry for account preparation, integration and go-live steps; the landing page itself provides no credentials, webhook configuration, checkout action, terminal setup or completed-payment evidence. A broad platform description does not prove authorization, capture, settlement, payout or unified shopper recognition.

## Detail locators

- Lines 15–19: payments landing identity and cross-channel platform proposition.
- Lines 21–27: capability links for methods, risk, tokens, reporting and Uplift.
- `## Payment channels`, lines 29–49: choose online, in-person or both and navigate to channel areas.
- `## Set up payments with Adyen`, lines 51–57: setup-checklist navigation only.

## Related

- [[adyen-online-payments]] — website/mobile checkout route.
- [[adyen-payment-terminals]] — physical POS device route.
- [[adyen-unified-commerce]] — cross-channel customer/payment-data proposition.
- [[adyen-risk-management]] — separate risk feature detail.
- [[adyen-tokenization]] — separate stored-detail and recurring conditions.
- [[adyen-reporting]] — separate reporting and reconciliation detail.

## Raw Sources

- [[raw/adyen/docs/payments/2026-09-15|Adyen Payments landing page, captured 2026-09-15]]
