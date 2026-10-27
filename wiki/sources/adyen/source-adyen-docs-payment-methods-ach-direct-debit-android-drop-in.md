---
title: "ACH Direct Debit Android Drop-in integration"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/ach-direct-debit/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/ach-direct-debit/android-drop-in/2026-09-15.md"
tags: [adyen, ach, direct-debit, android, drop-in, sessions, advanced]
---

## Overview

This 2026-09-15 Adyen guide covers ACH Direct Debit additions to **existing Android Drop-in** Sessions and Advanced integrations. It scopes prerequisites, optional ACH UI settings, method-specific request additions, delayed bank outcome and TEST return simulation. It does not establish a complete Android implementation, validated bank account, mandate, live acceptance or settled funds. [[adyen]] [[adyen-online-payments]] [[adyen-android-sdk]]

## Key takeaways

- **Sessions** requires an existing Android Drop-in Sessions flow with **Checkout API v68 or later**, ACH added in Customer Area and `DIRECT_DEBIT_NOTICE_OF_CHANGE_NOTIFICATION` subscription for outdated bank details. The table's **Merchant allow bank-refund** API-credential and Customer Area roles are specifically for issuing refunds by those channels, not a blanket ACH-payment prerequisite. No ACH-specific additional `/sessions` parameters are needed. See raw lines 25–43.
- **Advanced** requires an existing Android Drop-in Advanced flow, ACH addition and the notice-of-change webhook. Its section does **not** state a Checkout API minimum. It similarly says no ACH-specific additional `/payments` parameters; this does not erase base Advanced-flow fields, consumer account validation or shopper mandate obligations. See raw lines 102–112 and 143–147. [[source-adyen-docs-payment-methods-ach-direct-debit]] [[source-adyen-docs-payment-methods-ach-direct-debit-verification-with-giact]]
- Both flows offer optional ACH configuration: `setSubmitButtonVisible(false)` hides the submit button (default visible), `setAddressConfiguration` controls the shopper address form (default `FullAddress`), and `setShowStorePaymentField(false)` hides the future-payment checkbox (default visible). The sample uses `supportedCountryCodes = listOf("US", "PR")` inside address configuration; this UI example is not proof of live merchant/bank eligibility. This page gives no Android SDK version minimum. See raw lines 45–72 and 114–141.
- After Adyen receives a request, **bank authorization may take up to five business days**. If the bank authorizes, the payment appears in the Settlement details report; if it fails, Adyen says a `CHARGEBACK` webhook follows. Drop-in completion or request receipt does not prove bank authorization or funds availability. See raw lines 74–80 and 149–155.
- TEST examples accept correctly formatted bank account and routing numbers with any owner name; `ownerName=chargeback:<reason>` (for example `chargeback:R01`) simulates an ACH return. These are only test fixtures; reason-specific ACH retry and dispute rules belong in the separate ACH chargebacks guide. See raw lines 82–100 and 157–173.

## Detail locators

- Sessions requirements, refund-role scope and request boundary: raw lines 25–43.
- Sessions ACH UI configuration, outcome and TEST fixtures: raw lines 45–100.
- Advanced requirements, optional configuration and `/payments` boundary: raw lines 102–147.
- Advanced delayed outcome, TEST simulation and related links: raw lines 149–179.

## Related

- [[adyen-online-payments]] — Android online-payment route.
- [[adyen-android-sdk]] — Drop-in/ACH configuration context.
- [[source-adyen-docs-payment-methods-ach-direct-debit]] — ACH overview, SEC and mandate.
- [[source-adyen-docs-payment-methods-ach-direct-debit-verification-with-giact]] — consumer account-validation route.

## Raw Sources

- [[raw/adyen/docs/payment-methods/ach-direct-debit/android-drop-in/2026-09-15|ACH Direct Debit Android Drop-in, captured 2026-09-15]]
