---
title: "Adyen ACH Direct Debit for Web"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/ach-direct-debit/web"
raw_files:
  - "adyen/docs/payment-methods/ach-direct-debit/web/2026-09-15.md"
tags: [adyen, ach-direct-debit, web, navigation]
---

## Overview

Adyen's 2026-09-15 ACH Direct Debit Web page is an integration chooser. It links Web Drop-in and Components method guides plus the corresponding Sessions and Advanced base guides. It does not itself establish ACH authorization, verification, request fields, settlement, return handling or current merchant eligibility. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The Drop-in child is labeled an all-in-one UI solution for websites; the Components child is a separate method guide (raw lines 19-27). The Components description says “Use the Ach” without a complete Component name, so this chooser is not authority for a class or export name.
- The page instructs merchants to create their main Web integration before adding ACH Direct Debit, linking Drop-in and Components for both Sessions and Advanced flows (raw lines 29-36). These are navigation options, not a claim that every child method path or account configuration supports the same behavior.
- Method-level ACH bank validation, mandate/SEC-code, return and settlement qualifications belong to [[source-adyen-docs-payment-methods-ach-direct-debit]]; this chooser provides no operational sequence.

## Related raw API references

- [[raw/adyen/docs/payment-methods/ach-direct-debit/web-drop-in/2026-09-15|ACH Web Drop-in child guide (unread navigation)]]
- [[raw/adyen/docs/payment-methods/ach-direct-debit/web-component/2026-09-15|ACH Web Component child guide (unread navigation)]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/ach-direct-debit/web/2026-09-15|ACH Direct Debit Web chooser (2026-09-15 snapshot)]]
