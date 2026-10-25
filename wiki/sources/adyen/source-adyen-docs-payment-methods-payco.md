---
title: "PayCo"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/payco"
raw_files:
  - "adyen/docs/payment-methods/payco/2026-09-15.md"
tags: [adyen, payco, kcp, korea, wallet, online-payments]
---

## Overview

This 2026-09-15 PayCo overview describes a South Korean online payment method provided via Korea Cyber Payment (KCP). It says PayCo is linked to the shopper's credit card, while its historical capability table classifies the Adyen route as a KR/KRW redirect wallet. It routes to platform-specific integration guides; it does not show a live merchant entitlement or payment result. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Provider and payment path:** the source attributes PayCo provision to KCP and says the shopper's PayCo is directly linked to a credit card. Its table labels the payment type `Wallets`, flow `redirect`, country `KR` and currency `KRW`. The card-link statement does not by itself convert this source into a direct card-entry/3DS integration guide. (raw lines 23–29)
- **Historical capability marks:** the row check-marks refunds, partial refunds and multiple partial refunds. It x-marks recurring, separate capture, partial capture, multiple partial capture and chargebacks. These are the page's capability marks, not current account eligibility or evidence that any refund or capture occurred. (raw lines 27–29)
- **Integration routes:** the overview links Web, iOS and Android pre-built UI paths plus an API-only path for merchant-built UI on website or iOS/Android. It provides no endpoint, SDK/API minimum, redirect return procedure, TEST/LIVE gate or asynchronous outcome sequence. (raw lines 31–55)
- **Further navigation:** the See also list links Online payments, 3D Secure, Capture and Payment methods. Those links do not establish PayCo-specific 3DS or capture behavior beyond the table's own marks. (raw lines 57–62)

## Detail locators

- KCP provider, credit-card link and KR/KRW redirect-wallet table: raw lines 23–29.
- Refund and recurring/capture/chargeback marks: raw lines 27–29.
- Web, iOS, Android and API-only child guide routes: raw lines 31–55.
- General See also links: raw lines 57–62.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/payco/2026-09-15|Adyen PayCo overview, 2026-09-15 snapshot]]
