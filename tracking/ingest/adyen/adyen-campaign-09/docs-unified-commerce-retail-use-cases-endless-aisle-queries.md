# Endless aisle landing-page retrieval checks

Canonical route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-unified-commerce.md` → `wiki/sources/adyen/source-adyen-docs-unified-commerce-retail-use-cases-endless-aisle.md` → `raw/adyen/docs/unified-commerce/retail-use-cases/endless-aisle/2026-09-15.md`.

## Q1 — purpose, scope, and what not to infer

This landing page defines endless aisle as customers placing ecommerce orders in a store or other physical location, with out-of-stock, online-exclusive and showroom examples (`raw/adyen/docs/unified-commerce/retail-use-cases/endless-aisle/2026-09-15.md:19–23`). It is a scenario index. The page does not define seller/payee/MoR, payment API, authorization or capture timing, terminal setup, inventory synchronization, delivery, return or completed order. Those details require the linked scenario guides; do not import their behavior into this overview or assume their flows are identical.

## Q2 — central capability, prerequisites, and warnings

The page routes the reader to two distinct variants: order items while in store and ship to a home address, or order items while in store for later store pickup (`:25–38`). It suggests wider product selection and delivery to an address as possible customer benefits (`:19–23`). It states no technical prerequisites, eligibility conditions, payment-status handling or fulfillment guarantees. For implementation questions, follow the separately reviewed `source-adyen-docs-unified-commerce-retail-use-cases-endless-aisle-e-a-ship-home` or `source-adyen-docs-unified-commerce-retail-use-cases-endless-aisle-e-a-store-pickup` route as applicable.
