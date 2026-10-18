---
title: "Adyen Platforms in-person split-refund methods"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/in-person-payments/split-transactions/split-refunds"
raw_files:
  - "adyen/docs/platforms/in-person-payments/split-transactions/split-refunds/2026-09-15.md"
tags: [adyen, platforms, in-person-payments, refunds, split-payments]
---

## Overview

This Adyen for Platforms in-person split-refunds hub, last modified 2024-01-24 and captured 2026-09-15, compares a referenced Terminal API refund with explicit split instructions against a refund that follows the original payment split. It directs readers to separate procedure pages for each method. The page describes request choice and limits, not asynchronous outcomes, actual balance bookings, or shopper receipt.

## Key takeaways

- A user returning funds to a customer requires a refund request to Adyen. The page allows a full captured-amount refund, a partial refund, or multiple partial refunds, while the sum of partial refunds cannot exceed the captured amount. Some payment methods do not support partial refunds; check the applicable method.
- For a split payment, this hub recommends including refund split instructions to control which balance accounts are debited and to support partial or multiple partial scenarios. If instructions are omitted, it says the refund follows the split of the original payment request, deducting from the same balance accounts. The hub does not define partial-refund allocation, rounding, or all eligibility conditions for that original-split option; use the linked method guide for its exact behavior.
- Both choices on this page use a *referenced* Terminal API `ReversalRequest`. The selectable routes are “Refund with split instructions” (recommended) and “Refund with original split ratio” (labeled API-only). These labels do not describe an unreferenced refund or a separate provider outcome. The operation-specific guides hold request fields, standalone/integration limits, and outcome tracking.

## Detail locators

- `# Split refunds`: refund amount options, aggregate partial-refund cap, payment-method caveat.
- `## Refund methods`: explicit versus original split choice, recommendation, omitted-instructions wording, referenced Terminal API reversal requirement.
- `## Select a refund method`: links to “Refund with split instructions” and API-only “Refund with original split ratio” procedures.

## Related

- [[adyen-platforms]] — main Platforms concept and source route.
- [[source-adyen-docs-platforms-in-person-payments-split-transactions-split-refunds-refund-split-instructions]] — detailed explicit split procedure.
- [[source-adyen-docs-platforms-in-person-payments-split-transactions-split-refunds-refund-original-split]] — detailed original split procedure.
- [[adyen]] — provider profile.

## Raw Sources

- [[raw/adyen/docs/platforms/in-person-payments/split-transactions/split-refunds/2026-09-15|Adyen split refunds (fetched 2026-09-15)]]
