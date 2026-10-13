---
title: "Adyen Docs: Payments India compliance guide"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/payments-india-compliance-guide"
raw_files:
  - "adyen/docs/online-payments/payments-india-compliance-guide/2026-09-15.md"
tags: [adyen, india, local-acquiring, card-storage, recurring-payments]
---

## Overview

This [[adyen]] guide describes Adyen's India setup and payment-data and recurring-payment workflow for **local acquiring in India**. The page expressly excludes cross-border payments and says it supplements Reserve Bank of India (RBI) regulations, may change with them, and is not legal advice. The 2026-09-15 snapshot has 2021-12-10 `last_modified` metadata; it is not current regulatory, legal, account-eligibility, or payment-execution proof. See [[adyen-online-payments]].

## Key takeaways

- To start processing locally in India, the page says the merchant needs a local Indian entity, onboarding through its Adyen account manager, a separate company account for the Indian business, and compliance with RBI rules on payment-data storage and recurring payments. These are stated for local processing, not cross-border payments.
- For merchants processing **card payments locally in India**, the guide says only the last four card-number digits and issuer name may be stored for transaction tracking and reconciliation. It lists report columns redacted as a consequence; consult raw **Storing card details** for the per-report list. This page does not establish what a cross-border or other-region merchant may store.
- For locally acquired one-off payments using saved card details, the page describes the **CardOnFile** model and points to RBI rules allowing only authorised card networks to tokenize cards. The raw applicability table distinguishes this from locally acquired recurring payments using **Subscription** or **UnscheduledCardOnFile**; `shopperInteraction` values and exact payment-type mapping remain in that table.
- For locally acquired recurring card payments, the page says the shopper must be notified before a charge. Its described setup sends the billing plan in the payment request, has the shopper authenticate a transaction to create an issuer mandate, sends a pre-debit notification using mandate details, and charges after a **48-hour cooling period**. It names subscriptions and non-fixed-schedule automatic top-ups, and also mentions recurring UPI payments; the linked card and UPI implementation pages carry the method-specific instructions. See raw **Recurring payments**.
- The guide lists Online Banking India, Paytm, UPI, and Wallets India as local methods that require processing locally in India, in addition to cards from India. See raw **Payment methods** and the linked **India go-live checklist** for further navigation.

## Detail locators

- Raw opening paragraphs and applicability table — legal/snapshot caveat, local-acquiring boundary, onboarding actors, payment-type models, and `shopperInteraction` mapping.
- Raw **Storing card details** — local-card data limits and affected report columns.
- Raw **CardOnFile payments** and **Recurring payments** — saved-detail, tokenization, mandate, pre-debit, and cooling-period guidance with linked RBI and method pages.

## Related

- [[source-adyen-docs-online-payments-tokenization-make-token-payments]] — broader token-payment API route; the India-specific conditions in this snapshot govern the local-acquiring discussion here.

## Raw Sources

- [[raw/adyen/docs/online-payments/payments-india-compliance-guide/2026-09-15|Payments India compliance guide (2026-09-15 snapshot)]]
