---
title: "Stripe: Apple Pay Best Practices"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/apple-pay/best-practices"
raw_files:
  - "stripe-apple-pay-best-practices-2026-11-07.md"
  - "stripe-apple-pay-best-practices-2025.md"
tags: [stripe, wallets, apple-pay, best-practices, certificate-renewal, conversion, express-checkout, merchant-tokens]
---

## Overview

Stripe's Apple Pay best-practices guide covers express checkout placement, moving registration until after purchase, default payment selection, Apple Pay setup prompts, certificate renewal, testing changes, and merchant tokens for recurring transactions. The 2026-05-07 and 2026-11-07 captures have the same substantive advice; their captured content diff adds only whitespace before **Activate** in the certificate paragraph. These captures describe recommendations and reported case studies, not a measured outcome or certificate state for another merchant.

## Key takeaways

- **Express checkout:** For Apple Pay-ready customers, Stripe suggests placing the button on product detail, list, or search pages. Collect required order selections first; if the user taps before selection is complete, highlight what is missing rather than leaving the button disabled. Stripe reports that Indiegogo saw a **250% increase in conversion rate** after implementing an express checkout. This is Indiegogo's reported result, not a forecast for other merchants (November lines 15–24).
- **Registration and default selection:** The guide suggests removing mandatory pre-purchase sign-up for Apple Pay-ready users, asking only for transaction-relevant information, and requesting account details after payment. It suggests defaulting to Apple Pay on capable devices or preselecting it in the payment selector. In Wish's A/B test of **new users who were Apple Pay-ready**, defaulting to Apple Pay yielded a **“2X higher conversion rate increase”**. This is a claim about that test's conversion-rate *increase*; it does not establish that Wish's overall conversion rate doubled or that another merchant will see the same lift (November lines 26–43).
- **Setup and communication:** For a capable device without a Wallet card, the guide suggests a **Set Up Apple Pay** prompt during checkout, in account payment settings, or in payment-update messages. It also suggests showing Apple Pay acceptance in checkout and other customer communications (November lines 45–65).
- **Certificate renewal:** The captured guide says the certificate lasts **25 months** from activation, with notifications to the Apple Developer Account team agent at **30, 15, and 7 days** before expiration. Obtain a **new CSR from Stripe**, upload the new certificate to Stripe **before** activating it in the Apple Developer portal, and keep both old and new certificates in the Stripe Dashboard during transition. Apple starts using the new public key approximately five minutes after activation. The guide says no app update is needed after replacement and recommends a transaction with test API keys. This is a procedure, not evidence that a particular merchant's certificate was renewed or tested (November lines 67–75).
- **Changes and recurring payments:** Before changing the integration or Apple Merchant ID, verify token creation and payment completion. For recurring, deferred, or automatic-reload merchant-initiated transactions, Stripe recommends configuring Apple Pay to return a merchant token (MPAN). The recommendation does not establish merchant-specific availability or successful authorization (November lines 77–83).

## Related

- [[stripe-wallets]] — Apple Pay and other wallet context.
- [[stripe]] — Stripe provider.

## Raw Sources

- [[raw/stripe-apple-pay-best-practices-2026-11-07|Stripe Apple Pay best practices, 2026-11-07]] — same substantive advice in the later capture.
- [[raw/stripe-apple-pay-best-practices-2025|Stripe Apple Pay best practices, 2026-05-07]] — earlier capture.
