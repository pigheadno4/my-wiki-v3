---
title: "Clearpay for Android | Adyen Docs"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/clearpay/android"
raw_files:
  - "adyen/docs/payment-methods/clearpay/android/2026-09-15.md"
tags: [adyen, clearpay, android, navigation]
---

## Overview

This 2026-09-15-captured [[adyen]] page is an **Android integration chooser** for Clearpay. It links Android Drop-in and Components child guides plus four main Android integration guides. The related [[source-adyen-docs-payment-methods-clearpay]] overview supplies the captured GB/GBP product and regional-brand scope; this chooser itself does not establish current merchant availability, request requirements or a completed payment. See [[adyen-online-payments]].

## Key takeaways

- **Child routes:** Drop-in is described as the all-in-one Android UI route. Components points to `InstantPaymentComponent` for handling the Clearpay redirect (raw lines 19–27). Consult the selected child guide for its own server-flow, request, redirect and lifecycle conditions.
- **Base integration first:** The page says to create the main integration before adding Clearpay, then links Android Drop-in and Components base guides for both **Sessions** and **Advanced** flows (raw lines 29–36). These are navigation links, not a claim that the two child guides have identical prerequisites or that a merchant is enabled.
- The chooser contains no country/currency matrix, field table, capture rule or result-status procedure. Use the overview and selected child guide for those scopes.

## Detail locators

- Purpose and Drop-in/Components child routes: pinned raw `# Clearpay for Android` and `### How do you want to integrate?`, lines 15–27.
- Main-integration prerequisite and four Android Sessions/Advanced base routes: pinned raw `## See also`, lines 29–36.

## Related

- [[adyen-online-payments]] — provider checkout context.
- [[source-adyen-docs-payment-methods-clearpay]] — GB/GBP product and regional-brand overview.
- [[source-adyen-docs-payment-methods-clearpay-android-drop-in]] — Android Drop-in add-on.
- [[source-adyen-docs-payment-methods-clearpay-android-component]] — Android Components add-on.

## Raw Sources

- [[raw/adyen/docs/payment-methods/clearpay/android/2026-09-15|Clearpay Android chooser, captured 2026-09-15]]
