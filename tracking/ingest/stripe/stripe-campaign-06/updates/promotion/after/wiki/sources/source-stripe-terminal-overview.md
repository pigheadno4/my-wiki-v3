---
title: "Stripe Terminal Overview"
type: source
date_ingested: 2026-04-23
date_updated: 2026-11-24
original_format: webpage
canonical_url: "https://docs.stripe.com/terminal"
raw_files:
  - "stripe-terminal-2026-11-07.md"
  - "stripe-terminal-overview-2025.md"
tags: [stripe, terminal, in-person, point-of-sale, card-reader, tap-to-pay, offline-payments, connect, sdks]
---

## Stripe Terminal Overview

Stripe’s product landing page describes accepting in-person payments, managing them with online payments in the same Dashboard, and integrating with Stripe Connect. The captures are dated April 23, 2026 at <https://stripe.com/docs/terminal> and November 7, 2026 at <https://docs.stripe.com/terminal>. They give capability descriptions and links to integration guides.

## Key Takeaways

### Integration options

April lists five paths. November retains those and adds Stripe’s own no-code **Preview** route.

| Path | Description | Code required |
| --- | --- | --- |
| **Custom POS** | Build a POS with an Android, iOS, JavaScript or React Native SDK, or use the server-driven Stripe API | Yes |
| **Tap to Pay** | Accept contactless payments on a compatible iPhone or Android device using the Terminal SDK | Yes (SDK) |
| **Apps on Devices** | Deploy an Android POS app to a Stripe smart reader | Yes |
| **Terminal without coding (November Preview)** | Run standalone mode on a compatible reader or use the Stripe Terminal app on a supported iPhone or Android device | No code |
| **Third-party POS** | Integrate Terminal into an existing third-party POS, hardware and commerce setup | No code |
| **Gateway** | Use a gateway-supported POS with third-party hardware and commerce integrations | No code |

The separate November ready-made guide calls standalone mode **public preview** and the mobile Terminal app **private preview**. Both require internet. See [[raw/stripe-terminal-payments-ready-made-apps-2026-11-07|November ready-made apps guide]], lines 9–18, for that scope.

### In-person fundamentals

- **Save cards at POS** — save for subscriptions, attach to a customer’s online account, or defer payment
- **Cancel or refund payments** — authorization and capture, cancellation and refund flows
- **Display cart details** — update a smart reader’s screen with line items and total
- **Send receipts** — prebuilt or custom receipts that meet card-network and local requirements

### SDK and features

Both captures route to Terminal JavaScript SDK v1 for browser POS and to the iOS, Android and React Native SDK references. They describe the server-driven Stripe API as another choice for custom integrations.

The landing pages point to reader choices, tip adjustments, multiple payment methods, Connect and offline payments. The separate [[source-stripe-terminal-offline-payments]] route describes the conditions for offline integrations.

## Relevant Wiki Pages

- [[stripe]] — Stripe company overview
- [[stripe-terminal]] — Stripe Terminal concept
- [[stripe-inapp-payments]] — related mobile SDK payment integrations
- [[source-stripe-terminal-select-reader]] — reader and integration selection
- [[source-stripe-terminal-connect]] — Terminal for Connect platforms

## Raw Sources

- [[raw/stripe-terminal-2026-11-07|November 7, 2026 Terminal landing page]]
- [[stripe-terminal-overview-2025]] — April 23, 2026 verbatim Terminal landing page
