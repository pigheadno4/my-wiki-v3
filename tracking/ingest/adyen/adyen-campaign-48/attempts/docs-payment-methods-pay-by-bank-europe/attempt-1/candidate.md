---
title: "Adyen Pay by Bank (Europe) overview"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/pay-by-bank-europe"
raw_files:
  - "adyen/docs/payment-methods/pay-by-bank-europe/2026-09-15.md"
tags: [adyen, pay-by-bank-europe, open-banking, bank-transfer, chargebacks, online-payments]
---

## Overview

This captured [[adyen]] overview describes **Pay by Bank (Europe)** as an open-banking, account-to-account redirect method involving Adyen's partner Tink and the shopper's bank. It states onboarding needs approval through an Adyen contact and routes readers to Web, API-only and Pay by Link integrations. Its most consequential qualification is that a successful `AUTHORISATION` webhook means a bank transfer was initiated, while funds may still fail to arrive. [[adyen-online-payments]]

## Key takeaways

- **Onboarding and geography:** The page requires onboarding approval via an Adyen contact. Its prose says the solution is available in **Germany, France and the United Kingdom**, but the capability table lists **FR, DE, GB and FI** with EUR and GBP. This is a captured source conflict about Finland; do not infer current FI availability or pair every listed country/currency from the table (raw lines 21–27, 41–43).
- **Shopper route:** The shopper is redirected to Tink, then to their bank website or mobile app, and finally back to the merchant's website or app. In one path, the shopper chooses a bank at Tink; in the other, issuer selection happens in the merchant payment form before Tink, **supported in the UK only** (raw lines 29–39).
- **Capability table:** The table marks recurring with “See note,” refunds, partial refunds, multiple partial refunds, and chargebacks available, while separate, partial and multiple partial captures are unavailable. The captured page does not give a clear recurring note; treat the mark as high-level overview information, not a tokenization recipe or merchant entitlement (raw lines 41–43).
- **Authorization versus funds:** A successful `AUTHORISATION` webhook indicates issuer/partner verification passed and bank transfer initiation succeeded; it does **not** guarantee funds. The shopper can cancel where a bank permits it, or delayed processing can allow an insufficient-funds failure. Adyen says it may not learn of that failure or whether the bank might later process it. The payment remains `SentForSettle` until funds arrive. If funds have not arrived after **8 weekdays**, the page says status becomes `Settled`, then `Chargeback`, with a `CHARGEBACK` webhook. Such chargebacks cannot be defended; if money arrives later, `CHARGEBACK_REVERSED` follows (raw lines 45–60). These are documented lifecycle statements, not proof of a particular transfer outcome.
- **Integration choices:** Web links to prebuilt UI, API-only to merchant-built UI for website/iOS/Android, and Pay by Link to payment-link acceptance. The overview does not specify endpoint request fields or implement the flow (raw lines 62–80).

## Detail locators

- Identity, onboarding, availability and shopper route: pinned raw lines 15–39.
- Capability table and availability tension: pinned raw lines 41–43.
- Authorization, settlement uncertainty and chargeback lifecycle: pinned raw lines 45–60.
- Web, API-only and Pay by Link routes: pinned raw lines 62–80.

## Related

- [[adyen-online-payments]] — provider online payment architecture and method routes.

## Raw Sources

- [[raw/adyen/docs/payment-methods/pay-by-bank-europe/2026-09-15|Pay by Bank (Europe) overview, captured 2026-09-15]]
