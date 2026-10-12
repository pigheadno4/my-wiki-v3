---
title: "Adyen Co-badged Cards Compliance"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/co-badged-cards-compliance"
raw_files:
  - "adyen/docs/online-payments/co-badged-cards-compliance/2026-09-15.md"
tags: [adyen, online-payments, co-badged-cards, card-brands, compliance, eea, australia]
---

## Overview

This Adyen Docs page is an unversioned integration-compliance guide for co-badged cards. It distinguishes European Economic Area and Australian requirements, provides captured minimum integration versions or configuration routes, and explains brand choice, routing, presentation, and stored-card treatment. The retained page is snapshot evidence, not legal advice or proof of current merchant eligibility, configuration, or successful payment execution. See [[adyen]] and [[co-badged-cards]].

## Key takeaways

- The page says some regions require additional configuration and recommends staying on the latest available version. Its captured compatibility matrix routes API-only and custom-card integrations to implementation-specific guidance and gives minimum versions for Web, iOS, Android, React Native, Flutter, Salesforce Commerce Cloud SFRA, and Adobe Commerce; exact versions and routes remain in the raw.
- For the captured Drop-in path, a listed minimum-version Drop-in used with Checkout API v71 is described as compliant out of the box. An earlier Checkout API version requires additional front-end configuration. This statement is integration- and version-qualified, not a general guarantee for Components, API-only, custom-card, or Classic integrations.
- For co-badged cards issued in the EEA, the page says that when the merchant supports both brands, the cardholder must be allowed to choose the brand. Available schemes must be identified clearly with comparable visual quality, clarity, and size; a checkout accepting both credit and debit cards must not label the card section as credit-card-only.
- In the EEA guidance, a selected brand must be honored and the payment must not be routed to another scheme. If the cardholder makes no choice, the merchant may select and preselect a scheme but must make the intended routing clear. For the first transaction that stores a co-badged card, the shopper must be offered a scheme choice and told that recurring payments use that scheme; a chosen scheme must be stored and honored for recurring transactions, while the merchant may choose and visibly preselect a scheme when the shopper does not choose.
- For Australia, letting the cardholder choose a network is optional in this page's guidance, but any offered choice must be honored. If the shopper does not choose, the checkout must reasonably indicate that either network can process the transaction. If the checkout does not offer a network choice, it must identify the available processing networks and show all their logos.

## Detail locators

- `## Requirements for integration`, lines 21–38 — integration-specific routes, captured minimum versions, and the Drop-in plus Checkout API v71 qualification.
- `### Tab: European Economic Area` through `#### Clearly identify payment schemes`, lines 42–52 — EEA-issued-card and supported-brand condition, choice requirement, and scheme presentation.
- `#### Do not discriminate between card products`, lines 54–65 — debit/credit labeling, debit-offering examples, and version/integration-specific naming guidance.
- `#### Honor the cardholder's choice` through `#### Preselect a scheme for cardholders that do not make a choice`, lines 67–73 — selected-brand routing prohibition and no-choice preselection/disclosure.
- `### Guidelines for stored co-badged cards`, lines 75–80 — first-transaction disclosure plus chosen and no-choice recurring routing.
- `### Tab: Australia`, lines 82–96 — optional shopper choice, honoring an offered choice, either-network disclosure, and all-network-logo presentation when no choice is offered.

## Related

- [[adyen]] — provider page.
- [[co-badged-cards]] — cross-provider concept covering regulatory and implementation evidence.

## Raw Sources

- [[raw/adyen/docs/online-payments/co-badged-cards-compliance/2026-09-15|Adyen co-badged cards compliance (2026-09-15 snapshot)]]
