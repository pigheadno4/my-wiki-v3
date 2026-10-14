---
title: "Mail Order/Telephone Order (MOTO) payments | Adyen Docs"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/unified-commerce/mail-order-telephone-order"
raw_files:
  - "adyen/docs/unified-commerce/mail-order-telephone-order/2026-09-15.md"
tags: [adyen, unified-commerce, moto, card-not-present, remote-payments]
---

## Overview

This Adyen overview defines a Mail Order/Telephone Order (**MOTO**) payment as a **card-not-present** transaction in which a shopper gives card details to the merchant by mail or phone and the merchant processes the payment. It lists takeaway orders taken by phone and travel-agency call-center payments as examples. The page names Customer Area, API request and payment-terminal routes, but leaves each implementation to a child guide. Its fraud and chargeback wording is a dated documentation claim (last modified 2024-12-10; captured 2026-09-15), not proof of current merchant eligibility or a completed payment. [[adyen]] [[adyen-unified-commerce]]

## Key takeaways

- The page says the shopper's provision of card details gives permission to process **a MOTO payment**. Its three-step outline is: shopper supplies details by mail/phone, merchant uses them to make the payment, and merchant informs the shopper of the outcome. This does not itself establish recurring-use consent, tokenization permission, data-retention policy, a specific authorization response, or settlement. See **Mail Order/Telephone Order (MOTO) payments** and **How it works**, pinned raw lines 15–34.
- The overview offers three routes: **Virtual Terminal in Customer Area**, an **API request**, or entering card details on a **payment terminal**. The payment-terminal route remains MOTO/card-not-present despite the physical device. The overview does not specify each route's required roles, request fields, terminal mode, environment, PCI steps, or availability; follow the linked child guide selected for the integration. See pinned raw lines 26 and 42–56.
- Adyen's page describes MOTO as higher-fraud-risk and less secure than shopper-present entry, and says the merchant is liable for all chargebacks and defending a dispute is difficult. This broad warning belongs to the dated MOTO overview; it does not establish the outcome, legal allocation or dispute defensibility of a specific transaction, jurisdiction or contract. See **Risk of fraud**, pinned raw lines 36–40.

## Detail locators

- **Mail Order/Telephone Order (MOTO) payments** (pinned raw lines 15–26) — card-not-present identity, remote card-detail handoff, example use cases and three route names.
- **How it works** (pinned raw lines 28–34) — shopper permission and three-step payment/outcome communication outline.
- **Risk of fraud** (pinned raw lines 36–40) — source's higher-risk, chargeback and dispute statements.
- **Next steps** (pinned raw lines 42–56) — exact Virtual Terminal/Customer Area, API request and POS-terminal guide routes.

## Related

- [[adyen-unified-commerce]] — primary provider route for this cross-channel MOTO overview.
- [[adyen-terminal-api]] — POS message context; this overview does not specify that the terminal route must use Terminal API.

## Raw Sources

- [[raw/adyen/docs/unified-commerce/mail-order-telephone-order/2026-09-15|Adyen MOTO overview, fetched 2026-09-15]]
