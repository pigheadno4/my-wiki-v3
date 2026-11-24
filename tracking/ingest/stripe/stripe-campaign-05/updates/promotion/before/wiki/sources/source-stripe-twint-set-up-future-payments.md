---
title: "Stripe: Set Up Future TWINT Payments"
type: source
date_ingested: 2026-05-03
original_format: webpage
raw_files:
  - "stripe-twint-set-up-future-payments-2025.md"
tags: [stripe, twint, switzerland, chf, recurring, setup-intents, save-payment-method]
---

## Summary

Guide for saving a TWINT payment method for future off-session use via a SetupIntent — no payment upfront. Covers Checkout (setup mode), Elements, and Direct API. Distinct from [[source-stripe-twint-save-during-payment]], which saves the method during an active payment using `setup_future_usage`.

## Key Details

### Checkout path

- `mode: "setup"`, `payment_method_types: ["twint"]`, customer or customer_account ID
- Retrieve the SetupIntent from the `checkout.session.completed` webhook (`setup_intent` key) or via `success_url` (expand `setup_intent` on the session)
- Monitor `setup_intent.succeeded` → store `payment_method` ID

### Elements path

- Create SetupIntent server-side with `payment_method_types: ["twint"]`
- Client-side: `stripe.confirmSetup()` with `return_url`
- Monitor `setup_intent.succeeded` webhook → store `payment_method` ID

### Direct API path

- Client-side: `stripe.confirmTwintSetup(clientSecret, { return_url })` → redirects to TWINT-hosted setup page
- Server-side manual: `confirm: true` + `payment_method_data.type: 'twint'` + `mandate_data.customer_acceptance.online` (ip_address + user_agent) + `return_url`
- SetupIntent status flow: `requires_action` → `succeeded` (authorized) or `requires_payment_method` (declined)

### Off-session charging

- Identical across all three paths: `off_session: true`, `confirm: true`, CHF currency
- `return_url` **not required** when using a previously saved TWINT method (SetupIntent or `setup_future_usage`)

### Testing

- `decline@` email → generic decline (`payment_method_provider_decline`)
- `revoke@` email → mandate revocation (`payment_intent_mandate_revoked`)

### Accounts v2 API

- `customer_account` param supported as alternative to `customer` throughout

## Raw Sources

- [[stripe-twint-set-up-future-payments-2025]] — verbatim webpage content (1199 lines, Checkout + Elements + Direct API)
