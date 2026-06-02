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
- **Recurring**: Not native — requires saving as [[stripe-sepa-debit]] mandate. Bancontact payment can be converted to a SEPA Direct Debit for future recurring charges.
- **Refunds**: Up to 180 days
- **Invoicing**: Invite-only. Express Checkout Element: unsupported.

## Payment Flows

**Web/card flow**: checkout → redirect to Bancontact site → enter credentials → immediate confirmation → optional return to merchant site.

**Mobile app flow**: checkout → QR code displayed → scan with Bancontact app → enter PIN → immediate confirmation → optional return to merchant site.

## Integration

**Checkout**: `payment_method_types: ['bancontact']`, `eur`. No special test numbers.

**Direct API**: `stripe.confirmBancontactPayment(clientSecret, { payment_method: { billing_details: { name } }, return_url })`. Optional `preferred_language: 'fr'|'nl'|'de'` (default `'en'`). Bank account details (BIC, IBAN last 4) on charge after completion.

**iOS**: `STPPaymentMethodBancontactParams` + name in billing details + `STPPaymentHandler.confirmPayment()`.

**Android**: `PaymentMethodCreateParams.createBancontact(billingDetails)` + `PaymentLauncher.confirm()`.

## Sources

- [[source-stripe-bancontact]] — primary source: properties, payment flows, disputes, refunds
- [[source-stripe-bancontact-accept-payment]] — integration guide: Checkout + Direct API + iOS + Android + React Native, preferred_language, bank details on charge
- [[source-stripe-bancontact-save-during-payment]] — save IBAN as SEPA mandate: setup_future_usage + generated_sepa_debit, SEPA mandate text (7 languages), 6 test email/token patterns
- [[source-stripe-bancontact-set-up-payment]] — SetupIntent path (no payment): confirmBancontactSetup, Stripe charges/refunds 0.02 EUR, generated_sepa_debit
