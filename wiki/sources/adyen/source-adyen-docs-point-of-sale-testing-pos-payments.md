---
title: "Adyen Docs: Test a point-of-sale integration"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/testing-pos-payments"
raw_files:
  - "adyen/docs/point-of-sale/testing-pos-payments/2026-09-15.md"
tags: [adyen, point-of-sale, payment-testing, terminal-api, test-cards]
---

## Overview

This Adyen Docs webpage describes **test integration** coverage for point-of-sale payments before live operation. It routes happy flow, timeout and connection recovery with transaction-status checks, simulated declines, and cardholder verification methods (CVM). Its physical card, gift-card, and QR-wallet examples are test fixtures and simulated Terminal API outcomes; they do not establish a live payment, merchant eligibility, or full production acceptance. The page separately recommends testing the live integration. See [[adyen-payment-testing]], [[adyen-terminal-api]], and [[adyen]].

## Key takeaways

- **Physical card tests:** a test terminal or Mobile solution uses a test card for dummy payments with no credits or debits to a live bank account. Adyen's multi-application card can vary brand, language, country/region, currency, and CVM and exercise declines; B2 sets are mainly for brand-support testing in Adyen's test environment. Other providers' test cards may be incompatible with Adyen test terminals. Test payment details appear in test Customer Area. [Raw: Testing credit and debit cards]
- **Gift-card simulation:** the page supplies provider-specific dummy numbers and uses the last three digits of `RequestedAmount` to select simulated Terminal API `Result`, `ErrorCondition`, and refusal/message values. The provider's own test environment and physical test cards may require separate credentials and availability; the page also mentions small-amount live tests for other scenarios. [Raw: Testing gift cards; Gift card numbers; Test scenarios]
- **Wallet limits:** NFC wallets such as Apple Pay are described as live-only for testing. QR wallets can use Adyen's simulator or live in-app penny tests. Merchant-initiated and shopper-initiated QR flows have different simulator behavior; amount endings choose additional simulated approved, abandoned/error, or refused outcomes. The page gives a PIX >10 BRL display exception and routes IRIS amount behavior to separate documentation. [Raw: Testing NFC wallets; Testing QR code wallets; Adyen simulator; Test scenarios]
- **Operational scope:** the checklist includes non-happy flows such as timeout and connection problems with transaction-status verification. Simulated success or failure in this POS page is evidence about a test setup and the named fixture, not proof of Checkout API behavior, live authorization, settlement, or method availability. [Raw: introduction and scenario tables]

## Detail locators

- Raw `Testing credit and debit cards` distinguishes Adyen and B2 physical cards, test Customer Area results, and incompatible third-party cards.
- Raw `Testing gift cards` has dummy numbers and a `RequestedAmount` suffix-to-Terminal-API-response table. These numbers are test fixtures.
- Raw `Testing QR code wallets` has distinct merchant- and shopper-initiated simulator flows and a second amount-suffix table. Follow its flow-specific conditions before interpreting an outcome.
- Raw `Testing NFC wallets` states the live-only testing limit. The linked live-integration and individual card guides are navigation targets, not evidence read for this entry.

## Related

- [[adyen-payment-testing]] — provider testing hub
- [[adyen-terminal-api]] — in-person message and response context
- [[adyen]] — company and knowledge-status page

## Raw Sources

- [[raw/adyen/docs/point-of-sale/testing-pos-payments/2026-09-15|POS testing — Adyen Docs snapshot, 2026-09-15]]
