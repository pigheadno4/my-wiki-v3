---
title: "Adyen test cards and credentials hub"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/test-cards-and-credentials"
raw_files:
  - "adyen/docs/development-resources/test-cards-and-credentials/2026-09-15.md"
tags: [adyen, testing, test-cards, test-credentials]
---

## Overview

This Adyen test-cards-and-credentials landing page directs integration testers to test card numbers, alternative-payment-method test credentials, and instructions for creating their own test cards. It is a navigation page, not the card-number catalog or a record of a completed transaction. The raw page was last modified 2023-11-23 and captured 2026-09-15. See [[adyen]] and [[adyen-payment-testing]].

## Key takeaways

- The page tells integrators to use Adyen test card numbers and other test credentials while testing, and says they can create their own test cards. It does not list specific card data or credentials on this landing page.
- Its three routes are **Card numbers** for Adyen test card numbers, **Alternative payment methods** for method-specific test credentials, and **Creating test cards** for creating custom test cards. Follow the corresponding detailed source before claiming any credential, API prerequisite, method behavior, or simulator outcome.
- The See also link routes to Adyen's broader **Testing online payments** guide. Test credentials and navigation to test fixtures do not prove live payment acceptance, eligibility, authorization, capture, or settlement.

## Detail locators

- Lines 15–19: identity and testing purpose.
- Lines 21–25: card-number route.
- Lines 27–31: alternative-payment-method credential route.
- Lines 33–37: custom test-card creation route.
- Lines 39–41: broader online-payments testing route.

## Related

- [[adyen-payment-testing]] — provider testing concept and reciprocal source route.
- [[source-adyen-docs-development-resources-test-cards-and-credentials-test-card-numbers]] — detailed test-card catalog.
- [[source-adyen-docs-development-resources-test-cards-and-credentials-alternative-payment-method-credentials]] — method-specific test credential details.
- [[source-adyen-docs-development-resources-test-cards-and-credentials-create-test-cards]] — custom test-card creation guide.
- [[source-adyen-docs-development-resources-testing]] — broader integration testing guide.

## Raw Sources

- [[raw/adyen/docs/development-resources/test-cards-and-credentials/2026-09-15|Test cards and credentials landing page, captured 2026-09-15]]
