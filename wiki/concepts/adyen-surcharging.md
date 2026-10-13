---
title: "Adyen Surcharging"
type: concept
category: technology
tags: [adyen, online-payments, surcharge, cards, compliance]
---



## POS methods and boundary

Adyen's point-of-sale surcharge guide describes configuration-based rules at account, store, or terminal scope and dynamic surcharges calculated by the merchant or a third party for an integrated payment request. Standalone terminals support configuration-based surcharges only. When both methods are present, a dynamic request amount overrides the configured surcharge; they are not added together. The POS guide excludes surcharge plus DCC on one transaction, and its terminal confirmation screen is unavailable in the Mobile solution, where another disclosure form remains necessary. These POS methods and their hardware/settings boundaries are separate from the online API-only card surcharge pilot described above.
## Definition

Adyen's documented online-payments surcharge feature is a pilot for API-only card integrations using raw or encrypted card data. The merchant server retrieves card characteristics through `/cardDetails`, owns the decision and calculation logic, discloses the surcharge to the shopper, and submits `surcharge.value` while setting `amount.value` to the original amount plus the surcharge.



## In-person configuration-based surcharge

Adyen's separate point-of-sale guide configures automatic surcharge rules through Management API terminal settings at company, merchant-account, store or terminal scope for eligible Terminal API, Tap to Pay Mobile, or standalone solutions. The ordered rules use the first matching brand, funding-source, issuer-country, currency and optional commercial-card condition; fixed amounts and caps use minor units. The commercial-card check is unavailable on Mobile solutions and when a terminal is offline. Tap to Pay has no surcharge confirmation screen and requires Support-enabled single tap plus another form of disclosure. From terminal software v1.117, configured rules also cover MOTO/MKE, creating a double-surcharge risk when the merchant already charges those flows separately. Firmware gates, hardware exclusions, credential roles and applicable legal/scheme constraints remain qualified in the linked 2026-09-15 source; configuration is not proof of current eligibility or payment outcome. [[source-adyen-docs-point-of-sale-surcharge-configuration]]
## Compliance and lifecycle boundaries

The feature does not automate global compliance enforcement. The retained snapshot says schemes require signage that tells customers which payment methods are subject to surcharges and the related costs, such as the surcharge percentage. Surcharging remains subject to applicable legal, regulatory, local, and card-scheme rules; the snapshot gives EEA-issued consumer cards in the EEA and US debit cards as examples where surcharging is not allowed. These statements are snapshot evidence, not exhaustive or current legal advice, and current scheme and local rules require verification.

The guide says surcharges cannot be applied to authorization adjustments or overcaptures, and the surcharge cannot exceed the amount disclosed at purchase. Capture and refund requests for a surcharged transaction use the full amount including the surcharge. Pilot documentation and API examples do not prove current availability, merchant eligibility, production enablement, compliant configuration, or transaction success.

## Sources

- [[source-adyen-docs-point-of-sale-surcharge]] — Adyen POS website overview of configuration-based and dynamic surcharge methods, device/region limits, disclosure, DCC exclusion, and optional reporting (2026-09-15 snapshot).


- [[source-adyen-docs-point-of-sale-surcharge-configuration]] — Adyen in-person Management API surcharge-configuration guide captured 2026-09-15 for scope, rule precedence, feature gates, disclosure and MOTO/MKE opt-out


- [[source-adyen-docs-point-of-sale-surcharge-dynamic]] — Adyen Docs website guide to merchant-calculated Terminal API POS surcharge, card acquisition, confirmation/disclosure and response fields (2026-09-15 snapshot).


- [[source-adyen-docs-development-resources-surcharge-compliance]] — Adyen general and regional surcharge-compliance guidance across ecommerce and in-person reporting, disclosure, notifications, and dated restrictions (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-online-payments-surcharge]] - 2026-09-15 Adyen guide to the pilot API-only card surcharge flow, merchant-owned eligibility logic, legal and payment-method boundaries, request arithmetic, and capture/refund handling
