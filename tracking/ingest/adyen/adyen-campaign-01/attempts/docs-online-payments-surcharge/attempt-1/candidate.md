---
title: "Adyen Online Payments Surcharge"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/surcharge"
raw_files:
  - "adyen/docs/online-payments/surcharge/2026-09-15.md"
tags: [adyen, online-payments, surcharge, cards, compliance]
---

## Overview

This Adyen guide describes a pilot feature for adding a card-payment surcharge in an API-only online-payments integration. The documented flow has the merchant retrieve card characteristics through `/cardDetails`, decide whether a surcharge is permitted and calculate it, disclose it to the shopper, and submit it in the `/payments` request.

## Key takeaways

- The snapshot requires an API-only card integration using raw or encrypted card data, an API credential with the Checkout webservice role, and Standard webhooks. It labels the feature as a pilot with possible restrictions and directs merchants to contact Adyen to participate.
- The merchant server calls `/cardDetails`; the response can include card brand, funding source, consumer-versus-commercial status, and issuing country. The merchant implements the eligibility and calculation logic rather than relying on Adyen for global compliance enforcement.
- The surcharge must be shown to the shopper before payment. The `/payments` request carries the surcharge in `surcharge.value`, while `amount.value` is the original transaction amount plus the surcharge.
- For a capture or refund of a surcharged transaction, the guide says to pass the full amount including the surcharge. Receiving the surcharge amount in `/payments` additional data or the `AUTHORISATION` webhook is an optional Customer Area configuration.

## Material qualifications and warnings

- Surcharging remains subject to legal, regulatory, local, and card-scheme requirements. The page gives jurisdiction-specific examples: no surcharge on an EEA-issued consumer card in the EEA, and no surcharge on US debit-card payments. These are examples in a 2026-09-15 documentation snapshot, not an exhaustive or current legal determination; the page recommends checking current scheme rules and consulting legal counsel.
- Adyen does not provide automated global compliance enforcement for this feature. Merchant logic and configuration must account for the applicable payment method and jurisdiction.
- The guide says surcharges cannot be applied to authorization adjustments or overcaptures, and the surcharge cannot exceed the amount disclosed at purchase.
- Collecting raw card data requires full PCI compliance. The guide's request and SDK examples are version-qualified examples, not proof of current account eligibility, production enablement, API behavior, transaction success, or a compliant surcharge decision.

## Detail locators

- API-only integration, credential, webhook, pilot, adjustment/overcapture, disclosure-cap, and legal-review prerequisites: `## Requirements`, raw lines 21-32.
- Scheme, EEA consumer-card, US debit-card, local-law, and non-automated-enforcement boundaries: `## Compliance`, raw lines 34-40.
- Five-step server and checkout sequence: `## How it works`, raw lines 42-50.
- Raw-versus-encrypted card-number inputs, full-PCI warning, request examples, and example SDK versions: `## Get card details`, raw lines 52-285.
- Card attributes used by merchant eligibility and calculation logic: `/cardDetails` response table and following instruction, raw lines 287-319.
- Payment request arithmetic and versioned example payload: `## Make a payment including the surcharge`, raw lines 321-360.
- Payment response fields, capture/refund amount handling, and optional surcharge additional data: raw lines 362-377.
- Test-card instruction and related compliance/in-person routes: `## Test and go live` and `## See also`, raw lines 381-389.

## Related

- Company: [[adyen]]
- Main concept: [[adyen-surcharging]]
- Online-payments architecture: [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/online-payments/surcharge/2026-09-15|Adyen online-payments surcharge documentation snapshot]] - complete collected guide covering the pilot prerequisites, merchant decision flow, compliance boundaries, payment request, and capture/refund handling
