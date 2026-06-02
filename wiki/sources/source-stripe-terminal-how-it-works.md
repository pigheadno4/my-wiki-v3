---
title: "Stripe Terminal: How It Works"
type: source
date_ingested: 2026-04-23
original_format: webpage
raw_files:
  - "stripe-terminal-how-it-works-2025.md"
tags: [stripe, terminal, in-person, point-of-sale, card-reader, tap-to-pay, encryption, p2pe, e2ee, connect, sdks, fleet-management]
---

## Stripe Terminal: How It Works

Detailed technical overview of Stripe Terminal's architecture, features, encryption options, and integration scope. Complements the Terminal landing page with deeper coverage of how the SDK, readers, and Stripe API interact.

Source URL: <https://docs.stripe.com/terminal>

## Key Takeaways

### Architecture — four components

Every Terminal deployment consists of:

1. **Your application** — web-based, mobile, or desktop POS
2. **Your backend** — server-side logic communicating with the Stripe API
3. **A Stripe Terminal reader** — pre-certified hardware that encrypts card data
4. **The Stripe Terminal SDK** — bridges the POS app, reader firmware, and Stripe API

The SDK enables in-person payments to be accepted using the same PaymentIntents flow as online payments.

### How readers work

- Readers accept EMV (chip), contactless, and swiped payment details
- Readers encrypt sensitive card data on-device and return a token via the SDK — raw card data never touches your application
- Terminal works **only** with Stripe pre-certified readers and Tap to Pay on iPhone/Android — no third-party reader hardware

### Connection types

Readers connect via:
- **Bluetooth** — mobile readers
- **USB** — Android with mobile readers only
- **Internet** — all readers in network-enabled environments

### Fleet management

- Order pre-certified readers and accessories from the Stripe Dashboard
- Choose shipping destination; as a Connect platform, enable connected accounts to receive readers at their own business location
- Monitor fleet of readers from the Dashboard

### Encryption tiers

| Tier | Description | Cost | Best for |
|---|---|---|---|
| **E2EE** (end-to-end encryption) | Default for all Terminal payments | Included | All businesses |
| **P2PE** (point-to-point encryption) | PCI-audited; adds HSM decryption step before card networks; validated by third party; no additional integration required | Paid (optional) | Healthcare, education, regulated industries |

P2PE simplifies PCI compliance, reduces PCI audit scope and cost. Consult the P2PE Instruction Manual (PIM) if enabled.

### Key features summary

- **Online compatibility** — unified online and in-person payments in one system
- **Flexible SDKs** — JavaScript, iOS, Android, React Native + server-driven API
- **Reader choices** — multiple reader hardware options
- **Connection types** — Bluetooth, USB (Android only), internet
- **Dashboard fleet management** — ordering, shipping, monitoring

### Use cases

- Extend online business to physical locations
- Enable in-person payments for Connect platforms (readers per connected account)
- Capture cards in-person for recurring online billing via Stripe Billing
- Build or integrate a custom POS

### Integration scope (4 steps)

1. Sample integration (quickstart)
2. Design your integration
3. Integrate the SDK (use simulated reader during development)
4. Order a physical reader and test card

## Relevant Wiki Pages

- [[stripe]] — Stripe company overview
- [[stripe-terminal]] — Stripe Terminal concept page

## Raw Sources

- [[stripe-terminal-how-it-works-2025]] — verbatim "Accept in-person payments with Terminal" page
