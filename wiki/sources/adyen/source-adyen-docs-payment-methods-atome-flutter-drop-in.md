---
title: "Adyen Atome Flutter Drop-in integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/atome/flutter-drop-in"
raw_files:
  - "adyen/docs/payment-methods/atome/flutter-drop-in/2026-09-15.md"
tags: [adyen, atome, flutter, drop-in, redirect, malaysia, singapore]
---

## Overview

This captured guide adds Atome-specific instructions to an existing Flutter Drop-in integration, with separate Sessions and Advanced server-flow sections. It describes request additions, redirect handling, partial-refund amount and test/live setup; the main Flutter integration guide supplies shared steps. The guide does not establish current merchant eligibility or a completed payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions flow:** existing Flutter Drop-in, Checkout API v68 or later, `action.type=redirect` handling, and Support contact to add Atome in Customer Area. The `/sessions` request table marks shopper name, email, telephone, billing address, `lineItems` and `countryCode` required; delivery address is optional when it matches billing. The supported pairs are MY/MYR and SG/SGD. This section says no extra Atome configuration parameters are needed.
- **Advanced flow:** existing Flutter Drop-in with redirect handling and Atome added in Customer Area. Its `/payments` table adds `paymentMethod.type=atome` and the same shopper, invoice, item and country/currency fields, with the same delivery-address condition. This section also says no extra Atome configuration parameters are needed. The Advanced requirements table does not repeat the Sessions section's Checkout API v68+ gate; do not silently generalize that row to both flows.
- **Redirect outcome warning:** the Advanced example is headed “successful payment,” yet its response is `resultCode=RedirectShopper` with a redirect `action`. This indicates a next step, not authorization, capture or settled success. The Sessions requirements link labeled Flutter Sessions flow points to an `advanced-flow` URL; use the separately linked Sessions redirect/session steps and the raw headings to distinguish the flows.
- **Example request warning:** the Sessions and Advanced curl examples have `-X POST` without a shell continuation before `-d` (raw lines 63–64, 812–813), so they are not ready-to-run shell commands. The Sessions curl body repeats `countryCode` with the same `SG` value (lines 72 and 78). The examples are test-environment illustrations.
- Partial refunds specify `amount` in `/payments/{paymentPspReference}/refunds`. Testing needs an Atome sandbox shopper account requested through an Adyen contact; use separate test accounts for multiple countries. The page links MY/SG test apps for QR flow. Live Atome use requires Support to add it in the live Customer Area.
- Related Atome overview authority says portable electronics are excluded and must be disabled in checkout business logic, and says capture is automatic after authorization. Those are overview facts, not stated in this Flutter child guide; consult that source for product eligibility and capture rules.

## Detail locators

- Raw `# Atome Flutter Drop-in`, lines 15–36: scope, Sessions prerequisites and redirect. Raw `## Add additional parameters to your /sessions request`, lines 40–52: required fields and MY/MYR, SG/SGD. Sessions curl lines 58–114: sample syntax and duplicate country code.
- Raw `## Advanced flow Drop-in`, lines 768–801: Advanced prerequisites, no extra configuration, payment fields and regional pairs. Advanced curl lines 805–866: sample syntax.
- Raw lines 1518–1530: mislabeled `RedirectShopper` example. Raw `## Refunds and cancellations` and `## Test and go live`, lines 1534–1560: partial-refund amount, testing and live setup.
- [[source-adyen-docs-payment-methods-atome]]: portable-electronics exclusion, automatic capture and product overview.

## Related

- [[source-adyen-docs-payment-methods-atome]] — method-level restrictions and capture summary
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/atome/flutter-drop-in/2026-09-15|Atome Flutter Drop-in guide, captured 2026-09-15]]
