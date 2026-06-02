---
title: "Stripe Terminal Overview"
type: source
date_ingested: 2026-04-23
original_format: webpage
raw_files:
  - "stripe-terminal-overview-2025.md"
tags: [stripe, terminal, in-person, point-of-sale, card-reader, tap-to-pay, offline-payments, connect, sdks]
---

## Stripe Terminal Overview

Overview of Stripe Terminal — Stripe's in-person card payment product that unifies physical card readers with the existing Stripe payments stack.

Source URL: <https://stripe.com/docs/terminal>

## Key Takeaways

### What Terminal is

Stripe Terminal enables businesses to accept in-person card payments using physical card readers. Crucially, it unifies online and in-person payments in a single Dashboard and integrates with Stripe Connect platforms — so a platform merchant can manage all payment types in one place.

### Integration options

Five distinct integration paths depending on business needs:

| Path | Description | Code required |
|---|---|---|
| **Custom POS** | Build fully custom POS using SDKs (Android, iOS, JavaScript, React Native) or the server-driven API | Yes |
| **Tap to Pay** | Accept contactless payments on a compatible iPhone or Android device — no dedicated reader hardware | Yes (SDK) |
| **Apps on devices** | Deploy a custom Android POS app directly to Stripe smart readers | Yes |
| **Third-party POS** | Plug Terminal into existing third-party POS, hardware, and commerce integrations | No code |
| **Gateway** | Combine Stripe payments with gateway-supported POS systems, third-party hardware, gift cards | No code |

### In-person fundamentals

Four core operational capabilities documented:

- **Save cards at POS** — save for subscriptions, attach to online account, or defer payment
- **Cancel or refund payments** — two-step authorization and capture; cancellation and refund flows
- **Display cart details** — dynamically update smart reader screen with line items and totals
- **Send receipts** — prebuilt or custom receipts meeting card network rules and local regulations

### SDK surface

| SDK | Target |
|---|---|
| JavaScript SDK v1 | Web / browser-based POS |
| iOS SDK | Native iOS POS |
| Android SDK | Native Android POS |
| React Native SDK | Cross-platform mobile |

Plus a server-driven API for any backend integration.

### Feature highlights

- **Tip adjustments** — supported during checkout on in-person transactions
- **Multiple payment methods** — debit/credit cards, contactless, mobile wallets
- **Offline payments** — works with intermittent, limited, or no internet connectivity
- **Multi-platform** — server-driven API means any backend can drive Terminal
- **Connect-compatible** — integrates with Stripe Connect for platform use cases

## Relevant Wiki Pages

- [[stripe]] — Stripe company overview
- [[stripe-terminal]] — Stripe Terminal concept page
- [[stripe-inapp-payments]] — Stripe mobile SDK payments (related: iOS/Android)

## Raw Sources

- [[stripe-terminal-overview-2025]] — verbatim Terminal landing page content
