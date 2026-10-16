---
title: "Adyen Transaction Descriptions"
type: concept
category: technology
tags: [adyen, transaction-description, shopper-statement, payment-methods]
---

## Definition

Adyen's transaction description is the text intended to help a shopper identify a charge on a bank statement. The merchant can set a static Doing Business As (DBA) name, use a transaction-specific shopper statement, or append that statement to the DBA name. The merchant-account address city and country/region are added even when the description is customized. [[source-adyen-docs-account-transaction-description]]

## Configuration boundary

The captured guide describes **live** Customer Area merchant-account/store settings and **live** Management API per-payment-method settings; a method-specific setting takes precedence. A dynamic description needs both the enabled setting and a `shopperStatement` in the payment request, with the configured DBA as fallback when that request value is absent. Configuration is limited to listed supported payment methods, with separate locale and channel rules. Use the source for roles, 22-character/truncation and allowed-character limits, CSV size and propagation timing, current-versus-new-method behavior, ecommerce/POS request placement, and Japan/localized-statement conditions.

## Sources

- [[source-adyen-docs-account-transaction-description]] — 2026-09-15 Adyen Docs snapshot covering live descriptor setup, request values, precedence, limits, supported methods, propagation and localization.

## Related

- [[adyen]]
