---
title: "iDEAL | Wero (Stripe)"
type: concept
category: technology
tags: [stripe, ideal, wero, netherlands, eur, bank-redirect, authenticated, sepa-debit]
---

## Definition

iDEAL | Wero (formerly iDEAL, now rebranding) is the Netherlands' dominant online payment method, operated by Currence (all major Dutch banks). API enum: `ideal`. Customer-initiated 2FA bank redirect, immediate notification.

**Currency**: EUR only. **Customers**: Netherlands only. **Business**: 40 countries.

> **Migration in progress**: Wero acquired iDEAL. Rebrand to "iDEAL | Wero" by Q1 2026; fully switch to Wero API in 2026–2027. See also [[stripe-wero]] — Wero as a standalone German payment method (separate from iDEAL|Wero).

## Key Properties

- **Confirmation**: Customer-initiated, immediate notification
- **Recurring**: Via [[stripe-sepa-debit]]. In the 2026-05-13 subscription guide, hosted Checkout uses iDEAL for the first subscription payment (or a refunded 0.01 EUR collection for a free trial); Direct API uses a refunded 0.01 EUR setup payment and a successful SetupIntent to obtain a generated SEPA Direct Debit payment method. Later SEPA payment success is separate.
- **Disputes**: No — customers can't dispute with bank; contact merchant directly
- **Refunds**: 180 days; up to 7 days pending; after 7 days without failure → considered successful
- **Full product support**: Connect, Checkout, Payment Links, Subscriptions, Invoicing, Elements

## Compliance Requirements

- **KVK number**: Netherlands-based businesses must display KVK (Chamber of Commerce) registration number on website; non-NL businesses must show equivalent local registration
- **Connect**: Connected account name must match actual business, not platform — required for regulatory compliance and customer trust

## Integration

**Checkout**: `payment_method_types: ['ideal']`, `eur`. Payment/setup/subscription all supported. No minimum charge amount.

**14 supported banks**: abn_amro, asn_bank, bunq, ing, knab, n26, nn, rabobank, revolut, regiobank, sns_bank, triodos_bank, van_lanschot, yoursafe.

**iOS**: `STPPaymentMethodParams(billingDetails:)` (name required) + `STPPaymentHandler.confirmPayment()`.

**Android**: `PaymentMethodCreateParams.create(ideal:, billingDetails:)` + `PaymentLauncher.confirm()`.

**React Native**: `confirmPayment(clientSecret, { paymentMethodType: 'Ideal' })` + deep linking.

## Sources

- [[source-stripe-ideal]] — primary source: properties, migration notice, disputes, refunds, KVK requirement, Connect rules
- [[source-stripe-ideal-accept-payment]] — integration guide: Checkout + iOS + Android + React Native + Elements, 14 banks, no minimum
- [[source-stripe-ideal-save-during-payment]] — save IBAN as SEPA mandate: setup_future_usage + generated_sepa_debit, SEPA mandate text (7 languages), 6 test patterns
- [[source-stripe-ideal-set-up-payment]] — SetupIntent (no payment): 0.01 EUR charged + refunded, confirmSetup, same mandate text and test patterns
- [[source-stripe-subscriptions-ideal]] — 2026-05-13 subscription variants: hosted Checkout first iDEAL charge or refunded trial setup, Direct API refunded 0.01 EUR setup and generated SEPA method; Direct API off_session update guidance and test cases. 2026-11-07 capture is a variant index only.
