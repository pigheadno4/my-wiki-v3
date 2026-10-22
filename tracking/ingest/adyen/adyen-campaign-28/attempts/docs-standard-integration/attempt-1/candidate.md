---
title: "Standard integration Hosted Checkout versus Drop-in"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/standard/integration"
raw_files:
  - "adyen/docs/standard/integration/2026-09-15.md"
tags: [adyen, standard-integration, online-payments, hosted-checkout, drop-in]
---

## Overview

This 2026-09-15-captured [[adyen]] Standard online-payments child page compares two prebuilt checkout presentations: **Hosted Checkout** redirects shoppers to Adyen's payment page, while **Drop-in** renders Adyen's form on the merchant website. It is an option-selection guide within [[adyen-online-payments]], not a claim that either path is deployed or every listed feature is enabled for a merchant (raw lines 15–26).

## Key takeaways

- Both options still require the merchant to build its **own payment server and webhook server**. Hosted Checkout moves the shopper to an Adyen-hosted domain; Drop-in keeps the shopper on the merchant's domain with embedded UI. The table assigns Adyen's Apple Pay certificate to Hosted Checkout and the merchant's own certificate to Drop-in, subject to the payment-method setup guide (raw lines 28–40).
- The table presents common **available features** such as payment with an available method, payment-detail storage, Uplift and accessibility support. Its “Required” icon is used as a table mark for feature availability; it does not show that every feature is mandatory in every integration or enabled for a particular account, shopper, region or method (raw lines 42–52).
- The comparison marks additional options only under **Drop-in**: payment-method styling, session amount update after start, custom client-side selection actions and an automatic Giving donation form. The page supplies no lifecycle detail for when a session amount may change or whether a donation is available; the linked child guides own those conditions (raw lines 53–56).
- The chooser routes to separate Standard Hosted Checkout and Drop-in implementation guides. Hosted Checkout is described as a server Checkout API request followed by a shopper redirect; Drop-in as one server Checkout API request plus prebuilt on-page form. A request or UI render is not an authorization, capture, settlement or webhook outcome (raw lines 60–68).

## Detail locators

- Standard two-option identity and selection criterion: raw lines 19–26.
- Domain, server/webhook ownership and Apple Pay certificate comparison: raw lines 28–40.
- Shared and Drop-in-only feature marks: raw lines 42–56.
- Child implementation routes: raw lines 60–68.

## Related

- [[source-adyen-docs-standard]]
- [[source-adyen-docs-standard-integration-hosted-checkout]]
- [[source-adyen-docs-standard-integration-drop-in]]
- [[source-adyen-docs-standard-integration-payment-method-setup]]

## Raw Sources

- [[raw/adyen/docs/standard/integration/2026-09-15|Pinned Standard integration chooser]]
