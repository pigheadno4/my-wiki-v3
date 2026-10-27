---
title: "Adyen SEPA Direct Debit for Android"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/sepa-direct-debit/android"
raw_files:
  - "adyen/docs/payment-methods/sepa-direct-debit/android/2026-09-15.md"
tags: [adyen, sepa-direct-debit, android, navigation]
---

## Overview

Adyen's 2026-09-15 SEPA Direct Debit Android page is an integration chooser. It routes readers to Android Drop-in or `SepaComponent` child instructions and to general Android Sessions and Advanced integration guides. It provides no SEPA payment request, mandate, capture, token or outcome procedure itself. See [[adyen]] and [[adyen-android-sdk]].

## Key takeaways

- The Drop-in route is described as an all-in-one UI solution; the Components route names `SepaComponent` (raw lines 19-27). The chooser describes that Component as handling a “redirect to SEPA Direct Debit,” while the fully read Android Component child requires `action.type: direct` in its Advanced route. Do not infer a redirect action solely from the chooser wording (chooser raw line 27; Component child raw lines 1093-1101).
- The page instructs merchants to establish a main integration before adding SEPA Direct Debit and links Android Drop-in and Components base guides for Sessions and Advanced flows (raw lines 29-36). These links are navigation, not proof of account enablement, a shopper mandate or final debit.
- The [[source-adyen-docs-payment-methods-sepa-direct-debit]] overview owns method-level mandate, pre-debit notice and funds/chargeback constraints. The child guides own request and Component behavior; this page supplies route selection only.

## Related raw API references

- [[raw/adyen/docs/payment-methods/sepa-direct-debit/android-drop-in/2026-09-15|SEPA Android Drop-in child guide (unread navigation)]]
- [[raw/adyen/docs/payment-methods/sepa-direct-debit/android-component/2026-09-15|SEPA Android Component child guide (fully read for action qualification)]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/sepa-direct-debit/android/2026-09-15|SEPA Direct Debit Android chooser (2026-09-15 snapshot)]]
