---
title: "BACS Direct Debit for Android integration chooser"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bacs/android"
raw_files:
  - "adyen/docs/payment-methods/bacs/android/2026-09-15.md"
tags: [adyen, bacs, direct-debit, android, integration-chooser]
---

## Overview

This 2026-09-15 Adyen page is a **BACS Android integration chooser**, linking method-specific Drop-in and Components guides plus the four base Android Sessions/Advanced integration guides. It contains no BACS request schema, SDK/API minimum, Direct Debit Instruction detail, clearing rule or final payment outcome. [[adyen]] [[adyen-online-payments]] [[adyen-android-sdk]]

## Key takeaways

- The **Drop-in** option links `/payment-methods/bacs/android-drop-in` as an all-in-one Android UI. The **Components** option links `/payment-methods/bacs/android-component` and names `BacsDirectDebitComponent`. Select the child matching the integration. See raw lines 19–27.
- The Components blurb says that `BacsDirectDebitComponent` handles a **redirect** to BACS Direct Debit. This single chooser sentence should not be treated as a complete action-handling contract: the reviewed [[source-adyen-docs-payment-methods-bacs-android-component]] reports an Advanced `Direct` prose versus `voucher` response-example conflict. Preserve that boundary rather than silently choosing one action type. See raw lines 25–27 and the linked child source.
- The page says to create the **main integration first**, linking Android Drop-in and Components guides for both Sessions and Advanced flows. It is a navigation route to those guides, not payment proof or live merchant enablement. See raw lines 29–36.

## Detail locators

- Android Drop-in and Components child links and redirect wording: raw lines 19–27.
- Base Sessions/Advanced guide routes: raw lines 29–36.

## Related

- [[adyen-online-payments]] — main BACS online-payment route.
- [[adyen-android-sdk]] — Android Drop-in/Components context.
- [[source-adyen-docs-payment-methods-bacs-android-drop-in]] — method-specific Drop-in child.
- [[source-adyen-docs-payment-methods-bacs-android-component]] — method-specific Component child.
- [[source-adyen-docs-payment-methods-bacs]] — DDI, clearing and return overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/bacs/android/2026-09-15|BACS Direct Debit for Android, captured 2026-09-15]]
