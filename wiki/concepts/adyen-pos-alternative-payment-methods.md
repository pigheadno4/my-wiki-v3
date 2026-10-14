---
title: "Adyen POS alternative payment methods"
type: concept
category: technology
tags: [adyen, point-of-sale, alternative-payment-methods, in-person-payments]
---

## Definition

Adyen's 2026-09-15 point-of-sale alternative-payment-methods overview groups three in-person terminal routes: stored-value gift cards, one-time numeric codes generated through a bank or payment app and entered on a terminal, and QR code wallet payments using a phone app and terminal QR communication. It separately links to Brazil meal or food vouchers. These routes concern in-person payments; online checkout actions and payment messaging have separate integration contexts.

## Evidence boundary

The overview names routes and gives short descriptions. It does not establish current method, scheme, wallet, or provider availability; account or shopper eligibility; integration requirements; or payment success. Gift-card loading, cash-out, and disabling depend on provider. Follow method-specific guides for implementation details and current account checks.

## Sources

- [[source-adyen-docs-point-of-sale-alternative-payment-methods-otc-digit-based-payments]] — 2026-09-15 Adyen Docs guide to Poland-only BLIK terminal code payments, merchant/shopper initiation, account activation and referenced `ReversalRequest` refunds.


- [[source-adyen-docs-point-of-sale-alternative-payment-methods-qr-code-wallets]] — 2026-09-15 captured POS QR wallet guide for terminal-menu, POS-specified, and shopper-scanned flows, wallet-specific scanner exclusions, and referenced refunds.


- [[source-adyen-docs-point-of-sale-alternative-payment-methods-brazil-vouchers]] — 2026-09-15 Adyen Docs guide to Brazilian PAT meal/food voucher payment flows, Terminal API field, software/activation gates, testing limit, and merchant eligibility.


- [[source-adyen-docs-point-of-sale-alternative-payment-methods-gift-cards-terminal-api-payment]] — 2026-09-15 captured Terminal API POS gift-card payment guide for balance-first versus partial-authorization flows; detailed lifecycle belongs to [[adyen-pos-gift-cards]].


- [[source-adyen-docs-point-of-sale-alternative-payment-methods]] — 2026-09-15 POS overview and child-guide routes.
