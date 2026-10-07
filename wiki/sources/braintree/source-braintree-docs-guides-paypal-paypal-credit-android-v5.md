---
title: "Braintree PayPal Credit — Android v5 Route"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal/paypal-credit/android/v5"
raw_files:
  - "braintree/docs/guides/paypal/paypal-credit/android/v5-2026-09-16.md"
tags: [braintree, paypal, paypal-credit, android, sdk-v5, deprecated]
---

## Overview

This 2026-09-16 Braintree website snapshot is routed as Android v5, but its retained body is a short, generic orientation page for PayPal Credit rather than an Android API or implementation guide. It describes PayPal Credit as an instant, reusable credit line presented as an additional checkout button, and the page is explicitly deprecated in favor of the Pay Later offers guide. The snapshot does not establish current availability, merchant or buyer eligibility, account enablement, financing approval, exact Android SDK-package support, GitHub implementation behavior, or payment execution.

## Key takeaways

- The page says the PayPal UI offers the financing options available to a customer, including US Easy Payments and UK Instalments, only if those options have been enabled for the merchant's PayPal account. It does not define current country coverage, customer qualification, offer terms, or approval behavior.
- The guide is deprecated and directs readers to the Pay Later offers guide. Treat this page as historical routing evidence, not the current integration authority.
- Its stated prerequisites are to complete a PayPal client-side integration and use either the Vault or Checkout flow. These are navigation-level client prerequisites; the page supplies no Android request type, method, code example, server-side transaction step, or lifecycle outcome.
- The body says offering PayPal Credit is similar to regular PayPal payments but provides no actionable integration detail. The Android v5 route and an unread `PayPalRequest` Javadoc URL containing version `3.17.2` do not establish compatibility with any current Braintree Android package or repository revision.

> [!warning] Scope boundary
> This is a dated Braintree website snapshot with generic PayPal Credit prose. Its account-enablement condition and client-side navigation must not be expanded into current merchant availability, buyer eligibility, server processing, financing approval, or successful payment claims; website routing also is not version-matched GitHub evidence.

## Detail locators

- Source URL, fetch date, and page metadata: lines 1–10.
- Deprecation and replacement-guide navigation: **IMPORTANT**, lines 17–18.
- Credit-line purpose, additional checkout button, financing presentation, countries named as examples, and account-enablement condition: line 22.
- Support-article navigation for availability and benefits: **Before you get started**, line 28.
- Client-side prerequisite and Vault-or-Checkout navigation: **Before you get started**, lines 31–34.
- High-level comparison with regular PayPal payments: **Integration**, lines 39–41.
- Android tokenization, Vault, Checkout, and support navigation: **See also**, lines 44–50.

## Related

- Company: [[braintree]]
- Concept: [[braintree-android-sdk]]

## Related raw API references

The captured Pay Later replacement, support article, client-side PayPal, Vault, Checkout, and Android `PayPalRequest` targets were not read for this entry. They are navigation only and provide no behavioral or current-version evidence here.

## Raw Sources

- [[raw/braintree/docs/guides/paypal/paypal-credit/android/v5-2026-09-16|Braintree PayPal Credit — Android v5 route (fetched 2026-09-16)]]
