---
title: "Stripe Terminal: Use Terminal with Connect"
type: source
date_ingested: 2026-04-24
original_format: webpage
raw_files:
  - "stripe-terminal-connect-2025.md"
tags: [stripe, terminal, in-person, connect, direct-charges, destination-charges, separate-charges, platform, connected-accounts]
---

## Stripe Terminal: Use Terminal with Connect

How to integrate Stripe Terminal with Connect platforms across all three charge types.

## Key Takeaways

### Prerequisite

Connected accounts must have the `card_payments` capability to perform Terminal transactions.

### Charge type comparison

| Charge type | API key | Stripe-Account header | Resource ownership |
| --- | --- | --- | --- |
| Direct charges | Platform key | ✓ Set to connected account | Connected account owns locations, readers, PaymentIntents |
| Destination charges | Platform key | ✗ Not set | Platform owns all; uses `on_behalf_of` + `transfer_data[destination]` |
| Separate charges + transfers | Platform key | ✗ Not set | Platform owns all; create transfers after capture |

### Direct charges

- Locations and readers created with `Stripe-Account` header → belong to connected account
- ConnectionToken created with `Stripe-Account` → only usable by that connected account's readers
- PaymentIntent: client-side creation available (iOS/Android/RN); JS SDK requires server-side
- Dashboard: view data by logging in **as the connected account**
- Connected account pays Stripe fees, handles refunds/chargebacks

**Platform-owned readers (private preview)**: Platform owns locations/readers, connected accounts own PaymentIntents. Allows single reader to process payments for multiple connected accounts. Server-driven only. Contact `stripe-terminal-betas@stripe.com`.

### Destination charges

- ConnectionToken: use platform key only (no `Stripe-Account`)
- PaymentIntent parameters:
  - `on_behalf_of` — connected account ID (required when platform country ≠ connected account country; auto-settles in account's country, uses account's fee structure)
  - `transfer_data[destination]` — connected account ID
  - `application_fee_amount` — platform's cut
- JS SDK: server-side PaymentIntent creation only
- Verifone P400: must create PaymentIntent server-side; retrieve via `Terminal.retrievePaymentIntent`
- Dashboard: view data logged into **platform account**

### Separate charges and transfers

- Platform creates charge on its own account (no `on_behalf_of` or `transfer_data`)
- Use `transfer_group` for tracking related payments and transfers
- After capture: create transfers to connected accounts
- **`source_transaction` trick**: tie transfer to specific charge to avoid balance timing issues (transfer executes when charge funds settle)
- Can split one payment across multiple connected accounts with separate transfers
- Dashboard: view data logged into platform account

### ConnectionToken scoping for all types

Use `location` parameter when creating ConnectionToken to restrict which readers can use it. Without a location, all platform readers can use the token.

## Relevant Wiki Pages

- [[stripe]] — Stripe company overview
- [[stripe-terminal]] — Stripe Terminal concept page

## Raw Sources

- [[stripe-terminal-connect-2025]] — verbatim Terminal + Connect guide (all 3 charge types + platform-owned readers preview)
