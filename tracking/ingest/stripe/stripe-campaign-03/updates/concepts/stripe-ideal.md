---
title: "iDEAL | Wero (Stripe)"
type: concept
category: technology
tags: [stripe, ideal, wero, netherlands, eur, bank-redirect, authenticated, sepa-debit]
---

## Definition

iDEAL | Wero (formerly iDEAL, now rebranding) is the Netherlands' dominant online payment method, operated by Currence (all major Dutch banks). API enum: `ideal`. Customer-initiated 2FA bank redirect, immediate notification.

**Currency**: EUR only. **Customers**: Netherlands only. **Business**: 40 countries.

> **Capture-dated migration notice**: The May 3 and November 7, 2026 iDEAL overviews both say Wero acquired iDEAL, instruct rebranding to "iDEAL | Wero" in Q1 2026, and direct a switch to Wero during 2026–2027. Q1 was already past by the November capture; these pages do not establish completion for a merchant or a specific API replacement. See [[source-stripe-ideal]] and [[stripe-wero]] for the separate Wero route.

## Key Properties

- **Confirmation**: Customer-initiated, immediate notification
- **Recurring**: Via [[stripe-sepa-debit]]. In the 2026-05-13 subscription guide, hosted Checkout uses iDEAL for the first subscription payment (or a refunded 0.01 EUR collection for a free trial); Direct API uses a refunded 0.01 EUR setup payment and a successful SetupIntent to obtain a generated SEPA Direct Debit payment method. Later SEPA payment success is separate.
- **Disputes**: No — customers can't dispute with bank; contact merchant directly
- **Refunds**: 180 days; up to 7 days pending; after 7 days without failure → considered successful
- **Manual capture**: No (both May 3 and November 7 overviews).
- **Full product support**: Connect, Checkout, Payment Links, Subscriptions, Invoicing, Elements

## Compliance Requirements

- **KVK number**: Netherlands-based businesses must display KVK (Chamber of Commerce) registration number on website; non-NL businesses must show equivalent local registration
- **Connect**: Connected account name must match actual business, not platform — required for regulatory compliance and customer trust
- **Business categories (November 7, 2026 capture)**: [[source-stripe-ideal]] adds a list described collectively as **prohibited or restricted** for iDEAL | Wero, including adult content, cannabis except CBD, NFTs, submerchant payment facilitators, P2P transfers, CFDs, weapons, donation crowdfunding, creator/live-streaming, open-loop gaming, and precious metals/minerals. It does not assign a separate prohibition grade to each category or establish a merchant's eligibility.

## Integration

**Checkout**: `payment_method_types: ['ideal']`, `eur`. Payment/setup/subscription all supported. No minimum charge amount.

**14 supported banks**: abn_amro, asn_bank, bunq, ing, knab, n26, nn, rabobank, revolut, regiobank, sns_bank, triodos_bank, van_lanschot, yoursafe.

**iOS**: `STPPaymentMethodParams(billingDetails:)` (name required) + `STPPaymentHandler.confirmPayment()`.

**Android**: `PaymentMethodCreateParams.create(ideal:, billingDetails:)` + `PaymentLauncher.confirm()`.

**React Native**: `confirmPayment(clientSecret, { paymentMethodType: 'Ideal' })` + deep linking.

## Sources

- [[source-stripe-ideal]] — May/November 2026 overviews: properties, dated Wero migration notice, Dashboard enablement, no manual capture, disputes, refunds, KVK/Connect rules, and November prohibited-or-restricted categories
- [[source-stripe-ideal-accept-payment]] — integration guide: Checkout + iOS + Android + React Native + Elements, 14 banks, no minimum
- [[source-stripe-ideal-save-during-payment]] — 2026-05-03 full guide for iDEAL-to-SEPA saving: off-session future usage, generated SEPA method, mobile mandate text and test patterns; 2026-11-07 capture is a variant navigation index only.
- [[source-stripe-ideal-set-up-payment]] — 2026-05-03 SetupIntent guide: an authenticated 0.01 EUR iDEAL setup payment is refunded, yielding a SEPA Direct Debit method for a separate later charge; explicit merchant mandate-text instructions are in its mobile variants. The 2026-11-07 canonical capture is a variant index only.
- [[source-stripe-subscriptions-ideal]] — 2026-05-13 subscription variants: hosted Checkout first iDEAL charge or refunded trial setup, Direct API refunded 0.01 EUR setup and generated SEPA method; Direct API off_session update guidance and test cases. 2026-11-07 capture is a variant index only.
