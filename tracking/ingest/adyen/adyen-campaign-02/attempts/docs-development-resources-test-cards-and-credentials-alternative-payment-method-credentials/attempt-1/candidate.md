---
title: "Alternative payment methods test credentials | Adyen Docs"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/test-cards-and-credentials/alternative-payment-method-credentials"
raw_files:
  - "adyen/docs/development-resources/test-cards-and-credentials/alternative-payment-method-credentials/2026-09-15.md"
tags: [adyen, testing, alternative-payment-methods, credentials, online-payments]
---

## Overview

This Adyen documentation page supplies method-specific credentials, values, and simulator routes for testing an existing online-payments integration. It covers bank methods, wallets, local payment methods, gift cards, and vouchers; the instructions differ by method and by test versus live environment.

## Key takeaways

- BLIK lists TEST-environment codes and amount-triggered One-Click and refusal scenarios. Doku routes Indonesian bank-transfer and convenience-store completion through method-specific simulators; for Alfamart, the separate Commit step is the route to an expected successful `AUTHORISATION` webhook after simulated payment.
- Google Pay documents a wallet enrolled in Google's test card suite and a route without that suite. In the latter route, real cards uploaded to the wallet map to Adyen test cards of the same brand and are not charged; that route limits 3D Secure 2 challenge testing to American Express or Discover. DPAN test-suite scenarios are limited to native Android and Chrome on Android.
- The page warns that the iDEAL | Wero test environment is unreliable. It recommends live penny tests to verify the integration; live acceptance first requires adding iDEAL | Wero in the live Customer Area. TEST-account simulations are conditional on the test environment being available.
- MobilePay payments cannot be tested in the test environment; its payment check uses low-amount live payments after the method is added in the live Customer Area, with server-side `AUTHORISATION` webhook and live payment-list status checks. Separately, MobilePay wallet payouts are experimental and supported only with `/payments`; that test flow uses the Vipps MobilePay test app, a recurring lifecycle webhook, and a Transfers API request with the received token.
- Vipps has a test-app flow after adding it to the test merchant account and a separate live-request and low-amount payment flow. Other method-specific conditions include Interac's 1.00 CAD test amount and Trustly's recommendation to supply `countryCode` to avoid IP-estimated unsupported-region errors. These are scoped test instructions, not evidence of live eligibility or successful production payments.

## Detail locators

- `## Requirements`; `## ACH` through `## Cash Ticket` — existing-integration scope, credentials and fixtures for ACH, Alipay, Apple Pay, BACS, BillDesk, BLIK, Boku, Boleto, Brazil vouchers and Cash Ticket.
- `## Doku` and its method headings — simulator URLs and method-specific Inquiry, Payment and, for Alfamart, Commit steps; check each method's `action.reference`, amount format and webhook expectations in the raw.
- `## EPS` through `## Google Pay` — EPS issuer, gift-card fixtures, and the two Google Pay test-wallet routes and limitations.
- `## iDEAL` through `## MobilePay` — iDEAL | Wero availability and live-penny route, Interac/Klarna checks, MobilePay live payment checks and experimental payout test.
- `## Oney 3x 4x` through `## Pay by Bank (Europe)` — country-specific Oney credentials/outcome triggers and regional Tink test issuer or login fixtures.
- `## PayPal` through `## Vipps` — PayPal sandbox email, PaySafeCard and SEPA fixtures, Trustly country-code caveat, and Vipps test versus live procedures.

## Related

- Company: [[adyen]]
- Concept: [[adyen-payment-testing]]
- Related testing guide: [[source-adyen-docs-development-resources-testing-payments-and-modifications]]

## Raw Sources

- [[raw/adyen/docs/development-resources/test-cards-and-credentials/alternative-payment-method-credentials/2026-09-15|2026-09-15 snapshot — alternative payment methods test credentials]]
