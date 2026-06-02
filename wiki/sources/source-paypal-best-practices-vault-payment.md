---
title: "Pay with PayPal for Vaulted Payments: Best Practices"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-best-practices-vault-payment.md"
tags: [paypal, vault, best-practices, o2o, mobile, app-switch, frictionless-login, ride-hailing, food-delivery]
---

## Pay with PayPal for Vaulted Payments: Best Practices

Official PayPal guide on best practices for vaulted payment flows — targeting high-frequency, low-AOV, mobile-first O2O (online-to-offline) merchants such as ride-hailing and food delivery.

Source URL: <https://developer.paypal.com/docs/checkout/standard/best-practices/vault/>

Last updated: 2025-09-17

## Key Takeaways

### When to use vaulted vs one-time payments

| Signal | Recommended flow |
| ------ | ---------------- |
| AOV < $40, high frequency, O2O | **Vaulted payments** |
| Customer actively initiates a one-off purchase, no recurring | **One-time payments** |

### Target use cases

Ride-hailing, food delivery, quick-service dining — mobile-first scenarios where the buyer starts on a merchant app and completes payment via the PayPal app. The buyer typically has an existing account with the merchant.

### Onboarding: preselect PayPal for active users

- Use PayPal APIs during onboarding to **detect if the customer already has a valid payment method** in their PayPal wallet
- **Preselect PayPal as default** for identified active users → higher conversion
- Use **latest PayPal marks/logos** for brand trust
- Pass customer contact information when initiating the PayPal flow

### Frictionless login by surface type

| Surface | Recommended approach |
| ------- | -------------------- |
| Native apps | PayPal Native SDK (low-friction login) |
| Hybrid apps (web inside app) | PopUp Bridge SDK (secure web views) |
| Websites | App Switch in PayPal JS SDK (listed as "coming soon") |
| Non-SDK merchants | Manual secure webview — AS-WAS on iOS, CCT on Android |

### App Switch

Core recommendation for mobile: redirect buyers to the PayPal app for streamlined authentication and checkout. Listed as "coming soon" for the JS SDK at time of writing (updated 2025-09-17).

## Notable positioning

This guide is explicitly scoped to **O2O mobile services** — distinctly different audience from the one-time payment guide (retail/ecommerce) and recurring payment guide (SaaS/subscriptions). The vault flow is designed for repeat, low-value transactions where speed and frictionless re-use of a saved method matters most.

## Images

- `raw/assets/paypal-best-practices-vault-onboarding.png` — 3-screen end-to-end vaulted payments flow (shared with overview page)
- `raw/assets/paypal-best-practices-vault-onboarding-preselect.png` — PayPal preselection screen during onboarding
- `raw/assets/paypal-best-practices-vault-frictionless-login.png` — frictionless login options across native, hybrid, and web surfaces

## Raw Sources

- [[paypal-best-practices-vault-payment]] — verbatim webpage content + downloaded images

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-vault]] — PayPal Vault / Payment Method Tokens concept
- [[source-paypal-best-practices-pay-with-paypal]] — parent best practices overview page
- [[source-paypal-checkout-recurring-payment]] — technical integration guide (vault setup token flow)
