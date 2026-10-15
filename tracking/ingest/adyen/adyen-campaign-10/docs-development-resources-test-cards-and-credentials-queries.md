# Retrieval checks — test cards and credentials

## Q1. What is this page for, what is its scope, and what must a reader not infer?

This Adyen landing page directs integration testers to test card numbers, alternative-payment-method test credentials, and custom test-card creation; it also links to the broader online-payments testing guide. Its opening says test card numbers and other test credentials are used to test an integration (`raw/adyen/docs/development-resources/test-cards-and-credentials/2026-09-15.md:15-19`), and the three navigation cards are at lines 21–37. The landing page does not itself specify card numbers, method-specific behavior, prerequisites for custom creation, a completed test result, or live payment acceptance. Its metadata says last modified 2023-11-23 and captured 2026-09-15, so it is a historical navigation snapshot.

Canonical retrieval route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-payment-testing.md` → `wiki/sources/adyen/source-adyen-docs-development-resources-test-cards-and-credentials.md` → `raw/adyen/docs/development-resources/test-cards-and-credentials/2026-09-15.md`. Canonical URL: https://docs.adyen.com/development-resources/test-cards-and-credentials.

## Q2. What central capability or process does it describe, with prerequisites and warnings?

Its central function is selecting the relevant detailed testing route: **Card numbers** for test-card numbers (`raw/adyen/docs/development-resources/test-cards-and-credentials/2026-09-15.md:21-25`), **Alternative payment methods** for their test credentials (`:27-31`), and **Creating test cards** for instructions to make test cards (`:33-37`). The See also route points to broader online-payments testing (`:39-41`). The page supplies no substantive setup or payment-result procedure; retrieve the linked detailed source for credential values, prerequisites, simulator behavior, and warnings. A test fixture is not proof of live authorization, capture, settlement, or payment-method eligibility.

Canonical retrieval route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-payment-testing.md` → `wiki/sources/adyen/source-adyen-docs-development-resources-test-cards-and-credentials.md` → `raw/adyen/docs/development-resources/test-cards-and-credentials/2026-09-15.md`.
