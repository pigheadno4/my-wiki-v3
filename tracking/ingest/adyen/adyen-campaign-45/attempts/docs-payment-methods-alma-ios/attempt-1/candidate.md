---
title: "Alma for iOS | Adyen Docs"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alma/ios"
raw_files:
  - "adyen/docs/payment-methods/alma/ios/2026-09-15.md"
tags: [adyen, alma, ios, integration, drop-in, components]
---

## Overview

This 2026-09-15 [[adyen|Adyen]] page is an **iOS integration chooser** for Alma. It routes to separate Drop-in and Components child guides, and to generic iOS Sessions and Advanced base integrations. It is navigation rather than a step-by-step Alma payment guide. See [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-alma|the Alma method overview]] for broader context.

## Key takeaways

- The page links the Alma **iOS Drop-in** child as the all-in-one UI option, and the **iOS Components** child as an `InstantPaymentComponent` option (raw lines 19–27). These are different integration routes; this chooser itself does not state request fields, SDK/API versions or payment outcomes.
- It says to create the main integration before adding Alma, then links four base guides: iOS Drop-in and Components, each with Sessions and Advanced flow (lines 29–36). Follow the matching integration type and server-side flow before the relevant Alma child.
- No account eligibility, live setup or successful payment can be inferred from this chooser. Consult the selected child and method overview for their scoped prerequisites and lifecycle details.

## Detail locators

- Purpose and child route labels: raw lines 15–27.
- Main-integration prerequisite and four iOS flow routes: lines 29–36.

## Related

- [[adyen-online-payments]] — provider online-payment integration concept.
- [[source-adyen-docs-payment-methods-alma]] — Alma method overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/alma/ios/2026-09-15|2026-09-15 Alma iOS integration chooser]]

## Related raw API references

- The pinned chooser links Alma iOS Drop-in and Components child guides and generic iOS Sessions/Advanced integration guides (raw lines 21–36); follow their own evidence before relying on detailed behavior.
