---
title: "Adyen Surcharging"
type: concept
category: technology
tags: [adyen, online-payments, surcharge, cards, compliance]
---

## Definition

Adyen's documented online-payments surcharge feature is a pilot for API-only card integrations using raw or encrypted card data. The merchant server retrieves card characteristics through `/cardDetails`, owns the decision and calculation logic, discloses the surcharge to the shopper, and submits `surcharge.value` while setting `amount.value` to the original amount plus the surcharge.

## Compliance and lifecycle boundaries

The feature does not automate global compliance enforcement. The retained snapshot says schemes require signage that tells customers which payment methods are subject to surcharges and the related costs, such as the surcharge percentage. Surcharging remains subject to applicable legal, regulatory, local, and card-scheme rules; the snapshot gives EEA-issued consumer cards in the EEA and US debit cards as examples where surcharging is not allowed. These statements are snapshot evidence, not exhaustive or current legal advice, and current scheme and local rules require verification.

The guide says surcharges cannot be applied to authorization adjustments or overcaptures, and the surcharge cannot exceed the amount disclosed at purchase. Capture and refund requests for a surcharged transaction use the full amount including the surcharge. Pilot documentation and API examples do not prove current availability, merchant eligibility, production enablement, compliant configuration, or transaction success.

## Sources

- [[source-adyen-docs-online-payments-surcharge]] - 2026-09-15 Adyen guide to the pilot API-only card surcharge flow, merchant-owned eligibility logic, legal and payment-method boundaries, request arithmetic, and capture/refund handling
