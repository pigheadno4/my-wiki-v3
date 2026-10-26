---
title: "Adyen Docs: MobilePay"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/mobilepay"
raw_files:
  - "adyen/docs/payment-methods/mobilepay/2026-09-15.md"
tags: [adyen, mobilepay, wallets, online-payments, payouts]
---

## Overview

This 2026-09-15 Adyen Docs overview describes MobilePay acceptance in online payments and links to channel-specific integration guides. It describes a DK/FI wallet redirect flow in DKK/EUR, with a separate, experimental route for payouts to linked cards. It is a captured guide, not evidence of present merchant enablement or payment execution. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Shoppers need the MobilePay app and at least one linked Visa, Mastercard, or Dankort card. An in-app payment switches to MobilePay for shopper authentication; a website payment first redirects to a MobilePay-hosted phone-number page, then sends a device notification to open the app for authentication. This describes shopper authentication, not a final authorization or settlement result. See raw lines 23–27.
- The overview's dated capability matrix labels MobilePay a redirect wallet for DK/FI and DKK/EUR. It marks recurring with an X, while marking refunds, partial and multiple partial refunds, separate and partial captures, multiple partial captures, and chargebacks with checkmarks. These are overview capability marks, not merchant-specific eligibility or successful lifecycle outcomes. See raw lines 29–31.
- The distinct payout route requires Adyen approval and a balance platform with Transfers API; the deprecated Payout API does not work for this feature. A MobilePay `/payments` request with `enablePayOut: true` creates a payout-only token delivered in a recurring lifecycle webhook. That token cannot be used for recurring or card-on-file payments. See raw lines 33–56.
- Adyen calls MobilePay payouts experimental. The snapshot limits them to Visa/Mastercard cards, requires separate merchant accounts when using both Visa/Mastercard payouts and MobilePay payouts to collect their associated pay-ins, and supports token creation only through `/payments`. After payout completion, MobilePay receives only the balance transfer ID as transaction reference. See raw lines 58–66. The payout-token lifecycle wording does not override the checkout matrix's recurring X.

## Detail locators

- Payout approval, platform, lifecycle webhook names, `enablePayOut`, token use, and `/transfers` counterparty parameter: raw lines 33–56.
- Web, iOS, Android, React Native, Flutter, API-only and Pay by Link navigation: raw lines 68–110. The child guides carry channel-specific implementation details.

## Related

- [[adyen-online-payments]]
- [[adyen-payouts]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/mobilepay/2026-09-15|MobilePay overview, fetched 2026-09-15]]
