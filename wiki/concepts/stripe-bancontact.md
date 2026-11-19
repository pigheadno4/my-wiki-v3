---
title: "Bancontact (Stripe)"
type: concept
category: technology
tags: [stripe, bancontact, belgium, eur, bank-redirect, sepa-debit]
---

## Definition

Bancontact is Belgium's dominant online payment method. Customers pay using a Bancontact card or mobile app linked to their Belgian bank account. API enum: `bancontact`. Customer-authenticated, immediate notification, redirect-based.

**Currency**: EUR only. **Customers**: Belgium only. **Business**: 40 countries.

## Key Properties

- **Confirmation**: Customer-authenticated (immediate — not delayed notification)
- **Disputes**: No chargebacks. Customer must authenticate with their bank, which prevents fraudulent disputes.
- **Recurring and setup boundary**: Native Bancontact is single-use; future recurring use can involve a generated [[stripe-sepa-debit]] payment method. The May 3 bank-redirects API matrix marked Bancontact SetupIntents and future usage supported. Its November 7 matrix marks SetupIntents unsupported but future usage supported through a generated SEPA Direct Debit footnote, while the same-date Bancontact method overview marks both SetupIntents and PaymentIntents with setup_future_usage unsupported. Preserve the unresolved route-specific conflict; none of these cells proves a particular account can complete a mandate. The separate May [[source-stripe-bancontact-set-up-payment|setup]] and [[source-stripe-bancontact-save-during-payment|save-during-payment]] guides document those generated-SEPA paths; the captures do not resolve their current support.
- **Refunds**: The 2026-11-07 overview allows full or partial refund submission within 730 days/two years; the 2026-05-03 overview said 180 days. Submission is not completion: check the Refund status or final events. See [[source-stripe-bancontact]].
- **Invoicing**: The May overview called it invite-only; the November matrix lists Invoicing with `send_invoice` collection only and does not resolve account-specific eligibility. Express Checkout Element is unsupported.

## Payment Flows

**Web/card flow**: checkout → redirect to Bancontact site → enter credentials → immediate confirmation → optional return to merchant site.

**Mobile app flow**: checkout → QR code displayed → scan with Bancontact app → enter PIN → immediate confirmation → optional return to merchant site.

## Integration

**Checkout**: `payment_method_types: ['bancontact']`, `eur`. No special test numbers.

**Direct API**: `stripe.confirmBancontactPayment(clientSecret, { payment_method: { billing_details: { name } }, return_url })`. Optional `preferred_language: 'fr'|'nl'|'de'` (default `'en'`). Bank account details (BIC, IBAN last 4) on charge after completion.

**iOS**: `STPPaymentMethodBancontactParams` + name in billing details + `STPPaymentHandler.confirmPayment()`.

**Android**: `PaymentMethodCreateParams.createBancontact(billingDetails)` + `PaymentLauncher.confirm()`.

## Sources

- [[source-stripe-bancontact]] — Bancontact overviews (2026-05-03 and 2026-11-07): single-use Belgian EUR redirect, eligibility, payment/refund boundaries, product support and dated setup conflict
- [[source-stripe-bank-redirects]] — May 3 and November 7, 2026 matrices; Bancontact SetupIntent and generated-SEPA future-use conflict with same-date method page
- [[source-stripe-bancontact-accept-payment]] — 2026-05-03 Bancontact acceptance guide for Checkout, Direct API, iOS, Android, and React Native, including preferred language and a Charge details example; web uses `confirmBancontactPayment`, React Native uses `confirmPayment`, and a redirect return requires PaymentIntent status verification. The 2026-11-07 canonical capture is a variant index only.
- [[source-stripe-bancontact-save-during-payment]] — save IBAN as SEPA mandate: setup_future_usage + generated_sepa_debit, SEPA mandate text (7 languages), 6 test email/token patterns
- [[source-stripe-bancontact-set-up-payment]] — SetupIntent path (no payment): confirmBancontactSetup, Stripe charges/refunds 0.02 EUR, generated_sepa_debit
