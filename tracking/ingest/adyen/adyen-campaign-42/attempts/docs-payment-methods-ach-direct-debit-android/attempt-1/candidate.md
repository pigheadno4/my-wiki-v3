---
title: "ACH Direct Debit for Android integration chooser"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/ach-direct-debit/android"
raw_files:
  - "adyen/docs/payment-methods/ach-direct-debit/android/2026-09-15.md"
tags: [adyen, ach, direct-debit, android, integration-chooser]
---

## Overview

This 2026-09-15 Adyen page is an **Android ACH Direct Debit integration chooser**. It points to Android Drop-in and Components ACH child guides and to the four base Android Sessions/Advanced guides. It does not specify ACH request fields, SDK/API versions, mandate/verification steps, account eligibility, or payment outcome. [[adyen]] [[adyen-online-payments]] [[adyen-android-sdk]]

## Key takeaways

- The page links **Drop-in** as an all-in-one UI route at `/payment-methods/ach-direct-debit/android-drop-in` and **Components** at `/payment-methods/ach-direct-debit/android-component`. Choose the child matching the actual Android integration. See raw lines 19–27.
- The Components description calls it a **Redirect Component** and says it handles a redirect to ACH Direct Debit. This wording is in tension with the linked ACH-specific Android Component child, which shows `ACHDirectDebitComponent` setup; do not infer a redirect-only ACH flow from this chooser line. See raw lines 25–27; compare reviewed [[source-adyen-docs-payment-methods-ach-direct-debit-android-component]].
- The page says to build the **main** integration first, linking Android Drop-in/Components under each of Sessions and Advanced. This chooser is navigation, not a substitute for those main flow guides or the ACH method overview. See raw lines 29–36.

## Detail locators

- Drop-in and Components ACH child links, including Redirect wording: raw lines 19–27.
- Sessions/Advanced base-guide routes: raw lines 29–36.

## Related

- [[adyen-online-payments]] — main ACH payment route.
- [[adyen-android-sdk]] — Android Drop-in/Components choice.
- [[source-adyen-docs-payment-methods-ach-direct-debit-android-drop-in]] — ACH Drop-in child.
- [[source-adyen-docs-payment-methods-ach-direct-debit-android-component]] — ACH Component child.
- [[source-adyen-docs-payment-methods-ach-direct-debit]] — ACH mandate, verification and payment lifecycle context.

## Raw Sources

- [[raw/adyen/docs/payment-methods/ach-direct-debit/android/2026-09-15|ACH Direct Debit for Android, captured 2026-09-15]]
