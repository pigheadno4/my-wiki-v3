---
title: "Adyen PaymentMethodVariant Reference"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/paymentmethodvariant"
raw_files:
  - "adyen/docs/development-resources/paymentmethodvariant/2026-09-15.md"
tags: [adyen, payment-methods, variants, management-api]
---

## Overview

Adyen's `PaymentMethodVariant` reference maps `paymentMethodVariant` values to the payment method type used in a transaction. The listed values are not exhaustive: Adyen says other variants can be returned depending on configuration. The same snapshot also contains a separate Management API table of payment method variants available when **adding** a method, with distinct ecommerce and point-of-sale columns and method-specific notes. A transaction's returned variant is a classification; it does not by itself establish that a merchant can add or offer that method.

## Key takeaways

- The reference groups card-network, wallet and other method variants in tables, including card subtype and wallet-on-card variants. Preserve exact case and spelling when matching a returned value; use the raw table for a particular code rather than treating the list as a closed enum.
- The `## Management API` table is about adding payment methods through the Management API. Its ecommerce/POS indicators and notes vary by method; some rows specify extra parameters, shopper interaction, currencies, approval or regional limits. Check the relevant row and linked method/API documentation for an actual setup decision. The snapshot is documentation, not evidence of merchant enablement or live availability.

## Detail locators

- `## American Express` through `## Others`: transaction `paymentMethodVariant` names and descriptions, including card subtype and ecommerce/POS variants.
- `## Management API`: adding-method variants, ecommerce versus point-of-sale columns, and row-specific conditions. For example, the ACH Direct Debit row notes approval, and the Cartes Bancaires row limits support to stores in France.

## Related

- [[adyen]]
- [[adyen-payment-method-variants]]

## Raw Sources

- [[raw/adyen/docs/development-resources/paymentmethodvariant/2026-09-15|Adyen PaymentMethodVariant webpage snapshot (2026-09-15)]]
