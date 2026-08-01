---
title: "Recurring Payments"
type: concept
category: technology
tags: [recurring-payments, subscriptions, stored-credentials, billing-cycles, dunning, merchant-initiated]
---

## Definition

Recurring payments are **merchant-initiated charges** made on a schedule or based on usage, without requiring buyer interaction at the time of each charge. Common models: subscriptions, automatic bill payments, usage-based billing, and installments.

## Core Mechanics

All recurring payment systems share the same 3-step pattern:

1. **Buyer consent** — buyer agrees to future charges during an initial checkout (explicit authorization)
2. **Credential storage** — merchant stores a token representing the buyer's payment method (never the raw card)
3. **Merchant-initiated charge** — merchant triggers future charges using the stored token, without buyer present

The stored credential must be declared to card networks using standardized fields (see Stored Credentials below) so that authentication and liability rules apply correctly.

## Recurring Payment Models

| Model | Amount | Frequency | Examples |
| --- | --- | --- | --- |
| Fixed subscription | Fixed | Regular | Netflix, SaaS monthly |
| Usage-based | Variable | Regular | Utilities, metered API |
| Unscheduled | Fixed/variable | Irregular | Top-up when balance low |
| Installment | Fixed | Defined schedule | BNPL, financing |

## Stored Credentials Standard

Card networks (Visa, Mastercard) require merchants to flag merchant-initiated transactions (MITs) with stored credential metadata. Key fields across platforms:

- **payment_initiator**: MERCHANT (vs CUSTOMER for buyer-present)
- **usage**: SUBSEQUENT (vs FIRST for initial consent)
- **charge_type / usage_pattern**: nature of the recurring charge (subscription, unscheduled, installment)

Failure to include these fields correctly can result in higher decline rates, wrong liability assignment, or SCA challenges on MIT charges.

## Dunning & Retry Logic

Failed recurring charges require dunning — a retry sequence to recover the payment:

- **Smart retry**: use card network decline codes to decide when/whether to retry (e.g. `do_not_retry` codes should not be retried)
- **Retry windows**: typically 3–7 days after initial failure, with 2–4 attempts before cancellation
- **Subscriber notification**: email/SMS before retry; critical for reducing involuntary churn
- **Account updater**: automatically fetch updated card details when cards expire or are replaced (Visa/Mastercard network service)

## Key Considerations

- **Buyer consent language**: must clearly disclose recurring charge amount, frequency, and cancellation terms (FTC requirements in US; PSD2 in EU)
- **SCA (Strong Customer Authentication)**: EU regulations require strong auth on first setup; subsequent MITs are exempt if correctly flagged
- **Currency**: most platforms require single currency per billing plan/subscription
- **Cancellation**: must be as easy as sign-up (FTC Click-to-Cancel rule, 2024)
- **Proration**: mid-cycle plan changes require calculating and crediting unused time

## Platform Implementations

| Platform | Approach | Token type |
| --- | --- | --- |
| PayPal | Vault (setup token → payment token) + `usage_pattern` | Payment Method Token |
| Stripe | Setup Intents → Payment Methods + `setup_future_usage` | Payment Method ID |
| Adyen | Recurring API with `shopperReference` + `recurringDetailReference` | Recurring Detail |
| Braintree iOS PayPal | Vault or checkout-with-vault consent → Braintree nonce/server vault | Braintree payment-method nonce/token |

See platform-specific concept pages for integration details:

- [[paypal-vault]] — PayPal tokenization lifecycle
- [[paypal-subscriptions]] — PayPal Subscriptions API and billing plan structure

## Key Players

- [[paypal]] — Vault + Subscriptions API + Orders API recurring
- [[stripe]] — Billing (subscriptions) + Payment Intents with `setup_future_usage`; SetupIntents API for saving payment methods without charging
- **Adyen** — Recurring API, tokenization

## Platform-Specific Implementation

- **Stripe**: See [[stripe-subscriptions]] for full Subscriptions API, Checkout integration, customer portal, flexible billing mode, and provisioning pattern
- **PayPal**: See [[paypal-subscriptions]] for Subscriptions API + vault-based recurring
- **Braintree iOS**: [[braintree-ios-sdk]] can collect PayPal billing-agreement consent and recurring-plan metadata, but the merchant server still owns token storage and later charges. An Apple Pay recurring request shown by the demo is not, by itself, a recurring-payment engine.

## Open Questions

- How do Stripe's dunning/smart-retry features compare to PayPal's?
- What are typical involuntary churn rates by payment method?

## Sources

- [[source-stripe-recurring-payments-overview]] — Stripe recurring payments guide: 5 use cases, 3 payment types, 6-product comparison table, subscription creation via Dashboard/Payment Links/Checkout/Elements, flexible billing mode
